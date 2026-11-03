from pathlib import Path
import hashlib,zipfile,json
root=Path(__file__).resolve().parents[2]
repo=root/'work/github-zsery';bundle=repo/'atlas-work'
files=sorted(p for p in bundle.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt' and not p.name.startswith('~$') and '__pycache__' not in p.parts)
for p in files:
 assert p.suffix.lower() not in {'.dmp','.pem','.key','.exe','.dll'},p.name
 assert not p.name.startswith('~$') and '__pycache__' not in p.parts,p.name
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(bundle).as_posix()+'\n' for p in files)
(bundle/'SHA256SUMS.txt').write_text(manifest,encoding='utf8')
for line in manifest.splitlines():
 digest,rel=line.split('  ',1)
 assert hashlib.sha256((bundle/rel).read_bytes()).hexdigest()==digest,rel
archive=root/'outputs/Atlas_predani_po_oprave_Book1_2026-11-03.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for p in [repo/'Atlas.7z',repo/'Book1.xlsx',*files,bundle/'SHA256SUMS.txt']:
  z.write(p,p.relative_to(repo).as_posix())
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 for p in files:
  assert hashlib.sha256(z.read(p.relative_to(repo).as_posix())).hexdigest()==hashlib.sha256(p.read_bytes()).hexdigest()
 print(json.dumps({'manifestFiles':len(files),'zipEntries':len(z.namelist()),'zipBytes':archive.stat().st_size,'zipSha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'zipWorkbookSha256':hashlib.sha256(z.read('atlas-work/outputs/Book1_2026-11-03/Book1_Atlas_konsolidovany_2026-11-03.xlsx')).hexdigest()}))
