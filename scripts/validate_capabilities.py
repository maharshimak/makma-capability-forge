#!/usr/bin/env python3
"""Validate the *structure* of a capability-graph JSON document.

Usage: python scripts/validate_capabilities.py capabilities.json
This cannot verify implementation, evidence authenticity, safety or performance.
"""
import argparse
import json
import re
from pathlib import Path

STATUSES = {'VERIFIED_SOURCE', 'VERIFIED_RUNTIME', 'INFERRED', 'HYPOTHESIS', 'UNKNOWN', 'BLOCKED'}
MATURITIES = {'M0', 'M1', 'M2', 'M3', 'M4'}
EDGES = {'DEPENDS_ON', 'PRODUCES_FOR', 'CONFLICTS_WITH', 'ADAPTS_TO', 'VERIFIED_WITH', 'SUBSTITUTES'}
REQUIRED = {'id', 'name', 'problem', 'status', 'maturity', 'inputs', 'outputs', 'invariants', 'dependencies', 'failure_modes', 'tests', 'evidence'}


def validate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ['Root must be an object'], []
    if data.get('schema_version') != '1.0':
        errors.append('schema_version must be "1.0"')
    caps = data.get('capabilities')
    edges = data.get('edges')
    if not isinstance(caps, list):
        return errors + ['capabilities must be an array'], warnings
    if not isinstance(edges, list):
        return errors + ['edges must be an array'], warnings
    ids = set()
    for i, item in enumerate(caps):
        label = f'capabilities[{i}]'
        if not isinstance(item, dict):
            errors.append(f'{label}: expected object')
            continue
        missing = REQUIRED - set(item)
        for k in sorted(missing):
            errors.append(f'{label}: missing {k}')
        cid = item.get('id')
        if not isinstance(cid, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', cid):
            errors.append(f'{label}: id must be lowercase kebab-case')
        elif cid in ids:
            errors.append(f'{label}: duplicate id {cid}')
        else:
            ids.add(cid)
        if item.get('status') not in STATUSES:
            errors.append(f'{label}: invalid evidence status')
        if item.get('maturity') not in MATURITIES:
            errors.append(f'{label}: invalid maturity')
        for field in ('inputs', 'outputs', 'invariants', 'dependencies', 'failure_modes', 'tests', 'evidence'):
            if field in item and (not isinstance(item[field], list) or not all(isinstance(x, str) and x.strip() for x in item[field])):
                errors.append(f'{label}: {field} must be a list of nonempty strings')
        if item.get('status') in ('VERIFIED_SOURCE', 'VERIFIED_RUNTIME') and not item.get('evidence'):
            errors.append(f'{label}: verified claim must have evidence citations')
        if item.get('maturity') == 'M4' and item.get('status') != 'VERIFIED_RUNTIME':
            warnings.append(f'{label}: M4 should have verified runtime evidence')
        for f in ('name', 'problem'):
            if f in item and (not isinstance(item[f], str) or not item[f].strip()):
                errors.append(f'{label}: {f} must be nonempty text')
    for i, item in enumerate(caps):
        if isinstance(item, dict) and isinstance(item.get('dependencies'), list):
            for dep in item['dependencies']:
                if isinstance(dep, str) and dep not in ids:
                    errors.append(f'capabilities[{i}] dependency missing: {dep}')
    for i, e in enumerate(edges):
        label = f'edges[{i}]'
        if not isinstance(e, dict):
            errors.append(f'{label}: expected object')
            continue
        if e.get('type') not in EDGES:
            errors.append(f'{label}: invalid edge type')
        for end in ('from', 'to'):
            if not isinstance(e.get(end), str) or e.get(end) not in ids:
                errors.append(f'{label}: {end} must be an existing capability id')
        if not isinstance(e.get('contract'), str) or not e['contract'].strip():
            errors.append(f'{label}: missing edge contract')
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('json_file', type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.json_file.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as e:
        parser.error(f'Unable to read valid JSON: {e}')
    errors, warnings = validate(data)
    for warning in warnings:
        print(f'WARN: {warning}')
    for error in errors:
        print(f'ERROR: {error}')
    if errors:
        print(f'FAILED: {len(errors)} structural error(s)')
        raise SystemExit(1)
    print(f'PASS: {len(data["capabilities"])} capabilities; {len(data["edges"])} edges; {len(warnings)} warning(s). Structural validity only.')


if __name__ == '__main__':
    main()
