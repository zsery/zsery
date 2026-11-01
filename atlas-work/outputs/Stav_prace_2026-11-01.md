# Stav práce — navázání po 1. 11. 2026

## Uložení do GitHubu

Na pokyn uživatele je pro sdílení pracovních výstupů určen repozitář `zsery/zsery`. Tato dodávka používá větev `codex/atlas-stav-2026-11-01` a složku `atlas-work/outputs/`; přehled je v `atlas-work/README.md`. Původní Book1.xlsx a Atlas.7z v kořeni nejsou přepsány. Souborové cesty `outputs/...` níže jsou platné relativně ke složce `atlas-work/`. Technické lokální cesty `work/...` popisují původní prostředí; tyto mezisoubory se do repozitáře nekopírovaly. Další analýza se dnes neprovádí; uloženy jsou současné výstupy.

## Dohodnutý směr

Solution architecture integrace Vodafone Group a Vodafone CZ. Postupovat od nejnovější analýzy Martina Dostála v mezích závazného MVP: analytické podklady → aktuální FREQ a související capabilities → business ArchiMate vrstva a případně BPMN → aplikační ArchiMate vrstva, integrační vazby a SREQ → aktualizace EA → následně Word SO (Solution Overview).

Book1 slouží jako průběžná evidence dat, postupu a vazeb. Záložky se budou postupně revidovat; existující model v Atlas.xml nejprve prověřit a opravit/doplnit, nepřetvářet bez zdůvodnění. Zachovávat identitu/GUID. Book1 ani EA samy nejsou autoritou pro aktuální business scope.

## Aktuální výstup

Pracovní sešit: `outputs/book1-v02/Book1_Atlas_pracovni_v02_2026-11-01.xlsx`.

- 14 záložek, včetně nových Postup revize, Business a FREQ, EA SREQ.
- Business a FREQ: 159 existujících EA FREQ záznamů (dva mají v názvu neúplný prefix -REQ) a šest analytických vstupů z přímo přečteného UC005. Nejde o 165 schválených požadavků ani dokončenou nejnovější baseline.
- EA SREQ: 111 modelových prvků identifikovaných SREQ ID, včetně případných opakování stejného ID. To není počet unikátních SREQ.
- Původní FREQ mapping obsahuje 219 řádků. U 87 se našlo SREQ ID v projektové větvi exportu, u 132 ne. Shodné ID není potvrzením obsahu/scope; nenalezené ID není automaticky chybějící schopnost.
- Doplněny EA GUID, aktuální modelové texty a stav dohledání do FREQ mapping a SREQ Aplikační role.
- Zachováno sedm původních Excel tabulek, dva souborové díly externích odkazů a nesouvisející buňky/vzorce. Původní chyba EAM App!F459 (#VALUE!) zůstává. Zachovány původní filtry/skryté řádky.
- Sešit byl znovu načten a nové oblasti vizuálně zkontrolovány. Není ověřen jako úplná schválená business/EA baseline.

Starší výstupy: `outputs/book1-revize/`, `outputs/ea-revize/`, poznámky SharePoint/OneDrive/Confluence a analýzy v outputs. Souhrn v02 má pro stav postupu přednost před staršími tvrzeními „EA export chybí“.

## Vstupy a technické zpracování

Uživatelem dodané soubory: `Y:/zsery/Downloads/Book1.xlsx`, `Y:/zsery/Downloads/Atlas.xml`. Y: někdy vyžaduje konkrétní oprávnění k čtení. Lokální pracovní kopie jsou dostupné:

- `work/book1/Book1-original.xlsx`, `work/book1/data.json`.
- `work/ea/Atlas-original.xml` (111 925 351 bajtů), `work/ea/index.json` a `work/ea/audit-summary.json`.
- Export: 18 536 záznamů v EA Extension/elements, 14 898 konektorů, 664 diagramů. Projektová větev `01_07_2026_ServiceHub_Atlas_CZ_PR25_0837`: 2 093 záznamů prvků, 55 diagramů. Záznamy zahrnují balíčky a pomocné prvky. Export zahrnuje i jiné projekty/autory.
- Autor uživatele v modelu je SeryZ; autor a umístění nejsou samy o sobě důkazem aktuálnosti. Diagramy využívají i sdílené prvky mimo projektovou větev.
- Zpracování: `work/ea/prepare_book1_v02.py`, `work/book1/revise-v02.mjs`, `work/book1/preserve-v02.py`, `work/book1/verify-v02.mjs`. Příprava JSON → authoring @oai/artifact-tool → přenos autorizovaných změn do původního OOXML kvůli zachování externích vazeb a původní dynamické oblasti → kontrola. Souhrny kontrol v `work/book1/v02-native-check.json` a `work/book1/v02-final-check.json`.
- Při dalším vytváření Excelu použít spreadsheet skill a bundled runtime; prostý artifact export odstraňuje externí link parts a přepočítává původní EAM oblast. Nepřepsat vstupy. Před novou authoring operací dodržet marker podle skillu.

## Závazné věcné body

- `Atlas CZ Launch – Architecture Board Confirmation of Phased Implementation Approach.docx` je podle výslovného potvrzení uživatele poslední závazný scope.
- SSO je základ MVP: standalone ServiceHub, přihlášení VFID, SH specifickým voláním vyjedná token s CZ DXL a obdržený token použije v hlavičkách dalších VFCZ DXL volání. Endpoint/grant/audience/formát tokenu a hlavičky/expirace/obnova/chyby nejsou potvrzeny; nevymýšlet Bearer/JWT ani převzetí generického shared-code flow.
- ONSC/WSC portálová integrace, navigace a context handover nejsou aktuální MVP. Odlišit je od upstream rolí/vztahů poskytovaných přes DXL.
- V4 customer/user onboarding do SNOW je manuální; automatizaci nepřevzít z historie.
- Minimum Marketplace company identifier/data readiness zůstává potřebné. Automatický Siebel retrieval/prefill/population je v MVP Requirements vyloučen bez opětovného potvrzení.
- UC005: automaticky zvolit jedno dostupné CRM ID; následně umožnit přepínání. Priorita automatické volby nedoložena. Oprávněný admin má specifický obsah; uživatel bez admin role obecnou stránku. Oddělit od Atlas subscription eligibility UC006.
- RBAC/eligibility a SNOW company scope nerozmělnit do jedné podmínky. Konkrétní pravidla zatím vyžadují ověření.

## Podklady a dosavadní rozsah čtení

Podklady Martina jsou ve SharePoint `CZ local folder` a jeho podsložkách. Relevantní přímé poznámky: `outputs/sharepoint-cz-local-pruzkum.md`, `outputs/notepad-odkazy-a-zavazny-scope.md`, `outputs/onedrive-servicehub-pruzkum.md`.

- U1: `PR25_0837_ServiceHub_Atlas_Use_Case_Specification.docx`, verze 0.1, Last Update 14.10.2026; přímo čten zejména UC005 s.19–21. Metadata knihovny pozdější, přesnou nejnovější interní verzi je třeba ověřit. Staré červnové obrázky mají jiná UC čísla.
- BRD: `PR25_0837_ServiceHub_Atlas_BRD.docx`, relevantní části přímo čteny, změna v knihovně 23.10.; přesná interní aktuální revize a úplný obsah nepotvrzeny.
- M1: `Service_Hub_Atlas_MVP_Requirements.xlsx`, změna v knihovně 19.10.; přímo čteny MVP Scope a MVP Functional Decomposition. Group vlastní SH UI/selector/chování, CZ lokální integrace/data/procesy a E2E akceptaci.
- R1: `Service Hub+Atlas - Requirements.xlsx`, Support_Material, změna 21.8., starý draft. IAM ID se mezi zdroji liší; přímo ve zdroji jsou opakovaná IAM-30/31/32 pro jiné obsahy (ř.85–87 a107–109). Nepřečíslovat bez dohledání zdroje/verze/textu a rozhodnutí.
- `Solution_Overview_ServiceHub.docx` byl přímo otevřen jako 30stránkový Concept SO; kompletní obsah a tabulky ještě nebyly zkontrolovány. Přegenerování SO je budoucí krok.
- V knihovnách jsou další procesy, analýzy, technické dokumenty (včetně DXL podkladů ze složky 29.10.), které byly často zatím jen inventarizovány. Neoznačovat za přečtené.

## Modelové body pro další ověření

- Paralelní větve `90.2 Application layer/Functionalities` a `90.2 Application layer/VFCZ/Functionalities` obsahují různé GUID pro stejné názvy. Neprovádět automatické slučování; ověřit záměr a kanonické použití.
- SREQ-CRM-09 v EA je email configuration pro assisted Atlas tickets; původní Book1 jej váže na lead-create. Zdrojový rozpor je třeba vyřešit, shoda ID nestačí.
- V některých novějších EA SREQ je dokumentace pouze MVP a přitom jde o portálové entrypointy. Označení v modelu nesmí přebít závazný Board scope.
- V exportovaných sedmi projektových UML Interaction nebyly nalezeny message záznamy. Diagram SSO to ServiceHub má zobrazované účastníky, ale příslušná interaction nemá message/lifeline záznamy. Nevyvozovat automaticky, že v živém EA nic neexistuje; ověřit export a kontext. Nelze tím potvrdit tokenový flow.

## Stažený závěr CustomerContext — nezopakovat

Původní doporučení opravovat CustomerContext kvůli generalizacím na CRM ID a user_id bylo po diskusi s uživatelem staženo jako nedoložené. Uživatel používá dědění definic; z pouhého vztahu nelze určit chybu ani automaticky navrhovat náhradu asociací. Nález neopakovat jako potvrzenou chybu. Stažení je zaznamenáno v Postup revize a v úvodu původní EA analýzy.

Uživatel důrazně odmítl nepodložené hodnocení a následné opakované omluvy/sliby. Komunikovat stručně, konkrétně a pracovat; nedělat z nejasného záměru modelu chybu. Nepředkládat další obecné poučování.

## Zítřejší první krok

Navázat aktuálním Book1 v02 a listem Business a FREQ. Pokračovat u nejnovějších Martinových analýz a jejich verzí proti B1, doplnit aktuální business text a zdrojovou sekci a vazby na existující business prvky/capabilities/BPMN. Až potom dopracovávat aplikační dekompozici a SREQ. Šest UC005 vstupů dosud nemá uměle vytvořená FREQ ID; je třeba je spárovat s kanonickými požadavky.

Datová příprava Marketplace/Siebel je následná důležitá oblast: zjistit konkrétní reporty, význam klíčů (CRM ID/CA/BA/BAN/company UUID nejsou zaměnitelné), master atributů a způsob opravy. Rozlišit bez match, více matchů, duplicitu a existující vazbu s rozdílnými daty; nevymýšlet schválený opravný mechanismus.

## Přístupová pravidla

Remote VDI pouze čtení; výjimka zadávání do vyhledávání SharePoint/Confluence/Teams/Outlook/Copilot. Uživatel později dovolil libovolné ukládání v konkrétní vzdálené OneDrive projektové podsložce AI; mimo ni platí read-only. Nic v EA, zdrojovém XML, SharePoint dokumentech ani produkčních datech nebylo měněno. Žádné obcházení firemních blokací neprovádět. User-facing lokální výstupy ukládat pod outputs.

Uživatel požádal uložit stav a pokračovat zítra; po uložení nepokračovat v analýze.
