"""Behavior tests using isolated synthetic data; never mutate live census staging."""
from pathlib import Path
import importlib.util
import json
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[3]
CENSUS=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('staging_review',CENSUS/'scripts/render-staging-review.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)


def save_record(path,data):
    path.write_text('# Test record\n\n<!-- census-record -->\n```json\n'+json.dumps(data,indent=2)+'\n```\n')


class StagingReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        self.census=self.root/'analysis/ngo-census'
        shutil.copytree(CENSUS/'tests/fixtures/review-demo',self.census)
        self.handoff=self.census/'staging/handoff.md'
        self.review=self.census/'staging/review.md'
        self.output=self.root/'output/ngo-census/previews/owner-review'

    def test_owner_choices_bound_to_current_inputs(self):
        m=r.build_model(self.census)
        b={'schema_version':1,'type':'census-owner-decisions','owner_name':'Test owner',
           'context':r.decision_context(m),'decisions':[
           {'change_id':'change-01','choice':'accept','comment':''},
           {'change_id':'change-02','choice':'reject','comment':''},
           {'change_id':'change-03','choice':'defer','comment':''},
           {'change_id':'change-04','choice':'request changes','comment':'Check region'}]}
        self.assertEqual(len(r.validate_owner_decisions(b,m)),4)
        b['decisions'][-1]['comment']=''
        with self.assertRaises(ValueError):r.validate_owner_decisions(b,m)
        b['decisions'][-1]['comment']='Check region'
        self.edit_handoff(lambda h:h.update(objective='Changed assignment'))
        with self.assertRaises(ValueError):r.validate_owner_decisions(b,r.build_model(self.census))

    def tearDown(self):self.temp.cleanup()

    def edit_handoff(self,fn):
        h=r.read_record(self.handoff);fn(h);save_record(self.handoff,h)

    def test_reviewed_fixture_and_safe_render(self):
        before={str(p.relative_to(self.census)):p.read_bytes() for p in self.census.rglob('*') if p.is_file()}
        model=r.render(self.census,self.output,CENSUS/'templates/staging-review.html')
        self.assertEqual(model['errors'],[])
        self.assertEqual([c['review_status'] for c in model['changes']],['accepted','accepted','correction requested','deferred','accepted','rejected'])
        page=(self.output/'index.html').read_text()
        self.assertIn('SYNTHETIC TEST DATA',page)
        self.assertIn('&lt;script&gt;',page)
        self.assertNotIn('<script>alert(',page)
        self.assertIn('1200',page)
        self.assertIn('2022', (self.census/'sources/org-demo/financial-history.csv').read_text())
        self.assertEqual(before,{str(p.relative_to(self.census)):p.read_bytes() for p in self.census.rglob('*') if p.is_file()})
        self.assertGreater(len(list((self.output/'assets').glob('*'))),0)

    def test_approval_and_role_notes_do_not_change_approval_digest(self):
        before=r.build_model(self.census)
        self.edit_handoff(lambda h:h.update(current_role='owner',view_stage='signoff',completion_notes='pending',owner_approval={'digest':before['approval_digest'],'change_ids':h['integration_ids'],'owner':'test owner'}))
        after=r.build_model(self.census)
        self.assertTrue(after['ready'])
        self.assertEqual(before['approval_digest'],after['approval_digest'])
        self.assertTrue(after['approval_state'].startswith('Matches'))

    def test_changed_value_invalidates_review_and_owner_approval(self):
        original=r.build_model(self.census)
        def change(h):
            h['view_stage']='signoff'
            h['owner_approval']={'digest':original['approval_digest'],'change_ids':h['integration_ids']}
            h['changes'][1]['after']['amount']='9999'
        self.edit_handoff(change)
        model=r.build_model(self.census)
        self.assertEqual(model['changes'][1]['review_status'],'stale')
        self.assertFalse(model['ready'])
        self.assertTrue(model['approval_state'].startswith('STALE'))

    def test_retained_row_conflict_blocks_signoff(self):
        with (self.census/'sources/org-demo/financial-history.csv').open('a') as f:
            f.write('org-demo,revenue,2023,44,USD,other-source,other locator\n')
        self.edit_handoff(lambda h:h.update(view_stage='signoff'))
        model=r.build_model(self.census)
        self.assertFalse(model['ready'])
        self.assertTrue(any('retained destination' in x for x in model['errors']))

    def test_missing_dependency_blocks_signoff(self):
        self.edit_handoff(lambda h:h.update(view_stage='signoff',integration_ids=['change-02']))
        model=r.build_model(self.census)
        self.assertFalse(model['ready'])
        self.assertTrue(any('missing an integration dependency' in x for x in model['errors']))

    def test_dependency_change_invalidates_dependent_review(self):
        self.edit_handoff(lambda h:h['changes'][0].update(summary='Changed meaning in dependency'))
        model=r.build_model(self.census)
        self.assertEqual(model['changes'][0]['review_status'],'stale')
        self.assertEqual(model['changes'][1]['review_status'],'stale')

    def test_source_hash_mismatch_detected(self):
        src=self.census/'staging/proposed-changes/sources/org-demo/990/2023-demo.txt'
        src.write_text(src.read_text()+'\nChanged source contents\n')
        model=r.build_model(self.census)
        self.assertTrue(any('source hash' in x for x in model['errors']))
        self.assertEqual(model['changes'][1]['review_status'],'stale')

    def test_path_escape_and_unsafe_change_id_rejected(self):
        self.edit_handoff(lambda h:h['changes'][0].update(after_file='../../outside.txt'))
        with self.assertRaises(ValueError):r.build_model(self.census)
        self.edit_handoff(lambda h:h['changes'][0].update(after_file='staging/proposed-changes/sources/org-demo/990/2023-demo.txt',change_id='../outside'))
        with self.assertRaises(ValueError):r.build_model(self.census)

    def test_independent_reviewer_and_assignment_match(self):
        review=r.read_record(self.review);review['reviewer_id']='fixture-researcher';save_record(self.review,review)
        self.assertTrue(any('cannot be the researcher' in x for x in r.build_model(self.census)['errors']))
        review['assignment']='another assignment';save_record(self.review,review)
        with self.assertRaises(ValueError):r.build_model(self.census)

    def test_duplicate_ids_and_dependency_cycles_rejected(self):
        self.edit_handoff(lambda h:h['changes'].append(dict(h['changes'][0])))
        with self.assertRaises(ValueError):r.build_model(self.census)
        h=r.read_record(self.handoff);h['changes'].pop();h['changes'][0]['depends_on']=['change-02'];save_record(self.handoff,h)
        with self.assertRaisesRegex(ValueError,'cycle'):r.build_model(self.census)

    def test_geometry_validation_and_unknown(self):
        path=self.census/'staging/proposed-changes/sources/org-demo/footprint.geojson'
        data=json.loads(path.read_text());data['features'][0]['geometry']=None;path.write_text(json.dumps(data))
        summary=r.geometry_summary(path)
        self.assertEqual(summary['null_geometry_features'],1)
        self.assertIsNone(summary['bounds'])
        data['features'][0]['geometry']={'type':'Polygon','coordinates':[[[0,0],[1,0],[1,1],[0,1]]]};path.write_text(json.dumps(data))
        with self.assertRaises(ValueError):r.geometry_summary(path)

    def test_empty_staging_has_no_active_assignment(self):
        shutil.rmtree(self.census/'staging')
        model=r.render(self.census,self.output,CENSUS/'templates/staging-review.html')
        self.assertFalse(model['active'])
        self.assertIn('No active assignment',(self.output/'index.html').read_text())

    def test_lead_cannot_become_financial_finding(self):
        self.edit_handoff(lambda h:h['changes'][4].update(target='sources/org-next/financial-history.csv'))
        self.assertTrue(any('lead-only' in x for x in r.build_model(self.census)['errors']))


if __name__=='__main__':unittest.main()
