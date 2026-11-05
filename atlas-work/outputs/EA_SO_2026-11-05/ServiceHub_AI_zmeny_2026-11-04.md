# Změny pracovních kopií ServiceHub/AI

## Book1.xlsx

Aktuální zdroj `Documents/Projects/ServiceHub/Atlas/Book1.xlsx` byl zkopírován standardní funkcí OneDrive **Copy to** do existující složky `Documents/Projects/ServiceHub/AI`. OneDrive potvrdil „Copied Book1.xlsx“. Cílový seznam následně zobrazil nový Book1.xlsx, 402 KB. Původní sešit nebyl přepsán ani nahrazen starším lokálním souborem.

Excel Copilot dostal úzce vymezený úkol změnit pouze `FREQ mapping!D109` a `H109`, ostatní buňky zachovat. Ohlásil dokončení a uložení. Přímým výběrem obou buněk přes name box a čtením formula bar byly ověřeny výsledky:

| Buňka | Ověřený obsah |
|---|---|
| D109 | CONFLICT ALLOW/DENY |
| H109 | C109 allows access, whereas J109 denies access. This ALLOW/DENY conflict requires an explicit role decision; neither rule takes precedence until that decision is confirmed. |

Příslušný FREQ text, cílová funkcionalita i SREQ zůstaly zachované. Oprava nepředstírá business rozhodnutí o oprávnění role. Copilot uvedl zachování všech ostatních buněk a formátování; úplný binární diff kopie přes VDI nebyl dostupný, proto toto tvrzení není vydáváno za nezávislou byte-level kontrolu.

Opravené vazby CRM-04 ↔ IAM-25 a CRM-03 ↔ IAM-24 v aktuální práci Copilota se znovu neměnily. Starší 14listý lokální Book1 není použit jako náhrada aktuální sedmilisté verze.

Po opravě byl Copilotu zadán read-only audit **všech** řádků FREQ mapping vůči textu rolí a funkcionalit, s přesnými odkazy na buňky. Jeho výsledky musí být ověřeny před další změnou; samotné zadání není dokončený audit.

## Solution Overview

Teams Copilot dostal přiložený původní Solution_Overview_ServiceHub a zadání vytvořit celý nový Word se zachováním struktury, aktuálním Board MVP, Dostálovými UC005–UC011, standalone VFID/DXL, manuálním V4 onboardingem a vyřazením ONSC navigace a Siebel prefill z MVP. Bylo výslovně zadáno zachovat originály, uvést zdroje a označit neznámé skutečnosti.

Copilot vytvořil `Solution_Overview_ServiceHub_Revised_MVP_2026-11-04.docx`; odkaz byl skutečně otevřen. WordWeb zobrazil 32 stran a 8 598 slov. Soubor vznikl v OneDrive `Documents/Copilot/Created`; přemístění do `Documents/Projects/ServiceHub/AI` a obsahové QA jsou samostatné následné kroky. Vygenerovaný soubor není automaticky schválený SO ani ověřené zachování každého původního odstavce.
