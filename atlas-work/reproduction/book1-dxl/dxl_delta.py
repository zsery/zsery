from pathlib import Path
import runpy, contextlib, io, json, hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
with contextlib.redirect_stdout(io.StringIO()):
    reader=runpy.run_path(str(HERE/'read_sources.py'))
canonical=ROOT/'outputs/Book1_2026-11-03/Book1_Atlas_konsolidovany_2026-11-03.xlsx'
assert hashlib.sha256(canonical.read_bytes()).hexdigest()=='10998f6652bcea8f0bdc357cd092663bed5334d21bf9db0255470a969fc786a2'
current=reader['read_book'](canonical)
old=json.loads((HERE/'validated-plan.json').read_text(encoding='utf8'))
new=json.loads((HERE/'changes.json').read_text(encoding='utf8'))
for sheet, cells in old['operations'].items():
    for ref, expected in cells.items():
        assert current[sheet]['cells'].get(ref,'')==expected,(sheet,ref)
delta={}
for sheet,cells in new['operations'].items():
    for ref,value in cells.items():
        if current[sheet]['cells'].get(ref,'')!=value:
            delta.setdefault(sheet,{})[ref]=value
result={**new,'operations':delta,'summary':{'changedCells':sum(map(len,delta.values())),'changedSheets':list(delta),'sourceSha256':hashlib.sha256(canonical.read_bytes()).hexdigest()}}
(HERE/'delta.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
(HERE/'canonical-before.xlsx').write_bytes(canonical.read_bytes())
print(json.dumps(result['summary'],ensure_ascii=False))
