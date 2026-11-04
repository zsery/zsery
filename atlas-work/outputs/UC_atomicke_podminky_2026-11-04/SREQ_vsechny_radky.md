# Kontrola všech 219 mapovacích řádků, 4. 11. 2026

Navazuje na [detail 77 řádků UC005–UC011](SREQ_review.md). Obsahově přečteno a posouzeno také zbývajících 142 řádků. Strojová evidence `SREQ_kontrola_vsech_219_radku.json` zachovává každý původní FREQ text, SREQ ID, EA text a GUID a připojuje konkrétní závěr a další krok. Všech 219 řádků 2–220 je zastoupeno právě jednou.

Jde o sémantickou kontrolu uložených mapovacích textů proti známému MVP a primární UC evidenci. Není tím potvrzen současný stav aplikací, celý živý EA, technické API ani schválení baseline. Book1, Atlas.xml a SO se v tomto kroku nemění.

## Další věcné rozpory

| Řádek FREQ mapping | Zjištění | Význam |
|---|---|---|
| 6 | CRM-09: FREQ vytvořit lead, EA konfigurovat email pro assisted tickets. | Jde o jinou funkci. |
| 7 | CRM-10: FREQ uložit telefon leadu, EA potvrdit Atlas/Type C reprezentaci a identifikaci. | Jde o jinou funkci. |
| 54 | Identifier readiness a auto Siebel lookup ve společném textu. | EA manuální/batch populaci nelze vydávat za automatický lookup. |
| 77–84 | Emailový VFID/admin lookup. | Konflikt se zákazem emailu jako stabilního mapovacího klíče. |
| 85–89 | Vytvoření první subscription a ACTIVE. | UC002 order acceptance není dokončený provisioning/aktivace. |
| 213 | Povinná selection journey při více kontextech. | Ruční výklad by odporoval UC005 automatické volbě jednoho CRM ID. |

Další konkrétní rozpory CRM-03/04, SH-07 a ID-07 jsou v předchozím detailu. U jedenácti nově čtených řádků je EA text pouze `MVP`; to není obsahový důkaz shody. U prázdného EA GUID/textu se nevytváří nové prvky jen z absence ID.

## Hranice aplikačního návrhu

Portálová navigace, handover a roundtrip zůstávají mimo standalone MVP. VFID autentizace a upstream role/vztahy jsou relevantní i bez této navigace. Data readiness zůstává potřebná, automatický Siebel retrieval/prefill zůstává vyloučený bez reconfirmation. Manuální V4 customer/admin onboarding neprokazuje automatické lifecycle eventy. Product readiness sama nepotvrzuje všechny historické bundle/add-on kombinace. Marketing lead větev vyžaduje samostatně potvrzený rozsah.

Přesné pořadí potřebných oprav: oddělit konfliktní významy a sdružené FREQ, potvrdit technické kontrakty a odpovědnosti, potom promítnout do kanonického Book1 a EA se zachováním GUID. Nezakládat 132 nových SREQ jen kvůli chybějícímu ID v indexu. Prokázaná obsahová slučitelnost neznamená novou CZ implementační deltu.

## Přehled posouzení

| Závěr | Řádků |
|---|---:|
| AUTHENTIZACE SE SMÍŠENÝMI KANÁLY | 2 |
| AUTO SIEBEL MIMO POTVRZENÝ MVP | 14 |
| BEZ EA PROTĚJŠKU V INDEXU | 20 |
| CHANNEL ROUNDTRIP MIMO MVP | 4 |
| CÍLOVÝ LIFECYCLE VERSUS MANUÁLNÍ MVP | 3 |
| DATA DEPENDENCY NENÍ SH CHOVÁNÍ | 4 |
| DEEPLINK DETAIL NEPOTVRZEN | 3 |
| DETAIL DATA READINESS NEPOTVRZEN | 9 |
| EA TEXT NEDOKLÁDÁ OBSAH | 11 |
| KANDIDÁT PRO REUSE | 17 |
| KONFLIKT EMAIL IDENTITY | 8 |
| KONFLIKT MAPOVÁNÍ | 2 |
| KONFLIKT VÝZNAMU | 2 |
| LIFECYCLE ROZHODNUTÍ OTEVŘENÉ | 1 |
| MANUÁLNÍ VALIDACE KANDIDÁT | 1 |
| NEUZAVŘENÝ KONTRAKT IDENTITY | 1 |
| NEUZAVŘENÝ NFR | 1 |
| NEUZAVŘENÝ ONBOARDING KONTRAKT | 5 |
| NEUZAVŘENÝ SNOW DETAIL | 17 |
| ORDER NENÍ AKTIVACE | 5 |
| PORTÁLOVÁ INTEGRACE MIMO MVP | 15 |
| PRODUKTOVÁ KONFIGURACE K POTVRZENÍ | 7 |
| PŘÍMÝ ROZPOR ALLOW/DENY | 1 |
| ROLE VYŽADUJE POTVRZENÍ | 7 |
| ROZPOR APLIKAČNÍHO PŘIŘAZENÍ | 1 |
| ROZPOR POČÁTEČNÍHO TOKU | 1 |
| SAMOSTATNÝ MARKETING SCOPE | 32 |
| SESSION DETAIL K DOPLNĚNÍ | 2 |
| SILNĚJŠÍ SREQ | 1 |
| SMÍŠENÝ SCOPE | 1 |
| SMÍŠENÝ SCOPE A VAZBA | 2 |
| STANDALONE KANDIDÁT | 2 |
| UPŘESNĚNÍ HRANICE PŘÍSTUPU | 1 |
| UPŘESNĚNÍ VÝZNAMU | 1 |
| ČÁSTEČNÁ ELIGIBILITY A UX | 5 |
| ČÁSTEČNÉ POKRYTÍ SDĚLENÉHO TEXTU | 4 |
| ČÁSTEČNÝ VÝZNAM | 3 |
| ŠIRŠÍ HISTORICKÝ SCOPE | 3 |

Součet: 219. Závěry se vztahují vždy jen k příslušnému zdrojovému řádku; neznamenají rozhodnutí o celém rozsahu aplikace.
