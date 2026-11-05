---
name: follow-explicit-scope
description: Continue the user's Vodafone CZ Atlas and ServiceHub architecture work within explicit scope, read-only VDI, identity and GitHub constraints.
---

## Copilot ve VDI — závazné pravidlo uživatele

Ve VDI používej Copilot jako první volbu všude, kde je dostupný a použitelný pro zadaný úkol. Teams Copilot používej pro dohledání napříč SharePointem, Teams, e-maily a přepisy schůzek; Copilot ve Wordu a Excelu pro rozbor otevřených podkladů. Používej i další dostupné panely Copilotu. Před rozsáhlým ručním procházením ověř dostupnost Copilotu a zadej cílený dotaz. Vyžaduj odkazy a verze podkladů a závěry ověřuj proti primárním zdrojům. Detailní informace jsou v Confluence. Pro jejich vyhledávání v Teams používej konkrétního specializovaného agenta **Confluence Agent**, nikoli běžný Teams Copilot. Confluence čti přes tohoto agenta nebo přímo přes URL stránek. Pro přímý přístup přes URL musí být aktivní přihlášení účtem uživatele; ověř přihlášení a pokud chybí nebo vypršelo, dej uživateli vědět a požádej ho o ruční přihlášení. Přihlašovací dialogy neautomatizuj a nevyžaduj heslo do chatu. U výsledků Confluence Agentu vyžaduj URL primární stránky a dostupné údaje o verzi či datu; detail, který agent nevrátí, ověř přímým čtením stránky po přihlášení. Výsledek agenta není dokladem úplného průzkumu všech stránek a podsložek.

Platí zákaz změn zdrojových dat ve VDI: zadávání dotazů do Copilotu je povoleno, ale nepoužívej Apply/Insert/Edit ani jiné provedení změn do zdrojových dokumentů, sešitů či dat. Výjimku má pouze výslovně povolená projektová složka OneDrive AI. Při překážce zaznamenej konkrétní omezení a pokračuj jinou povolenou cestou. Běžně zadatelný dotaz nepřenášej na uživatele.


# Atlas / ServiceHub VFCZ

## Upřesnění rozsahu 5. 11. 2026

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
