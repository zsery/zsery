"""Apply the 3 Nov read-only VDI evidence to the one existing Book1 builder.
Executed inside prepare_changes.py after the three-way consolidation.
All derived links are working analysis; direct EA relation columns stay intact.
"""
PRIMARY='Overeni_zdroju_VDI_2026-11-03.md'
UC='PR25_0837_ServiceHub_Atlas_Use_Case_Specification.docx'
MVP='Service_Hub_Atlas_MVP_Requirements.xlsx'
TR='PR25_0837_ServiceHub_Atlas_Traceability_Decomposition.xlsx'
prov=f'Přímé čtení VDI 3.11.2026: {PRIMARY}. '
why='Primární BRD/UC/MVP/Traceability znovu přečteny 3.11.; pracovní odvození odděleno od EA vazeb a approval.'

summaries={
 'UC001':'Sales dokončí obchodní prodej v CRM a BidBot (V2) / OfferTool (V4), zaznamená podepsanou smlouvu a výsledek a předá UC002. V UC001 se nezakládá Marketplace customer/order/subscription. Atlas jen pro vlastní podnikání koncového zákazníka, nikoli resale.',
 'UC002':'Interní uživatel v Logins ověří VFID a admin roli pro daného zákazníka. Chybějící setup dokončí zákazník mimo UC. Následně ověří/opětovně použije nebo vytvoří/opraví Marketplace customer/user a odešle první order s admin profilem. UC končí přijetím orderu. Žádné duplicity.',
 'UC003':'Upgrade zahrne úplný vymezený M365 subscription/licence scope do Atlasu bez souběžné unmanaged proposition v tomtéž scope. Podkladové M365 zůstává součástí Atlasu. Sales CRM/OfferTool/BidBot; V2 Provisioning/ICT Hub ověří Marketplace/CSP/tenant/GDAP/licence a odešle kompletní order do UC012.',
 'UC004':'Downgrade zachová/obnoví M365 a respektuje committed term a renewal boundary; žádné předčasné ukončení Atlas licence. V2 Provisioning/ICT Hub plánuje či provede dostupnou Marketplace operaci. Stejné omezení pro Atlas Premium→Standard. Úplné ukončení je UC009, nikoli UC004.',
 'UC005':'Standalone SH URL, autentizace Vodafone Identity, poté DXL customer/user/relationship/role/CRM IDs. Eligible admin: automaticky právě jedno dostupné CRM ID, následně přepnutí dostupného CRM ID. Bez role/CRM generic obsah. Selhání autentizace před DXL. Nedostupné zvolené ID se neaktivuje. Priorita automatické volby neuvedena.',
 'UC006':'SH získá Marketplace product/subscription data pro aktivní autorizované CRM ID. V tomto projektu zobrazuje jen managed Atlas, nikoli ostatní Marketplace produkty nebo data výlučně jiného CRM ID. Bez Atlasu no-Atlas výsledek; nedostupná data se nevydávají za ověřená. Změna kontextu vyvolá nové vyhodnocení.',
 'UC007':'Autorizovaný Customer User vytvoří Atlas support request pro aktivní CRM ID a dostupný Atlas. SH validuje povinné údaje a podá do SNOW; ID/status a úspěch až po potvrzení SNOW. Změna kontextu před podáním nesmí poslat request pod původním CRM ID.',
 'UC008':'Lokální telefonická podpora BCS/LME je jen pro whitelisted V2 Customer User. V4 tuto lokální cestu nemá. LME ověří whitelist a kontext, zaznamená pomoc nebo eskalaci v SNOW. Samotné předání není vyřešení. Detail resolver/routing patří do MSO modelu.',
 'UC009':'Plné ukončení Atlas: Frontline přijme požadavek a založí jej v Siebel, předá ICT Hub/Provisioning, ten založí odpovídající termination v Marketplace, Marketplace předá SNOW a MSO provede offboarding. Nepotvrzené předání není hotové. Přesné payloady a error handling čekají na FR.',
 'UC010':'Pouze čtení Atlas support request seznamu/detailu/status ze SNOW pro aktivní autorizované CRM ID. Data výlučně jiného contextu se nezobrazí, po změně CRM ID se načtou a nahradí novými. Nedostupná data se nevydávají za ověřená. Přesná pole/statusy/sort/filter nejsou potvrzeny.',
 'UC011':'Změna existujícího Atlas requestu jen pro aktivní CRM ID, aktuální SNOW state a povolenou operaci. Nepovolené/nevalidní/nepotvrzené změny nejsou úspěch. Změna stavu nebo kontextu před podáním vyžaduje nové vyhodnocení. Editable fields/comments/attachments/transitions zatím nejsou potvrzeny.',
 'UC012':'MSO Central Backoffice ověří Customer ID/Country Code a existenci customer v SNOW, založí nebo aktualizuje bez duplicity, doplní inventář/contact a iniciuje onboarding request. Workflow pokračuje úkoly zákazníka a specialistů. Detail M365/DNS/GDAP/migrací/modify/error větví patří do FR. Nejde o důkaz automatického customer onboardingu.'
}
entries=[]
def matrix(cj,uc,p,stream,cap,sub,subid=''):
 entries.append([cj,uc,p,stream,cap,sub,subid])
for sub,sid in [('Product Definition','PPM-01'),('Commercial Offer Enablement','PPM-02'),('Contract Agreement','PPM-03'),('Terms & Conditions','PPM-04'),('Customer Technical Specification','PPM-05')]:
 matrix('CJ01','UC001','P01 Atlas Sales & Contracting','Sell','Product & Pricing Management',sub,sid)
for sub,sid in [('Marketplace Company Identifier Readiness','ONB-01'),('Marketplace Company Data Readiness','ONB-03'),('Atlas Subscription Readiness','ONB-05')]:
 matrix('CJ01','UC002','P02 First Atlas Order & Enablement','Build','Service Onboarding',sub,sid)
matrix('CJ01','UC012','P10 Atlas Managed Service Onboarding','Build','Service Onboarding','Managed Service Onboarding')
matrix('CJ02','UC003','P03 M365 to Atlas Upgrade','Sell','Product & Pricing Management','Product Definition','PPM-01')
matrix('CJ02','UC003','P03 M365 to Atlas Upgrade','Build','Service Onboarding','Atlas Subscription Readiness','ONB-05')
matrix('CJ02','UC003','P03 M365 to Atlas Upgrade','Run','Exception Handling','Data Consistency','EXC-02')
matrix('CJ03','UC005','P04 Service Hub Access','Build','Channel & Entry Management','Entry Points and Navigation','CHM-02')
matrix('CJ03','UC005','P04 Service Hub Access','Build','Identity & Access Management','Authorization Input Readiness','IAM-02')
matrix('CJ03','UC005','P04 Service Hub Access','Build','Identity & Access Management','Customer Context Input Readiness','IAM-03')
matrix('CJ03','UC006','P05 Atlas Service Visibility','Run','Service Visibility','Atlas Service Data Availability','SVI-01')
matrix('CJ04','UC007','P06 Digital Support Request','Run','Support Management','Channel Handling','SUP-02')
matrix('CJ04','UC007','P06 Digital Support Request','Run','Support Management','Routing & Forwarding','SUP-03')
matrix('CJ04','UC008','P07 Assisted Support','Run','Support Management','Assisted Support','SUP-04')
matrix('CJ04','UC008','P07 Assisted Support','Run','Exception Handling','Escalation Handling','EXC-04')
matrix('CJ04','UC010','P06 Digital Support Request Management','Run','Support Management','Support Request Visibility')
matrix('CJ04','UC011','P06 Digital Support Request Management','Run','Support Management','Support Request Update')
for cj,uc,p in [('CJ05','UC004','P08 Atlas to M365 Downgrade'),('CJ06','UC009','P09 Atlas Service Termination')]:
 matrix(cj,uc,p,'Run','Service Offboarding','Termination Handling','OFF-01')
 matrix(cj,uc,p,'Run','Exception Handling','Escalation Handling','EXC-04')
assert len(entries)==26

put('Business a FREQ','J1','Aktuální pracovní business výklad — 3.11.2026',why)
put('Business a FREQ','R1','Business capability / sub-capability — pracovní přiřazení',why)
put('Business a FREQ','S1','UC / proces — pracovní přiřazení',why)

def classify(r,ident,text):
 # Row sets address stable original EA rows and their reviewed original text.
 if 'MKT-' in ident:
  return ('SAMOSTATNÝ MARKETING SCOPE','Historický marketing/lead požadavek. Starší primární Requirements jej uvádí mimo tento projekt (samostatný VBU Digital Marketing & Communication brief). Nový CZ MVP neprokazuje převzetí do CZ BRD. Vložený NFR posoudit odděleně.','Samostatný marketing owner; nepřiděleno CZ Atlas implementaci','Marketing & Lead Management — historický samostatný scope','Žádná potvrzená UC vazba této CZ baseline','Starší Requirements, Functional_Requirements ř.4; nový BRD 1.2 a MVP_Scope')
 if 4<=r<=22:
  cap='Channel & Entry Management / SUBCAP-CHM-02 Entry Points and Navigation'
  if r in [4,5,6,7,10,11,14,15,16,17,18]:
   return ('MIMO MVP – PORTÁLOVÁ INTEGRACE','Původní portálový entry/navigation/handover požadavek je mimo samostatné URL MVP. Neimplementovat jako CZ MVP FR bez změny závazného scope.','Mimo CZ MVP',cap,'UC005 / P04','BRD 1.2; UC úvod; MVP_Scope ř.14 a 58')
  if r in [8,9]:
   return ('POTVRZENÝ MVP VÝSLEDEK – VFG ZÁVISLOST','ServiceHub je samostatný portál na dedicated URL. VFCZ řeší lokální vstupy, distribuční/access podmínky a akceptaci, nikoli vývoj Group UI.','VFG SH; VFCZ lokální integrace',cap,'UC005 / P04','UC005 Description/Preconditions; MVP CHM-02')
  if r in [12,13]:
   return ('DETAIL NEPOTVRZEN PRO MVP','Dedicated URL je potvrzena, přesné deep-link chování není novým UC/MVP atomicky potvrzeno. SH navigace je VFG-owned; nevytvářet novou CZ implementaci.','VFG funkcionalita; CZ acceptance jen po potvrzení',cap,'UC005 / P04 – pouze tematické přiřazení','UC005; MVP CHM-02')
  return ('ZPŘESNIT ELIGIBILITY PODLE UC','Oddělit admin roli a aktivní CRM ID (UC005) od Atlas Marketplace service/subscription dostupnosti (UC006). Bez role/context generic, bez Atlasu no-Atlas outcome; přesný produktový promo UI není potvrzen.','VFG vyhodnocení; CZ data/role/context vstupy','Channel & Entry Management / SUBCAP-CHM-03 Eligibility Input Readiness','UC005/P04 a UC006/P05','UC005/006; MVP CHM-03')
 if 'IAM-' in ident:
  n=int(re.search(r'IAM-(\d+)',ident)[1])
  if n<=7:
   return ('POTVRZENÝ CÍL – ZPŘESNIT CZ VSTUPY','VFID autentizace před DXL, pak DXL customer/user/role/CRM data pro autorizaci. Selhání VFID nezakládá session a nevolá DXL pro tato data. MVP používá dedicated URL. CZ specifické vyjednání tokenu dle uživatele zůstává součástí integrace; přesný kontrakt neověřen.','VFG VFID/SH; VFCZ DXL integrační vstupy','Identity & Access Management / SUBCAP-IAM-02 Authorization Input Readiness','UC005 / P04','UC005; MVP IAM-02; uživatel – CZ DXL token')
  if n<=15:
   return ('ROLE DETAIL NEPOTVRZEN NOVÝM UC','Aktuální UC005 vyžaduje eligible ONSC/WSC administrativní roli a dostupné CRM ID; bez ní generic page. Konkrétní historický seznam rolí z původního textu není tímto znovu schválen. Ověřit role API kontrakt.','VFCZ role vstupy; VFG authorization','Identity & Access Management / SUBCAP-IAM-02 Authorization Input Readiness','UC005 / P04','UC005; MVP IAM-02; starší role seznam jen Draft')
  if n<=29:
   return ('POTVRZENÝ CONTEXT CÍL – ZPŘESNIT TEXT','Použít DXL dostupné CRM ID pro eligible admin. SH automaticky aktivuje právě jedno dostupné CRM ID a dovolí následné přepnutí; izoluje data/akce podle aktivního kontextu. Výběr z více ONSC/WSC user IDs není aktuální model: VFID sub↔user vždy 1:1. Holding parent–child v TMF691 je samostatná relace.','VFCZ data/user relationships; VFG selector a active context','Identity & Access Management / SUBCAP-IAM-03 Customer Context Input Readiness','UC005/P04, UC006/P05','UC005/006; MVP IAM-03; uživatel 1:1 a TMF691')
  if n<=39:
   return ('VFG ZÁVISLOST – ODDĚLIT UC006','Pro aktivní autorizované CRM ID vyhodnotit Marketplace data a v tomto projektu zobrazit pouze managed Atlas. Bez Atlasu no-Atlas, nedostupná data se nezobrazí jako ověřená. Původní ostatní produkty, přesná UI hlášení a omezení portálových entry points nejsou aktuálně potvrzený CZ FR.','VFG SH vyhodnocení/UI; VFCZ Marketplace data readiness','Service Visibility / SUBCAP-SVI-01 Atlas Service Data Availability','UC006 / P05','UC006; MVP SVI-01; historické IAM ID jsou duplicitní')
  return ('VFG SUPPORT ZÁVISLOST – API DETAIL OTEVŘEN','Atlas requesty se čtou/mění jen pro aktivní autorizované CRM ID. Vytvoření a update úspěšné až po potvrzení SNOW, update podle aktuálního stavu/povolené operace. VFID sub↔ONSC/WSC user vždy 1:1, email není klíč. Přesná SNOW identity/onboarding pole, ostatní ticket oprávnění a stavy vyžadují kontrakt; V4 manuální onboarding MVP se tím nemění.','VFG SH/SNOW; VFCZ vstupy a lokální provoz','Support Management / Support Request Visibility a Support Request Update; IAM-03 vstupy','UC007, UC010, UC011 / P06','UC007/010/011; MVP SUP a IAM-03; uživatel 1:1 a manuální V4 onboarding')
 if 'ONB-' in ident:
  n=int(re.search(r'ONB-(\d+)',ident)[1])
  if n<=12:
   return ('MINIMUM POTVRZENO – DETAIL VALIDACE OTEVŘEN','V Marketplace musí být dostupný, správně definovaný/vlastněný a úplný CRM nebo Siebel company identifier. Konkrétní numeric-only, CA vs BA význam a edit/read oprávnění původního textu nejsou novým MVP atomicky potvrzeny. Neslučovat CRM ID, CA, BA, company UUID.','VFCZ minimum dat a ownership; Marketplace implementace podle dohody','Service Onboarding / SUBCAP-ONB-01 Marketplace Company Identifier Readiness','UC002/P02; UC003/P03 – tematické','MVP ONB-01; TR ř.7; UC002')
  if n<=27:
   return ('AUTO SIEBEL RETRIEVAL/POPULATION MIMO MVP','Automatické načítání/předvyplnění ze Siebelu je v MVP vyloučeno, dokud nebude znovu potvrzeno. Zachovat lokální připravenost a ruční kontrolu/opravování Marketplace customer/user podle UC002. Není tím schválena nová retrieval ani automatická reconciliation služba.','VFCZ manuální data readiness; auto integrace mimo MVP','Service Onboarding / SUBCAP-ONB-03 Marketplace Company Data Readiness; EXC-02 Data Consistency','UC002/P02; UC003/P03','MVP ONB-03; UC002 A3; starší retrieval Draft')
  if n<=35:
   return ('NAHRADIT EMAILOVOU VALIDACI POSTUPEM UC002','Před prvním orderem interní uživatel ověří VFID a příslušnou admin roli v Logins. Chybějící setup řeší zákazník mimo UC002 a následně se opakuje kontrola. Email není konzistentní mapovací klíč VFID. Automatická email→VFID validace starého textu není aktuálně potvrzená implementace.','VFCZ interní ověření v Logins; identitní služby dle kontraktu','Identity & Access Management / SUBCAP-IAM-02 Authorization Input Readiness','UC002 / P02','UC002 Basic Flow/A1; uživatel – email není klíč')
  if n<=40:
   return ('POTVRZENÝ CÍL – DETAIL IMPLEMENTACE OTEVŘEN','Oprávněný interní uživatel připraví zákazníka/user bez duplicit a odešle první Atlas order s admin profilem. Marketplace potvrdí přijetí. Subscription association, active status a identifier musí být dostupné downstream; přesný okamžik/state API není potvrzen tímto UC.','VFCZ readiness a interní proces; VFG/Marketplace product capability','Service Onboarding / SUBCAP-ONB-05 Atlas Subscription Readiness','UC002/P02; UC003/P03','UC002; MVP ONB-05; TR ř.9 a 12')
  return ('GROUP ONBOARDING ZÁVISLOST – PAYLOAD OTEVŘEN','Přijatý Atlas order/product payload je vstup UC012. MSO ověří Customer ID a Country Code a vytvoří/aktualizuje zákazníka, inventář/contact a onboarding request v SNOW. Historická automatická activation notifikace neurčuje schválený MVP payload ani automatický V4 onboarding.','VFG Marketplace/SNOW/MSO; VFCZ input/acceptance','Service Onboarding / Managed Service Onboarding (TR bez nového SUBCAP ID)','UC012 / P10','UC012; TR ř.10; uživatel – manuální V4 onboarding')
 if 'PPM-' in ident:
  return ('LOKÁLNÍ PRODUCT ENABLEMENT – DETAIL OTEVŘEN','Atlas je non-public Marketplace C-product. VFCZ lokální bundle/standalone/add-on/product-code/eligibility/commercial dopady podle dohodnutého product definition. Konkrétní kombinace původního textu potvrdit v product specification; Group vývoj se nepřenáší do CZ scope.','VFCZ lokální product/commercial změny; VFG C-product','Product & Pricing Management / SUBCAP-PPM-01 Product Definition','UC001/P01; UC003/P03','BRD 1.2.7; MVP PPM-01; TR ř.2 a 11')
 raise ValueError(('Unreviewed original FREQ row',r,ident,text))

semantic={};classified=[]
for r in range(2,161):
 ident=br.get('A'+str(r),'');raw=br.get('C'+str(r),'')
 state,current,owner,cap,ucs,source=classify(r,ident,raw)
 for col,value in [('I',state),('J',current),('N',owner),('O',prov+source),('R','PRACOVNÍ PŘIŘAZENÍ: '+cap),('S','PRACOVNÍ PŘIŘAZENÍ: '+ucs)]:put('Business a FREQ',col+str(r),value,why)
 append('Business a FREQ','Q'+str(r),'3.11. provedeno obsahové třídění proti primárním zdrojům. Navržené přiřazení není přímá EA vazba ani schválení FR.',why)
 m=re.search(r'IAM-(\d+)',ident)
 if m and 30<=int(m[1])<=50:append('Business a FREQ','P'+str(r),'PŘÍMO OVĚŘENO: historický Requirements používá IAM-30–50 opakovaně pro odlišná znění. Ztotožnění jen podle ID není přípustné; ponechat EA GUID a text/sekci.',why)
 semantic.setdefault(norm(raw),[]).append((r,state,current,owner,cap,ucs,source))
 classified.append({'row':r,'guid':br.get('D'+str(r)), 'id':ident,'state':state,'capability':cap,'useCases':ucs})

for r in range(161,167):
 put('Business a FREQ','O'+str(r),prov+UC+' UC005; knihovna modified dnes Martin Dostál, cover 0.1 / 14.10.2026.',why)
 put('Business a FREQ','R'+str(r),'TR ř.14–16: Channel & Entry Management / CHM-02; Identity & Access Management / IAM-02 a IAM-03. Pracovní obsahová návaznost.',why)
 put('Business a FREQ','S'+str(r),'UC005 / P04; přímá EA vazba není potvrzena.',why)
 put('Business a FREQ','Q'+str(r),'UC005 přímo znovu ověřeno 3.11. Kanonické FREQ ID/approval a nové EA vazby nebyly přiděleny.',why)

for i,(cj,uc,p,stream,cap,sub,sid) in enumerate(entries,167):
 trrow=i-165
 row={'B':uc+' – '+sub,'C':summaries[uc], 'F':'Martin Dostál – UC; traceability knihovna Klára Štěpničková',
 'G':'Ověřeno 3.11.2026; TR modified 27.10.; UC cover 0.1 / 14.10.',
 'H':'TR1 – přímý přepis business návaznosti, nikoli nový FREQ',
 'I':'BUSINESS TRACEABILITY – BEZ KANONICKÉHO FREQ ID','J':summaries[uc],
 'N':'Dle konkrétní lokální změny; Group funkce jsou dependency/acceptance, ne automatický CZ FR',
 'O':f'{prov}{TR}, Traceability ř.{trrow}; {UC}, {uc}'+(f'; {MVP} / SUBCAP-{sid}' if sid else '; TR neuvádí SUBCAP ID, nové nevytvořeno'),
 'P':'Teprve odvodit/ověřit atomické FREQ a modelové vazby. P06 má v TR dvě textové varianty názvu.' if p.startswith('P06') else 'Teprve odvodit/ověřit atomické FREQ, konkrétní lokální delta a modelové vazby.',
 'Q':'PŘEPSÁNA ZDROJOVÁ BUSINESS NÁVAZNOST. Není to nová EA vazba ani schválený FREQ.',
 'R':cap+' / '+('SUBCAP-'+sid+' ' if sid else '')+sub,'S':cj+' / '+uc+' / '+p+' / '+stream}
 for col,value in row.items():put('Business a FREQ',col+str(i),value,why)

# Propagate only exact original-text matches, including CHM when its historical ID differs.
# This does not resolve the identity conflict or invent an EA relation.
mapped=[]
for i in range(2,221):
 candidates=semantic.get(norm(fm.get('C'+str(i),'')),[])
 if len(candidates)!=1:continue
 r,state,current,owner,cap,ucs,source=candidates[0]
 put('FREQ mapping','K'+str(i),state,why)
 put('FREQ mapping','L'+str(i),current,why)
 put('FREQ mapping','M'+str(i),owner,why)
 append('FREQ mapping','N'+str(i),prov+source,why)
 append('FREQ mapping','O'+str(i),f'3.11. obsahové přiřazení k Business a FREQ!{r} podle přesného normalizovaného textu, nikoli ztotožnění ID. Pracovní capability: {cap}; {ucs}.',why)
 mapped.append(i)
 for j in range(2,221):
  if sr.get('K'+str(j))==str(i) and sr.get('A'+str(j))==fm.get('A'+str(i)) and sr.get('B'+str(j))==fm.get('F'+str(i)):
   append('SREQ Aplikační role','W'+str(j),f'Nové primární ověření FREQ mapping!{i}: {state}. FREQ/SREQ sémantická vazba není tímto schválena.',why)

exact_mapped=list(mapped)
manual_groups=[
 ([41,48],'SAMOSTATNÝ MARKETING SCOPE','Historická validace lead formuláře a jeho chybové zprávy patří do samostatného marketingového briefu. Nové CZ MVP nepřebírá tyto UI detaily jako Atlas FR.','VBU Digital Marketing & Communication','Starší Requirements Functional_Requirements ř.4; BRD scope'),
 ([50,139],'HISTORICKÝ NFR – MITIGACE NEPOTVRZENA','V2 user-info/customer-context výkonové omezení je historický technický vstup. Nové UC005 potvrzuje DXL data po autentizaci, nikoli konkrétní výkonový limit či implementovanou mitigaci. Vyžaduje aktuální měření a kontrakt.','VFCZ DXL/identity; VFG SH','UC005; historický NFR-01; MVP IAM-02/03'),
 ([54],'SDRUŽENÝ POŽADAVEK – ROZDĚLIT SCOPE','Minimum company identifier a ruční data readiness zůstává v MVP (ONB-01/03). Část požadující automatické získání zákaznických dat ze Siebelu je mimo MVP do opětovného potvrzení. Zachovat původní sdružený text; nerozhodovat celý řádek jediným ano/ne. CA/BA/CRM ID/company UUID nezaměňovat.','VFCZ data readiness; auto retrieval mimo MVP','MVP ONB-01/03; UC002 A3'),
 ([123,185,186],'VFG SERVICE VISIBILITY – DETAIL OTEVŘEN','UC006 vyhodnocuje pouze managed Atlas a Marketplace data aktivního autorizovaného CRM ID. Oddělit no-Atlas, nedostupná data a zákaz zobrazení jiného CRM ID. Historické ostatní produkty a přesná UI hlášení nejsou tímto potvrzeny.','VFG SH; VFCZ Marketplace vstupy','UC006/P05; MVP SVI-01'),
 ([129,130],'VFG TICKET VISIBILITY – OPRÁVNĚNÍ OTEVŘENA','UC010 potvrzuje seznam/detail Atlas requestů pro aktivní autorizované CRM ID. Přesná pravidla viditelnosti podle autora ticketu a SNOW role vyžadují kontrakt; netvrdit automaticky přístup ke všem ticketům zákazníka.','VFG SH/SNOW; VFCZ vstupy','UC010/P06; MVP Support Management'),
 ([142,143,144,145],'CHANNEL ROUNDTRIP NEPOTVRZEN PRO MVP','Původní identifikace původu, uchování kanálu a návrat do odpovídajícího místa portálu nejsou potvrzeny standalone URL MVP. Bez potvrzení požadavek nepřenášet do CZ implementace.','VFG navigace; CZ portálová integrace mimo MVP','BRD scope; UC005; MVP CHM-02'),
 ([159],'V4 USER IDENTITA – MANUÁLNÍ ONBOARDING MVP','VFID sub a odpovídající WSC user jsou vždy 1:1; email není párovací klíč. Přesné předání identity do SNOW a ticket oprávnění vyžadují kontrakt. V4 customer/admin onboarding zůstává manuální MVP.','VFCZ user vstupy; VFG SH/SNOW','UC005/007/010/012; výslovná pravidla uživatele'),
 ([160,161,162,167,168],'LIFECYCLE CÍL – AUTOMATIZACE MIMO POTVRZENÍ','Historický NFR-03 požaduje V4 admin lifecycle a zdrojové události/informace. MVP podle uživatele používá manuální customer/admin onboarding do SNOW. Automatický event/API synchronizační mechanismus tím není schválen; oddělit cílový lifecycle od nynějšího postupu.','VFCZ identity vstupy; VFG SNOW; manuální provoz MVP','Historický NFR-03; UC002/012; pravidlo uživatele manuální V4'),
 ([175,176],'LIFECYCLE VÝSLEDEK – EVENT KONTRAKT OTEVŘEN','UC002 končí přijetím orderu; UC006 čte Marketplace Atlas data a UC012 provádí managed onboarding. Potřebný aktuální subscription stav neprokazuje konkrétní event delivery, schema, pořadí ani automatický V4 onboarding.','VFG Marketplace/SH/SNOW; VFCZ data readiness','UC002/006/012; MVP ONB-05/SVI-01'),
 ([177,210,211,212],'MIMO MVP – PORTÁLOVÝ HANDOVER','Sdružená portálová navigace nebo předání customer context z ONSC/WSC do SH není součást standalone MVP. UC005 používá DXL dostupné user/role/CRM vztahy po VFID autentizaci; nejde o portálový handover.','Mimo CZ MVP portálovou integraci; VFCZ DXL vstupy zůstávají','BRD scope; UC005/P04; MVP CHM-02/IAM-03'),
 ([213,214],'NAHRADIT AKTUÁLNÍ VOLBOU KONTEXTU','UC005 automaticky aktivuje právě jedno dostupné CRM ID i při více dostupných ID a následně umožní selector. Historické větvení podle počtu kontextů ani direct selector journey není současný potvrzený postup. Priorita automatické volby zůstává neuvedena.','VFG SH selector; VFCZ DXL dostupné CRM ID','UC005/P04; MVP IAM-03'),
 ([215,217],'GROUP UI DETAIL NEPOTVRZEN','Dedicated SH URL je potvrzena. Přesný deep-link error page nebo navigace produktové informační stránky nejsou novým CZ UC atomicky potvrzeny. Vyžadují Group UX/acceptance podklad.','VFG SH UX; CZ acceptance po potvrzení','UC005/006; MVP CHM-02/03'),
 ([216],'ZPŘESNIT ELIGIBILITY OUTCOMES','Oddělit generic obsah při chybějící eligible roli/CRM ID (UC005) od no-Atlas výsledku a nedostupnosti Marketplace dat (UC006). Historický redirect na produktovou informační stránku není aktuálním UC automaticky potvrzen.','VFG SH UX/authorization; CZ role/data vstupy','UC005/006; MVP IAM-02/03 a SVI-01')]
manual_rows=[]
for rows,state,current,owner,source in manual_groups:
 for i in rows:
  assert i not in mapped and fm.get('C'+str(i)),('Unexpected manual review row',i)
  for col,value in [('K',state),('L',current),('M',owner)]:put('FREQ mapping',col+str(i),value,why)
  append('FREQ mapping','N'+str(i),prov+source,why)
  append('FREQ mapping','O'+str(i),'3.11. samostatné obsahové posouzení původního sdruženého/odlišného textu. Žádné ztotožnění EA GUID ani schválení SREQ vazby; původní ID a text zachovány.',why)
  manual_rows.append(i);mapped.append(i)
assert len(exact_mapped)==188 and len(manual_rows)==31 and set(mapped)==set(range(2,221))

for j in range(2,221):
 rawrow=sr.get('K'+str(j),'')
 if not rawrow.isdigit() or int(rawrow) not in mapped:continue
 i=int(rawrow)
 for target,source in [('L','K'),('M','L')]:put('SREQ Aplikační role',target+str(j),ops['FREQ mapping'][source+str(i)],why)
 append('SREQ Aplikační role','N'+str(j),f'3.11. aktuální pracovní výklad: FREQ mapping!{i}; '+PRIMARY,why)
 append('SREQ Aplikační role','O'+str(j),'Aktualizován pracovní scope zdrojového FREQ. Původní aplikační role a shoda SREQ zůstávají neověřenou technickou vazbou.',why)

func=base['Functionalities']['cells']
for j in range(2,max(int(re.search(r'\d+',x)[0]) for x in func)+1):
 ids=set(re.findall(r'SREQ-[A-Z]+-\d+',func.get('D'+str(j),'')))
 if not ids:continue
 rows=[i for i in mapped if fm.get('F'+str(i),'') in ids and fm.get('A'+str(i),'')==func.get('E'+str(j),'')]
 if not rows:continue
 states=list(dict.fromkeys(ops['FREQ mapping']['K'+str(i)] for i in rows))
 put('Functionalities','J'+str(j),'3.11. pracovní scope navázaných FREQ:\n'+'\n'.join(states),why)
 put('Functionalities','K'+str(j),'Aktuální význam/zdroj je ve FREQ mapping ř. '+', '.join(map(str,rows))+'. Odkazy nalezeny přes původní SREQ ID a aplikaci, neprokazují realizaci konkrétní funkce. '+PRIMARY,why)
 append('Functionalities','L'+str(j),'3.11. aktualizován pracovní souhrn. Přímou modelovou funkci/GUID a AS-IS deltu je stále nutné ověřit.',why)

for j in range(2,113):
 guid=ea.get('B'+str(j),'')
 linked=[i for i in mapped if guid and guid in fm.get('R'+str(i),'').splitlines()]
 if linked:append('EA SREQ','L'+str(j),'3.11. primárně ověřený pracovní scope ve FREQ mapping ř. '+', '.join(map(str,linked))+'. Z workbookové reference nevzniká schválená EA FREQ vazba. '+PRIMARY,why)

for row,state,detail,source in [
 (2,'AUTO SIEBEL RETRIEVAL/PREFILL MIMO MVP','MVP ONB-03 explicitně vylučuje automatic Siebel retrieval/population do opětovného potvrzení. Minimální identifikátor ONB-01 a lokální data readiness zůstávají. Původní katalogový kontrakt G:H není tímto potvrzen.',MVP+' ONB-01/03; UC002 A3'),
 (3,'SAMOSTATNÝ MARKETING SCOPE','Starší primární Requirements ř.4 vyjímá marketing/lead do samostatného VBU briefu. Toto rozhraní není na základě katalogu novým CZ Atlas MVP závazkem.','Requirements Functional_Requirements ř.4; BRD MVP scope'),
 (4,'MVP SSO/DXL INTEGRACE – ODDĚLIT KONTRAKTY','UC005 potvrzuje DXL user/relationship/role/CRM data po VFID autentizaci. CZ specifické vyjednání tokenu dle uživatele je MVP integrace, přesný grant/endpoint/token/header neověřen. VFID sub↔ONSC/WSC user 1:1, email ne jako klíč; TMF691 holding parent–child.',UC+' UC005; MVP IAM-02/03; výslovná pravidla uživatele'),
 (12,'CZ UŽIVATELSKÉ VSTUPY – KONTRAKT OTEVŘEN','ONSC role/user vztahy jako vstup DXL nejsou portálové embedding/context handover. VFID sub↔příslušný user 1:1. SNOW lifecycle a schema nejsou aktuálním UC podrobně potvrzeny.',UC+' UC002/005/012; uživatel 1:1'),
 (17,'VFID SUB IDENTITA – EMAIL NENÍ PÁROVACÍ KLÍČ','Lookup podle emailového atributu se nesmí zaměnit za stabilní párování user identity. UC002 aktuálně ověřuje VFID/admin v Logins interním uživatelem; automatická email→VFID validace není potvrzený MVP požadavek.',UC+' UC002; uživatel email není klíč'),
 (18,'V4 IDENTITA 1:1 – SNOW ONBOARDING MANUÁLNÍ MVP','VFID sub↔odpovídající WSC user 1:1. Company/holding vztahy jsou samostatné. V4 customer/user onboarding do SNOW zůstává manuální dle zadání; samotná existence katalogového GraphQL rozhraní nedokládá automatickou synchronizaci.',UC+' UC005/012; uživatel 1:1 a manuální V4 onboarding')]:
 put('Interfaces','I'+str(row),state,why)
 append('Interfaces','J'+str(row),'3.11. '+detail,why)
 append('Interfaces','K'+str(row),prov+source,why)

controls=[
 ['Primární zdroje 3.11.','BRD reader do G6; UC reader do konce UC012; TR 26 řádků; MVP Scope + Functional Decomposition.','Ověřeno v aktuálním CZ local folder, bez editoru. '+PRIMARY,'Knižní modified není approval ani interní revize. Obrázky/zakryté řádky UC nebyly zvalidovány.'],
 ['BRD verze a maturity','Cover 0.1, revize 0.2 / Martin Dostál / 23.10.; knihovna dnes Barbora Poláková.','BRD 1.1–1.8 a kap.2/G5/G6 čtecí text.','Věcné FR/acceptance tabulky jsou šablonové, nepřidělovat automaticky schválené FR.'],
 ['UC aktuální obsah','Všech 12 UC do konce readeru. UC005 znovu potvrzuje DXL a právě jedno automaticky aktivní dostupné CRM ID.','UC cover 0.1 / 14.10.; SharePoint dnes Martin Dostál.','Priorita volby a detail DXL/SNOW kontraktů zůstávají otevřené.'],
 ['Business traceability','26 původních TR záznamů přeneseno do Business a FREQ ř.167–192.','TR ř.2–27, CJ01–06, UC001–012, P01–10.','Jde o business návaznosti bez FREQ ID/EA GUID. P06 má dvě varianty názvu.'],
 ['MVP dekompozice','19 provozních sub-capability položek a jedna rebaseline aktivita, odhad BA/DM celkem 20 MD.','MVP_Functional_Decomposition ř.4–26.','INI-01 je rebaseline aktivita. Odhad není implementační pracnost ani approval FR.'],
 ['Duplicitní historické IAM ID','IAM-30–50 mají různé texty v různých sekcích téhož starého Requirements.','Např. ř.103 a 127 obě IAM-48, ale session context vs V4 ticket identity.','Spojovat přes text+sekci+GUID, ne ID samotné. Nová upozornění doplněna u EA řádků.'],
 ['UC008 V2/V4 support','BCS/LME telefonická Atlas cesta jen whitelisted V2, ne V4.','UC008 BR-UC008-01–03.','Obecný V4 fallback v BRD tím nezaměnit za lokální BCS/LME.'],
 ['Data cleansing – provozní vstup','Nový Marketplace export s CA/BA; porovnat se Siebelem, zpracovat jednoznačné a ručně ověřit konfliktní.','Otevřený email Re: Čištění dat zákazníků, 3.11.9:43; celý thread nepřečten.','Existující chybná CA může projít. Dry-run/reconciliation není doložená implementace. Detail '+PRIMARY],
 ['Zbývající odborná práce','Přesná atomická FR baseline/approval, EA vztahy/GUID review, token/API kontrakty, detailní cleansing a SO.','Zadání uživatele.','Toto ověření není kompletní průzkum všech podsložek tří původních Group tabů ani aktualizace EA/SO.']]
for row,values in enumerate(controls,48):
 for col,value in zip('ABCD',values):put('Postup revize',col+str(row),value,why)
for row,col,value in [(8,'D','3.11. reader prošel UC001–012 do konce; překryvná karta místy zakrývala část textu, obrázky nebyly ověřeny. '+PRIMARY),(9,'D','3.11. BRD reader prošel do G6. Cover/revize/modified odlišeny; kap.2 a G5/G6 jsou šablonové.'),(37,'D','TR 26 řádků znovu přímo přečteno 3.11. a přepsáno do Business a FREQ!167–192; žádné FREQ/SREQ ID ve zdroji.'),(46,'D','Průzkum všech původních Group podsložek stále není hotový. CZ BRD/UC/MVP/TR bylo nyní znovu ověřeno, zdrojová evidence v novém zápisu.')]:put('Postup revize',col+str(row),value,why)
put('Cover','B13','3.11.2026. Konsolidace v03 doplněna přímým ověřením CZ BRD, UC, MVP Requirements a business traceability.',why)
put('Cover','B15','Business scope a primární návaznosti ověřeny 3.11. Atomická schválená FR baseline a úplný soulad EA/SREQ nejsou uzavřeny.',why)
put('Cover','B16','159 původních EA FREQ, 6 UC005 vstupů a 26 zdrojových business návazností. Pracovní klasifikace oddělena od approval a přímých EA vazeb.',why)
put('Postup revize','C2','Konsolidovaná v03 + přímé primární ověření CZ zdrojů 3.11.; 26 business návazností a klasifikace původních EA FREQ.',why)
put('Revize MVP','B24','Primární CZ BRD, UC001–012, TR 26 řádků a MVP sešit byly nyní přímo znovu přečteny ve VDI. '+PRIMARY,why)
put('Revize MVP','C24','Interní verze není datum knihovny. Starší Requirements jsou Draft a mají duplicitní IAM ID. Schválená atomická FR baseline není doložena.',why)
put('Revize MVP','B25','Business a FREQ obsahuje pracovní capability/UC návaznosti v R:S a 26 přímých záznamů TR na ř.167–192.',why)
put('Revize MVP','C25','K:L:M přímé EA vazby a GUID zůstaly zachovány. Pracovní přiřazení neprokazuje existenci nových EA vztahů.',why)
primary_summary={'reviewedOriginalEaFreqRows':len(classified),'traceabilityRowsAdded':26,'exactTextMappedBook1Rows':len(exact_mapped),'manuallyReviewedBook1Rows':len(manual_rows),'totalReviewedBook1MappingRows':len(mapped),'scopeStates':dict(collections.Counter(x['state'] for x in classified))}
(HERE/'primary-classification.json').write_text(json.dumps({'summary':primary_summary,'eaRows':classified,'mappingRows':sorted(mapped),'exactTextMappingRows':exact_mapped,'manualReviewRows':sorted(manual_rows),'traceability':entries},ensure_ascii=False,indent=2),encoding='utf8')
