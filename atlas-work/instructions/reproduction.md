# Reprodukce a pokračování

Dodaná v03 je ověřený výsledek; není nutné ji znovu vytvářet pro prosté pokračování analýzy. Poslední DXL změny jsou zatím jen `pending/book1-dxl-update/`, viz START_HERE.

## Obnovení layoutu

Z kořene checkoutu, s dostupným Pythonem:

```powershell
python atlas-work/tools/restore_workspace.py --target 'C:/Users/your-user/Documents/AtlasContinuation' --dry-run
python atlas-work/tools/restore_workspace.py --target 'C:/Users/your-user/Documents/AtlasContinuation'
```

Zvol skutečnou novou cestu, neexistující cílová složka je vyžadována. Skript nic nespouští, nepřepisuje existující práci, nepřenáší klíče ani VDI data. Výsledný layout odpovídá původním relativním cestám `outputs/…`, `work/book1-consolidation`, `work/ea`, `work/book1`. Pending zůstává mimo aktivní builder.

## Runtime a knihovny

Původní PC:

```text
Python: C:/Users/zsery/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe
Node:   C:/Users/zsery/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe
```

Na novém PC použij jeho `load_workspace_dependencies` a spreadsheet skill. Python části vyžadují lxml, JS `@oai/artifact-tool`. Nekopíruj původní instalaci závislostí ani nehledat package internals. Ve skriptech consolidate.mjs a verify_final.mjs je původní absolutní cesta k bundled node/package.json; **před spuštěním upravit na skutečný loader nové instance**. Neinstalovat neautorizované knihovny do repo.

## Ověřený Book1 builder a pending změna

Před přenosem pending porovnej tři soubory proti `work/book1-consolidation`. Pending nebyl spuštěn ani nevygeneroval nový XLSX. Po kontrole kopíruj pouze primary_update.py, consolidate.mjs a preserve_and_verify.py z pending do aktivního builderu (přenos lokálního pracovního kódu, nikoli VDI). Ostatní zachovat z ověřené reprodukce. Spouštěj z obnoveného pracovního kořene:

```powershell
python -X utf8 work/book1-consolidation/read_sources.py > work/book1-consolidation/source-read.log
python -X utf8 work/book1-consolidation/prepare_changes.py
```

read_sources vygeneruje sources.json a identity-delta.json ze tří přiložených původních pracovních sešitů. prepare_changes vytvoří changes.json a primary-classification.json. Před prvním skutečným authoringem proveď přesně marker vyžadovaný právě dostupným spreadsheet skillem; neužívej historickou absolutní cestu jako důkaz, že skill existuje na druhém PC.

```powershell
node work/book1-consolidation/consolidate.mjs
python -X utf8 work/book1-consolidation/preserve_and_verify.py
node work/book1-consolidation/verify_final.mjs
python -X utf8 work/book1-consolidation/publish_report.py
```

Nejprve zkontroluj zdroj/účinky skriptů. consolidate importuje v02, zadá explicitní změny přes Artifact Tool, přepočítá scratch, exportuje authored.xlsx a rendery. preserve_and_verify přenese jen whitelist buněk/stylů do původního nativního balíčku; zachovává formule/cache, tabulky, externí linky, hidden a další metadata. Ověř reimport všech změn a prohlédni nové viditelné rozsahy. Původní hidden řádky neměnit jen kvůli náhledu. verify_final nyní renderuje dva nové ručně posouzené řádky; pro DXL doplnění přidej dotčený viditelný rozsah. Nevydávej zachované cache za nativní Excel recalculation.

**Neprovádět automaticky refresh_delivery.py:** je to historický jednorázový publikační skript s pevnými starými počty/hash a appendy. Nové počty/hash/stavy odvodit z verification/reimport JSON a aktualizovat aktuální stav, handoff, README i klasifikační JSON. Zveřejnit jen jednu kanonickou XLSX variantu. Podklady v GitHubu a předávací balíček musí mít shodný hash XLSX.

## EA XML index

V root repa je původní Atlas.7z, ve workspace `inputs/Atlas.7z`. Obsah rozbal jen lokálně podporovaným 7z nástrojem do `work/ea/`, XML pojmenuj Atlas-original.xml; původní zdroj nepřepisovat. Ověřený SHA-256 XML:

```text
dcc42289f422c120105d791725bb27549238cc8c106812ac1ad36582c1a3861c
```

Pak:

```powershell
python -X utf8 work/ea/index.py > work/ea/inventory.txt
python -X utf8 work/ea/review_primary_business.py
```

index.json má asi 100 MB **na jednom řádku**. Nečti přes head/Get-Content/rg celé řádky; načti JSON a tiskni jen zvolené agregace/GUID. Index používá XML parser bez externích entit a s no_network. Review report je strukturální evidence, ne automatická úprava XMI. Původní Book1 parsed data je v `work/book1/data.json` jen jako vstup pro starší audit, nikoli aktuální sešit. Ostatní historické reprodukční skripty se nespouštějí jako neověřená hromadná pipeline.

## Skills druhé instance

Z repozitářového `instructions/skills/follow-explicit-scope/SKILL.md` vytvoř nebo sluč do lokálního `$CODEX_HOME/skills/follow-explicit-scope/SKILL.md`, případně skutečné uživatelské skills cesty. Použij tamní skill-creator; adresář nezaměnit za checkout ani VDI. Pokud existuje, nejprve čti a zachovej relevantní pravidla. Po zápisu znovu načti uložený soubor a validuj dostupným quick_validate.py. Tento balíček sám neinstaloval skill na cizí PC.

## Stav při předání

Nový DXL builder nemá nové changes.json/verification ani hash XLSX. Hotový Book1 zůstává `10998f…786a2`, 4663 změn. Board reader byl otevřen a čeká na pokračování od začátku; zatím pouze nově potvrzená věta Varianta 2 = MVP, nikoli rozdělení projektu do dropů. Nezapisovat tuto dílčí kontrolu jako celé Board čtení. Živý stav znovu zjistit po přerušení.
