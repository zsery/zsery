from pathlib import Path
import json,csv,re,collections,hashlib
ROOT=Path(__file__).resolve().parents[2]
j=json.loads((ROOT/'work/ea/index.json').read_text(encoding='utf8'));es=j['elements']
marker='/01_07_2026_ServiceHub_Atlas_CZ_PR25_0837'
project={k:v for k,v in es.items() if v.get('path','').endswith(marker) or marker+'/' in v.get('path','')}
st=lambda e:e.get('properties',{}).get('stereotype',e.get('type',''))
ucs=sorted([v for v in project.values() if st(v)=='business use case'],key=lambda x:x['name'])
# Semantic correspondence proposals from names, not identity joins and not approved model edits.
correspondence={
 'UC001':('UC005','Obsahová návaznost','Přístup do SH. Doplnit aktuální DXL/role/automatické CRM ID a odlišit od historického UC čísla.'),
 'UC002':('UC006','Částečná návaznost','Zobrazení purchased services se překrývá s aktuálním UC006. Zachovat samostatný GUID a zkontrolovat překryv s původním UC004.'),
 'UC003':('UC010','Částečná návaznost','Seznam ticketů je dnes Atlas support request visibility pro aktivní autorizované CRM ID. Přesný field/status scope otevřen.'),
 'UC004':('UC006','Částečná návaznost','Service overview se překrývá s původním UC002. Dva modelové prvky neslučovat bez posouzení jejich obsahu a použití.'),
 'UC005':('UC010','Částečná návaznost','Ticket detail je součást dnešního UC010. Rozlišit list/detail, nezaměnit se současným UC005 login.'),
 'UC006':('UC007','Obsahová návaznost','Digitální vytvoření Atlas requestu. Úspěch až po potvrzení SNOW, správné aktivní CRM ID.'),
 'UC007':('UC008','Částečná návaznost','Asistovaná lokální cesta jen whitelisted V2 BCS/LME. Nový UC008 neprokazuje obecné jednání za zákazníka.'),
 'UC008':('','Group/MSO závislost','Triage je interní support činnost. Nová specifikace ji nečísluje jako samostatný key UC.'),
 'UC009':('','Group/MSO závislost','Resolver práce je Group/MSO závislost; není novým UC009, který znamená úplné ukončení Atlasu.'),
 'UC010':('','Nepotvrzeno aktuální specifikací','Service Desk on behalf není automaticky schváleným MVP use casem ani z něj neplyne impersonation/delegace.'),
 'UC011':('UC012','Částečná návaznost','Asistovaný onboarding je dnes část role MSO/LME v UC012. Rozlišit customer vytvoření, workflow a V4 manuální MVP.'),
 'UC012':('UC008 / EXC-04','Provozní návaznost','Eskalace je součást support/exception procesu, nikoli totožný dnešní UC012 onboarding.'),
 'UC013':('EXC-04','Provozní/Group návaznost','Group resolution feedback a closure jsou provozní závislosti, nejsou samostatným key UC v nové specifikaci.'),
 'UC014':('UC002 / UC012','Lifecycle závislost','Subscription activation a první order/managed onboarding nejsou stejný okamžik. Současný UC002 končí přijetím orderu, detail activation payloadu otevřen.'),
 'UC015':('UC006','Částečná návaznost','Marketplace data a zobrazení managed Atlas pro aktivní CRM ID. Přesný lifecycle state nezavádět odhadem.'),
 'UC016':('EXC-02 / EXC-04','Provozní návaznost','Data consistency, mismatch/delay a correction/escalation. Nová analýza nevymezuje samostatný key UC.'),
 'UC017':('UC002','Změnit kanál podle aktuálního MVP','Nové enablement kroky probíhají v Marketplace. BRD 1.2.7 říká, že SH není MVP sales/activation channel.'),
 'UC018':('UC009','Změnit kanál podle aktuálního UC','Plné ukončení: zákaznický kontakt → Frontline/Siebel → ICT Hub/Provisioning → Marketplace → SNOW/MSO. SH UI termination není tím potvrzeno.'),
 'UC019':('EXC-04','Provozní návaznost','Nonstandard/unsupported handling rozpracovat jako exception/operational postup podle schváleného rozsahu.'),
 'UC020':('UC002','Obsahová návaznost','Interní první enablement. Aktuálně předchází ověření VFID/admin v Logins a reuse/correction Marketplace záznamů.'),
 'UC021':('UC001','Částečná návaznost','Obchodní engagement rozpracovat proti aktuálnímu prodeji CRM a BidBot/OfferTool. UC001 končí smlouvou/výsledkem před Marketplace orderem.')
}
out=ROOT/'outputs/ea-revize';out.mkdir(exist_ok=True)
rows=[]
for e in ucs:
 old=re.match(r'UC\d+',e['name'])[0];new,kind,note=correspondence[old]
 edges=[c for c in j['connectors'] if e['id'] in [c['source'],c['target']]]
 rows.append({'EA GUID':e['id'],'EA UC ID':old,'EA název':e['name'],'Autor EA':e.get('project',{}).get('author',''),'EA cesta':e['path'],'Obsahová návaznost na nový zdroj':new,'Typ pracovní návaznosti':kind,'Rozhodnutí / omezení':note,'Incidentní konektory v exportním indexu':len(edges),'Stav':'Pracovní sémantické porovnání názvu a aktuálního UC; není provedená změna XMI'})
with (out/'EA_UC_obsahovy_crosswalk_2026-11-03.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter=';');w.writeheader();w.writerows(rows)
diagrams=[d for d in j['diagrams'] if '/01_07_2026_ServiceHub_Atlas_CZ_PR25_0837/' in d.get('path','')]
refs={x.get('subject') for d in diagrams for x in d.get('elements',[])}
external=[es[x] for x in refs if x in es and x not in project]
touch=[c for c in j['connectors'] if c['source'] in project or c['target'] in project]
real=[c for c in touch if c.get('properties',{}).get('stereotype')=='ArchiMate_Realization']
req=lambda id: id in es and st(es[id])=='ArchiMate_Requirement'
freq=lambda id:id in es and bool(re.match(r'(?:F-)?REQ-|^-REQ-',es[id]['name'])) and 'FREQs/' in es[id].get('path','')
directreq=[c for c in touch if freq(c['source']) or freq(c['target'])]
summary={'xmlSha256':j['sha256'],'projectElements':len(project),'projectDiagrams':len(diagrams),'projectBusinessUseCases':len(ucs),'projectExplicitArchiMateCapabilities':sum(st(e)=='ArchiMate_Capability' for e in project.values()),'allExplicitArchiMateCapabilities':sum(st(e)=='ArchiMate_Capability' for e in es.values()),'projectApplicationFunctions':sum(st(e)=='ArchiMate_ApplicationFunction' for e in project.values()),'projectTouchingConnectors':len(touch),'realizationConnectors':len(real),'realizationEndpointTypes':dict(collections.Counter(st(es.get(c['source'],{}))+' -> '+st(es.get(c['target'],{})) for c in real)),'freqIncidentConnectors':len(directreq),'externalDiagramElementTypes':dict(collections.Counter(st(e) for e in external)),'ucCoreCrossReferences':sum(any(v in {e['id'] for e in ucs} for k,v in x.get('attributes',{}).items() if not k.endswith('}id')) for x in j['core']),'limitations':'Observed XMI export/index, not live EA. Semantic correspondence proposals are not identity equivalence, approved requirements, or XMI edits.'}
(out/'EA_business_kontrola_2026-11-03.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
print(json.dumps([{'source':es[c['source']]['name'],'target':es[c['target']]['name'],'targetGuid':c['target']} for c in real if not es[c['target']]['name'].startswith('SREQ-')],ensure_ascii=False))
details={'constraints':[e for e in project.values() if st(e)=='ArchiMate_Constraint'],'nonSreqRealizationTargets':[es[c['target']] for c in real if not es[c['target']]['name'].startswith('SREQ-')]}
(out/'EA_constraints_zdroj_2026-11-03.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding='utf8')
