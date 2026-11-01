# Přímý průzkum CZ local folder

1. 11. 2026. SharePoint Atlas Programme → 2. Portfolio → Atlas Expansion – Czech → Interlock-Pack → CZ local folder. Ve VDI pouze čtení; lokální poznámky. Průzkum probíhá, nejde o potvrzení přečtení všech souborů.

## Přímo přečtené klíčové zdroje

### Support_Material / Service_Hub_Atlas_MVP_Requirements.xlsx

Seznam uvádí změnu 19. října, Blanka Mikešová. Přečten celý viditelný obsah listu MVP Scope a tabulka MVP Functional Decomposition (ř. 4–26). Schválení ani interní verze se tím nepotvrzují.

MVP Scope: CZ BRD pokrývá jen lokální změny, integrační požadavky a procesy. VFID a standalone URL jsou Group dependencies. Výslovně bez ONSC/WSC integration. CZ scope: lokální product definition/business rules, Marketplace enablement/data, V4/SP-Siebel ordering, licence/lifecycle, VFCZ/VFG support routes, lokální dokumentace a E2E acceptance. Out of scope: ServiceHub vývoj, UX/internal behaviour, VFID/Customer Selector, Atlas C-product development, interní Group provisioning/lifecycle a ONSC/WSC integration.

Dekompozice ř. 4–23 obsahuje: Existing Asset & Scope Inventory, Product Definition, Commercial Offer Enablement, Contract Agreement, Terms & Conditions, Customer Technical Specification, Entry Points and Navigation, Eligibility Input Readiness, Authentication Input Readiness, Customer Context Input Readiness, Marketplace Company Identifier Readiness, Marketplace Company Data Readiness, Atlas Subscription Readiness, Atlas Service Data Availability, Channel Handling, Routing & Forwarding, Assisted Support, Termination Handling, Data Consistency, Escalation Handling.

Významné poznámky: CZ definuje eligibility inputs, Group vyhodnocuje; Group dodává autentizační/autorizační chování a Customer Selector; u Marketplace identifier ponechat minimální data; automatický Siebel retrieval/population excluded unless reconfirmed; Group onboarding outcome jako acceptance evidence, Group ticket lifecycle/UI jako dependency. Odhad tabulky 18 MD + 2 MD cross-cutting = 20 MD není schválený delivery závazek.

### Support_Material / Service Hub+Atlas - Requirements.xlsx

Přímo otevřen zdroj uvedený změnou 21. srpna, Martin Dostál. List Functional Requirements má skutečná čísla řádků. Přečteny ř. 1–109 v několika pohledech; další obsah dosud neprošel úplnou kontrolou.

**Oprava druhé odpovědi Copilotu:** nalezený soubor přímo potvrzuje významy CHM z Book1, nikoli chybné přečíslování v odpovědi Copilotu:

| Řádky zdroje | ID | Přečtený význam |
|---|---|---|
| 26 | CHM-05 | Standalone portál |
| 27–29 | CHM-06/07/08 | ONSC/WSC předá kontext; ServiceHub ho použije jako initial execution context |
| 31 | CHM-09 | Přímá URL |
| 32–35 | CHM-10/11/12/13 | Vstup WSC/ONSC, deep link a cílová stránka |
| 36–39 | CHM-14/15/16/17 | ONSC/WSC odkazy v ServiceHub a otevření nového okna/tabu |
| 40–42 | CHM-18/19/20 | Výběr kontextu při více; přímý vstup při jednom; chyba deep-link target |
| 44–50 | CHM-21 až 27 | Entry všem autentizovaným; eligibility; povolení/zákaz funkcí; info page a navigace |

CHM-20/21/25/26/27 tedy existují. Copilotovo „nenalezeno“ a jeho ID→text tabulka nejsou použitelné jako kanonické mapování.

Další zásadní opravy: IAM-29 v ř. 84 znamená předání V4 kontextu WSC → ServiceHub, nikoli povinný počáteční selector. IAM-39 v ř. 94 znamená customer selection při více kontextech, nikoli viditelnost odkazu na portálech. IAM-34 v ř. 89 upravuje access-context selection při více V2/V4 admin kontextech. IAM-44 v ř. 99 je následný customer-context selector.

**Dvojznačná ID přímo ve zdroji:** IAM-30/31/32 jsou použita v ř. 85–87 pro kontext WSC, znovu v ř. 107–109 pro subscription eligibility. Pro traceability musí být součástí reference i list, řádek, text a verze. Nepřečíslovávat bez rozhodnutí vlastníka požadavků.

Stará podmínka „více kontextů → výběr“ je doložena CHM-18, IAM-34/39; novější UC005 používá automatickou volbu jednoho dostupného CRM ID a následný selector. Přesné zrušení starých položek zatím nedoloženo.

## Dosud prohlédnuté adresáře

- Business Requirements Document: Use Cases; PR25_0837 BRD; Traceability Decomposition. Obsah již částečně přečten dříve.
- Use Cases (samostatně pod kořenem): Customer Roles Description.docx (27. 8.), List of Use Cases.xlsx (8. 6.), ServiceHub+Atlas Use Cases Specification (14. 10.) a staré PNG UC001–UC021 (červen). Číslování starých PNG se liší od říjnové specifikace; nemíchat jejich UC ID.
- Support_Material: vedle dvou sešitů také projektová retrospektiva/plán, BRD Atlas V4 Customer Lifecycle, BRD Plan Drops, Cosmos Scoping CZ, Decision Input for V4 Customers and Admin…, LME Process Activity Summary, Marketplace Company Pivot, Možnosti doručení, ONSC manual, Product Specification, Service Hub V2 Enablement, Delivery Blockers, User Journey Customer Context a launch checklist. Zatím jen seznam mimo dva sešity.
- Architecture: DXL/29.10.2026 se dvěma Word API podklady (TMF629 Customer Management a TMF691 Federated Identity), SH_group_architecture.url a Solution Overview ServiceHub.docx (24. 9.). Zatím seznam, ne úplný obsah.
- Business Workshops: List of Use Cases.xlsx (15. 6.) a WS_20260604.pptx (1. 6.). Zatím seznam.

Další prohlédnuté seznamy:

- Customers Documents: CZE/ENG Vodafone Services T+Cs, technické specifikace Office365/M365+Atlas a URL návrhu TS. Zatím názvy a metadata.
- ISS: Atlas Target Plan, Estimated Delivery Plan Update, Launch CheckPoint, Book.xlsx, Managed SaaS Atlas ISS Word, Microsoft Operator CSP Programme Guide a starší BRD. Zatím seznam.
- Obsolete: WS E2E procesy + SCENARE.docx. Archivní umístění zaznamenáno.
- Processes: AS-IS L2C VBU V2 sešit; Atlas/ServiceHub, Care V2/V4, Marketplace V2/V4, Sales V2/V4 a Sell Atlas PDF; podsložky To-Be a VFG Processes.
- Processes/To-Be: PROC-01 Marketplace Customer & User Creation.jpg, PROC-02 Atlas Product Order.jpg, PROC-03 SNOW Customer Lifecycle Initial… a ServiceHub.qea. PROC-01 otevřen jako diagram, drobný text v celkovém náhledu není dostatečný pro úplný přepis toku.
- VFG Processes/Build Process: onboarding, GDAP, mail/file migration, licence/add-ons, cancellation, closure, build modify a error handling; také CZ Build Process Detail V0.1.xlsx. Podsložka Updated Process With System& Task Type má zářijové varianty 13 PDF (autor metadata Harish Kumar Bhar), včetně M365/Integrated Customer Onboarding a cancellation změněných 30. 9. Nekládat srpnové a zářijové varianty automaticky na roveň.
- VFG Processes/Run Process: Customer Case Resolution, Escalation, Internal Access, Knowledge, Major Issue, ITSM Tickets, MyIT Tickets, Service Request a Case Management PDF (většinou 29. 9.). Zatím seznam.
- VFG Processes/Sell Process: Atlas Czech Republic SELL E2E.docx (5. 10.) a PDF (26. 8.). Zatím seznam; Word a PDF mají různá data změny.
- Project Documents CZ PMO: fáze 01 Ideation až 07 Closure, VF Internal estimations, Processes/Procedures, FIT, Project Finance, Archive a Communication Matrix.xlsx. Hlubší PMO větve zatím neprošly kontrolou, při prioritizaci Martinových analýz nebyly otevřeny.
- V4 Interim Approach Process: SharePoint výslovně zobrazil prázdnou složku.

Kořen také obsahuje LME.xlsx a ServiceHub Atlas CRG 2026-04.pptx; zatím neotevřeno. Seznamy všech 11 přímých podsložek kořene byly prohlédnuty. To není úplná obsahová revize všech dokumentů; řada PDF/Word/Excel podkladů čeká na detailní čtení.
