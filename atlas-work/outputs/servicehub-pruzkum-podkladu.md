# ServiceHub + Atlas: průzkum podkladů pro architektonickou analýzu

Datum kontroly: 31. 10. 2026. Přístup přes obrazovku VDI AOProd W11.

## Závěr a rozsah

Podklady umožňují sestavit analýzu aplikačních komponent, odpovědností, integračních vazeb, zákaznických a uživatelských identit, návazností use cases a architektonických rizik. Hlavním analytickým zdrojem je dokumentace Martina Dostála.

Bylo otevřeno 38 uložených odkazů ve větvi ServiceHub včetně podsložek Atlas, Confluence, Group a Tasks a jeden přímý odkaz nadřazené složky Projects. Kontrola posuzovala dostupnost a využitelnost zdrojů. Nejde o kompletní přečtení všech dokumentů a příloh uvnitř odkazovaných knihoven ani o hotovou detailní analýzu. Sousední projekty VBTS a SNOW nejsou zahrnuty do tohoto soupisu.

## Důležité nálezy

- **Martin Dostál, PR25_0837 ServiceHub + Atlas – Use Case Specification:** ověřeno autorství. Starší přímá záložka vede na dokument s datem 10. 6. 2026; přes BRD nové / Business Requirements Document / Use Cases byla nalezena další verze s titulním datem 14. 10. 2026. Nejdříve je nutné stanovit platnou výchozí verzi a porovnat obsah.
- Ve starší specifikaci je výslovně vymezeno zaměření na chování a interakce. Detailní datový model a atributy nejsou jejím cílem. Vstupní kanály zahrnují ONSC, WSC a přímou URL při zachování autentizace a zákaznického kontextu.
- **Concept Solution Overview, ServiceHub + Atlas / PR25_0837:** obsahuje kapitoly pro ServiceHub, Marketplace/AppDirect, CRM/Siebel, Local DXL, Vodafone Identity/IDaaS, SNOW EVE, ONSC/WSC, IVR a billing/Kenan. Úvod popisuje ServiceHub jako vstupní bod pro spravované služby Atlas/Microsoft 365.
- **Czech Market’s Customer Segment & User Management Requirements for the Atlas Launch:** uvádí preferenci řízení zákazníků přes CRM a životního cyklu uživatelů lokálními systémy. Marketplace má být omezen na objednávání. Některé vazby pro V4 jsou označeny jako nepotvrzené. Jde o požadavek/preferovaný model, nikoli důkaz nasazeného stavu.
- **CZ Discussion v0.1:** řeší rozdíl mezi CRM Account Number a Marketplace Account Number, včetně více záznamů Marketplace pro jeden CRM účet. To je zásadní pro korelaci zákaznického kontextu.
- **CZ – Arch & SD requirements:** dostupná tabulka rozlišuje automatickou tvorbu zákazníka a mapování produktů od ručních činností vytváření uživatelů, administrátorů a deaktivace. Aktuálnost těchto pravidel je nutné porovnat s říjnovou specifikací.
- **Decision Input for V4 Customers and Admins into SNOW:** řeší vlastnictví zavedení V4 zákazníků a propagace životního cyklu administrátorů do SNOW mezi projekty ServiceHub/Atlas a SNOW EVE.
- **DXL Federated Identity / TMF691:** dostupné konkrétní mapování V2 user assets na TMF691 včetně identifikátorů, entity type, asset type a rolí. Lze tedy doložit i část datových kontraktů z technických zdrojů.
- **APIX:** dokumentace rozlišuje hlavní APIX2 pro DXL služby, APIX2 STC pro integraci SM-DP+ / eSIM a APIX2 EPNS pro AppDirect Marketplace. V modelu je nutné rozlišit konkrétní integrační instanci.
- **Digital Roadmap a Core backends input:** dostupné plánovací diagramy. Digital Roadmap je označena DRAFT; tyto zdroje nesmí samy sloužit jako důkaz realizované architektury.
- **COSMOS is now ServiceHUB:** doloženo přejmenování projektu; staré názvy mohou vést na relevantní podklady.

## Stav zaznamenaných rizik

| Záznam | Ověřený stav v UI | Význam pro další analýzu |
|---|---|---|
| [DMM-63198](https://vodafone-business.atlassian.net/browse/DMM-63198) | In Progress | Dva CZ zákaznické segmenty, oddělené portály a IT stacky; potřeba potvrdit integrační rozsah a dopady podpory obou stacků. |
| [DMM-64918](https://vodafone-business.atlassian.net/browse/DMM-64918) | In Progress | Otevřené architektonické body; dostupná příloha vyžaduje detailní rozbor. |
| [DMM-63200](https://vodafone-business.atlassian.net/browse/DMM-63200) | Done | Historické riziko chybějících uživatelů v CZ IDaaS a blokovaného SSO; komentář odkazuje na řešení přes Atlas Subscription Enablement. Nepřebírat mezi otevřená rizika pouze podle názvu záložky. |

## Soupis otevřených záložek

„Dostupné“ znamená, že se zobrazil dokument nebo knihovna. Neznamená kompletní přečtení obsahu.

| Větev | Záložka | Výsledek kontroly |
|---|---|---|
| Projects | DD Jirky | Dostupný dokument V2 Identifiers MKT, Microsoft, Foris, Snow; výslovně omezen na V2. |
| ServiceHub | BRD nové | Dostupná knihovna BRD, traceability a Use Cases; nalezena říjnová Dostálova specifikace. |
| ServiceHub | Decision Input for V4 Customers and Admins into SNOW | Dostupný rozhodovací dokument. |
| ServiceHub | Nacenění | Dostupný ServiceHub User Management: Scope and Effort Assessment. |
| ServiceHub | Account selection for SH | Dostupná knihovna Cosmos Architecture a prezentace Account Selection in Service Hub. |
| ServiceHub | Sharepoint V4 Customer OnBoarding | Chyba SharePointu: položka není dostupná / mohla být přesunuta nebo chybí přístup. |
| ServiceHub | V4 OnBoarding J. Krejčí | Dostupný HL Solution Overview CR03 Atlas – Create V4 Customer in SNOW, PR25_0749. |
| ServiceHub | Solution Overview | Dostupný Concept Solution Overview. |
| ServiceHub | Use cases | Dostupná červnová Dostálova specifikace. |
| ServiceHub | Foris CA data report | Dostupný Excel report Marketplace company identifiers; vhodný pro ověřování kardinalit účtů. |
| ServiceHub | Cyber Security Demand Portal – SPDA | Otevřel se portál; konkrétní SPDA dokument nebyl přečten. |
| ServiceHub | Sharepoint CZ folder | Dostupná CZ local folder s analytickými a architektonickými podklady. |
| ServiceHub | CZ – Service Now | Při kontrole zůstala prázdná karta; obsah neověřen. |
| ServiceHub | IDEA | Lokální Jira zobrazila vyhledávání bez výsledků a výzvu k přihlášení. |
| ServiceHub | Core-backends-input | Po přihlášení dostupný diagram B2B stack (V2) modernization plans. |
| Atlas | Pankaj Document | Dostupný Atlas: VF-CZ: MVP IT SC, export z 27. 5. 2026. |
| Atlas | Sharepoint CZ | Dostupná CZ local folder; překryv s jinou záložkou. |
| Atlas | BRD | Dostupný původní ServiceHub + Atlas BRD v0.1. |
| Atlas | DXL – Federated identity | Dostupná technická specifikace TMF691 a mapování V2 user assets. |
| Atlas | Viewpage | Skupinová Confluence IDaaS API Exposure: Page Not Found; příčina nerozlišena mezi neexistující stránkou a přístupem. |
| Atlas | System Documentation | Dostupný systémový rozcestník DXL s podstránkami. |
| Atlas | CZ – Arch & SD requirements.xlsx | Dostupný sešit s požadavky a ručními/automatickými úkoly. |
| Atlas | Atlas recap | Otevře recap Atlas Ramp-up session I; záznam a AI shrnutí již nedostupné. |
| Atlas | Word diskuse account | Dostupný CZ Discussion v0.1. |
| Atlas | Atlas – Ramp-up session I | Stejný recap jako Atlas recap; záznam a AI shrnutí již nedostupné. |
| Atlas | Sharepoint | Dostupná domovská stránka Atlas Programme. |
| Atlas | Interlock Sharepoint | Při kontrole zůstala prázdná karta; obsah neověřen. |
| Confluence | Road map | Dostupný Digital Roadmap [DRAFT]. |
| Confluence | VBU | Dostupný diagram VBU iniciativ a návazností. |
| Confluence | APIX | Dostupná dokumentace integrační brány a její architektury. |
| Group | RBAC | Dostupná prezentace RBAC Authorization (VF-ID), Kapil Jain, aktualizace srpen 2026. |
| Group | Document business reqs | Dostupné Czech Market User Management Requirements. |
| Group | Projects Jira | Dostupný seznam projektových prostorů skupinové Jiry. |
| Group | OpCo’s Prototypes [Service Hub] | Dostupný Figma prototyp My services / Service Hub. |
| Group | Support model Sharepoint | Dostupná knihovna Support Model. |
| Group | Sharepoint | Dostupná stránka COSMOS is now ServiceHUB. |
| Tasks | DMM-63198 | Dostupný záznam, In Progress. |
| Tasks | DMM-64918 | Dostupný záznam, In Progress. |
| Tasks | DMM-63200 | Dostupný záznam, Done. |

## Doporučená struktura vlastní analýzy

1. Potvrdit platné verze BRD, Dostálových use cases a Solution Overview.
2. Vytvořit katalog aplikačních komponent a jejich odpovědností s vazbou na zdroje.
3. Zpracovat integrační matici: zdroj, cíl, služba/rozhraní, přenášená data, spouštěč, synchronní/asynchronní průběh, vlastník a stav doložení.
4. Oddělit V2/V4, zákazníka/účet/uživatele/administrátora a jejich identifikátory.
5. Mapovat use cases na aplikace a služby; samostatně označit ruční kroky.
6. Vést seznam doložených rozhodnutí, návrhů, předpokladů, historických rizik a otevřených bodů.
7. Připravit aplikační pohled ArchiMate; technologickou vrstvu doplnit pouze z podkladů o platformách a nasazení.

Copilot byl otevřen, ale nebyl úspěšně použit k dotazu: přenos textu přes VDI vložil starý obsah schránky. Nesprávný neodeslaný text byl odstraněn. Žádné závěry v tomto soupisu nejsou založeny na odpovědi Copilotu.
