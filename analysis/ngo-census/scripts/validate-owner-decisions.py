#!/usr/bin/env python3
"""Validate exported owner choices against current staging; never apply or approve them."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('review_renderer', HERE/'render-staging-review.py')
r=importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('decisions',type=Path)
p.add_argument('--census-root',type=Path,default=HERE.parent)
a=p.parse_args()
try:
    model=r.build_model(a.census_root.resolve())
    items=r.validate_owner_decisions(json.loads(a.decisions.read_text()),model)
    print('Current proposal match: '+str(len(items))+' owner choices. No records changed.')
    for item in items:
        print(item['change_id']+': '+item['choice'])
    if model['errors']:
        print('Proposal validation problems remain; acceptance does not override them.',file=sys.stderr)
except (ValueError, OSError, KeyError, TypeError) as exc:
    print('Decision validation failed: '+str(exc),file=sys.stderr)
    sys.exit(1)
