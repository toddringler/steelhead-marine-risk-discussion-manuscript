#!/usr/bin/env python3
"""Read-only staging review renderer. Python 3.10+, standard library only."""
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import html
import io
import json
import math
from pathlib import Path
import re
import shutil
import sys
import subprocess
from datetime import datetime, timezone
from urllib.parse import urlparse

MARKER = '<!-- census-record -->'
STAGES = {'research': 'Research proposal', 'reviewed': 'Reviewed proposal', 'signoff': 'Ready for owner signoff'}
DISPOSITIONS = {'accepted', 'correction requested', 'deferred', 'rejected'}
KINDS = {'csv-row', 'text', 'document', 'geojson'}


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_record(path):
    """Exactly one machine-readable JSON section; prose elsewhere is preserved."""
    text = path.read_text(encoding='utf-8')
    pattern = re.escape(MARKER) + r'\s*```json\s*\n(.*?)\n```'
    matches = re.findall(pattern, text, re.S)
    if len(matches) != 1:
        raise ValueError(f'{path.name}: expected exactly one {MARKER} JSON block')
    data = json.loads(matches[0], parse_constant=lambda x: (_ for _ in ()).throw(ValueError(f'Invalid number {x}')))
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise ValueError(f'{path.name}: schema_version must be 1')
    return data


def confined(root, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError('Paths must be nonempty, relative paths')
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes census directory: {relative}')
    return path


def target_path(root, relative):
    path = confined(root, relative)
    allowed = ('sources/', 'input-data/', 'methods/')
    if not relative.startswith(allowed) and relative not in ('decisions.md', 'discovery-log.csv'):
        raise ValueError(f'Unsupported retained destination: {relative}')
    return path


def proposal_path(root, relative):
    path = confined(root, relative)
    if not path.is_relative_to((root / 'staging/proposed-changes').resolve()):
        raise ValueError(f'Proposed files must be inside staging/proposed-changes: {relative}')
    if not path.is_file():
        raise ValueError(f'Missing proposed file: {relative}')
    return path


def require_string(data, name):
    if not isinstance(data.get(name), str) or not data[name].strip():
        raise ValueError(f'{name} must be a nonempty string')


def unique(items, name):
    values = [i.get(name) for i in items]
    if any(not isinstance(v, str) or not v for v in values) or len(set(values)) != len(values):
        raise ValueError(f'Missing or duplicate {name}')


def current_row(path, key):
    if not path.exists():
        return None
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        if not set(key).issubset(reader.fieldnames or []):
            raise ValueError('CSV key fields absent from retained file')
        matches = [r for r in reader if all(r.get(k) == v for k, v in key.items())]
    if len(matches) > 1:
        raise ValueError('CSV key matches multiple retained rows')
    return matches[0] if matches else None


def geometry_summary(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('type') != 'FeatureCollection' or not isinstance(data.get('features'), list):
        raise ValueError('GeoJSON must be a FeatureCollection')
    points = []
    null_count = 0
    for feature in data['features']:
        if feature.get('type') != 'Feature':
            raise ValueError('Invalid GeoJSON feature')
        geo = feature.get('geometry')
        if geo is None:
            null_count += 1
            continue
        if geo.get('type') not in ('Polygon', 'MultiPolygon'):
            raise ValueError('Only Polygon, MultiPolygon, and null geometry supported')
        polygons = [geo.get('coordinates')] if geo['type'] == 'Polygon' else geo.get('coordinates')
        if not isinstance(polygons, list) or not polygons:
            raise ValueError('Empty polygon coordinates')
        for polygon in polygons:
            if not isinstance(polygon, list) or not polygon:
                raise ValueError('Polygon requires rings')
            for ring in polygon:
                if not isinstance(ring, list) or len(ring) < 4 or ring[0] != ring[-1]:
                    raise ValueError('Polygon rings must be closed with at least four positions')
                for point in ring:
                    if not isinstance(point, list) or len(point) < 2:
                        raise ValueError('Invalid coordinate position')
                    x, y = point[:2]
                    if any(not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v) for v in (x, y)):
                        raise ValueError('Coordinates must be finite numbers')
                    if not -180 <= x <= 180 or not -90 <= y <= 90:
                        raise ValueError('Coordinates outside longitude/latitude bounds')
                    points.append((x, y))
    bounds = [min(p[0] for p in points), min(p[1] for p in points), max(p[0] for p in points), max(p[1] for p in points)] if points else None
    return {'features': len(data['features']), 'null_geometry_features': null_count, 'bounds': bounds,
            'validation_limit': 'Structural/range checks only; topology and scientific extent need independent review.'}


def build_model(census_root):
    handoff_file = census_root / 'staging/handoff.md'
    if not handoff_file.exists():
        return {'active': False, 'errors': [], 'warnings': [], 'changes': [], 'sources': [], 'proposal_hashes': {}}
    h = read_record(handoff_file)
    for field in ('assignment', 'base_commit', 'researcher_id', 'current_role', 'view_stage'):
        require_string(h, field)
    if h['view_stage'] not in STAGES or h['current_role'] not in ('researcher', 'reviewer', 'steward', 'owner', 'closed'):
        raise ValueError('Invalid view_stage or current_role')
    if not h.get('synthetic') and not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', h['base_commit']):
        raise ValueError('base_commit must be a full Git hash (except synthetic fixtures)')
    for name in ('changes', 'sources', 'execution_notes', 'integration_ids'):
        if not isinstance(h.get(name), list):
            raise ValueError(f'{name} must be a list')
    if not isinstance(h.get('organizations'), list) or not h['organizations']:
        raise ValueError('organizations must be a nonempty list')
    unique(h['organizations'], 'org_id')
    unique(h['sources'], 'source_id')
    unique(h['changes'], 'change_id')
    errors, warnings = [], []
    sources = {}
    for source in h['sources']:
        for field in ('source_id', 'title', 'path', 'sha256'):
            require_string(source, field)
        path = confined(census_root, source['path'])
        if not path.is_relative_to((census_root/'sources').resolve()) and not path.is_relative_to((census_root/'staging/proposed-changes').resolve()):
            raise ValueError('Evidence paths must be retained sources or proposed changes')
        if not path.is_file():
            raise ValueError(f'Missing evidence: {source["path"]}')
        actual = file_hash(path)
        sources[source['source_id']] = {**source, 'actual_sha256': actual, '_path': path}
        if actual != source['sha256']:
            errors.append(f'{source["source_id"]}: retained bytes do not match declared source hash')
    current_commit='not applicable (synthetic fixture)'
    if not h.get('synthetic'):
        result=subprocess.run(['git','-C',str(census_root),'rev-parse','HEAD'],text=True,capture_output=True)
        if result.returncode: errors.append('Cannot identify current retained Git commit')
        else: current_commit=result.stdout.strip()
        check=subprocess.run(['git','-C',str(census_root),'cat-file','-e',h['base_commit']+'^{commit}'],capture_output=True)
        if check.returncode: errors.append('Recorded base commit is not available in this repository')
        if current_commit!=h['base_commit']: warnings.append('Current Git commit differs from assignment base; expected destination values are checked below')
    review_file = census_root/'staging/review.md'
    r = read_record(review_file) if review_file.exists() else None
    if r and r.get('assignment') != h['assignment']:
        raise ValueError('review.md belongs to another assignment')
    if r:
        require_string(r, 'reviewer_id')
        require_string(r, 'reviewer_type')
        if r['reviewer_type'] not in ('agent', 'human'):
            raise ValueError('reviewer_type must be agent or human')
        if not isinstance(r.get('items'), list):
            raise ValueError('review items must be a list')
        unique(r['items'], 'change_id')
        if r['reviewer_id'] == h['researcher_id']:
            errors.append('Independent reviewer cannot be the researcher')
    elif h['view_stage'] != 'research':
        errors.append('Reviewed/signoff stage requires review.md')
    reviews = {i['change_id']: i for i in (r or {}).get('items', [])}
    proposed_ids = {c['change_id'] for c in h['changes']}
    if set(reviews)-proposed_ids:
        errors.append('Review references unknown change IDs')
    org_ids = {o['org_id'] for o in h['organizations']}
    changes, hashes = [], {}
    for original in h['changes']:
        c = dict(original)
        for field in ('change_id', 'org_id', 'kind', 'target', 'summary', 'submission_type'):
            require_string(c, field)
        if c['org_id'] not in org_ids or c['kind'] not in KINDS or c['submission_type'] not in ('finding', 'lead'):
            raise ValueError(f'{c["change_id"]}: invalid organization, kind or submission_type')
        if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', c['change_id']):
            raise ValueError('change_id must be a safe lowercase identifier')
        c.setdefault('depends_on', [])
        if not isinstance(c.get('source_ids'), list) or not isinstance(c['depends_on'], list):
            raise ValueError('source_ids and depends_on must be lists')
        if set(c['source_ids'])-sources.keys():
            raise ValueError(f'{c["change_id"]}: unresolved source reference')
        if set(c['depends_on'])-proposed_ids or c['change_id'] in c['depends_on']:
            raise ValueError(f'{c["change_id"]}: invalid dependency')
        target = target_path(census_root, c['target'])
        c['_target_path'] = target if target.is_file() else None
        if 'before' not in c:
            raise ValueError(f'{c["change_id"]}: expected before value is required')
        if c['kind'] == 'csv-row':
            key = c.get('key')
            if not isinstance(key, dict) or not key or not all(isinstance(v, str) for v in key.values()):
                raise ValueError('csv-row requires nonempty string-valued key')
            for label in ('before', 'after'):
                if c.get(label) is not None and (not isinstance(c[label], dict) or not all(isinstance(v, str) for v in c[label].values())):
                    raise ValueError('CSV rows must contain string-valued dictionaries or null')
            if c.get('after') is not None and any(c['after'].get(k) != v for k,v in key.items()):
                raise ValueError('Proposed CSV row does not match key')
            if c['before'] is None and c.get('after') is None:
                raise ValueError('CSV change needs a before or after row')
            c['actual_before'] = current_row(target, key)
            c['after_value'] = c.get('after')
        else:
            if c['kind'] == 'text' and c['before'] is not None and not isinstance(c['before'], str):
                raise ValueError('Text before must be a string or null')
            if c['kind'] != 'text' and c['before'] is not None and not re.fullmatch(r'[0-9a-f]{64}', c['before']):
                raise ValueError('Document/GeoJSON before must be a SHA-256 or null')
            path = proposal_path(census_root, c.get('after_file'))
            c['_after_path'] = path
            if c['kind'] == 'text':
                c['actual_before'] = target.read_text(encoding='utf-8') if target.exists() else None
                c['after_value'] = path.read_text(encoding='utf-8')
            else:
                c['actual_before'] = file_hash(target) if target.exists() else None
                c['after_value'] = file_hash(path)
            if c['kind'] == 'document' and target.exists() and c['actual_before'] != c['after_value']:
                errors.append(f'{c["change_id"]}: original documents cannot be overwritten; use a new destination')
            if c['kind'] == 'geojson':
                c['geometry'] = geometry_summary(path)
                c['before_geometry'] = geometry_summary(target) if target.exists() else None
        c['base_matches'] = c['actual_before'] == c['before']
        if not c['base_matches']:
            errors.append(f'{c["change_id"]}: retained destination changed or expected before is incorrect')
        if not c['source_ids'] and c['submission_type'] == 'finding':
            warnings.append(f'{c["change_id"]}: no supporting source IDs supplied; independent evidence review required')
        # Deliberately excludes current_role, owner decisions, display timestamps and completion notes.
        c['inventory'] = {k: c.get(k) for k in ('change_id','org_id','kind','target','submission_type','before','key','depends_on','summary')}
        c['inventory']['after'] = c['after_value']
        c['inventory']['evidence'] = [{k:v for k,v in sources[sid].items() if not k.startswith('_')} for sid in sorted(c['source_ids'])]
        c['proposal_hash'] = hashes[c['change_id']] = digest(c['inventory'])
        item = reviews.get(c['change_id'])
        c['review'] = item
        c['review_status'] = 'unreviewed'
        if item:
            if item.get('disposition') not in DISPOSITIONS:
                raise ValueError('Invalid review disposition')
            for field in ('rationale','reviewed_date','scope'):
                require_string(item,field)
            # Dependency hashes are folded in below before deciding review applicability.
            if c['submission_type'] == 'lead' and item['disposition'] == 'accepted' and item['scope'] != 'lead only':
                errors.append(f'{c["change_id"]}: lead acceptance must have lead only scope')
        if c['submission_type'] == 'lead' and c['target'] not in ('sources/entities.csv', 'input-data/seed-candidate-list.md','decisions.md','discovery-log.csv'):
            errors.append(f'{c["change_id"]}: lead-only proposal cannot become retained financial/activity/geometry findings')
        changes.append(c)
    # Detect dependency cycles even though the prototype never applies proposals.
    adjacency = {c['change_id']:c['depends_on'] for c in changes}
    def visit(node, active, done):
        if node in active: raise ValueError('Proposal dependency cycle')
        if node in done: return
        for dep in adjacency[node]: visit(dep, active | {node}, done)
        done.add(node)
    done=set()
    for cid in adjacency: visit(cid,set(),done)
    by_id = {c['change_id']: c for c in changes}
    finished = set()
    def final_hash(cid):
        if cid in finished: return hashes[cid]
        c=by_id[cid]
        c['inventory']['dependency_hashes']={dep:final_hash(dep) for dep in sorted(c['depends_on'])}
        c['proposal_hash']=hashes[cid]=digest(c['inventory'])
        finished.add(cid)
        return hashes[cid]
    for c in changes:
        final_hash(c['change_id'])
        if c['review']:
            c['review_status']=c['review']['disposition'] if c['review'].get('proposal_hash')==c['proposal_hash'] else 'stale'
            if c['review_status']=='stale': warnings.append(f'{c["change_id"]}: review hashes no longer match the proposal or dependencies')
    selection = h['integration_ids']
    if len(selection)!=len(set(selection)) or set(selection)-proposed_ids:
        raise ValueError('integration_ids must be unique known change IDs')
    by_id = {c['change_id']: c for c in changes}
    inventory = {'base_commit':h['base_commit'], 'reviewer': {k:(r or {}).get(k) for k in ('reviewer_id','reviewer_type')}, 'changes':[]}
    for cid in sorted(selection):
        c=by_id[cid]
        if set(c['depends_on'])-set(selection): errors.append(f'{cid}: selected proposal is missing an integration dependency')
        if c['review_status'] != 'accepted': errors.append(f'{cid}: selected proposal lacks current independent acceptance')
        inventory['changes'].append({'proposal':c['inventory'], 'actual_before':c['actual_before'], 'review':c['review']})
    approval_digest = digest(inventory) if selection else None
    if h['view_stage']=='signoff' and not selection: errors.append('Signoff stage requires a nonempty reviewed integration subset')
    ready = h['view_stage']=='signoff' and bool(selection) and not errors
    approval=h.get('owner_approval') or {}
    approval_state='Not recorded'
    if approval:
        approval_state = 'Matches selected proposal (recorded owner statement; renderer does not authenticate approval)' if approval.get('digest')==approval_digest and sorted(approval.get('change_ids',[]))==sorted(selection) else 'STALE — recorded approval does not match this proposal'
    if h['view_stage']=='research' and r: warnings.append('Prior review is shown as history; this page is still a research proposal')
    return {'active':True,'current_commit':current_commit,'handoff':h,'review_record':r,'sources':list(sources.values()),'changes':changes,
            'proposal_hashes':hashes,'integration_inventory':inventory,'approval_digest':approval_digest,
            'approval_state':approval_state,'ready':ready,'errors':errors,'warnings':warnings,
            'input_hashes':{'handoff.md':file_hash(handoff_file),'review.md':file_hash(review_file) if review_file.exists() else None}}


def escape(value):
    return html.escape(str(value), quote=True)


def pretty(value):
    return json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)


def safe_url(url):
    return isinstance(url,str) and urlparse(url).scheme in ('https','http') and bool(urlparse(url).netloc)


def decision_context(model):
    if not model['active']:
        return None
    return {'assignment': model['handoff']['assignment'],
            'base_commit': model['handoff']['base_commit'],
            'input_hashes': model['input_hashes'],
            'approval_digest': model['approval_digest'],
            'proposals': {c['change_id']: c['proposal_hash'] for c in model['changes']}}


def validate_owner_decisions(bundle, model):
    context = decision_context(model)
    if not context or bundle.get('schema_version') != 1 or bundle.get('type') != 'census-owner-decisions':
        raise ValueError('Not an owner decision file for an active assignment')
    if bundle.get('context') != context:
        raise ValueError('Stale decisions: assignment, proposals, evidence, review or handoff changed; inspect a refreshed preview')
    if not isinstance(bundle.get('owner_name'), str) or not bundle['owner_name'].strip():
        raise ValueError('Owner name is required (self-reported, not authentication)')
    if not isinstance(bundle.get('decisions'), list) or not bundle['decisions']:
        raise ValueError('No decisions supplied')
    seen = set()
    for item in bundle['decisions']:
        cid = item.get('change_id')
        if cid not in context['proposals'] or cid in seen:
            raise ValueError('Unknown or duplicate change ID')
        seen.add(cid)
        if item.get('choice') not in ('accept', 'reject', 'defer', 'request changes'):
            raise ValueError('Invalid owner choice')
        if not isinstance(item.get('comment'), str):
            raise ValueError('Comment must be text')
        if item['choice'] == 'request changes' and not item['comment'].strip():
            raise ValueError('Requested changes need a comment')
    return bundle['decisions']


def render(census_root, output, template):
    model=build_model(census_root)
    output.mkdir(parents=True,exist_ok=True)
    # Only renderer-owned snapshots are reset, never staging or retained research.
    assets=output/'assets'
    if assets.exists(): shutil.rmtree(assets)
    assets.mkdir()
    def snapshot(path):
        sha=file_hash(path)
        ext=path.suffix.lower()
        if ext not in ('.pdf','.png','.jpg','.jpeg','.txt','.csv','.md','.json','.geojson'):
            ext='.txt' # Avoid serving source HTML/scripts as executable documents.
        name=sha+ext
        dest=assets/name
        if not dest.exists():shutil.copyfile(path,dest)
        return 'assets/'+name
    def file_link(path,label):
        if path is None:return '<span class="muted">No previous file</span>'
        return f'<a href="{snapshot(path)}" target="_blank" rel="noopener">{escape(label)}</a>'
    if not model['active']:
        body='<div class="notice">No active assignment. Staging is empty or has no handoff.</div>'
        title='No active assignment'
    else:
        h=model['handoff'];title=h['assignment']
        label=STAGES[h['view_stage']]
        if h['view_stage']=='signoff' and not model['ready']:label='Not ready for owner signoff'
        synthetic='<div class="fixture">SYNTHETIC TEST DATA — not real census research, review, or owner approval</div>' if h.get('synthetic') else ''
        counts={status:sum(c['review_status']==status for c in model['changes']) for status in ('unreviewed','accepted','correction requested','deferred','rejected','stale')}
        cards=[('Organizations',len(h['organizations'])),('Source documents',len(model['sources'])),('Proposed entries',len(model['changes'])),('Lead-only proposals',sum(c['submission_type']=='lead' for c in model['changes'])),('Accepted findings',sum(c['review_status']=='accepted' and c['submission_type']=='finding' for c in model['changes'])),('Reused observations',h.get('reused_count',0))]
        body=synthetic+f'<div class="stage">{escape(label)} · Next role: {escape(h["current_role"])}</div><h1>{escape(title)}</h1><p class="intro">{escape(h.get("objective",""))}</p>'
        body+='<div class="cards">'+''.join(f'<div class="card"><strong>{escape(v)}</strong><span>{escape(k)}</span></div>' for k,v in cards)+'</div>'
        body+='<div class="notice">This is a local integration preview, not a published census release. A lead is not an established finding. Enter your choices below and download them for the agent. Choices do not modify research records or replace independent review.</div>'
        for kind in ('errors','warnings'):
            if model[kind]:body+=f'<section class="{kind}"><h2>{kind.title()}</h2><ul>'+''.join(f'<li>{escape(x)}</li>' for x in model[kind])+'</ul></section>'
        body+='<section><h2>Review and proposed integration</h2><p>'+escape(' · '.join(f'{k}: {v}' for k,v in counts.items()))+'</p>'
        body+=f'<p><b>Selected change IDs:</b> {escape(", ".join(h["integration_ids"]) or "None yet")}</p><p><b>Proposal digest:</b> <code>{escape(model["approval_digest"] or "Not available until a subset is selected")}</code></p><p><b>Owner approval:</b> {escape(model["approval_state"])}</p>'
        for key,label2 in (('owner_questions','Owner decisions needed'),('gaps','Gaps and limits')):
            body+=f'<h3>{label2}</h3><ul>'+''.join(f'<li>{escape(x)}</li>' for x in h.get(key,[]))+'</ul>'
        body+='</section><section><h2>Your decisions</h2><p>Choose within each proposal below. Unselected proposals have no decision. Comments can resolve a disagreement or explain a requested correction. Download before closing or refreshing; entries are not saved automatically.</p><label>Your name<input id="owner-name" autocomplete="name"></label><p><button type="button" id="download-decisions">Download my decisions</button></p><p id="decision-message" role="status" aria-live="polite"></p><p>Acceptance expresses your choice on a proposal. It does not authorize commits, cleanup, pushing or publishing, and cannot bypass unresolved evidence or independent-review requirements.</p></section><section><h2>Inspect changes</h2><div class="filters"><label>Search names, IDs, files, values<input id="search" type="search" placeholder="Search all changes"></label><label>Review status<select id="status"><option value="">All statuses</option>'+''.join(f'<option>{escape(x)}</option>' for x in counts)+'</select></label><label>Submission<select id="submission"><option value="">Findings and leads</option><option value="finding">Findings</option><option value="lead">Leads only</option></select></label></div><p id="visible-count" aria-live="polite"></p>'
        orgs={o['org_id']:o['name'] for o in h['organizations']}
        for c in model['changes']:
            cid=c['change_id'];status=c['review_status'];prior=c['actual_before'];after=c['after_value']
            terms=canonical({k:v for k,v in c.items() if not k.startswith('_')})+' '+orgs[c['org_id']]
            body+=f'<details class="change" data-status="{escape(status)}" data-submission="{escape(c["submission_type"])}" data-search="{escape(terms.lower())}" id="{escape(cid)}"><summary><span class="badge">{escape(status)}</span> <strong>{escape(cid)}</strong> · {escape(orgs[c["org_id"]])}<span class="summary-text">{escape(c["summary"])}</span></summary><div class="detail">'
            body+=f'<div class="owner-choice"><h3>Your choice for {escape(cid)}</h3><label for="choice-{escape(cid)}">Decision for {escape(cid)}</label><select id="choice-{escape(cid)}" class="decision-choice" data-change-id="{escape(cid)}"><option value="">No decision yet</option><option value="accept">Accept</option><option value="reject">Reject</option><option value="defer">Defer</option><option value="request changes">Request changes</option></select><label for="comment-{escape(cid)}">Comment for {escape(cid)}</label><textarea id="comment-{escape(cid)}" rows="3" placeholder="Explain your decision, resolve a disagreement, or specify requested changes"></textarea></div>'
            body+=f'<p><b>Scope:</b> {escape(c["submission_type"])} · <b>Organization:</b> {escape(c["org_id"])}<br><b>Destination:</b> <code>{escape(c["target"])}</code><br><b>Depends on:</b> {escape(", ".join(c["depends_on"]) or "None")}</p>'
            if c['kind']=='csv-row':
                body+='<table><thead><tr><th>Field</th><th>Retained before</th><th>Proposed after</th></tr></thead><tbody>'
                for key in sorted(set(prior or {})|set(after or {})):
                    a=(prior or {}).get(key);b=(after or {}).get(key)
                    body+=f'<tr class="{"altered" if a!=b else ""}"><th>{escape(key)}</th><td>{escape(a) if a is not None else "<i>Absent</i>"}</td><td>{escape(b) if b is not None else "<i>Absent</i>"}</td></tr>'
                body+='</tbody></table>'
                name=cid+'.csv';buf=io.StringIO();writer=csv.DictWriter(buf,fieldnames=list((after or prior).keys()));writer.writeheader();writer.writerow(after or prior);(assets/name).write_text(buf.getvalue())
                body+=f'<p><a href="assets/{escape(name)}" download>Download proposed entry</a></p>'
            elif c['kind']=='text':
                diff='\n'.join(difflib.unified_diff((prior or '').splitlines(),after.splitlines(),fromfile='retained before',tofile='proposed after',lineterm=''))
                body+='<div class="twocol"><div><h3>Retained before</h3><pre>'+escape(prior if prior is not None else 'No previous record')+'</pre></div><div><h3>Proposed after</h3><pre>'+escape(after)+'</pre></div></div><details><summary>Text diff</summary><pre>'+escape(diff)+'</pre></details>'
            elif c['kind']=='geojson':
                body+='<div class="notice">Raw geometry and extent comparison only in this prototype; no basemap or visual scientific validation is implied.</div><div class="twocol"><div><h3>Retained extent</h3><pre>'+escape(pretty(c['before_geometry']))+'</pre></div><div><h3>Proposed extent</h3><pre>'+escape(pretty(c['geometry']))+'</pre></div></div>'
                body+='<details><summary>Proposed GeoJSON</summary><pre>'+escape(c['_after_path'].read_text())+'</pre></details>'
            else:
                body+='<p>Original source document addition. Inspect the retained bytes and its source metadata below; origin checking does not establish every extracted finding.</p>'
            body+='<p>'+file_link(c['_target_path'],'Inspect current retained file')
            if c.get('_after_path'):body+=' · '+file_link(c['_after_path'],'Inspect proposed file')
            body+='</p><h3>Evidence</h3><ul>'
            for sid in c['source_ids']:
                src=next(x for x in model['sources'] if x['source_id']==sid)
                external=f' · <a href="{escape(src["url"])}" target="_blank" rel="noopener">Public origin</a>' if safe_url(src.get('url')) else ''
                body+=f'<li><b>{escape(sid)}</b> — {escape(src["title"])} · {file_link(src["_path"],"Inspect saved evidence")}{external}<br>{escape(src.get("publisher",""))} · Period: {escape(src.get("period","unknown"))} · Locator: {escape(src.get("locator","not supplied"))}<br>Origin check: {escape(src.get("origin_check","pending"))}<br><code>{escape(src["actual_sha256"])}</code></li>'
            body+='</ul><h3>Reviewer findings</h3>'
            if c['review']:
                item=c['review'];body+=f'<p><b>Recorded disposition:</b> {escape(item["disposition"])} · <b>Current applicability:</b> {escape(status)}<br><b>Scope:</b> {escape(item["scope"])}<br>{escape(item["rationale"])}</p>'
            else:body+='<p>Not independently reviewed.</p>'
            body+=f'<details><summary>Exact proposal identity</summary><code>{escape(c["proposal_hash"])}</code><pre>{escape(pretty(c["inventory"]))}</pre></details></div></details>'
        body+='</section><section><h2>Execution and retained-state provenance</h2><p><b>Base commit:</b> <code>'+escape(h['base_commit'])+'</code><br><b>Current retained commit:</b> <code>'+escape(model['current_commit'])+'</code></p><p><b>Researcher:</b> '+escape(h['researcher_id'])+' · <b>Reviewer:</b> '+escape((model['review_record'] or {}).get('reviewer_id','not assigned'))+'</p><details><summary>Model settings and execution notes</summary><pre>'+escape(pretty(h['execution_notes']))+'</pre></details><details><summary>Exact rendered input hashes</summary><pre>'+escape(pretty(model['input_hashes']))+'</pre></details><details><summary>Approval digest inventory</summary><pre>'+escape(pretty(model['integration_inventory']))+'</pre></details><p><a href="preview.json">Download preview inventory and proposal hashes</a></p></section>'
    if model['active']:
        payload=json.dumps(decision_context(model), ensure_ascii=True).replace('<', r'<').replace('>', r'>').replace('&', r'&')
        body+='<script type="application/json" id="decision-context">'+payload+'</script>'
    generated=datetime.now(timezone.utc).isoformat(timespec='seconds')
    page=template.read_text().replace('@@TITLE@@',escape(title)).replace('@@BODY@@',body).replace('@@GENERATED@@',escape(generated))
    (output/'index.html').write_text(page,encoding='utf-8')
    serial={k:v for k,v in model.items() if k not in ('sources','changes')}
    serial['generated_at']=generated
    serial['changes']=[{k:v for k,v in c.items() if not k.startswith('_')} for c in model['changes']]
    serial['sources']=[{k:v for k,v in source.items() if not k.startswith('_')} for source in model['sources']]
    (output/'preview.json').write_text(pretty(serial)+'\n')
    return model


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    repo_default=Path(__file__).resolve().parents[3]
    parser.add_argument('--repository-root',type=Path,default=repo_default)
    parser.add_argument('--census-root',type=Path,help='Override for an isolated synthetic fixture, never for a second live assignment')
    parser.add_argument('--output',type=Path,help='Must be inside repository-root/output')
    parser.add_argument('--strict',action='store_true',help='Exit nonzero if semantic validation errors are present; still render warnings for inspection')
    args=parser.parse_args()
    repo=args.repository_root.resolve();census=(args.census_root or repo/'analysis/ngo-census').resolve()
    output=(args.output or repo/'output/ngo-census/previews/owner-review').resolve()
    allowed=(repo/'output').resolve()
    if not output.is_relative_to(allowed) or output==allowed:
        parser.error('Output must be a subdirectory of repository-root/output')
    template=Path(__file__).resolve().parent.parent/'templates/staging-review.html'
    try:
        model=build_model(census) # Fail schema/path validation before touching prior preview.
        model=render(census,output,template)
    except (ValueError,OSError,KeyError,TypeError,json.JSONDecodeError) as exc:
        output.mkdir(parents=True,exist_ok=True)
        (output/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Preview unavailable</title><h1>Preview unavailable</h1><p>No valid current proposal is displayed.</p><pre>'+escape(exc)+'</pre></html>')
        print(f'Cannot render review: {exc}',file=sys.stderr)
        return 2
    print(output/'index.html')
    for error in model['errors']: print('ERROR: '+error,file=sys.stderr)
    return 1 if args.strict and model['errors'] else 0


if __name__=='__main__':
    sys.exit(main())
