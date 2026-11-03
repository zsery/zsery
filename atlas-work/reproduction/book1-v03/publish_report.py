from pathlib import Path
import json,csv
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
plan=json.loads((HERE/'changes.json').read_text(encoding='utf8'))
books=json.loads((HERE/'sources.json').read_text(encoding='utf8'))
out=ROOT/'outputs/Book1_2026-11-03'
report=json.loads((HERE/'verification.json').read_text(encoding='utf8'))
report['artifactReimport']=json.loads((HERE/'reimport-qa.json').read_text(encoding='utf8'))
(out/'Kontrola_konsolidace.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
with (out/'Zmeny_bunek.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['List','Bunka','Predchozi hodnota v02','Nova hodnota v03','Duvod'])
 for s,changes in plan['operations'].items():
  for ref,value in changes.items():w.writerow([s,ref,books['base'][s]['cells'].get(ref,''),value,plan['reasons'][s+'!'+ref]])
print('Published verification JSON and 702-row change log.')
