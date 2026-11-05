---
name: follow-explicit-scope
description: Continue the user's Vodafone CZ Atlas and ServiceHub architecture work within explicit scope, read-only VDI, identity and GitHub constraints.
---

## Nejnovější závazná pravidla pro pokračujícího agenta

- V EA smíš prohlížet/exportovat pouze uživatelovu projektovou složku `Zdeněk Šerý sandbox / 01_07_2026_ServiceHub_Atlas_CZ_PR25_0837` a její obsah. Neprocházej ostatní sandboxy ani jiné části sdíleného repository. Připojené EA je jen pro čtení: nic neměň, nemaž, neimportuj ani neukládej modelové změny. Výjimka pro pracovní OneDrive AI soubory se na zdrojové EA nevztahuje.
- Business procesy EA pouze orientační. Aplikační vrstva a UML entity nedokončené, přibližně správné; potvrzovat je proti závazným zdrojům, nikoli přebírat jako hotové řešení.
- Technické zdroje Confluence jsou dostupné v browseru VDI, pokud je relace přihlášená. Nejprve ověř skutečný stav; při požadavku na login požádej uživatele o ruční přihlášení a počkej s přístupem k chráněnému obsahu. Login neautomatizuj, nevyžaduj heslo. Lze použít i Teams agenta **Confluence**, jeho odpověď ověřit proti primární stránce. Neprohlašuj přístup za neexistující jen proto, že chybí konektor.
- Šetři kredity: pokračuj od uloženého ověřeného mezistavu, neopakuj hotové hledání, exporty, instalace, doplnění nebo kontroly bez věcného důvodu. Zadávej Copilotu konkrétní úkoly a cíleně ověřuj výsledek. Nepřidávej nevyžádané audity, reporty, alternativní postupy nebo přestavby řešení. Nezahlcuj uživatele opakovanými potvrzeními, omluvami, plány a nezměněnými stavovými zprávami; oznamuj konkrétní výsledek, podstatnou změnu nebo potřebný zásah.
- Nelži o postupu ani výsledku: rozlišuj zadáno / běží / skutečně změněno / uloženo / ověřeno. Push není hotový bez ověření remote SHA; prompt Copilotu není provedená oprava; částečný SO není plný dokument. Chybu oprav konkrétně, nepřekrývej ji tvrzením o dokončení ani slibem bez provedení.
- Připomínka, otázka nebo stížnost není souhlas s novou činností. Dotaz, jak spustit agenta z jiného PC, řeš úplným spouštěcím zadáním, ne samovolným spuštěním dalšího agenta. Bez nového výslovného příkazu další agenty nespouštěj. Toto pravidlo nebrání dokončit již autorizovanou věcnou práci.
- Nový agent na jiném PC si připraví checkout sám; uživatel nemá ručně otevírat/klonovat projekt jako náhradu spouštěcího zadání. Součástí předání je příprava vlastního GitHub přístupu: pro novou instanci vyhrazený SSH klíč, bez přepsání existujících klíčů, veřejný klíč předat uživateli k autorizaci zápisu, soukromý jen lokálně. Poté ověřit autentizaci a přístup k pracovní větvi. Klíč nikdy nevkládat do repozitáře ani přenášet z jiné instance. Je-li vlastní přístup instance již ověřeně připravený, zbytečně ho neobnovovat. Veřejné čtení není důkaz oprávnění zápisu.
- Začni aktuálním [prováděcím předáním](../../../POKRACOVANI_AGENTA.md) a nejnovějším stavem, nikoli překonanými historickými úkoly. Pokyny a skutečné výstupy průběžně ukládej do určené pracovní větve GitHubu; main neměň.

## Copilot ve VDI — závazné pravidlo uživatele

Ve VDI používej Copilot jako první volbu všude, kde je dostupný a použitelný pro zadaný úkol. Teams Copilot používej pro dohledání napříč SharePointem, Teams, e-maily a přepisy schůzek; Copilot ve Wordu a Excelu pro rozbor otevřených podkladů. Používej i další dostupné panely Copilotu. Před rozsáhlým ručním procházením ověř dostupnost Copilotu a zadej cílený dotaz. Vyžaduj odkazy a verze podkladů a závěry ověřuj proti primárním zdrojům. Detailní informace jsou v Confluence. Pro jejich vyhledávání v Teams používej konkrétního specializovaného agenta **Confluence Agent**, nikoli běžný Teams Copilot. Confluence čti přes tohoto agenta nebo přímo přes URL stránek. Pro přímý přístup přes URL musí být aktivní přihlášení účtem uživatele; ověř přihlášení a pokud chybí nebo vypršelo, dej uživateli vědět a požádej ho o ruční přihlášení. Přihlašovací dialogy neautomatizuj a nevyžaduj heslo do chatu. U výsledků Confluence Agentu vyžaduj URL primární stránky a dostupné údaje o verzi či datu; detail, který agent nevrátí, ověř přímým čtením stránky po přihlášení. Výsledek agenta není dokladem úplného průzkumu všech stránek a podsložek.

Platí zákaz změn zdrojových dat ve VDI: zadávání dotazů do Copilotu je povoleno, ale nepoužívej Apply/Insert/Edit ani jiné provedení změn do zdrojových dokumentů, sešitů či dat. Výjimku má pouze výslovně povolená projektová složka OneDrive AI. Při překážce zaznamenej konkrétní omezení a pokračuj jinou povolenou cestou. Běžně zadatelný dotaz nepřenášej na uživatele.


# Atlas / ServiceHub VFCZ

## Upřesnění rozsahu 5. 11. 2026

Business procesy v EA podle výslovného upozornění uživatele nemusejí být správné: používej je pouze orientačně, nikoli jako závazný zdroj požadavků nebo správného chování. Aplikační vrstva a UML entity jsou nedokončené a pouze předběžně přibližně správné. Zachovej existující GUID a ber je jako pracovní základ; jejich obsah a vztahy ověřuj proti Board MVP, aktuálním UC a technickým specifikacím Confluence. Samotná přítomnost v EA nepotvrzuje správnost ani úplnost.

Uživatel následně otevřel Sparx Enterprise Architect ve VDI se svým repository a výslovně povolil prohlížení a případný export, ale zakázal cokoli měnit nebo mazat. Připojené repository DEV-MODEL-MAIN je pouze zdroj ke čtení. Neprováděj import, úpravy elementů/vazeb/diagramů, mazání ani ukládání modelových změn. Exportuj pouze do nového pracovního souboru; zachovej původní model. Tento novější zákaz má přednost před dřívějším plánem dokončovat změny přímo v nativním EA.

Uživatel výslovně odmítl samostatný audit. Původní úkol je zkontrolovat aktuální Book1 po práci Copilota a dokončit navazující EA a vlastní SO. Nevytvářej ani nerozšiřuj další auditní listy, reporty nebo analytické review balíky jako náhradu dokončení. Existující správnou práci Copilota zachovej. Již vytvořené auditní artefakty nejsou požadovaným finálním výstupem; jejich historie nesmí řídit další úkoly. Potřebné cílené ověření konkrétní změny prováděj jako součást jejího dokončení.

## Výslovné upřesnění uživatele, 4. 11. 2026

Při práci s daty na OneDrive, SharePointu, v Outlooku a Teams nejprve použij Copilot. Preferuj Teams Copilot; pro otevřený dokument či sešit použij dostupný Copilot ve Wordu nebo Excelu, případně Outlook Copilot. Před přímým průzkumem zadej cílený dotaz a vyžádej odkazy na primární zdroje a dostupné verze. Toto pravidlo platí i pro krátké pokračování čtení. Ověření citovaných primárních zdrojů následuje po tomto kroku. Pro Confluence použij specializovaný Confluence Agent nebo autorizované přímé URL dle pravidel výše. Nedostupnost konkrétního Copilotu musí být skutečně ověřená; nevymýšlej výjimku podle délky práce. Zdrojová data pouze čti, nepoužívej Apply/Insert/Edit.

Read `atlas-work/AGENT_PROMPT.md` for the complete task instructions, repository access, evidence and exact incomplete state. Read the source notes it references. Use your own GitHub authorization for writes. Public repository reads use HTTPS. Do not assume access credentials or runtime paths from any other agent.

Follow only the user-authorized scope and necessary supporting steps. Never invent sources, API contracts, identifiers, approvals or completion. Keep facts, user decisions and working interpretations distinct. Preserve existing EA GUIDs and source text. Same historical IDs do not prove semantic identity.

VDI is read-only: no create/edit/delete of source data. Authorized search input is permitted; the specifically authorized project OneDrive AI folder is a narrow exception. Use explicit Immersive Reader for DOCX and Preview for XLSX. Do not bypass outbound clipboard restrictions, automate authentication dialogs, invoke documented write APIs, or inspect Outlook accessibility. Read the available computer-use skill before UI actions, observe the intended window, perform one action and refresh.

VFID sub maps 1:1 to the corresponding ONSC/WSC USER. Email is not the identity key. TMF691 target holding parent-child is separate. V4 SNOW customer/admin onboarding is manual MVP. Automatic Siebel retrieval/prefill is excluded until reconfirmed; minimum Marketplace data readiness remains. SH/CZ DXL token negotiation is part of MVP; do not infer the full Atlas contract from a generic SSO example. Class inheritance does not require instances; do not change CustomerContext generalizations without semantic evidence.

Continue substantive work, keep commentary concise, save progress to the specified GitHub branch, and verify remote SHA after writes. Keep validated Book1 separate from unexecuted pending scripts. Do not call the full task complete while required work remains. User instructions and platform restrictions take precedence.


## Přenos práce a zdroje – výslovné pokyny 5. 11. 2026

Technické informace, integrační kontrakty a jejich parametry ověřuj v Confluence. Použij přímou autorizovanou stránku nebo agenta v Teams s názvem **Confluence** (v dřívějším UI Confluence Agent). Vyžádej primární URL a dostupnou verzi či datum. Běžný Copilot není náhradou technické specifikace v Confluence. Pro ostatní vyhledávání, analýzu a práci s dokumenty/sešity používej Copilot. Rozlišuj návrh z emailu, technický kontrakt a potvrzení nasazení.

Pokud Confluence přístup chybí nebo vyprší, požádej uživatele o ruční přihlášení. Přihlášení neautomatizuj a nežádej heslo. Pokračuj nezávislou povolenou prací; technické mezery nevyplňuj odhadem.

Průběžně ukládej na GitHub také vlastní přenosné skills, mezistav, rozhodnutí, zdrojové odkazy, výstupy a reprodukční skripty. Udělej checkpoint po věcném milníku, před předáním a před ukončením práce; pushni pracovní větev a porovnej lokální a vzdálené SHA. Při nedostupné síti uchovej lokální checkpoint a výslovně uveď, že push není potvrzený. Main neměň. Nepřenášej přístupové údaje, SSH klíče, cookies ani přihlášené relace.

Předání musí odlišovat hotové a ověřené změny, rozpracované soubory a skutečné překážky, uvést další konkrétní krok a umístění pracovních kopií v OneDrive. Samotné zadání Copilotu není dokončení; ověř jeho výsledek. Zachovej jeho už provedené správné změny.

Uživatel výslovně zvolil zachování původního render_docx.py. Nepovažuj dřívější číselnou volbu 1 za platný souhlas s nahrazením rendereru Microsoft Wordem; konečné potvrzení bylo „Zachovej původní renderer“.
