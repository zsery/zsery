# Pokračování práce Atlas / ServiceHub VFCZ

## Aktuální checkpoint 5. 11. 2026

Pokyny ke zdrojům, přihlášení a průběžnému GitHub ukládání: instructions/skills/follow-explicit-scope/SKILL.md, sekce Přenos práce a zdroje. Nejnovější stav: STATE_2026-11-05.md. Starší časové zápisy níže jsou historie, nikoli současné potvrzení dokončení.


## Nejnovější pokračování 4 listopadu večer

Aktuální OneDrive Documents/Projects/ServiceHub/Atlas/Book1.xlsx byl zkontrolován po práci Copilotu; není nahrazen starší lokální revizí. Přesné FREQ mapping!F4:F5 = SREQ-CRM-04 / SREQ-CRM-03 potvrzují, že starý CRM-03/04 mapping konflikt už Copilot opravil. Aktuální ř.109 ale stále má allow v C109, deny v J109 a SHODA v D109; Copilot potvrdil rozpor. Žádná zdrojová VDI data nebyla upravena.

Vznikla skutečná dílčí pracovní XML revize osmi documentation polí, se zachováním všech ostatních bajtů, GUIDů, konektorů a diagramů. Výstup a původní/nové texty: outputs/EA_SO_2026-11-04/. XML SHA-256 fb0cfe908c40bf58928d5b8a837760bce19304d9293d1f331377183a268a21a6. Není to dokončená architektonická baseline ani ověřený nativní import EA.

Primárně otevřen email RE: ServiceHub - DXL, 15.10.2026 16:35: SH BFF předá IDaaS token jako subject_token přes APIX do AuthX; validace přes IDaaS /oidc/introspect; vrátí se DXL token. TMF691 CRM_ID a TMF629 customer name jsou oddělené. Přesný verzovaný kontrakt a produkční oprávnění zůstávají otevřené. Nalezen 74stránkový TMF621 SNOW Integration PDF; čtený rozsah a meze použitelnosti jsou v ServiceHub_pokracovani_2026-11-04.md. Neoznačovat jej automaticky za Atlas kontrakt.

Změnové kapitoly SO jsou hotové jako textový obsah .md pro zapracování do původního SO. DOCX vizuální QA blokuje chybějící soffice.exe; neověřený DOCX není vydaný. Native EA import/diagram QA, úplná aktuální traceability, role rozhodnutí, uzavření kontraktů a plná editace původního SO zůstávají nedokončené. Předchozí tvrzení o zcela nezměněném Atlas.xml je historické: původní export zůstává nezměněný, ale nová dílčí pracovní kopie nyní existuje.


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
SHA-256: `2888fc4e7a78fcd25b8ed32ec745f6d0530753b0f40bc4937706fafe30fb0e90`.
14 listů, 219 pracovně posouzených mapovacích řádků; 188 přes text, 31 samostatně. 159 EA FREQ, 6 UC005 analytických vstupů a 26 business traceability záznamů. 4663 ověřených změn, 1878 vzorců/cache zachováno. Toto není schválení atomické FR baseline ani všech SREQ vazeb.

Dříve pending DXL poznatky jsou nově promítnuty do XLSX: 60 změn proti předchozímu kanonickému souboru v šesti listech, reimport a vizuální QA dokončeny, vzorce/cache a nativní části zachovány. Viz outputs/Book1_2026-11-03/DXL_doplneni_2026-11-03.md, Kontrola_DXL_doplneni.json a Zmeny_DXL_bunek.csv. Původní konsolidační evidence 4663 změn je historická. Pending README popisuje provedení; neopakovat doplnění naslepo. Reprodukce cílené delty je v reproduction/book1-dxl.

Atlas.xml a Word SO nejsou aktualizované. Úplný průzkum všech Group podsložek není dokončen. TMF691 čtecí text prošel do konce bez diagramů; TMF629 má přečtené vybrané GET a celé OLC/V2 mapping části. Board reader byl dočten přes In scope a Out of scope k nadpisu Rizika (viz outputs/Board_pokracovani_2026-11-04.md). Aktuální Teams Copilot průzkum a cílené ověření přepisu MVP Assessment z 2.11. jsou v outputs/Copilot_MVP_Assessment_2026-11-04.md; oddělují Copilot vodítka a primární výroky. Živý VDI stav vždy znovu zjisti.

### Závazná pravidla

Pracovní rozpad UC005–UC011 z 4.11. je v `outputs/UC_atomicke_podminky_2026-11-04/UC_review.md` a `Kontrolni_matice.json`: 30 podmínek, 41 existujících FREQ kandidátů s původními GUID, 77 existujících mapovacích řádků, deset podmínek bez přímého protějšku v porovnávané sadě. Jde o návrh pro review, nikoli schválení nebo nové EA vztahy. Dřívější překážka scrollu je vyřešená tažením posuvníku. Živý stav vždy znovu pozorovat.

Následně je obsahově posouzeno všech 219 řádků FREQ mapping: `outputs/UC_atomicke_podminky_2026-11-04/SREQ_vsechny_radky.md` a `SREQ_kontrola_vsech_219_radku.json`. Zachované texty/GUID, konkrétní konflikty CRM-03/04, CRM-09/10, SH-07 a aplikační owner ID-07. Nejde o AS-IS implementační audit nebo approval. Confluence Agent našel SnowConnector návrh PR25_0749, pageId 254750255; přímá stránka vyžaduje ruční přihlášení uživatele. Přesný stav a osobní skill v `outputs/Confluence_SNOW_voditka_2026-11-04.md`. Žádost o ruční přihlášení je otevřená; neautomatizovat login.

Uživatel je solution architect VFCZ. Směr práce: závazný Architecture Board MVP → nejnovější analýza Martina Dostála v CZ local folder → FREQ/capabilities/business procesy → aplikační vrstva/SREQ → EA → vlastní SO. Group závislost není automaticky požadavek na VFCZ implementaci.

VDI pouze čti. Neměň, nevytvářej ani nemaž zdrojová data. Povoleno zadávání do vyhledávání; úzce vymezená projektová OneDrive AI složka je výjimka, nikoli všeobecné oprávnění. DOCX otevři explicitně v Immersive Readeru, XLSX v Preview. Neobcházej blokování schránky z VDI ven. Neautomatizuj přihlašovací dialogy. Před ovládáním čti vlastní dostupný computer-use skill. Nečti Outlook accessibility tree.

VFID sub ↔ příslušný ONSC/WSC USER vždy 1:1. Email není párovací klíč. TMF691 holding parent–child je jiný vztah. V4 SNOW customer/admin onboarding je manuální MVP. Automatický Siebel retrieval/prefill/population je mimo potvrzený MVP; minimum Marketplace data readiness zůstává.

SSO zahrnuje VFID login, specifické SH/CZ DXL vyjednání tokenu a jeho použití v dalších DXL hlavičkách. TMF691 dokládá Bearer/UserInfo a explicitní V2 parametr; přesný Atlas negotiation kontrakt a holding payload zůstávají otevřené.

Zachovej EA GUIDy a zdrojové texty. Stejné IAM/CHM/UC číslo neznamená totožný význam. CustomerContext generalizace neměň bez významového podkladu; dědičnost tříd nevyžaduje instanci.

Nevymýšlej zdroje, kontrakty, schválení ani dokončení. Odděluj fakta, rozhodnutí uživatele a pracovní návrhy. Pracuj souvisle v zadaném rozsahu, průběžně ukládej výsledky a stručně uváděj skutečný stav.
