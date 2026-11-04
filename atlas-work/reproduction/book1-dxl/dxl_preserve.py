from pathlib import Path
from lxml import etree as E
import zipfile,json,posixpath,copy,re,hashlib
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
S='http://schemas.openxmlformats.org/spreadsheetml/2006/main';R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
q=lambda n:'{'+S+'}'+n
plan=json.loads((HERE/'delta.json').read_text(encoding='utf8'))
base=zipfile.ZipFile(HERE/'canonical-before.xlsx')
author=zipfile.ZipFile(HERE/'authored.xlsx')
parts={n:base.read(n) for n in base.namelist()}
def xml(z,n):return E.fromstring(z.read(n))
def save(p,node):parts[p]=E.tostring(node,encoding='utf-8',xml_declaration=True)
def sheetmap(z):
 wb=xml(z,'xl/workbook.xml');rs=xml(z,'xl/_rels/workbook.xml.rels')
 rm={r.get('Id'):posixpath.normpath('xl/'+r.get('Target')) if not r.get('Target').startswith('/') else r.get('Target').lstrip('/') for r in rs}
 return {s.get('name'):rm[s.get('{'+R+'}id')] for s in wb.find(q('sheets'))}
bm=sheetmap(base);am=sheetmap(author)
styles=xml(base,'xl/styles.xml');astyles=xml(author,'xl/styles.xml');offsets={}
for name in ['fonts','fills','borders','cellStyleXfs']:
 a=styles.find(q(name));b=astyles.find(q(name));offsets[name]=len(a)
 for x in b:a.append(copy.deepcopy(x))
 a.set('count',str(len(a)))
fmtmap={};dest=styles.find(q('numFmts'));src=astyles.find(q('numFmts'))
if dest is None:dest=E.Element(q('numFmts'));styles.insert(0,dest)
nextid=max({int(x.get('numFmtId')) for x in dest}|{163})+1
if src is not None:
 for x in src:
  n=copy.deepcopy(x);fmtmap[int(x.get('numFmtId'))]=nextid;n.set('numFmtId',str(nextid));nextid+=1;dest.append(n)
dest.set('count',str(len(dest)))
def fixxf(x):
 for attr,coll in [('fontId','fonts'),('fillId','fills'),('borderId','borders'),('xfId','cellStyleXfs')]:
  if attr in x.attrib:x.set(attr,str(int(x.get(attr))+offsets[coll]))
 old=int(x.get('numFmtId','0'))
 if old in fmtmap:x.set('numFmtId',str(fmtmap[old]))
for x in list(styles.find(q('cellStyleXfs')))[offsets['cellStyleXfs']:]:fixxf(x)
dest=styles.find(q('cellXfs'));style_offset=len(dest)
for x in astyles.find(q('cellXfs')):
 n=copy.deepcopy(x);fixxf(n);dest.append(n)
dest.set('count',str(len(dest)));save('xl/styles.xml',styles)
strings=list(xml(author,'xl/sharedStrings.xml')) if 'xl/sharedStrings.xml' in author.namelist() else []
def cp(c):
 c=copy.deepcopy(c)
 if c.get('s') is not None:c.set('s',str(int(c.get('s'))+style_offset))
 if c.get('t')=='s':
  v=c.find(q('v'));idx=int(v.text);c.remove(v);c.set('t','inlineStr');node=E.SubElement(c,q('is'))
  for x in strings[idx]:node.append(copy.deepcopy(x))
 return c
def colnum(ref):
 n=0
 for x in re.match('[A-Z]+',ref)[0]:n=n*26+ord(x)-64
 return n
row_heights={}
for name in plan['operations']:
 row_heights.setdefault(name,set()).update(int(re.search(r'\d+',ref)[0]) for ref in plan['operations'].get(name,{}) if int(re.search(r'\d+',ref)[0])>1)
for name,changes in plan['operations'].items():
 o=xml(base,bm[name]);a=xml(author,am[name]);data=o.find(q('sheetData'))
 rows={int(r.get('r')):r for r in data};arows={int(r.get('r')):r for r in a.find(q('sheetData'))}
 ac={c.get('r'):c for c in a.findall('.//'+q('sheetData')+'/'+q('row')+'/'+q('c'))}
 for ref in changes:
  ri=int(re.search(r'\d+',ref)[0]);row=rows.get(ri)
  if row is None:row=E.SubElement(data,q('row'),{'r':str(ri)});rows[ri]=row
  old=row.find(q('c')+"[@r='"+ref+"']")
  if old is not None:row.remove(old)
  assert ref in ac,('Missing authored cell',name,ref)
  row.append(cp(ac[ref]));row[:]=sorted(row,key=lambda c:colnum(c.get('r')))
 for ri in row_heights.get(name,set()):
  for attr in ['ht','customHeight']:
   value=arows.get(ri).get(attr) if ri in arows else None
   if value is not None:rows[ri].set(attr,value)
 data[:]=sorted(data,key=lambda r:int(r.get('r')))
 dim=o.find(q('dimension'))
 if dim is not None:
  # Existing used area may include deliberate empty formatting; only extend it.
  refs=[c.get('r') for c in data.iter(q('c'))]
  maxrow=max(int(re.search(r'\d+',r)[0]) for r in refs);maxcol=max(colnum(r) for r in refs)
  old=dim.get('ref').split(':')[-1];maxrow=max(maxrow,int(re.search(r'\d+',old)[0]));maxcol=max(maxcol,colnum(old))
  label='';n=maxcol
  while n:n,rem=divmod(n-1,26);label=chr(65+rem)+label
  dim.set('ref',f'A1:{label}{maxrow}')
 if False:
  cols=o.find(q('cols'));acol=a.find(q('cols'))
  for col in acol:
   if int(col.get('min'))>=18 and int(col.get('max'))<=19:
    n=copy.deepcopy(col)
    if n.get('style') is not None:n.set('style',str(int(n.get('style'))+style_offset))
    cols.append(n)
 save(bm[name],o)
outdir=ROOT/'outputs/Book1_2026-11-03';outdir.mkdir(exist_ok=True)
out=outdir/'Book1_Atlas_konsolidovany_2026-11-03.xlsx'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for n,data in parts.items():z.writestr(n,data)
final=zipfile.ZipFile(out);preserved_cells=0;new_cells=0;formula_count=0;untouched_parts=[]
assert final.testzip() is None
assert set(base.namelist())==set(final.namelist()),'Unexpected package part changes'
assert sheetmap(final)==bm,'Sheet identities/order changed'
allowed_parts={'xl/styles.xml'}|{bm[s] for s in plan['operations']}
for n in base.namelist():
 if n not in allowed_parts:
  assert base.read(n)==final.read(n),('Unintended package mutation',n);untouched_parts.append(n)
for name,p in bm.items():
 a=xml(base,p);b=xml(final,p)
 ac={c.get('r'):c for c in a.findall('.//'+q('sheetData')+'/'+q('row')+'/'+q('c'))};bc={c.get('r'):c for c in b.findall('.//'+q('sheetData')+'/'+q('row')+'/'+q('c'))}
 changes=plan['operations'].get(name,{})
 for ref,c in ac.items():
  assert ref in bc,('Deleted cell',name,ref)
  if ref not in changes:
   assert E.tostring(c)==E.tostring(bc[ref]),('Unintended cell mutation',name,ref);preserved_cells+=1
  if c.find(q('f')) is not None:
   assert E.tostring(c.find(q('f')))==E.tostring(bc[ref].find(q('f'))),('Changed formula',name,ref);formula_count+=1
 for ref in set(bc)-set(ac):assert ref in changes;new_cells+=1
 for ref,expected in changes.items():
  c=bc[ref]
  if c.get('t')=='inlineStr':actual=''.join(c.find(q('is')).itertext())
  elif c.get('t')=='s':raise AssertionError(('Unexpected shared string reference',name,ref))
  else:actual=c.find(q('v')).text if c.find(q('v')) is not None else ''
  assert actual==expected,('Authored value mismatch',name,ref)
 # Preserve filter/validation/table state and all original hidden row/column attributes.
 excluded=['sheetData','dimension']+[]
 meta_a=[E.tostring(child) for child in a if E.QName(child).localname not in excluded]
 meta_b=[E.tostring(child) for child in b if E.QName(child).localname not in excluded]
 assert meta_a==meta_b,('Changed sheet metadata',name)
 if False:
  oldcols=list(a.find(q('cols')));newcols=list(b.find(q('cols')))
  assert [E.tostring(x) for x in newcols[:len(oldcols)]]==[E.tostring(x) for x in oldcols]
  assert newcols[len(oldcols):] and all(int(x.get('min'))>=18 and int(x.get('max'))<=19 for x in newcols[len(oldcols):])
 for row in a.find(q('sheetData')):
  ri=int(row.get('r'));after=b.find(q('sheetData')+'/'+q('row')+"[@r='"+str(ri)+"']")
  for k,v in row.attrib.items():
   if k in ['ht','customHeight'] and ri in row_heights.get(name,set()):continue
   assert after.get(k)==v,('Changed row state',name,ri,k)
all_cells={}
for name,p in bm.items():
 all_cells[name]={c.get('r'):c for c in xml(final,p).findall('.//'+q('sheetData')+'/'+q('row')+'/'+q('c'))}
errors=[name+'!'+ref+': '+str(c.find(q('v')).text if c.find(q('v')) is not None else '') for name,cs in all_cells.items() for ref,c in cs.items() if c.get('t')=='e']
baseerrors=[name+'!'+c.get('r')+': '+str(c.find(q('v')).text if c.find(q('v')) is not None else '') for name,p in bm.items() for c in xml(base,p).findall('.//'+q('sheetData')+'/'+q('row')+'/'+q('c')) if c.get('t')=='e']
assert errors==baseerrors,('Formula error cache changed',errors,baseerrors)
report={**plan['summary'],'output':str(out),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'sheets':list(bm),
 'preservedUnchangedCells':preserved_cells,'newAuthoredCells':new_cells,'originalFormulasPreserved':formula_count,
 'nativeTablePartsPreserved':sum(n.startswith('xl/tables/') and n.endswith('.xml') for n in untouched_parts),
 'externalLinkPartsPreserved':sum(n.startswith('xl/externalLinks/') for n in untouched_parts),
 'unchangedPackageParts':len(untouched_parts),'preExistingFormulaErrors':errors,'unintendedChanges':0,
 'nativeExcelRecalculation':'Not performed; no new formulas added; existing formula text/cache preserved byte-for-byte.'}
(HERE/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))

