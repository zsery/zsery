# Cílená DXL aktualizace Book1

Autorování provedl Artifact Tool; dxl_preserve.py přenesl pouze 60 určených buněk do původního ZIP balíčku a ověřil zachování ostatního obsahu. delta.json je skutečný plán. Kontroly a stav jsou v outputs/Book1_2026-11-03/DXL_doplneni_2026-11-03.md.

Pro reprodukci nejprve připrav pracovní layout podle instructions/reproduction.md z commitu 21e806fbf9e52ff6f354b6cace4e07e038673af6. Použij jeho původní kanonický XLSX (SHA 10998f6652bcea8f0bdc357cd092663bed5334d21bf9db0255470a969fc786a2), nikoli nynější výsledek. Vytvoř ověřený původní plán jako validated-plan.json. Poté přenes zdejší primary_update.py a znovu vygeneruj changes.json. dxl_delta.py ověří původních 4663 hodnot a vytvoří canonical-before.xlsx a delta.json. Skripty patří do work/book1-consolidation pod obnoveným pracovním kořenem.

Načti vlastní spreadsheet skill a runtime, renderuj původní sešit, proveď požadovaný marker a spusť dxl_author.mjs edit, dxl_preserve.py a dxl_author.mjs final. visible_preview.py vytváří pouze dočasné odkryté kopie pro QA skrytých řádků. Původní hidden stav se do výsledku přenáší beze změny. Node resolver lze nastavit proměnnou CODEX_NODE_PACKAGE_JSON na package.json runtime z load_workspace_dependencies. Tato kopie neobsahuje přístupové údaje. Časová metadata ZIP se při nové reprodukci mohou lišit; ověřuj obsah a nově vzniklý hash.
