# Pokračování práce Atlas / ServiceHub VFCZ

## Copilot ve VDI — závazné pravidlo uživatele

Ve VDI používej Copilot jako první volbu všude, kde je dostupný a použitelný pro zadaný úkol. Teams Copilot používej pro dohledání napříč SharePointem, Teams, e-maily a přepisy schůzek; Copilot ve Wordu a Excelu pro rozbor otevřených podkladů. Používej i další dostupné panely Copilotu. Před rozsáhlým ručním procházením ověř dostupnost Copilotu a zadej cílený dotaz. Vyžaduj odkazy a verze podkladů a závěry ověřuj proti primárním zdrojům. Detailní informace jsou v Confluence. Pro jejich vyhledávání v Teams používej konkrétního specializovaného agenta **Confluence Agent**, nikoli běžný Teams Copilot. Confluence čti přes tohoto agenta nebo přímo přes URL stránek. Pro přímý přístup přes URL musí být aktivní přihlášení účtem uživatele; ověř přihlášení a pokud chybí nebo vypršelo, dej uživateli vědět a požádej ho o ruční přihlášení. Přihlašovací dialogy neautomatizuj a nevyžaduj heslo do chatu. U výsledků Confluence Agentu vyžaduj URL primární stránky a dostupné údaje o verzi či datu; detail, který agent nevrátí, ověř přímým čtením stránky po přihlášení. Výsledek agenta není dokladem úplného průzkumu všech stránek a podsložek.

Platí zákaz změn zdrojových dat ve VDI: zadávání dotazů do Copilotu je povoleno, ale nepoužívej Apply/Insert/Edit ani jiné provedení změn do zdrojových dokumentů, sešitů či dat. Výjimku má pouze výslovně povolená projektová složka OneDrive AI. Při překážce zaznamenej konkrétní omezení a pokračuj jinou povolenou cestou. Běžně zadatelný dotaz nepřenášej na uživatele.

## Zadání pro samostatného agenta

Pracuj s repozitářem `zsery/zsery`, větví `codex/atlas-stav-2026-11-01`.

### Připojení

Repozitář je veřejný. Čtení nevyžaduje SSH klíč:

```sh
git clone --branch codex/atlas-stav-2026-11-01 --single-branch https://github.com/zsery/zsery.git
cd zsery
git status --short
```

Pokud máš checkout, nejprve ověř jeho větev a změny; nepřepisuj rozpracované soubory.

Pro zápis použij svůj připojený GitHub konektor nebo vlastní GitHub autorizaci. Ověř oprávnění k `zsery/zsery`; dostupnost veřejného čtení sama nezaručuje zápis. Přihlášení browseru nepovažuj za autorizaci Git klienta. Nepřenášej přístupové údaje jiné instance a nevkládej klíče do repozitáře.

GitHub konektor: načti metadata repozitáře, ověř oprávnění push, přečti větev. Pro dávkové uložení podporuje Git data operace create_blob → create_tree nad existujícím base tree → create_commit s existujícím parent SHA → update_ref pracovní větve s expected_sha. Nepoužívej force. Po zápisu znovu načti HEAD větve a ověř SHA.

Git s vlastní funkční autorizací:
```sh
git add -- atlas-work
git commit -m "Update Atlas working analysis"
git push origin HEAD:refs/heads/codex/atlas-stav-2026-11-01
git rev-parse HEAD
git ls-remote origin refs/heads/codex/atlas-stav-2026-11-01
```
Obě SHA musí souhlasit. Nezapisuj do main, obsahuje deployment workflow. Pokud zápis není povolen, dál čti veřejné podklady a přesně uveď chybějící oprávnění.

### Načtení práce

Přečti:
- `atlas-work/AGENTS.md`
- `atlas-work/instructions/skills/follow-explicit-scope/SKILL.md`
- `atlas-work/PREDANI_2026-11-03.md` pro věcný stav a zdroje
- `atlas-work/outputs/Book1_2026-11-03/Stav_Book1_2026-11-03.md`
- `atlas-work/outputs/ea-revize/EA_business_revize_2026-11-03.md`
- `atlas-work/outputs/DXL_TMF691_overeni_2026-11-03.md`
- `atlas-work/outputs/DXL_TMF629_overeni_2026-11-03.md`
- `atlas-work/pending/book1-dxl-update/README.md`

Sluč přiložený skill do vlastního adresáře skills podle svého skill-creator, zachovej relevantní pravidla, uložený soubor znovu načti. Nepřebírej cesty k runtime nebo přístupovým údajům z jiných prostředí. Pro spuštění použij své dostupné knihovny a nástroje.

### Ověřený stav

Kanonický Book1: `atlas-work/outputs/Book1_2026-11-03/Book1_Atlas_konsolidovany_2026-11-03.xlsx`.
SHA-256: `10998f6652bcea8f0bdc357cd092663bed5334d21bf9db0255470a969fc786a2`.
14 listů, 219 pracovně posouzených mapovacích řádků; 188 přes text, 31 samostatně. 159 EA FREQ, 6 UC005 analytických vstupů a 26 business traceability záznamů. 4663 ověřených změn, 1878 vzorců/cache zachováno. Toto není schválení atomické FR baseline ani všech SREQ vazeb.

Tři skripty v pending/book1-dxl-update nejsou spuštěné; nové TMF poznatky nejsou promítnuty do uvedeného XLSX. Reproduction obsahuje ověřený builder odděleně. Zkontroluj pending diff, vytvoř plán, proveď authoring podle spreadsheet skillu, zachování nativních částí, reimport a vizuální kontrolu; aktualizuj hash a stav až po ověření.

Atlas.xml a Word SO nejsou aktualizované. Úplný průzkum všech Group podsložek není dokončen. TMF691 čtecí text prošel do konce bez diagramů; TMF629 má přečtené vybrané GET a celé OLC/V2 mapping části. Board čtení pokračuje od začátku In scope. Živý VDI stav vždy znovu zjisti.

### Závazná pravidla

Uživatel je solution architect VFCZ. Směr práce: závazný Architecture Board MVP → nejnovější analýza Martina Dostála v CZ local folder → FREQ/capabilities/business procesy → aplikační vrstva/SREQ → EA → vlastní SO. Group závislost není automaticky požadavek na VFCZ implementaci.

VDI pouze čti. Neměň, nevytvářej ani nemaž zdrojová data. Povoleno zadávání do vyhledávání; úzce vymezená projektová OneDrive AI složka je výjimka, nikoli všeobecné oprávnění. DOCX otevři explicitně v Immersive Readeru, XLSX v Preview. Neobcházej blokování schránky z VDI ven. Neautomatizuj přihlašovací dialogy. Před ovládáním čti vlastní dostupný computer-use skill. Nečti Outlook accessibility tree.

VFID sub ↔ příslušný ONSC/WSC USER vždy 1:1. Email není párovací klíč. TMF691 holding parent–child je jiný vztah. V4 SNOW customer/admin onboarding je manuální MVP. Automatický Siebel retrieval/prefill/population je mimo potvrzený MVP; minimum Marketplace data readiness zůstává.

SSO zahrnuje VFID login, specifické SH/CZ DXL vyjednání tokenu a jeho použití v dalších DXL hlavičkách. TMF691 dokládá Bearer/UserInfo a explicitní V2 parametr; přesný Atlas negotiation kontrakt a holding payload zůstávají otevřené.

Zachovej EA GUIDy a zdrojové texty. Stejné IAM/CHM/UC číslo neznamená totožný význam. CustomerContext generalizace neměň bez významového podkladu; dědičnost tříd nevyžaduje instanci.

Nevymýšlej zdroje, kontrakty, schválení ani dokončení. Odděluj fakta, rozhodnutí uživatele a pracovní návrhy. Pracuj souvisle v zadaném rozsahu, průběžně ukládej výsledky a stručně uváděj skutečný stav.
