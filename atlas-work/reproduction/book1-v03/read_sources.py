from pathlib import Path
from lxml import etree as E
import zipfile,json,posixpath,re
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
S='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
q=lambda n:'{'+S+'}'+n
FILES={
 'first':'outputs/book1-revize/Book1_MVP_revize_2026-11-01.xlsx',
 'base':'outputs/book1-v02/Book1_Atlas_pracovni_v02_2026-11-01.xlsx',
 'identity':'outputs/Book1_Solution_2026-11-02/Book1_Atlas_MVP_revize_2026-11-02.xlsx'}
def read_book(path):
 with zipfile.ZipFile(path) as z:
  strings=[]
  if 'xl/sharedStrings.xml' in z.namelist():
   strings=[''.join(s.itertext()) for s in E.fromstring(z.read('xl/sharedStrings.xml'))]
  wb=E.fromstring(z.read('xl/workbook.xml'))
  rels=E.fromstring(z.read('xl/_rels/workbook.xml.rels'))
  rm={r.get('Id'):posixpath.normpath('xl/'+r.get('Target')) if not r.get('Target').startswith('/') else r.get('Target').lstrip('/') for r in rels}
  books={}
  for s in wb.find(q('sheets')):
   p=rm[s.get('{'+R+'}id')];root=E.fromstring(z.read(p));cells={};formulas={}
   for c in root.findall('.//'+q('sheetData')+'/'+q('row')+'/'+q('c')):
    ref=c.get('r');t=c.get('t');v=c.find(q('v'));f=c.find(q('f'))
    if f is not None:formulas[ref]=E.tostring(f).decode()
    if t=='s':value=strings[int(v.text)] if v is not None and v.text else ''
    elif t=='inlineStr':value=''.join(c.find(q('is')).itertext())
    else:value=v.text if v is not None else ''
    if value!='' or f is not None:cells[ref]=value
   books[s.get('name')]={'path':p,'cells':cells,'formulas':formulas,'state':s.get('state','visible')}
  return books
books={k:read_book(ROOT/p) for k,p in FILES.items()}
changes=[]
for name,ss in books['identity'].items():
 for ref,v in ss['cells'].items():
  old=books['first'][name]['cells'].get(ref,'')
  if old!=v:changes.append({'sheet':name,'cell':ref,'old':old,'identity':v,'base':books['base'][name]['cells'].get(ref,'')})
(OUT/'sources.json').write_text(json.dumps(books,ensure_ascii=False,indent=2),encoding='utf8')
(OUT/'identity-delta.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'sheets':{k:list(v) for k,v in books.items()},'deltaCounts':{n:sum(c['sheet']==n for c in changes) for n in books['identity']},'deltas':[{'sheet':c['sheet'],'cell':c['cell'],'identity':c['identity'][:180],'base':c['base'][:100]} for c in changes if c['sheet']!='EAM App'],'headers':{n:{r:v for r,v in b['cells'].items() if re.match(r'^[A-Z]+1$',r)} for n,b in books['base'].items()}},ensure_ascii=False,indent=2))
