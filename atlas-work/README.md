# ServiceHub + Atlas CZ — pracovní podklady

Stav k 1. 11. 2026. Tato složka obsahuje dosud vytvořené pracovní výstupy. Nejprve otevřít [Stav práce](outputs/Stav_prace_2026-11-01.md), pak [aktuální Book1 v02](outputs/book1-v02/Book1_Atlas_pracovni_v02_2026-11-01.xlsx).

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

Další poznámky v `outputs/` zachovávají historii průzkumu. Mohou obsahovat později překonané závěry; pro současný stav mají přednost Stav práce a Book1 v02. Složka `outputs/book1-revize/` obsahuje předchozí revizi, nikoli aktuální sešit. Copilot odpovědi a jejich rozbory nejsou kanonickým zdrojem požadavků; evidované opravy a omezení je nutné respektovat.

## Dohodnutý postup

Nejnovější analýza Martina Dostála → soulad se závazným MVP → FREQ/capabilities a business vrstva/BPMN → aplikační vrstva, odpovědnosti Group/CZ a SREQ → aktualizace Atlas.xml → následná aktualizace Word SO. Book1 slouží jako průběžná evidence.

Původní `Book1.xlsx` a `Atlas.7z` v kořeni repozitáře tato dodávka nemění. Technické mezisoubory a lokální složka `work/`, na které odkazují některé poznámky, nejsou součástí této dodávky. Soubor `SHA256SUMS.txt` uvádí kontrolní součty uložených výstupů.

Podklady jsou uloženy na větvi `codex/atlas-stav-2026-11-01`, protože stávající workflow na `main` spouští nasazení do OpenShiftu. Tato dodávka je uložení dokumentace a pracovních výstupů.
