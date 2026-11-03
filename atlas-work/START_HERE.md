# Start here – pokračování jiným Codex agentem

Stav předání 3.11.2026 po přerušení čtení Board dokumentu. Toto předání zahrnuje uložené podklady a rozhodnutí z dostupné historie, nikoli úplný export celého chatu nebo kompletní primární SharePoint dokumenty.

## Text ke vložení druhému agentovi

> Pokračuj v mé práci solution architekta Vodafone CZ na Atlas / ServiceHub integraci Vodafone Group a VFCZ. Repozitář je `zsery/zsery`, pracovní větev `codex/atlas-stav-2026-11-01`. Nejprve načti `atlas-work/AGENTS.md`, `atlas-work/START_HERE.md`, `atlas-work/PREDANI_2026-11-03.md` a `atlas-work/instructions/skills/follow-explicit-scope/SKILL.md`. Pro autentizaci nejprve přečti `atlas-work/instructions/github-access.md` a prověř určený deploy key; nevracej se k nefunkčním domněnkám o přihlášení browserem nebo propojení Windows účtů. Nainstaluj/přiměřeně sluč dodaný skill do lokálních skills této instance a znovu načti skutečně uložený soubor. Neprohlašuj instalaci bez kontroly. Nejnovější ověřený Book1 má SHA-256 `10998f6652bcea8f0bdc357cd092663bed5334d21bf9db0255470a969fc786a2`, 14 listů, 219 pracovně posouzených mapovacích řádků. Část nových DXL změn je jen ve složce `pending/`, zatím nebyla aplikována do XLSX. Přečti nové TMF691/TMF629 poznámky a poslední stav níže. VDI jen čti; nikdy neměň cizí zdroje. Pokračuj v Board scope → nejnovější analýza Martina Dostála → Book1 → řízená EA revize → vlastní SO. Zachovej moje explicitní rozhodnutí a GUIDy, nic nedoplňuj odhadem. Průběžně ukládej do této pracovní větve a ověř push. Kompletní práci nevydávej za dokončenou, dokud skutečně není.

## Co je skutečně hotové

- Git commit `532b4e94090262cdd19608f134fe3937e1d40921` byl před přípravou tohoto předání ověřen lokálně i vzdáleně. Obsahuje konsolidovaný Book1, revizi všech 219 mapovacích řádků a audit 21 starých EA UC s konkrétními GUID. Novější commit tohoto předání zjisti přes Git; nepoužívej toto historické SHA jako tvrzení o aktuálním HEAD.
- Kanonický XLSX: `outputs/Book1_2026-11-03/Book1_Atlas_konsolidovany_2026-11-03.xlsx`. 4 663 určených změn proti v02, 1 878 původních vzorců/cache zachováno, 7 tabulkových a 2 external-link díly zachovány, reimport všech změn ověřen. Zdrojová chyba EAM App!F459 #VALUE! zachována. Nativní Excel přepočet neproveden; žádné nové vzorce.
- 159 původních EA FREQ klasifikováno, 6 UC005 vstupů, 26 přepsaných business traceability záznamů. 188 přesných normalizovaných textových přiřazení + 31 samostatných obsahových posouzení. Žádné schválení atomické baseline ani SREQ sémantické ekvivalence tím nevzniklo.
- Nová technická poznámka `outputs/DXL_TMF691_overeni_2026-11-03.md`: čtecí text prošel do konce, bez vložených diagramů. Ověřen Bearer/UserInfo, explicitní V2 parametr, root-only V2, odlišné role, současné dokumentované limity a cílové rozdíly.
- `outputs/DXL_TMF629_overeni_2026-11-03.md`: vybrané GET části a celé OLC/V2 customer mapping sekce. Celý dokument nebyl přečten. Přeškrtnuté popisy, exportní TOC chyba a omezení jsou zaznamenány.

## Přesné rozpracování

`pending/book1-dxl-update/` obsahuje **tři nové verze builder souborů**: primary_update.py, consolidate.mjs, preserve_and_verify.py. Změny nejsou spuštěné. Přidávají doložené TMF691 informace do IAM FREQ, jejich pracovních návazností a Interfaces; TMF629 typování ID; nový Postup revize ř.57. Ověřený builder v `reproduction/book1-v03/` stále odpovídá dodanému XLSX. Nezkombinuj starý changes.json s novým builderem a netvrď, že nový kontrakt již je v sešitu. Postup: vytvoř lokální pracovní layout, zkontroluj pending diff, přenes 3 soubory, regenerate plan → Artifact authoring → native preservation → reimport/render → report; teprve potom publikuj nový XLSX/hash a stav.

Pozor `reproduction/book1-v03/refresh_delivery.py` je historický jednorázový publikační skript s pevnými starými počty/hash a připojuje text. **Nespouštět naslepo znovu.** Aktualizovat publikaci podle nových verification.json a primary-classification.json. Aktuální předání ukládá pending odděleně.

Poslední pozorované VDI: Horizon **AOProd W11**, Edge, nově otevřený OneDrive web `My files / Documents / Projects / ServiceHub`, Board DOCX přes Open in Immersive Reader. Titul viditelného textu „Prezentace pro Architecture Board / Atlas - Project Scope“; první odstavec říká Varianta 2 = MVP, nikoli rozdělení projektu do dropů. Čtení nyní skončilo na začátku „Architektonická struktura MVP / In scope“. Nejde o dokončení celého Board dokumentu. Po přerušení znovu vyber skutečné VDI okno a pořiď čerstvý stav; staré window ID/koordináty nepřebírat jako živý stav.

Funkční cesta k read-only Board souboru: VDI Explorer OneDrive – Vodafone Group/Documents/Projects → kontext složky ServiceHub → OneDrive → View online (složka, ne DOCX) → vybrat Board DOCX checkboxem → Open → Open in Immersive Reader. Explorer preview nepřinesl čitelný náhled. Nepoužívat dvojklik na DOCX do editoru. Ve fullscreen Readeru mizí překryvná karta. Změna režimu/Find vracela reader na začátek; browser Find nebyl ověřen jako hledání celého dokumentu.

Pokus `type_text` v browser Find vložil starý text vzdálené schránky, nikoli požadovaný dotaz. Pole opraveno klávesnicí a zavřeno, do dokumentu se nepsalo. Klávesy fungují, nevyvozuj z úspěchu nástrojového volání správné vložení. Nepoužívat schránku z VDI ven.

## Co stále není hotové

Úplný průzkum všech podsložek původních tří Group tabů, celé Board diagramy/obsah, finální schválené atomické FR, významové ověření všech SREQ, přesný Atlas token negotiation/grant/client-auth/expiry/refresh a holding payload; detailní provozní cleansing proces a konkrétní reporty. **Atlas.xml a Word SO nejsou aktualizované. Outlook není opravený.** Předchozí závěry o CustomerContext byly staženy; nepokračovat podle jejich historického textu jako podle opravy.

## Technické spuštění a přenos

1. Připojení a Git příkazy: `instructions/github-access.md`. Soukromý klíč je pouze mimo repo na původním PC; jeho přenos jinému PC musí proběhnout mimo repozitář schválenou cestou. Bez něj nelze slíbit write access, i když jsou všechny podklady v GitHubu.
2. Skill: `instructions/skills/follow-explicit-scope/SKILL.md`; použij místní skill-creator, zachovej existující relevantní pravidla. Repo AGENTS.md platí při práci v atlas-work i bez globální instalace skillu.
3. `tools/restore_workspace.py` obnoví pracovní layout z checkoutu do **nové neexistující složky**. Kopíruje jen explicitní projektové soubory. `--help` uvádí použití. Nepřepisuje existující rozpracovanou složku.
4. `instructions/reproduction.md` vysvětluje závislosti a pořadí příkazů. Nepotřebuje původní Windows účet pro GitHub. Živý VDI přístup poskytuje uživatel samostatně.
5. `SHA256SUMS.txt` umožňuje ověřit všechny zahrnuté soubory. Klíče, hesla/PINy, Outlook dump a neomezené celé úložiště nejsou v balíčku.
