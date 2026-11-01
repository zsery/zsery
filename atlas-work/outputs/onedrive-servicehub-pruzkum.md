# Průzkum pracovních podkladů OneDrive

**Následné potvrzení uživatele:** „Atlas CZ Launch – Architecture Board Confirmation of Phased Implementation Approach.docx“ je závazná poslední verze a scope projektu. Dřívější výhrada k nepotvrzené závaznosti níže je tímto potvrzením vyřešena; ostatní zdroje se proti tomuto scope posuzují.

Datum: 1. 11. 2026. Otevřeno přes VDI v Průzkumníku: OneDrive – Vodafone Group / Documents / Projects / ServiceHub. Nejde o průzkum celého firemního OneDrive. Uživatel výslovně povolil libovolnou práci a ukládání uvnitř projektové podsložky AI; mimo ni nadále pouze čtení. Při této kontrole nebyl ve VDI žádný soubor vytvořen, upraven ani smazán. Poznámky uloženy lokálně v Codex outputs.

## Struktura a dostupnost

- ServiceHub: 29 položek, z toho AI, Atlas, Build Process.
- AI: otevřena, prázdná. Je povoleným pracovním prostorem pro další výstupy.
- Atlas: 11 položek včetně Billing; Book1.xlsx, backup.qea, components.xml, procesy Marketplace V2/V4 a Sell Atlas, internetový zástupce Requirements, Solution_Overview_ServiceHub_result.docx, test.txt a UMLX13.DTD.
- Atlas/Billing: dva soubory – vzor AppDirect Billing Transactions reportu v XLSX a VF Azure Billing Summary via ADMP for CZ v2.pdf.
- Build Process: 14 PDF s onboardingem, add licences (dvě varianty), closure, file/mail migration, GDAP, in-flight cancellation, M365 onboarding, cancellation, increase licence, build modify, integrated customer onboarding, error handling a add-ons onboarding. Srpnové kopie; porovnat se zářijovými aktualizacemi na SharePointu.

## Kořenové dokumenty a modelové exporty

V seznamu byly přímo zjištěny: AppImpacts.docx; Atlas CZ Launch – Architecture Board Confirmation of Phased Implementation Approach.docx; Atlas VF-CZ MVP IT SC… Word; CSD Cancellation, Inflight Cancellation, Integrated Build Modify (Subsequent Order Handling), Integrated Customer Onboarding PDF; CZ-Build_Process_Detail_V0.1.xlsx; IT Cost Calculator template; Product Requirements Atlas launch in Czech ve formátech DOC/DOCX/MHTML; Rizika.xlsx; Service_Hub_Use_Case_Document XML a EA XMI varianty včetně WITH_DIAGRAMS; ServiceHubAuthenticationAuthorization.png; SH-CZ-BusinessScope DOCX/PDF; Solution_Overview_ServiceHub.docx; sreq.csv; UseCase_Actor_Association.docx; Usecases.csv. Názvy v UI a metadata neprokazují schválení ani shodu kopií.

## Přečtený obsah

### Atlas CZ Launch – Architecture Board Confirmation…

Seznam/Word uvádí poslední změnu 23. října. Přímo přečten text scope a rizik na prvních dvou stranách. Dokument má 10 stran; aplikační diagramy jsou při daném rozložení částečně oříznuté, jejich úplné vazby nebyly spolehlivě přečteny.

- Projektový scope odkazuje na dohodu Františka Kožíška a Alexandry Staňkové a na „Variantu 2“ jako MVP, nikoli rozdělení projektu do dropů.
- In scope: standalone ServiceHub přes dedicated URL; Atlas pro cílový segment V4; interní manuální onboarding V4 zákazníků/uživatelů do SNOW; Customer Selector pro V2/V4 dodávaný Group; support flow směrem ke SNOW; Vodafone ID a lokální autorizace ServiceHub + VFCZ DXL.
- Out of scope: ONSC/WSC ↔ ServiceHub integrace, customer-context propagation a bidirectional integrace; automatizovaný V4 onboarding do SNOW; další úpravy ServiceHub UI/functionality.
- U Customer Selector se zmiňují V2/více CA a testování RBAC; význam RBAC je třeba sladit s pozdějším chatem o stejných funkčních právech.
- Rizika v dokumentu: manuální V4 onboarding a dočasné řešení; monitoring/reporting chyb; změna konceptu Customer Selector; administrátor vidí i účty pod sebou; technický dluh; reporting/BI; anonymizace/GDPR. Uvádí vlastníky a stavy Akceptováno/Mitigováno. Jde o tvrzení pracovního dokumentu, nikoli samostatně ověřený záznam rozhodnutí boardu.
- U manuálního onboardingu má technickou část zajistit Group; dokument popisuje pozdější automatizaci jako další projekt. Riziko trvalého dočasného řešení má závazek k odstranění technického dluhu.

### AppImpacts.docx

Přímo přečtena krátká dvoustránková pracovní poznámka. Word uvádí Last Modified 15. října, zatímco seznam souborů ukazoval jiné datum (21. srpna); metadata kopií je nutné sjednotit.

- TIBCO: komunikace Marketplace → Siebel, ověření potřebných atributů.
- Marketplace onboarding: povinné CRM ID, numerická validace, lookup do Siebel přes TIBCO, předvyplnění a editace údajů; VFID admin role přes DXL; první Atlas subscription; notifikace SNOW.
- ONSC/WSC: prolink do ServiceHub s předáním customer/user/language/VFID context.
- DXL: V2 performance; SNOW EVE a ServiceHub jen stručné nadpisy/poznámka.

**Dopad:** tato poznámka obsahuje záměry odporující pozdějšímu standalone MVP a říjnovému MVP Requirements (např. ONSC/WSC handover a automatický Siebel retrieval bez reconfirmation). Nejde o aktuální závazný seznam aplikačních dopadů. Je vhodná jako historie návrhu k revizi.

### Atlas/Billing/VF Azure Billing Summary via ADMP for CZ v2.pdf

Otevřen 11stránkový přehled; přečten úvod, klíčové body, konfigurace produktů, billing flow, report summary, popisy invoice items, podstatné poznámky a odkazy na HLD. Text v detailním mapovacím diagramu nebyl kompletně ověřen.

- Účel výslovně initial assessment/project scoping; potvrzený design má být v ADMP a VF Group HLD. Nezaměňovat s požadavky Atlas.
- Přístup Azure přes ADMP, vlastní Azure resources přes Azure portal; měsíční usage účtované zpětně, předoceněné Azure list price.
- Produkty PAYG, reservations a support. Některé manuální objednávky označeny TBC.
- Billing flow: Microsoft Partner Center usage → CAE zpracování/mapování → AppDirect REST API → AppDirect subscriptions → CSV billing report → OpCo.
- Report má zachovat stávající metodu/formát; konkrétní pole jsou draft k potvrzení HLD. Mapování do CZ zmiňuje company custom attribute / BAN.
- Jemnější usage detail je v invoice_line_description, nikoli jen edition_name; pro jeho využití může být potřeba upravit rozhraní ADMP ↔ OpCo. Rozsah CRM produktového mapování a detail vyúčtování jsou označeny za otevřená design rozhodnutí.

## Stav průzkumu

Struktura otevřené projektové složky a všech jejích zobrazených podsložek je zmapována. Vybrané klíčové texty byly přečteny; nejde o úplnou obsahovou revizi všech modelů, PDF, sešitů a jejich verzí. EA modely/XMI ani zástupce nebyly importovány nebo spuštěny. Soubory nebyly přepisovány. Pro další analýzu nejdříve porovnat pracovní kopie s říjnovým SharePoint scope, následně doplnit model a mapování funkcí/FREQ/SREQ podle ověřených zdrojů.
