# Rozpracovaná DXL aktualizace – NESPUŠTĚNO

Tři soubory zde se liší od ověřené reprodukce. Doplnění je založené na nových technických poznámkách TMF691/TMF629. Neexistuje nový vygenerovaný XLSX ani ověřený changes.json pro tuto verzi.

- primary_update.py: IAM FREQ a propagace textových shod, Interfaces TMF691 Bearer/UserInfo/V2 parametr, TMF629 ID typy, NFR výkonová omezení dokumentována (bez tvrzení o implementaci/SLO); Postup revize nový ř.57.
- consolidate.mjs: style-copy rozsah Postup revize prodloužen do ř.57.
- preserve_and_verify.py: povolené výšky Postup revize prodlouženy do ř.57.

Původní CHM kontrola na Postup revize ř.42 zůstává zachovaná; DXL má vlastní ř.57. Před přenosem prověř skutečný diff, obsah a provenance, pak spusť celou odpovídající pipeline a vizuální QA. Instrukce v `../../instructions/reproduction.md`. Poslední ověřený XLSX zůstává v outputs/Book1_2026-11-03 s hashem 10998f6652bcea8f0bdc357cd092663bed5334d21bf9db0255470a969fc786a2.
