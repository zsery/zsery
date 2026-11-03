# Spuštění práce samostatným agentem

## Copilot ve VDI — závazné pravidlo uživatele

Ve VDI používej Copilot jako první volbu všude, kde je dostupný a použitelný pro zadaný úkol. Teams Copilot používej pro dohledání napříč SharePointem, Teams, e-maily a přepisy schůzek; Copilot ve Wordu a Excelu pro rozbor otevřených podkladů. Používej i další dostupné panely Copilotu. Před rozsáhlým ručním procházením ověř dostupnost Copilotu a zadej cílený dotaz. Vyžaduj odkazy a verze podkladů a závěry ověřuj proti primárním zdrojům. Běžnému Copilotu nepřisuzuj přístup do Confluence; specializovaného agenta použij jen podle jeho ověřeného přístupu.

Platí zákaz změn zdrojových dat ve VDI: zadávání dotazů do Copilotu je povoleno, ale nepoužívej Apply/Insert/Edit ani jiné provedení změn do zdrojových dokumentů, sešitů či dat. Výjimku má pouze výslovně povolená projektová složka OneDrive AI. Při překážce zaznamenej konkrétní omezení a pokračuj jinou povolenou cestou. Běžně zadatelný dotaz nepřenášej na uživatele.

Začni `../AGENT_PROMPT.md`. Získání dat: veřejné HTTPS čtení repozitáře zsery/zsery, větev codex/atlas-stav-2026-11-01. Zápis: vlastní GitHub autorizace agenta. Žádný přenos identity nebo přístupových údajů jiného agenta není podmínkou čtení.

Ověřený Book1 a jeho builder jsou v outputs/Book1_2026-11-03 a reproduction/book1-v03. Tři nespuštěné DXL změny jsou v pending/book1-dxl-update. Nezaměň je za hotový XLSX. Pro obnovu pracovního layoutu slouží tools/restore_workspace.py; vyžaduje nový prázdný cíl mimo checkout a podporuje --dry-run. Skript neprovádí builder ani API operace.

Použij vlastní dostupný spreadsheet skill, jeho runtime a @oai/artifact-tool; Python části potřebují lxml. Absolutní runtime cesty uvnitř reprodukčních skriptů přizpůsob vlastním nástrojům před spuštěním. Příkazy spouštěj z obnoveného pracovního kořene:

```sh
python -X utf8 work/book1-consolidation/read_sources.py
python -X utf8 work/book1-consolidation/prepare_changes.py
```

Po kontrole pending diff přenes tři pending soubory do aktivního builderu a znovu vytvoř plán. Proveď marker požadovaný dostupným spreadsheet skillem, pak:

```sh
node work/book1-consolidation/consolidate.mjs
python -X utf8 work/book1-consolidation/preserve_and_verify.py
node work/book1-consolidation/verify_final.mjs
python -X utf8 work/book1-consolidation/publish_report.py
```

Ověř zachování původních vzorců/cache, tabulek, external links, GUID a nesouvisejících buněk, reimport změn a viditelné rendery. Nativní Excel přepočet nebyl v dodaném výsledku proveden. refresh_delivery.py nespouštěj automaticky: používá pevné počty/hash a připojuje text. Publikaci uprav podle nových kontrolních JSON, aktualizuj stav a kontrolní součty.

Původní vstup Atlas.7z je v kořeni repozitáře. Extrahuj jej jen do pracovního adresáře, XML neměň bez řízené revize. Ověřený SHA256 XML: dcc42289f422c120105d791725bb27549238cc8c106812ac1ad36582c1a3861c. Index se vytváří work/ea/index.py; index.json má asi 100 MB na jediném řádku, čti jej parserem s omezeným výstupem. Následuje work/ea/review_primary_business.py. Revize není automatická změna XMI.
