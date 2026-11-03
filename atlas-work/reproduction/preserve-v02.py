"""Preserve original native Excel features while applying artifact-authored additions."""
from lxml import etree as E
from pathlib import Path
import zipfile,copy,posixpath,json,re
S='http://schemas.openxmlformats.org/spreadsheetml/2006/main';R='http://schemas.openxmlformats.org/officeDocument/2006/relationships';P='http://schemas.openxmlformats.org/package/2006/relationships';C='http://schemas.openxmlformats.org/package/2006/content-types';q=lambda n:'{'+S+'}'+n
orig=zipfile.ZipFile('outputs/book1-revize/Book1_MVP_revize_2026-11-01.xlsx');auth=zipfile.ZipFile('work/book1/v02-authored.xlsx');parts={n:orig.read(n) for n in orig.namelist()}
def xml(z,n):return E.fromstring(z.read(n))
def put(n,r):parts[n]=E.tostring(r,encoding='utf-8',xml_declaration=True)
os=xml(orig,'xl/styles.xml');ns=xml(auth,'xl/styles.xml');maps={}
for name in ['fonts','fills','borders','cellStyleXfs']:
 a=os.find(q(name));b=ns.find(q(name));maps[name]=len(a)
 for item in b:a.append(copy.deepcopy(item))
 a.set('count',str(len(a)))
fmtmap={};a=os.find(q('numFmts'));b=ns.find(q('numFmts'))
if a is None:a=E.Element(q('numFmts'));os.insert(0,a)
nextid=max({int(x.get('numFmtId')) for x in a}|{163})+1
if b is not None:
 for x in b:
  y=copy.deepcopy(x);fmtmap[int(x.get('numFmtId'))]=nextid;y.set('numFmtId',str(nextid));nextid+=1;a.append(y)
a.set('count',str(len(a)))
def fixxf(x):
 for attr,collection in [('fontId','fonts'),('fillId','fills'),('borderId','borders'),('xfId','cellStyleXfs')]:
  if attr in x.attrib:x.set(attr,str(int(x.get(attr))+maps[collection]))
 if int(x.get('numFmtId','0')) in fmtmap:x.set('numFmtId',str(fmtmap[int(x.get('numFmtId'))]))
for x in list(os.find(q('cellStyleXfs')))[maps['cellStyleXfs']:]:fixxf(x)
a=os.find(q('cellXfs'));offset=len(a)
for x in ns.find(q('cellXfs')):y=copy.deepcopy(x);fixxf(y);a.append(y)
a.set('count',str(len(a)));put('xl/styles.xml',os)
strings=list(xml(auth,'xl/sharedStrings.xml')) if 'xl/sharedStrings.xml' in auth.namelist() else []
def cellcopy(c):
 c=copy.deepcopy(c)
 if 's' in c.attrib:c.set('s',str(int(c.get('s'))+offset))
 if c.get('t')=='s':
  idx=int(c.find(q('v')).text);c.remove(c.find(q('v')));c.set('t','inlineStr');ins=E.SubElement(c,q('is'))
  for ch in strings[idx]:ins.append(copy.deepcopy(ch))
 return c
def sheetmap(z):
 wb=xml(z,'xl/workbook.xml');rels=xml(z,'xl/_rels/workbook.xml.rels');rm={r.get('Id'):posixpath.normpath('xl/'+r.get('Target')) if not r.get('Target').startswith('/') else r.get('Target').lstrip('/') for r in rels}
 return {s.get('name'):rm[s.get('{'+R+'}id')] for s in wb.find(q('sheets'))}
om=sheetmap(orig);am=sheetmap(auth)
def colno(ref):
 n=0
 for c in ref:
  if not c.isalpha():break
  n=n*26+ord(c)-64
 return n
def selected(name,ref):
 col=colno(ref);row=int(re.search(r'\d+',ref)[0])
 if name=='Cover':return col<=2 and 13<=row<=19
 if name=='Revize MVP':return col in [2,3] and row in [17,19]
 if name in ['FREQ mapping','SREQ Aplikační role']:return (col>=17 or col==16 and row>=2) and row<=220
 if name=='Functionalities':return col==12 and 2<=row<=956
 if name=='Interfaces':return col==10 and 2<=row<=55
 return False
modified=['Cover','Revize MVP','FREQ mapping','SREQ Aplikační role','Functionalities','Interfaces']
for name in modified:
 o=xml(orig,om[name]);a=xml(auth,am[name]);od=o.find(q('sheetData'));ad=a.find(q('sheetData'));rows={int(r.get('r')):r for r in od}
 for row in ad:
  ri=int(row.get('r'));cells=[c for c in row if selected(name,c.get('r'))]
  if not cells:continue
  target=rows.get(ri)
  if target is None:target=E.SubElement(od,q('row'),{'r':str(ri)});rows[ri]=target
  existing={c.get('r'):c for c in target}
  for c in cells:
   if c.get('r') in existing:target.remove(existing[c.get('r')])
   target.append(cellcopy(c))
  target[:]=sorted(target,key=lambda c:colno(c.get('r')))
  if name=='Cover':target.set('ht','60');target.set('customHeight','1')
 if name in ['FREQ mapping','SREQ Aplikační role']:
  cols=o.find(q('cols'))
  if cols is None:cols=E.Element(q('cols'));o.insert(list(o).index(od),cols)
  ac=a.find(q('cols'))
  if ac is not None:
   for c in ac:
    if int(c.get('max'))>=17:
     c=copy.deepcopy(c);c.set('min',str(max(int(c.get('min')),17)));cols.append(c)
  if o.find(q('dimension')) is not None:o.find(q('dimension')).set('ref','A1:W220')
 if name=='Cover' and o.find(q('dimension')) is not None:o.find(q('dimension')).set('ref','A1:B19')
 put(om[name],o)
wb=xml(orig,'xl/workbook.xml');rels=xml(orig,'xl/_rels/workbook.xml.rels');types=xml(orig,'[Content_Types].xml');sheets=wb.find(q('sheets'));maxid=max(int(s.get('sheetId')) for s in sheets)
newnames=['Postup revize','Business a FREQ','EA SREQ']
for i,name in enumerate(newnames,1):
 new=xml(auth,am[name])
 for row in new.find(q('sheetData')):
  for c in list(row):row.replace(c,cellcopy(c))
 for col in new.findall(q('cols')+'/'+q('col')):
  if 'style' in col.attrib:col.set('style',str(int(col.get('style'))+offset))
 newpath='xl/worksheets/book1_v02_'+str(i)+'.xml';put(newpath,new)
 rid='rIdBook1v02_'+str(i);node=E.Element(q('sheet'),{'name':name,'sheetId':str(maxid+i),'{'+R+'}id':rid});sheets.insert(i,node)
 E.SubElement(rels,'{'+P+'}Relationship',{'Id':rid,'Type':R+'/worksheet','Target':'worksheets/'+posixpath.basename(newpath)})
 E.SubElement(types,'{'+C+'}Override',{'PartName':'/'+newpath,'ContentType':'application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml'})
put('xl/workbook.xml',wb);put('xl/_rels/workbook.xml.rels',rels);put('[Content_Types].xml',types)
out=Path('outputs/book1-v02/Book1_Atlas_pracovni_v02_2026-11-01.xlsx');out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for n,b in parts.items():z.writestr(n,b)
final=zipfile.ZipFile(out);preserved=changed=0
for name,p in om.items():
 a=xml(orig,p);b=xml(final,p);ac={c.get('r'):c for c in a.findall('.//'+q('sheetData')+'/'+q('row')+'/'+q('c'))};bc={c.get('r'):c for c in b.findall('.//'+q('sheetData')+'/'+q('row')+'/'+q('c'))}
 for k,v in ac.items():
  if selected(name,k):changed+=1;continue
  assert E.tostring(v)==E.tostring(bc.get(k)),(name,k)
  preserved+=1
for n in orig.namelist():
 if n.startswith(('xl/tables/','xl/externalLinks/','xl/metadata')):assert orig.read(n)==final.read(n),n
report={'unaffectedOriginalCellsPreserved':preserved,'authorizedOriginalCellsUpdated':changed,'originalTablesPreserved':7,'externalLinkPartsPreserved':2,'sheets':len(sheets),'newSheets':newnames,'outputBytes':out.stat().st_size}
Path('work/book1/v02-native-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report,ensure_ascii=False))
