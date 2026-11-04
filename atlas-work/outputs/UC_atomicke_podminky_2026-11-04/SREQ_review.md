# Obsahová kontrola navazujících SREQ, 4. 11. 2026

Posouzeno 77 existujících řádků FREQ mapping navázaných na 41 kandidátů v [UC review](UC_review.md). Zdrojem je kanonický Book1 (stejný SHA-256 jako v kontrolní matici), původní EA text/GUID uložený v workbooku a dřívější primární UC evidence. Rozsah není všech 219 mapovacích řádků. Zjištění neznamená změnu živého EA nebo schválení SREQ baseline.

## Konkrétní rozpory

| FREQ mapping ř. | SREQ | Zjištění | Postup opravy |
|---|---|---|---|
| 4, 5 | CRM-03, CRM-04 | Hierarchy a customer separation jsou vůči přiřazeným IAM-25 a IAM-24 vzájemně prohozené. | Opravit významové vazby se zachováním GUID. Payload hierarchy nejprve ověřit. |
| 109 | SH-07 | FREQ-IAM-12 říká allow V2 End User Admin, EA SREQ říká deny stejné role. | Potvrdit role enum a rozhodnutí. ID shoda není sémantická shoda. |
| 166 | ID-07 | Workbook aplikace IDaaS, EA odpovědnost Local DXL. | Ověřit ownera a skutečný průchod, nerozdělovat aplikace jen podle rodiny ID. |

SREQ-SH-02 navíc zakazuje vlastní SH role model; tento silnější výrok neplyne sám z FREQ požadujícího upstream role data. Zaznamenané chatové podklady o vstupních admin rolích a stejných vnitřních právech jsou v [ověření Copilotu z 1.11.](../copilot-overeni-2026-11-01.md). Nejsou novým approval ani náhradou přesných role enumů.

## Pokrytí a aplikační hranice

U složených řádků 123, 129–130 a 185–186 neodpovídá jeden nalezený SREQ automaticky všem připojeným FREQ. Například MKP-06 poskytuje active Atlas data a MKP-07 availability/error stav, zatímco společný FREQ text obsahuje pět zobrazovacích pravidel. Povinnost datového providera a SH zobrazení musí mít samostatný důkaz.

CRM data dependency neprokazuje implementaci SH selectoru či session v CRM. Marketplace data nepokrývají VFID identity mapping. Upstream ONSC/WSC role a vztahy neobnovují vyloučený portálový handover. Obecný SNOW text neuzavírá konkrétní create/update operace, pole, status transitions nebo identifikační payload.

U 20 vybraných řádků není v tomto indexu EA GUID/text. Před založením nového prvku je nutné obsahové porovnání s existujícími SREQ/funkcemi a AS-IS. Chybějící ID samo nedokládá chybějící implementaci.

## Evidence po řádcích

`SREQ_obsahova_kontrola.json` obsahuje všech 77 řádků, původní FREQ a EA SREQ text, původní GUID, obsahové posouzení a konkrétní další krok. Kandidát pro reuse znamená pouze obsahovou slučitelnost v uvedeném rozsahu. Implementace, odpovědnost a schválení zůstávají samostatnou kontrolou. Book1 a Atlas.xml nebyly přepsány.
