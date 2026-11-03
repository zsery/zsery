# ServiceHub + Atlas CZ — pracovní podklady

Stav k 3. 11. 2026. Pro pokračování na jiném PC nejprve otevřít [Předání práce](PREDANI_2026-11-03.md). Obsahuje instrukce uživatele, známé zdroje, větve GitHubu, omezení dosavadního průzkumu a přesný nedokončený stav. Původní [stav z 1. 11.](outputs/Stav_prace_2026-11-01.md) je historický podklad.

## Nové podklady pro navázání

- [Předání práce a instrukce](PREDANI_2026-11-03.md).
- [SharePoint průzkum z 2. 11. a opravená pravidla VFID USER](notes/atlas-sharepoint-review-2026-11-02.md), převzato z větve `codex/atlas-sharepoint-review`, commit `c58e2b922916b6004973ce1dcb303b97fc123925`.
- [Book1 s pravidly identity z 2. 11.](outputs/Book1_Solution_2026-11-02/Book1_Atlas_MVP_revize_2026-11-02.xlsx). Pozor: vznikl ze starší první revize a postrádá tři nové listy v02 a externí link part. Nepřepisovat jím v02; nejprve kontrolovaně sloučit změny.
- [Přenositelná pravidla explicitního scope](instructions/follow-explicit-scope.md).
- [Analýza pádu Outlooku](outputs/outlook-crash-analysis-20261102.md). Příčina není definitivně určena a oprava není hotová; dump není v repozitáři.
- `reproduction/`: vybrané původní skripty a kontrolní výsledky pro dohledání změn. Obsahují lokální cesty; před spuštěním ověřit. Neobsahují deploy key.

## Aktuální práce

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

Další poznámky v `outputs/` zachovávají historii průzkumu. Mohou obsahovat později překonané závěry; pro současný stav má přednost Předání práce z 3. 11. Rozšířeným základem zůstává Book1 v02; pravidla přidaná do oddělené revize z 2. 11. je třeba do něj sloučit. Složka `outputs/book1-revize/` obsahuje starší revizi. Copilot odpovědi a jejich rozbory nejsou kanonickým zdrojem požadavků; evidované opravy a omezení je nutné respektovat.

## Dohodnutý postup

Nejnovější analýza Martina Dostála → soulad se závazným MVP → FREQ/capabilities a business vrstva/BPMN → aplikační vrstva, odpovědnosti Group/CZ a SREQ → aktualizace Atlas.xml → následná aktualizace Word SO. Book1 slouží jako průběžná evidence.

Původní `Book1.xlsx` a `Atlas.7z` v kořeni repozitáře tato dodávka nemění. Technické mezisoubory a lokální složka `work/`, na které odkazují některé poznámky, nejsou součástí této dodávky. Soubor `SHA256SUMS.txt` uvádí kontrolní součty uložených výstupů.

Podklady jsou uloženy na větvi `codex/atlas-stav-2026-11-01`, protože stávající workflow na `main` spouští nasazení do OpenShiftu. Tato dodávka je uložení dokumentace a pracovních výstupů.
