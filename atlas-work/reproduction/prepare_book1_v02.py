import json,re,html,collections,zipfile
from lxml import etree as E
from pathlib import Path
d=json.load(open('work/ea/index.json',encoding='utf8'));es=d['elements'];b=json.load(open('work/book1/data.json',encoding='utf8'));scope='01_07_2026_ServiceHub_Atlas_CZ_PR25_0837'
p={i:e for i,e in es.items() if scope in e['path']};reqs=[e for e in p.values() if e['properties'].get('stereotype')=='ArchiMate_Requirement']
def clean(s):return html.unescape(re.sub('<[^>]+>','',s or '')).strip()
def ids(e,prefix):return list(dict.fromkeys(re.findall(r'\b'+prefix+r'-[A-Z]+-\d+\b',e['name']+' '+e['properties'].get('alias',''))))
sr=collections.defaultdict(list)
for e in reqs:
 for id in ids(e,'SREQ'):sr[id].append(e)
adj=collections.defaultdict(list)
for c in d['connectors']:
 adj[c['source']].append(c);adj[c['target']].append(c)
def related(e,stereos):
 out=[]
 for c in adj[e['id']]:
  oid=c['target'] if c['source']==e['id'] else c['source'];o=es.get(oid,{})
  if o.get('properties',{}).get('stereotype') in stereos:out.append(o['name']+' ['+oid+']; '+c['properties'].get('stereotype',c['properties'].get('ea_type',''))+'; '+c['id'])
 return '\n'.join(out)
freqrows=[]
for e in reqs:
 if not re.match(r'^F?-REQ-',e['name']):continue
 raw=ids(e,'F-REQ');broken=not raw
 rawid=raw[0] if raw else re.match(r'^(-REQ-[A-Z]+-\d+)',e['name']).group(1)
 tag='K OVĚŘENÍ PROTI NEJNOVĚJŠÍ ANALÝZE'
 issue='EA text je vstupní inventura; aktuálnost a schválení business požadavku neověřeny.'
 if broken:issue='Název EA začíná -REQ místo F-REQ; ID není automaticky opraveno. '+issue
 if rawid.startswith('F-REQ-CHM-') and int(rawid.rsplit('-',1)[1]) in [1,2,3,4,6,7,8,10,11,12,13,14,15,16,17,21]:
  tag='ROZPOR / HISTORIE VŮČI MVP';issue+=' Portálový entrypoint/navigaci/handover ověřit vůči B1; nenahrazovat tím SSO.'
 freqrows.append([rawid,clean(e['name']),clean(e['properties'].get('documentation','')),e['id'],e['path'],e['project'].get('author',''),e['project'].get('modified',''),'E1 — EA export; business zdroj zatím nedoložen u řádku',tag,'',related(e,{'ArchiMate_Capability'}),related(e,{'ArchiMate_BusinessProcess','BusinessProcess','ArchiMate_BusinessService','ArchiMate_BusinessRole','ArchiMate_BusinessObject'}),related(e,{'ArchiMate_Requirement'}),'K doplnění po potvrzení business významu','',issue,'ČEKÁ — ověřit analýzu → scope → business vazby'])
uc=[
 ('Přihlášení','Uživatel se autentizuje přes VFID; při selhání autentizace nelze vytvořit odpovídající přihlášený přístup.'),
 ('Vstupní vztahy a role','ServiceHub získá přes DXL vztahy uživatele, role a dostupná CRM ID jako vstup pro přístup ke specifickému obsahu.'),
 ('Admin eligibility','Oprávněný admin získá specifický obsah; přihlášený uživatel bez admin role má obecnou stránku.'),
 ('Automatická volba kontextu','Automaticky se zvolí jedno dostupné CRM ID; priorita automatické volby není doložena.'),
 ('Přepínání kontextu','Uživatel může následně přepínat mezi dostupnými CRM ID pomocí Customer Selectoru.'),
 ('Chybějící zákaznický kontext','Bez CRM ID nebo při příslušném selhání získání dat nelze zobrazit zákaznicky specifický obsah; detail chybových stavů je třeba rozlišit podle UC.')]
for name,text in uc:
 freqrows.append(['','UC005 — '+name,text,'','','Martin Dostál','14.10.2026 — Last Update specifikace','U1 — UC005 s. 19–21; parafráze přímo přečtené analýzy','ANALYTICKÝ VSTUP — SPÁROVAT S FREQ','','','','','Group chování; CZ integrační/datové vstupy — zpřesnit','','Nevytvořeno nové FREQ ID. Nesloučit s Atlas subscription eligibility UC006.','ČEKÁ — dohledat kanonické FREQ a business vazby'])
mapping=[]
for n,r in enumerate(b['FREQ mapping']['values'][1:],2):
 xs=sr.get(str(r[5] or ''),[])
 marker='SREQ ID nalezeno; obsah a scope nejsou tím potvrzeny' if xs else 'SREQ ID nenalezeno v projektové větvi — dohledat nahrazení/konsolidaci'
 issue=''
 if any(e['properties'].get('documentation')=='MVP' for e in xs):issue='EA poznámka MVP sama nepotvrzuje soulad s B1 ani aktuální analýzou.'
 if n in [6,7,28]:issue+=' Historický obsahový rozpor mapování: vyřešit podle zdroje, ne podle stejného ID.'
 mapping.append([marker,'\n'.join(e['id'] for e in xs),'\n'.join(e['name'] for e in xs),'\n'.join(clean(e['properties'].get('documentation','')) for e in xs),'\n'.join(related(e,{'ArchiMate_ApplicationFunction'}) for e in xs),'E1 — porovnání aplikace/SREQ; ID je vyhledáno v projektové větvi',issue or 'Ověřit nejnovější business text, FREQ vazbu a odpovědnost Group/CZ.'])
ea_sreq=[]
for e in reqs:
 if not ids(e,'SREQ'):continue
 ea_sreq.append([ids(e,'SREQ')[0],e['id'],e['name'],clean(e['properties'].get('documentation','')),e['project'].get('author',''),e['project'].get('modified',''),related(e,{'ArchiMate_ApplicationFunction'}),'E1','INVENTURA — NENÍ POTVRZENÁ BASELINE','', '',''])
z=zipfile.ZipFile('outputs/book1-revize/Book1_MVP_revize_2026-11-01.xlsx');ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
def notes(path,col,first,last):
 root=E.fromstring(z.read(path));cells={c.get('r'):c for c in root.iter(ns+'c')};out=[]
 for i in range(first,last+1):
  c=cells.get(col+str(i));v=c.find(ns+'v') if c is not None else None
  out.append(v.text if v is not None and v.text is not None else ''.join(c.itertext()) if c is not None else '')
 return out
Path('work/book1/v02-data.json').write_text(json.dumps({'business':freqrows,'mapping':mapping,'sreq':ea_sreq,'sha':d['sha256'],'functionNotes':notes('xl/worksheets/sheet3.xml','L',2,956),'interfaceNotes':notes('xl/worksheets/sheet4.xml','J',2,55)},ensure_ascii=False),encoding='utf8')
print(json.dumps({'businessRows':len(freqrows),'eaFreqRows':len(freqrows)-len(uc),'ucInputs':len(uc),'eaSreqElements':len(ea_sreq),'mappingRows':len(mapping)}))
