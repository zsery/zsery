"""Carry eight evidenced documentation changes onto the live project export.

No connection to EA. Refuses changed source fields instead of overwriting them.
Run from any directory; paths are resolved relative to this repository script.
"""
from pathlib import Path
from collections import Counter
from xml.sax.saxutils import escape
from lxml import etree as E
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'outputs/EA_SO_2026-11-05'
SOURCE = OUT / 'ATLASLIVE.xml'
TARGET = OUT / 'Atlas_MVP_live_working_2026-11-07.xml'
X = '{http://schema.omg.org/spec/XMI/2.1}'
raw = SOURCE.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'c1177b4d100a64d29861d51490ebeb5de11da11d4b1a5e47bc3dda2a34a247ea'
changes = json.loads((ROOT / 'outputs/EA_SO_2026-11-04/Kontrola_EA_revize_2026-11-04.json').read_text(encoding='utf-8'))['changes']
auth = json.loads((OUT / 'Kontrola_AuthX_doplneni.json').read_text(encoding='utf-8'))
for change in changes:
    if change['guid'] == auth['guid']:
        assert change['after'] == auth['before']
        change['after'] = auth['after']

def parse(data):
    return E.fromstring(data, E.XMLParser(resolve_entities=False, no_network=True, huge_tree=True))

def elements(root):
    return {e.get(X+'idref'): e for e in root.find(X+'Extension').find('elements')}

original = parse(raw)
els = elements(original)
out = raw
patterns = []
for change in changes:
    guid = change['guid']
    assert els[guid].get('name') == change['name']
    assert els[guid].find('properties').get('documentation') == change['before'], guid
    pattern = (rb'(<element\s+xmi:idref="'+guid.encode()+rb'"[^>]*>.*?<properties\s+documentation=")([^"]*)(")')
    patterns.append(pattern)
    matches = list(re.finditer(pattern, out, re.S))
    assert len(matches) == 1
    m = matches[0]
    encoded = escape(change['after'], {'"':'&quot;', '\n':'&#10;', '\r':'&#13;', '\t':'&#9;'}).encode('utf-8')
    out = out[:m.start(2)] + encoded + out[m.end(2):]

def masked(data):
    for pattern in patterns:
        data, n = re.subn(pattern, lambda m:m.group(1)+b'FIELD'+m.group(3), data, flags=re.S)
        assert n == 1
    return data

assert masked(raw) == masked(out), 'Unexpected change outside the eight fields'
revised = parse(out)
new_els = elements(revised)
for change in changes:
    assert new_els[change['guid']].find('properties').get('documentation') == change['after']
for attribute in ['id', 'idref']:
    assert Counter(e.get(X+attribute) for e in original.iter() if e.get(X+attribute)) == Counter(e.get(X+attribute) for e in revised.iter() if e.get(X+attribute))
for section in ['connectors', 'diagrams']:
    assert E.tostring(original.find(X+'Extension').find(section)) == E.tostring(revised.find(X+'Extension').find(section))
assert SOURCE.read_bytes() == raw
if TARGET.exists():
    assert TARGET.read_bytes() == out, 'Refusing to overwrite another revision'
else:
    TARGET.write_bytes(out)
print(json.dumps({'file':TARGET.name, 'sha256':hashlib.sha256(out).hexdigest(), 'fields':len(changes), 'all_other_bytes_preserved':True, 'native_import_verified':False}))
