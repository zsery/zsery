# ServiceHub — kontrola aktuálního Book1, 4. 11. 2026

Kontrola ve VDI přibližně 16:22–16:42 CET, pouze v OneDrive Preview. Zdroj: Documents / Projects / ServiceHub / Atlas / Book1.xlsx. Seznam ukazoval 402 kB a změnu před 11 minutami v okamžiku otevření. Soubor nebyl stažen ani přepsán; jeho hash a úplnou historii změn tato kontrola neověřila. Autorství konkrétních změn je informace uživatele, nikoli ověřený audit verzí.

## Aktuální základ a zachovaná práce

Pro pokračování se posuzuje aktuální OneDrive Book1. Starší lokální konsolidovaný Book1 z 3.11. je srovnávací evidence, nikoli náhrada této práce. Nepouštět nad aktuálním souborem historické konsolidační ani DXL skripty.

Nabídka náhledu zpřístupnila sedm listů: Cover, Functionalities, Interfaces, FREQ mapping, EAM App, Siebel EA Export a SREQ Aplikační role. Cover navíc uvádí _Enums. Nejde o důkaz odstranění všech ostatních listů: skryté listy a úplný XLSX balíček nebyly prohlédnuty. Starší lokální revize měla 14 listů; přenos poznatků musí být obsahový a po jednotlivých změnách.

Přímo ověřeno:

| Místo | Pozorování | Závěr pro pokračování |
|---|---|---|
| Cover!A5:B11 | Aplikační role, FREQ mapování, hierarchie funkcí, abstraktní rozhraní, aplikační inventura a EA export jsou oddělené. | Zachovat tuto strukturu a účel listů. |
| SREQ Aplikační role!B4:C5, E4:F5 | CRM-03 = customer-entity separation / IAM-24; CRM-04 = customer hierarchy / IAM-25. | Toto je aktuální význam v listu rolí. Staré záměny nepřenášet automaticky. |
| SREQ Aplikační role!B6:F7 | CRM-09 = konfigurace service.vodafone.com emailu pro Atlas tickety; CRM-10 = Atlas/Type C reprezentace a identifikační pravidla. FREQ pole je zde prázdné. | Zachovaným technickým schopnostem nepřiřazovat lead FREQ jen podle historického čísla. |
| SREQ Aplikační role!G2:I14 | Vazba na funkcionalitu nalezena; UC detail nepotvrzuje a AS-IS delta není ověřena. Původní schopnost zachována, absence detailu v UC není důvod ke smazání. | Správně oddělená schopnost aplikace a prokázaná změna. Zachovat. |
| Interfaces!H4:K4 | UC005: DXL poskytuje Customer/User, vztahy a role; ServiceHub rozhoduje o oprávnění, automaticky volí dostupné CRM ID a řídí přepínání. | Zachovat odpovědnost SH; upstream data nejsou implementací selectoru v CRM. |
| Interfaces!H5:K6 | TMF622/TMF621 a Local DXL jsou zachované technické abstrakce; konkrétní realizace není potvrzena UC. | Samotné technické názvy v E:F nejsou schválený Atlas API kontrakt. |
| Interfaces!H7:K7 | UC006 potvrzuje Marketplace jako zdroj dat a SH jako vlastníka zobrazení; Local DXL/TMF637 zůstává technicky nepotvrzený. | Nenavrhovat novou CZ implementaci jen z katalogového názvu. |
| Interfaces!H13:K13 | ONSC/WSC navigace a návrat jsou FUTURE / MIMO MVP; standalone navigace patří SH workspace. | Zachovat oddělení standalone MVP a budoucí portálové integrace. |

Ve FREQ mapping!B4:B5 je IAM-25 a IAM-24 v opačném pořadí než v listu rolí; J4:J5 odkazují na hierarchy a separation funkcionality. Řádek není identitou požadavku a rozdílné pořadí samo o sobě není chyba. Před závěrem o záměně je nutné přečíst celé hodnoty F4:F5 a cíle funkcí. Sloupce L:M jsou označené jako stav před opravou: jejich staré hodnoty se nesmějí vydávat za aktuální mapování. Cílená křížová kontrola byla předána Copilotu.

## Skutečně zadané úkoly Copilotu

1. Souhrn otevřeného Book1. Výsledek rozlišuje traceability/review podklad a schválené požadavky či implementaci.
2. Kontrola CRM-03/04, CRM-09/10, SH-07 a ID-07 s adresami buněk. První odpověď pouze „Ok, stopped“; nejde o provedenou kontrolu.
3. Upřesněná analýza stejných konfliktů. Copilot uvedl omezený extrakt bez adres buněk a bez všech šesti porovnání. U CRM položek identifikoval zachované detaily nepotvrzené UC; to bylo následně přímo ověřeno v listu rolí. Žádné opětovné nahrávání souboru nebylo provedeno.
4. Přesný úkol „Compare CRM-03 and CRM-04 across sheets. Cite cells.“ Dokončená odpověď rozlišuje CRM-03 separation a CRM-04 hierarchy jako komplementární datové příspěvky, nikoli duplicity. Citaci Interfaces!A22:G22 bylo následně možné přímo ověřit: A22 obsahuje IF_CRM_02, C22 Customer Context Information Interface, D22 Customer Context / Customer Hierarchy / Access Context a E22 IF02 Customer Information. Dřívější podezření, že citace nesedí s prvním CRM řádkem, se nepotvrdilo: jde o další rozhraní dále v tabulce. Tato odpověď sama neuzavírá všechny aktuální FREQ mapping hodnoty.

## Navázání nedokončené práce

Přímá stránka SnowConnectoru je nyní ve VDI přístupná po dřívějším ručním přihlášení. Pozorovaný návrh PR25_0749 popisuje middleware mezi ServiceNow a Foris/V2DB/Remedy, provisioning i trouble ticket doménu, TMF688/TMF621 a asynchronní store-and-forward zpracování. To neprokazuje kontrakt ServiceHub–SNOW pro Atlas PR25_0837. Nepřenášet Remedy integrační trasu automaticky do Atlasu a nevolat endpointy.

Další revize EA/SO má vycházet z těchto hranic:

| Oblast | Co lze zachovat / použít | Co zůstává otevřené |
|---|---|---|
| Identity a selector | VFID sub ↔ příslušný ONSC/WSC user 1:1, oddělená role s rozsahem; SH volí a přepíná dostupný kontext. | Atlas role enum, holding payload a přesný token negotiation kontrakt. |
| CRM | Zachované aplikační schopnosti nejsou automaticky nová implementační delta. | Přesné aktuální FREQ–SREQ–funkce propojení CRM-03/04; AS-IS a původní zdroj detailů. |
| SNOW | Samostatná logická SH–SNOW hranice, manuální V4 customer/admin onboarding. | Konkrétní operace, payload, company/user scope, stavové přechody, vlastník a implementační trasa. |
| Marketplace | Datový zdroj a readiness; SH nese zobrazovací pravidla. | Identifikátory a reconciliation postup; order acceptance není aktivace. |
| EA export | Existující GUID a jednotlivé významy zachovat. | Aktuální export proti novému workbooku, skutečné konektory a dopady na diagramy. |

## Doplněné přímé ověření ID-07 a návaznost do EA

SREQ Aplikační role!A166:E166 ponechává IDaaS, SREQ-ID-07, F-REQ-IAM-21 a původní název Determine Access Eligibility. F166 ale nově výslovně rozděluje odpovědnost: identity-side claims pro relying systems, autentizace Vodafone Identity, retrieval vztahů/rolí/CRM ID v DXL a content eligibility v ServiceHubu. H166 uvádí, že UC doložil cíl, nikoli AS-IS deltu; I166 popisuje opravenou cílovou odpovědnost/výsledek podle celého Wordu. Text v buňce je v náhledu výškově oříznutý, konec nebyl domýšlen. To je obsahový pokrok proti starší evidenci a nesmí být přepsán starým obecným nálezem „owner nesedí“.

| Zachovaný EA GUID ze staršího exportu | Nově ověřený význam / navazující krok |
|---|---|
| CRM-03: EAID_B29907A2_5D0C_4308_9300_EC771777E513 | Separation dat mezi nesouvisejícími customer entities; v aktuálním listu rolí IAM-24. Zachovat GUID, ověřit skutečný konektor a odpovídající funkci v aktuálním exportu. |
| CRM-04: EAID_1958D137_B5E0_4656_A47A_F6E00EE88156 | Hierarchy/context data; v aktuálním listu rolí IAM-25. Zachovat GUID; konkrétní holding payload zůstává otevřený. |
| ID-07: EAID_94649FF3_077F_40c7_A722_AA7E5292AA7F | Starý EA text přisuzuje access-context resolution Local DXL. Aktuální F166 rozlišuje IDaaS claims, DXL upstream data a SH rozhodnutí. Do modelu přenášet tyto oddělené role, nikoli připisovat veškerou eligibility IDaaS podle historického názvu E166. Bez ověření nového exportu nepřepsat GUID ani aplikaci. |
| SH-07: EAID_2AD6393E_362F_43b4_A075_875D6EDEE47A | Historický allow/deny konflikt není touto kontrolou znovu potvrzený. Hledání SH v nabídce SREQ v náhledu nevrátilo shodu a přechod na řádek 109 jej nezpřístupnil; viditelné řádky přeskakují. Neodkrývat či neobnovovat zdrojové řádky naslepo. |

GUID pocházejí z dřívějšího uloženého exportu a JSON kontroly 219 mapování; aktuální OneDrive workbook je v této kontrole znovu nepotvrdil. Tato tabulka je navazující podklad pro EA revizi, nikoli provedená změna modelu.

Atlas.xml ani Word SO nebyly touto kontrolou aktualizované. Dočasný filtr ID-07 byl v náhledu zrušen a soubor ponechán na Cover. Ověření se týká vybraných oblastí, nikoli všech řádků, vzorců a skrytých částí workbooku.

GitHub synchronizace se nepodařila: origin přes SSH skončil lokálním NtCreateDirectoryObject / 0xC0000022; veřejný HTTPS pokus hlásil Could not resolve host: github.com. Vzdálené SHA nebylo ověřeno a tento výsledek není vydáván za publikovaný.

