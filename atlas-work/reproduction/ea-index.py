from lxml import etree as E
from collections import Counter
import json,re,hashlib
from pathlib import Path
p=Path('work/ea/Atlas-original.xml');tree=E.parse(str(p),E.XMLParser(resolve_entities=False,no_network=True,huge_tree=True));root=tree.getroot();X='{http://schema.omg.org/spec/XMI/2.1}'
ext=root.find(X+'Extension');model=root.find('{http://schema.omg.org/spec/UML/2.1}Model')
def at(e):return dict(e.attrib) if e is not None else {}
els={}
for e in ext.find('elements'):
 id=e.get(X+'idref');els[id]={'id':id,'name':e.get('name',''),'type':e.get(X+'type',''),'model':at(e.find('model')),'properties':at(e.find('properties')),'project':at(e.find('project')),'documentation':at(e.find('documentation')),'tags':[dict(t.attrib) for t in e.findall('tags/tag')],'xrefs':E.tostring(e.find('xrefs'),encoding='unicode') if e.find('xrefs') is not None else ''}
def path(id,seen=None):
 seen=set() if seen is None else seen
 if not id or id not in els or id in seen:return ''
 seen.add(id);e=els[id];return path(e['model'].get('package'),seen)+'/'+e['name']
for id,e in els.items():e['path']=path(id)
cons=[]
for e in ext.find('connectors'):
 s=e.find('source');t=e.find('target');cons.append({'id':e.get(X+'idref'),'source':s.get(X+'idref') if s is not None else None,'target':t.get(X+'idref') if t is not None else None,'properties':at(e.find('properties')),'documentation':at(e.find('documentation')),'labels':at(e.find('labels')),'tags':[dict(t.attrib) for t in e.findall('tags/tag')]})
diags=[]
for e in ext.find('diagrams'):
 d={'id':e.get(X+'id'),'model':at(e.find('model')),'properties':at(e.find('properties')),'project':at(e.find('project')),'elements':[dict(t.attrib) for t in e.findall('elements/element')]};d['path']=path(d['model'].get('package'));diags.append(d)
# Core UML element attributes/operations, including sequence messages, retained independently.
core=[]
for e in model.iter():
 if e.get(X+'id'):
  core.append({'id':e.get(X+'id'),'tag':E.QName(e).localname,'attributes':dict(e.attrib),'children':[{'tag':E.QName(c).localname,'attributes':dict(c.attrib)} for c in e if E.QName(c).localname in ['ownedAttribute','ownedOperation','lifeline','message','fragment','ownedParameter']]})
doc={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'elements':els,'connectors':cons,'diagrams':diags,'core':core}
Path('work/ea/index.json').write_text(json.dumps(doc,ensure_ascii=False),encoding='utf8')
print('COUNTS',len(els),len(cons),len(diags),len(core));print('AUTHORS',Counter(e['project'].get('author') for e in els.values()).most_common(8));print('STEREOTYPES',Counter(e['properties'].get('stereotype') for e in els.values()).most_common(16))
print('PROJECT PACKAGES')
for e in els.values():
 if e['type']=='uml:Package' and re.search('Atlas|Service.?Hub|PR25.0837',e['name'],re.I):print(e['id'],e['path'])
print('DIAGRAMS')
for d in diags:
 if re.search('Atlas|Service.?Hub|PR25.0837|SSO|CustomerContext|domain|integrat',d['properties'].get('name','')+' '+d['path'],re.I):print(d['id'],d['path'],d['properties'],d['project'],len(d['elements']))
