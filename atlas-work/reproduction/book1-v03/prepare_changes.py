from pathlib import Path
import json,re,unicodedata,collections
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
books=json.loads((HERE/'sources.json').read_text(encoding='utf8')); base=books['base']
delta=json.loads((HERE/'identity-delta.json').read_text(encoding='utf8'))
ops={}; reasons={}
def put(s,c,v,why):
 ops.setdefault(s,{})[c]=v;reasons[s+'!'+c]=why
def append(s,c,v,why):
 old=ops.get(s,{}).get(c,base[s]['cells'].get(c,''))
 if v not in old:put(s,c,old+'\n'+v if old else v,why)
def vals(s,r,cols):return [base[s]['cells'].get(c+str(r),'') for c in cols]
def norm(s):
 s=re.sub(r'^F?-?REQ-[A-Z]+-\d+\s*[:\-]?\s*','',s.strip(),flags=re.I)
 return re.sub(r'[^a-z0-9]+',' ',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip()
meaning=[c for c in delta if c['sheet']!='EAM App']
assert len(meaning)==23,len(meaning)
for c in meaning:
 s,ref,old,new=c['sheet'],c['cell'],c['old'],c['identity'];existing=base[s]['cells'].get(ref,'')
 if not old or old==existing:value=new
 elif new.startswith(old):value=existing+new[len(old):]
 else:raise ValueError(('Unresolved three-way merge',s,ref))
 put(s,ref,value,'Přenos věcné změny z 2.11.; třícestné sloučení proti první revizi a v02.')

cover=[
 ['Book1, konsolidovaná verze 03','3. 11. 2026. Sloučena rozšířená v02, pravidla identity z 2.11. a uložená pozorování SharePointu.'],
 ['Dokončeno v této verzi','Jedna pracovní verze se 14 listy. Přeneseno všech 23 věcných změn z 2.11.; původní EAM, vzorce, tabulky a externí vazby zachovány.'],
 ['Stav business baseline','NEUZAVŘENA: úplný aktuální BRD/UC a všechny Martinovy požadavky nebyly obsahově ověřeny. Tato verze není potvrzením úplné schválené baseline.'],
 ['Business a FREQ','159 EA FREQ záznamů a 6 analytických vstupů UC005. Přesná textová shoda a rozpory vůči Book1 jsou evidovány u řádků.'],
 ['Pravidla uživatele','VFID sub a odpovídající ONSC/WSC user 1:1; email není párovací klíč. TMF691: holding parent–child.'],
 ['Co zůstává otevřené','Kanonické FREQ/verze a capability vazby; technický DXL token kontrakt; Marketplace/Siebel opravy dat; aktuálnost všech SREQ.'],
 ['EA a SO','Atlas.xml nebyl změněn a Word SO nebyl aktualizován. Připravená evidence není důkazem hotové změny modelu nebo dokumentu.']]
for r,row in enumerate(cover,13):
 for col,v in zip('AB',row):put('Cover',col+str(r),v,'Aktuální čitelný stav celé dodávky.')
put('Postup revize','A2','BOOK1, KONSOLIDOVANÁ VERZE 03','Aktualizace stavu.')
put('Postup revize','B2','3. 11. 2026','Datum konsolidace.')
put('Postup revize','C2','Sloučena v02 a všech 23 věcných změn identity z 2.11.; doplněny uložené poznatky SharePointu.','Aktualizace stavu.')
put('Postup revize','D2','KONSOLIDACE DOKONČENA. Úplná business baseline, EA změny a SO zůstávají neuzavřené.','Oddělení dokončené konsolidace od nedokončené odborné revize.')
put('Postup revize','A6','Rozsah v03','Aktualizace verze.')
put('Postup revize','B9','PR25_0837_ServiceHub_Atlas_BRD.docx: titul 0.1; historie uvádí 0.2 z 23.10.; 25 stran.','Uložená pozorování SharePointu 2.11.')
put('Postup revize','C9','B2; notes/atlas-sharepoint-review-2026-11-02.md. Dřívější tvrzení verze 0.7 není ověřené.','Oprava evidence revize BRD.')
put('Postup revize','D9','OTEVŘENO: sjednotit titul a revizní historii, potvrdit poslední vydání a dokončit čtení.','Pravdivý stav zdroje.')
put('Postup revize','D8','Záznam z 2.11.: 51 stran, 13 171 slov, titul 0.1 / 14.10. Detailněji UC005; všech 12 UC není zvalidováno.','Záznam rozsahu skutečného čtení.')
put('Postup revize','D16','DOPLNĚNO: převzaty doložené výklady UC005 a přesné textové vazby. Kanonické FREQ a schválení jsou stále otevřené.','Zpřesnění postupu.')
put('Postup revize','B33','Sloučení v02 a identity; textové porovnání FREQ; workbookové reference do EA SREQ; doplnění pozorování ze 2.11.','Popis provedených změn.')
put('Postup revize','C33','Srovnání první revize, v02 a sešitu z 2.11.; uložené poznámky z VDI.','Provenance.')
newcontrols=[
 ['U2, identita uživatele','VFID sub a odpovídající ONSC user / WSC user jsou vždy 1:1. E-mail není párovací klíč.','Výslovné pravidlo uživatele, 2.11.2026.','ZAPRACOVÁNO: Interfaces, Functionalities, FREQ mapping, SREQ Aplikační role, EA SREQ a Revize MVP.'],
 ['U2, holding','TMF691 nese holding jako strukturu parent–child.','Výslovné pravidlo uživatele, 2.11.2026.','ZAPRACOVÁNO jako pravidlo; konkrétní payload a další kardinality čekají na API kontrakt.'],
 ['Zdroje, TR1','PR25_0837_ServiceHub_Atlas_Traceability_Decomposition.xlsx, list Traceability.','Pozorování 2.11.: 26 datových řádků, C101–C106, UC001–012, P01–P10, Sell/Build/Run.','Zdroj business traceability nemá FREQ/SREQ ID. Úplný řádkový přepis není uložen; nevytvářet vazby z pouhého seznamu capability.'],
 ['Zdroje, bezpečnost Marketplace','BSR_Appdirect_2023_Update...xlsx; 16 listů.','Pozorování 2.11.: baseline 2.6 z 1.4.2019, AppDirect aktualizace 2023.','Historický supplier assessment; odpovědi nejsou aktuální Atlas/ServiceHub bezpečnostní požadavky.'],
 ['UC005, chybové větve','Neúspěšná autentizace zastaví tok před DXL; bez role/CRM ID obecný obsah; nedostupné DXL obecný/nedostupný výsledek.','U1; uložený detail UC005 z 2.11.','DOPLNĚNO v Business a FREQ. Nezaměňovat s UC006 subscription eligibility.'],
 ['UC005, neplatný výběr','CRM ID, které už není dostupné, se nesmí aktivovat; selector se obnoví.','U1; uložený detail UC005 z 2.11.','DOPLNĚNO. Priorita počáteční automatické volby zůstává nedoložená.'],
 ['Model, capability a BPMN','V projektové větvi nebyl inventurou nalezen explicitní ArchiMate Capability; business procesy a BPMN existují.','E1; poznámky 2.11.','Modelové typy a vazby vyžadují kontrolu. Absence Capability není absence celé business vrstvy.'],
 ['Rozpor, CHM identifikátory','EA a Book1 mají u CHM-06–19 rozdílné texty/pořadí.','E1, původní Book1 a poznámky 2.11.','Rozpory jsou uvedeny u příslušných Business a FREQ řádků. Neslučovat jen podle ID.'],
 ['Rozpor, SREQ-CRM-09','EA jej popisuje jako assisted-ticket email configuration; Book1 jej používá pro lead-create.','E1 a původní mapování Book1.','OTEVŘENO: zdrojový rozpor není tímto sloučením rozhodnut.'],
 ['Konsolidace, EAM App','Ve větvi z 2.11. se oproti jejímu vstupu změnilo 608 hodnot EAM App po přepočtu.','Třícestná kontrola OOXML.','Tyto nesouvisející změny nejsou přeneseny. EAM App a původní vzorce/cache jsou zachovány z v02.'],
 ['Původní chyba sešitu','EAM App!F459 obsahuje původní chybu #VALUE!.','Zachovaný původní sešit a v02.','Není novou chybou této konsolidace. Nebyla skryta ani nahrazena nulou.'],
 ['Stav zdrojů','V podkladech jsou inventarizované, ale ne zcela přečtené dokumenty a podsložky.','SharePoint/OneDrive poznámky 1.–2.11.','NEDOKONČENO: úplný hloubkový průzkum a ověření nejnovějších verzí.'],
 ['Marketplace/Siebel, otevřený návrh','Reporty V2/V4, klíče CRM/CA/BA/BAN/company UUID, master atributů a způsob opravy.','Zadání uživatele; dosud neověřený provozní postup.','NEDOKONČENO: žádný/mnoho matchů, duplicity a již spárovaný zákazník s rozdílnými daty.']]
for r,row in enumerate(newcontrols,35):
 for col,v in zip('ABCD',row):put('Postup revize',col+str(r),v,'Doplnění dochovaných zdrojů, pravidel a neuzavřených bodů.')
put('Revize MVP','B1','2026-11-03','Datum konsolidace.')
put('Revize MVP','C1','Konsolidovaná pracovní revize v03; úplná aktuální BRD/FREQ/SREQ baseline není ověřena.','Pravdivý status.')
for r,row in enumerate([
 ['Konsolidace v03','Sloučena rozšířená v02 a všech 23 věcných změn z 2.11.','14 listů zachováno; EAM App, vzorce, tabulky, externí odkazy a GUID se nepřebírají z poškozené exportní větve.'],
 ['Rozsah dostupných zdrojů','Zapracována uložená pozorování BRD, UC005, traceability a Marketplace BSR z 2.11.','Úplné nové primární dokumenty zde nejsou. Verze BRD a úplnost všech FREQ nejsou potvrzené.'],
 ['FREQ/SREQ vazby','Přímá textová shoda je odlišena od stejného ID s jiným textem.','Reference na řádek Book1 není schválení ani nová EA vazba.'],
 ['EA a SO','Atlas.xml a Word SO v této konsolidaci nebyly změněny.','Nedokončené odborné kroky jsou v Postup revize; žádný výstup není označen za schválenou baseline.']
 ],23):
 for col,v in zip('ABC',row):put('Revize MVP',col+str(r),v,'Průhledný záznam konsolidace a zbývající práce.')

uc=[
 'Uživatel se autentizuje přes VFID. Při selhání tok končí před požadavkem na customer/role data z DXL.',
 'ServiceHub získá přes DXL vztahy uživatele, role a dostupná CRM ID pro customer-specific obsah. Přesný API kontrakt není doložen.',
 'Specifický obsah je dostupný pro příslušné ONSC/WSC administrativní role a dostupný CRM kontext. Bez role nebo CRM ID se zobrazí obecný obsah. To není UC006 subscription eligibility.',
 'Automaticky se zvolí jedno dostupné CRM ID. Priorita této volby není v přečteném podkladu doložena.',
 'Customer Selector umožní přepnout dostupné CRM ID a obnoví obsah pro nový kontext. Nedostupné vybrané CRM ID se neaktivuje a selector se obnoví.',
 'Bez příslušné role či CRM ID se použije obecný obsah bez aktivního customer kontextu. Při nedostupných datech DXL se použije obecný/nedostupný výsledek; konkrétní technické chyby musí určit kontrakt.'
]
for r,text in enumerate(uc,161):
 put('Business a FREQ','J'+str(r),text,'Parafráze UC005 z uložené přímé kontroly 1.–2.11.; bez přidělení nového FREQ ID.')
 put('Business a FREQ','O'+str(r),'U1, UC005 s.19–21; notes/atlas-sharepoint-review-2026-11-02.md. Zaznamenaná revize 0.1 / 14.10.; nejnovější vydání musí být potvrzeno.','Rozsah skutečně přečteného zdroje.')
 put('Business a FREQ','Q'+str(r),'VÝKLAD DOPLNĚN. Kanonické FREQ ID a business/capability vazby nejsou potvrzené.','Nezaměňovat vyplnění s approval.')

fm=base['FREQ mapping']['cells'];br=base['Business a FREQ']['cells'];cross=[]
for r in range(2,161):
 id=br.get('A'+str(r),'');raw=br.get('C'+str(r),'')
 candidates=[i for i in range(2,221) if fm.get('B'+str(i),'')==id] if id else []
 exact=[i for i in candidates if norm(raw)==norm(fm.get('C'+str(i),'')) and norm(raw)]
 if exact:
  proposals=list(dict.fromkeys(ops.get('FREQ mapping',{}).get('L'+str(i),fm.get('L'+str(i),'')) for i in exact));proposals=[v for v in proposals if v]
  sources=list(dict.fromkeys(ops.get('FREQ mapping',{}).get('N'+str(i),fm.get('N'+str(i),'')) for i in exact));sources=[v for v in sources if v]
  if proposals:put('Business a FREQ','J'+str(r),'PRACOVNÍ VÝKLAD Z MAPOVÁNÍ; schválení neověřeno.\n'+'\n'.join(proposals),'Shoda FREQ ID i normalizovaného zdrojového textu; přenesen pracovní návrh, nikoli schválení.')
  if sources:put('Business a FREQ','O'+str(r),'FREQ mapping, řádky '+', '.join(map(str,exact))+':\n'+'\n'.join(sources)+'\nÚplnost a poslední vydání primárního zdroje neověřeny.','Dohledatelná pracovní evidence.')
  put('Business a FREQ','Q'+str(r),'TEXT A ID SHODNÉ S BOOK1; aktuální schválení, capability a obsahová shoda SREQ zůstávají otevřené.','Výsledek textového porovnání.')
  state='exact'
 elif candidates and any(raw.startswith(fm.get('C'+str(i),'')) and 'NFR-' in raw[len(fm.get('C'+str(i),'')):] for i in candidates):
  append('Business a FREQ','P'+str(r),'EA text obsahuje znění FREQ z Book1 a navíc vložený NFR. Před převodem oddělit jednotlivá tvrzení a ověřit jejich scope.','Odlišit rozšířenou dokumentaci od změněného významu stejného FREQ ID.')
  put('Business a FREQ','Q'+str(r),'ROZŠÍŘENÝ TEXT EA S NFR; neprovádět automatické rozdělení ani schválení.','Přesný druh rozdílu.')
  state='extended_text'
 elif candidates:
  append('Business a FREQ','P'+str(r),'Stejné FREQ ID v Book1, ale jiný zdrojový text; FREQ mapping řádky '+', '.join(map(str,candidates))+'. Návrh nebyl automaticky přiřazen.','Řízené odmítnutí nesprávného spojení podle ID.')
  put('Business a FREQ','Q'+str(r),'ROZPOR ID/TEXTU; ověřit verzi a kanonický význam před propojením.','Zřetelný status rozporu.')
  state='text_conflict'
 else:
  append('Business a FREQ','P'+str(r),'V Book1 FREQ mapping není odpovídající přesné ID; porovnat zdrojové znění a verzi.','Úplná kontrola existujících řádků, bez domýšlení nahrazení.')
  state='no_id'
 cross.append({'businessRow':r,'id':id,'state':state,'mappingRows':exact if exact else candidates})

ea=base['EA SREQ']['cells'];sr=base['SREQ Aplikační role']['cells']
put('EA SREQ','J1','FREQ reference v Book1 / stav ověření','Rozlišit existenci workbookové reference od potvrzené vazby.')
for r in range(2,113):
 guid=ea.get('B'+str(r),'');id=ea.get('A'+str(r),'')
 matches=[i for i in range(2,221) if guid and guid in fm.get('R'+str(i),'').splitlines()]
 if matches:
  refs=['FREQ mapping!'+str(i)+': '+fm.get('B'+str(i),'') for i in matches]
  put('EA SREQ','J'+str(r),'WORKBOOKOVÁ REFERENCE; význam/scope nepotvrzeny.\n'+'\n'.join(refs),'Přesná EA GUID reference z existujícího v02 mapování; není nová EA vazba.')
 if id=='SREQ-ID-06':
  append('EA SREQ','L'+str(r),'U2, pravidlo uživatele 2.11.: VFID sub a odpovídající ONSC/WSC user 1:1; email není párovací klíč. Toto upřesnění nemění původní EA text v D.','Doplnění identity přímo k příslušnému modelovému SREQ.')
 if id=='SREQ-CRM-09':
  append('EA SREQ','L'+str(r),'ROZPOR: EA popisuje assisted-ticket email configuration, Book1 lead-create. Ověřit zdroj a verzi; stejné ID není potvrzení shody.','Známý sémantický konflikt.')

for i in range(2,221):
 id=fm.get('B'+str(i),'');bad=[x for x in cross if x['id']==id and x['state']=='text_conflict']
 if bad:
  note='ROZPOR FREQ ID/TEXTU proti EA; Business a FREQ řádky '+', '.join(str(x['businessRow']) for x in bad)+'.'
  append('FREQ mapping','W'+str(i),note,'Provázání řádkového konfliktu.')
  for j in range(2,221):
   if sr.get('A'+str(j))==fm.get('A'+str(i)) and sr.get('B'+str(j))==fm.get('F'+str(i)):
    append('SREQ Aplikační role','W'+str(j),note,'Propagace známého konfliktu pouze při shodě aplikace a SREQ.')

exec(compile((HERE/'primary_update.py').read_text(encoding='utf8'),str(HERE/'primary_update.py'),'exec'))
result={'operations':ops,'reasons':reasons,'primaryReview':primary_summary,'identityCells':[(c['sheet'],c['cell']) for c in meaning],
 'crosswalk':cross,'summary':{'meaningfulIdentityCells':len(meaning),'excludedEamRecalculationValues':sum(c['sheet']=='EAM App' for c in delta),'changedCells':sum(map(len,ops.values())),'changedSheets':list(ops),'businessTextMatches':dict(collections.Counter(c['state'] for c in cross))}}
(HERE/'changes.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(result['summary'],ensure_ascii=False,indent=2))
