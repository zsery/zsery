# Revize Book1 k 1. 11. 2026

Nový sešit obsahuje pracovní posouzení všech 219 řádků listu FREQ mapping vůči závaznému Board scope a dosud přímo přečteným částem MVP Requirements, BRD a Use Case Specification. Není schválenou úplnou aktuální baseline BRD. Detail, který nebyl doložen, zůstává výslovně k ověření.

Původních deset listů a jejich identifikátory zůstává zachováno. Nové modré sloupce přidávají aktuální význam, MVP status, odpovědnost, zdroj a problémy vazeb v listech FREQ mapping, SREQ Aplikační role, Functionalities a Interfaces. List Revize MVP vysvětluje zdroje a otevřené body. Vazby funkcionalit jsou posouzením navázaných SREQ, nikoli potvrzením správnosti každé funkce.

- SSO a specifické vyjednání tokenu mezi ServiceHub a CZ DXL je povinná část MVP. Přesný endpoint, grant, formát hlavičky, expirace a obnova nejsou ověřeny.
- ONSC/WSC navigace a portálový context handover jsou označeny mimo MVP. Zdrojové role a vztahy poskytované přes DXL nejsou tímto vyloučeny.
- UC005 mění starý povinný úvodní výběr na automatickou volbu jednoho dostupného CRM ID s možností následného přepínání. Priorita automatické volby není doložena.
- Automatický Siebel lookup/prefill je oddělen od potřebné datové připravenosti. V4 onboarding do SNOW je manuální.
- Řádky FREQ mapping 6, 7 a 28 obsahují nesoulad s odkazovanou funkcionalitou. IAM identifikátory se mezi verzemi liší; původní Requirements zdroj navíc opakuje IAM-30/31/32 pro různý obsah. ID nebyla svévolně přepsána.
- Postup čištění a párování Marketplace/Siebel je návrhem. Chybí konkrétní reporty, potvrzené klíče, master jednotlivých atributů a schválený způsob oprav.

EA soulad a skutečné AS-IS implementační rozdíly zůstávají neověřené do dodání EA/XMI. Pro dokončení baseline je nutná také úplná verzovaná sada aktuálních requirements/BRD a technické kontrakty.

Kontrola zachování porovnala původní buňky včetně vzorců a původní tabulky a externí odkazy. Nativní části byly ponechány z originálu, aby export nezměnil nesouvisející výpočty. V originálu již existuje chyba `#VALUE!` v `EAM App!F459`; je zachována a nebyla skryta ani opravena v rámci Atlas revize. Přepočet po otevření v Excelu může původní dynamickou oblast změnit podle dostupnosti závislostí.

Zdrojový soubor na Y: ani data ve VDI nebyly změněny.
