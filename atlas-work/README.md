# ServiceHub + Atlas CZ — pracovní podklady

## Copilot ve VDI — závazné pravidlo uživatele

Ve VDI používej Copilot jako první volbu všude, kde je dostupný a použitelný pro zadaný úkol. Teams Copilot používej pro dohledání napříč SharePointem, Teams, e-maily a přepisy schůzek; Copilot ve Wordu a Excelu pro rozbor otevřených podkladů. Používej i další dostupné panely Copilotu. Před rozsáhlým ručním procházením ověř dostupnost Copilotu a zadej cílený dotaz. Vyžaduj odkazy a verze podkladů a závěry ověřuj proti primárním zdrojům. Detailní informace jsou v Confluence. Pro jejich vyhledávání v Teams používej konkrétního specializovaného agenta **Confluence Agent**, nikoli běžný Teams Copilot. Confluence čti přes tohoto agenta nebo přímo přes URL stránek. Pro přímý přístup přes URL musí být aktivní přihlášení účtem uživatele; ověř přihlášení a pokud chybí nebo vypršelo, dej uživateli vědět a požádej ho o ruční přihlášení. Přihlašovací dialogy neautomatizuj a nevyžaduj heslo do chatu. U výsledků Confluence Agentu vyžaduj URL primární stránky a dostupné údaje o verzi či datu; detail, který agent nevrátí, ověř přímým čtením stránky po přihlášení. Výsledek agenta není dokladem úplného průzkumu všech stránek a podsložek.

Platí zákaz změn zdrojových dat ve VDI: zadávání dotazů do Copilotu je povoleno, ale nepoužívej Apply/Insert/Edit ani jiné provedení změn do zdrojových dokumentů, sešitů či dat. Výjimku má pouze výslovně povolená projektová složka OneDrive AI. Při překážce zaznamenej konkrétní omezení a pokračuj jinou povolenou cestou. Běžně zadatelný dotaz nepřenášej na uživatele.

**Pokračování jiným agentem: [START_HERE.md](START_HERE.md).** Startovní prompt, poslední stav, skills, připojení a obnovení layoutu.

Stav k 3. 11. 2026. Pro pokračování na jiném PC nejprve otevřít [Předání práce](PREDANI_2026-11-03.md). Obsahuje instrukce uživatele, známé zdroje, větve GitHubu, omezení dosavadního průzkumu a přesný nedokončený stav. Původní [stav z 1. 11.](outputs/Stav_prace_2026-11-01.md) je historický podklad.

## Nové podklady pro navázání

- [AKTUÁLNÍ Book1 v03](outputs/Book1_2026-11-03/Book1_Atlas_konsolidovany_2026-11-03.xlsx) a [stav revize a kontrol](outputs/Book1_2026-11-03/Stav_Book1_2026-11-03.md). Po primárním ověření 3.11.: 159 EA FREQ pracovně klasifikováno, 26 business návazností z TR přepsáno, 219 mapovacích řádků pracovně posouzeno (188 přes text, 31 samostatně). Schválení atomických FR, EA a SO zůstávají otevřené.
- [Přímé ověření CZ BRD, UC, MVP a Traceability 3.11.](outputs/Overeni_zdroju_VDI_2026-11-03.md). Metadata verzí, obsah UC001–012, řádkový přepis TR, rozdíly staršího Draftu a hranice skutečného čtení.
- [Předání práce a instrukce](PREDANI_2026-11-03.md).
- [SharePoint průzkum z 2. 11. a opravená pravidla VFID USER](notes/atlas-sharepoint-review-2026-11-02.md), převzato z větve `codex/atlas-sharepoint-review`, commit `c58e2b922916b6004973ce1dcb303b97fc123925`.
- [Historický Book1 s pravidly identity z 2. 11.](outputs/Book1_Solution_2026-11-02/Book1_Atlas_MVP_revize_2026-11-02.xlsx). Vznikl ze starší první revize a postrádá tři listy v02 a externí link part. Jeho věcné změny jsou již sloučené do aktuální v03; nepoužívat jej jako základ další práce.
- [Přenositelná pravidla explicitního scope](instructions/follow-explicit-scope.md).
- [Analýza pádu Outlooku](outputs/outlook-crash-analysis-20261102.md). Příčina není definitivně určena a oprava není hotová; dump není v repozitáři.
- `reproduction/`: vybrané původní skripty a kontrolní výsledky pro dohledání změn. Obsahují lokální cesty; před spuštěním ověřit. Neobsahují deploy key.

## Podklady z 1. listopadu (historie)

- [Stav práce a další kroky](outputs/Stav_prace_2026-11-01.md).
- [Book1 — pracovní verze 02](outputs/book1-v02/Book1_Atlas_pracovni_v02_2026-11-01.xlsx): Postup revize, Business a FREQ, EA SREQ a původní záložky s doplněnou kontrolou EA ID/GUID. Pracovní evidence, nikoli dokončená nejnovější business baseline.
- [První EA revize](outputs/ea-revize/Atlas_prvni_revize.md): obsahuje upozornění na stažené hodnocení CustomerContext; tento bod není doporučením ke změně.
- [Porovnání 219 mapovacích řádků Book1 s EA](outputs/ea-revize/Book1_EA_vazby.csv).
- [Inventura projektových diagramů](outputs/ea-revize/Diagramy_projektu.csv).

## Průzkum zdrojů

- [SharePoint CZ local folder](outputs/sharepoint-cz-local-pruzkum.md).
- [Závazný scope a odkazy](outputs/notepad-odkazy-a-zavazny-scope.md).
- [OneDrive podklady](outputs/onedrive-servicehub-pruzkum.md).
- [Průzkum dokumentace](outputs/servicehub-pruzkum-podkladu.md).

Další poznámky v `outputs/` zachovávají historii průzkumu. Mohou obsahovat později překonané závěry; pro současný stav má přednost aktualizované Předání práce z 3. 11. a Stav_Book1 u v03. Aktuálním základem je výhradně konsolidovaná v03. Starší sešity jsou ponechané pro dohledání historie. Copilot odpovědi a jejich rozbory nejsou kanonickým zdrojem požadavků; evidované opravy a omezení je nutné respektovat.

## Dohodnutý postup

Nejnovější analýza Martina Dostála → soulad se závazným MVP → FREQ/capabilities a business vrstva/BPMN → aplikační vrstva, odpovědnosti Group/CZ a SREQ → aktualizace Atlas.xml → následná aktualizace Word SO. Book1 slouží jako průběžná evidence.

Původní `Book1.xlsx` a `Atlas.7z` v kořeni repozitáře tato dodávka nemění. Technické mezisoubory a lokální složka `work/`, na které odkazují některé poznámky, nejsou součástí této dodávky. Soubor `SHA256SUMS.txt` uvádí kontrolní součty uložených výstupů.

Podklady jsou uloženy na větvi `codex/atlas-stav-2026-11-01`, protože stávající workflow na `main` spouští nasazení do OpenShiftu. Tato dodávka je uložení dokumentace a pracovních výstupů.

- [Kontrola business vrstvy EA a návazností](outputs/ea-revize/EA_business_revize_2026-11-03.md) a [crosswalk 21 původních UC s GUID](outputs/ea-revize/EA_UC_obsahovy_crosswalk_2026-11-03.csv). Nové UC číslování není totožná identita. XMI a SO zatím nezměněny.

## Poslední rozpracování pro předání

- [TMF691 – nové přímé technické ověření](outputs/DXL_TMF691_overeni_2026-11-03.md).
- [TMF629 – ověřené GET a customer mapping části](outputs/DXL_TMF629_overeni_2026-11-03.md), s přesným rozsahem nedokončeného čtení.
- [Nespuštěný DXL builder](pending/book1-dxl-update/README.md), oddělený od ověřeného XLSX.
- [GitHub transport a příkazy](instructions/github-access.md), [reprodukce](instructions/reproduction.md), [přenosný skill](instructions/skills/follow-explicit-scope/SKILL.md) a [repo instrukce](AGENTS.md).
