# UC005–UC011: atomické podmínky pro review, 4. 11. 2026

Pracovní rozpad 30 podmínek na základě přímo přečtené UC specifikace a dnešního cíleného rozboru přes Teams Copilot s agentem Atlas. Čísla řádků níže jsou lokální odkazy pro review, nejsou nová FREQ ID. Návrhy akceptace jsou analyticky odvozené z popsaného chování. Approval není doloženo. Book1 a Atlas.xml se tímto nemění.

Podklady: [primární čtení UC z 3.11.](../Overeni_zdroju_VDI_2026-11-03.md), [nové Copilot a metadata ověření](../Copilot_MVP_Assessment_2026-11-04.md), [závazný Board rozsah](../Board_pokracovani_2026-11-04.md), kanonický Book1 s SHA-256 `2888fc4e7a78fcd25b8ed32ec745f6d0530753b0f40bc4937706fafe30fb0e90`. Přesný kontrolní hash je ve strojové matici.

## Zjištění pro revizi

Existující FREQ nejlépe pokrývají obecnou identitu, kontext a viditelnost. Pro vytvoření a update požadavků chybí samostatně vyjádřené validační a potvrzovací podmínky. UC008 a UC009 nemají v porovnávaných 159 EA FREQ zjištěný přímý obsahový protějšek pro níže vymezená pravidla. To není důkaz absence v celém EA ani oprávnění automaticky založit nové GUID.

IAM-29 je potřeba vyložit spolu s UC005 automatickou volbou jednoho CRM ID. Text vyžadující vybraný kontext nemusí znamenat povinný ruční krok. SREQ-SH-19 ani CRM-08 proto nelze změnit jen podle stejného čísla. IAM-30–33 mají širší historický produktový rozsah než Atlas MVP. IAM-41/42 obecná viditelnost ticketů nenahrazuje přesné SNOW oprávnění a kontrakt. IAM-51 je vhodný obecný kandidát pro refresh, ale neřeší sám všechny podmínky submit/update.

VFID sub ↔ odpovídající ONSC/WSC user zůstává 1:1, email není párovací klíč. Manuální V4 SNOW customer/admin onboarding je oddělený od automatické volby CRM ID v SH. Group funkce jsou závislost či akceptované chování, nejsou automaticky CZ vývoj. Přesné CZ implementační delty se musí opřít o kontrakt a AS-IS.

## Podmínky a existující kandidáti

### UC005

| Ř. | Chování ze zdroje – parafráze | Návrh ověření | Kandidáti v Book1 a otevřený bod |
|---|---|---|---|
| 1 | Při neúspěšném VFID přihlášení ukončit přístupový tok před získáváním customer/role dat z DXL. | Neúspěšné přihlášení nevytvoří přihlášený přístup ani následný požadavek na customer/role data. | F-REQ-IAM-01 (ř.23), F-REQ-IAM-02 (ř.24). Doplnit výslovné pořadí kroků k IAM-02; přesný token kontrakt zůstává otevřený. |
| 2 | Pro zákaznický obsah použít role, vztahy a CRM ID získané přes DXL. | Oprávnění se vyhodnotí pro konkrétní identitu a aktivní CRM kontext. | F-REQ-IAM-06 (ř.28), F-REQ-IAM-07 (ř.29), F-REQ-IAM-20 (ř.42), F-REQ-IAM-21 (ř.43), F-REQ-IAM-22 (ř.44). Upstream ONSC/WSC data nejsou portálový handover. Oddělit VFID sub, lokální user a CRM kontext. |
| 3 | Zákaznický obsah zpřístupnit jen pro příslušnou administrativní roli a dostupné CRM ID. | Bez příslušné role zobrazit obecný obsah bez aktivního zákaznického kontextu. | F-REQ-IAM-08 (ř.30), F-REQ-IAM-09 (ř.31), F-REQ-IAM-10 (ř.32), F-REQ-IAM-11 (ř.33), F-REQ-IAM-12 (ř.34), F-REQ-IAM-13 (ř.35), F-REQ-IAM-14 (ř.36), F-REQ-IAM-15 (ř.37). Přesný povolený seznam V2/V4 rolí není novou UC baseline uzavřen. Historické názvy v IAM-08–15 nejsou automaticky schválené. |
| 4 | Automaticky zvolit jedno dostupné CRM ID. | Po vstupu je aktivní právě jedno oprávněné CRM ID i při více dostupných. | F-REQ-IAM-26 (ř.48), F-REQ-IAM-27 (ř.49), F-REQ-IAM-29 (ř.51). IAM-29 nevykládat jako povinnou ruční volbu před každým prvním vstupem. Priorita automatické volby není doložena. |
| 5 | Umožnit následné přepnutí mezi dostupnými CRM ID. | Přepnutí nahradí obsah a dostupné akce podle nového aktivního kontextu. | F-REQ-IAM-27 (ř.49), F-REQ-IAM-28 (ř.50), F-REQ-IAM-51 (ř.73). Upřesnit refresh a session pravidla bez zavedení favorites/default konfigurace nebo portálové propagace. |
| 6 | Neaktivovat CRM ID, které už není dostupné, a obnovit selector. | Ztracený vztah neumožní použít nedostupný kontext. | F-REQ-IAM-23 (ř.45), F-REQ-IAM-24 (ř.46), F-REQ-IAM-25 (ř.47), F-REQ-IAM-27 (ř.49). Plné chování není atomicky vyjádřeno v uvedených FREQ. Holding target není ověřený AS-IS payload. |
| 7 | Bez CRM ID nebo při nedostupných DXL datech nezobrazit zákaznicky specifický obsah. | Nedostupný DXL výsledek neotevře zákaznická data. | F-REQ-IAM-06 (ř.28), F-REQ-IAM-18 (ř.40), F-REQ-IAM-19 (ř.41). Rozlišit chybějící vztah od technické chyby; konkrétní timeouty a chybové kódy neurčeny. |

### UC006

| Ř. | Chování ze zdroje – parafráze | Návrh ověření | Kandidáti v Book1 a otevřený bod |
|---|---|---|---|
| 8 | Načítat Marketplace data pro aktivní CRM ID z UC005. | Služba z jiného zákaznického kontextu se nezobrazí. | F-REQ-IAM-30 (ř.52), F-REQ-IAM-33 (ř.55), F-REQ-IAM-34 (ř.56). Potřebný převod CRM ID na Marketplace company a konkrétní datová pole zůstávají k potvrzení. |
| 9 | V MVP zobrazovat Atlas managed services, skrýt non-managed a další managed produkty. | Ostatní produkt neotevře Atlas obsah jen proto, že existuje Marketplace subscription. | F-REQ-IAM-30 (ř.52), F-REQ-IAM-31 (ř.53), F-REQ-IAM-32 (ř.54), F-REQ-IAM-34 (ř.56). Zúžit historické and other Service Hub-related subscription; nešířit jím MVP na další služby. |
| 10 | Rozlišit žádnou dostupnou službu od nedostupnosti Marketplace dat. | Chyba Marketplace se nepředstaví jako úspěšně ověřený prázdný seznam. | F-REQ-IAM-35 (ř.57), F-REQ-IAM-36 (ř.58), F-REQ-IAM-37 (ř.59), F-REQ-IAM-38 (ř.60). Přesná UX znění, viditelné subscription stavy a cache pravidla nejsou uzavřené. |
| 11 | Po změně kontextu znovu vyhodnotit službová data pro nový kontext. | Starý zákaznický obsah nenahradí ověření nového CRM ID. | F-REQ-IAM-26 (ř.48), F-REQ-IAM-28 (ř.50), F-REQ-IAM-51 (ř.73). Doplnit návaznost UC005–006, technický refresh kontrakt neurčen. |

### UC007

| Ř. | Chování ze zdroje – parafráze | Návrh ověření | Kandidáti v Book1 a otevřený bod |
|---|---|---|---|
| 12 | Vytvoření support requestu zpřístupnit oprávněnému uživateli s Atlas službou v aktivním kontextu. | Nesplněné oprávnění nevede k vytvoření ticketu. | F-REQ-IAM-19 (ř.41), F-REQ-IAM-43 (ř.65), F-REQ-IAM-44 (ř.66), F-REQ-IAM-46 (ř.68). SNOW user/company scope a manuální V4 onboarding posoudit zvlášť od obecného přístupu do SH. |
| 13 | Před odesláním validovat povinné vstupy. | Neplatný povinný vstup se neodešle do SNOW. | Bez přímého protějšku v porovnané sadě. Přesný seznam mandatory/optional polí ani validace není potvrzen; nelze doplnit odhadem. |
| 14 | Úspěšné vytvoření potvrdit až po potvrzení SNOW. | Odmítnuté nebo nepotvrzené vytvoření se neprezentuje jako úspěch. | Bez přímého protějšku v porovnané sadě. Chybí atomické vyjádření v porovnávané sadě FREQ. Payload, assignment a routing vyžadují kontrakt. |
| 15 | Při změně CRM kontextu před odesláním nepoužít starý kontext. | Rozpracovaný požadavek nelze vytvořit pod neaktuálním CRM kontextem. | F-REQ-IAM-26 (ř.48), F-REQ-IAM-28 (ř.50), F-REQ-IAM-51 (ř.73). Obecný IAM-51 neuzavírá detail submit chování; nezavádět automatické přenesení formuláře. |

### UC008

| Ř. | Chování ze zdroje – parafráze | Návrh ověření | Kandidáti v Book1 a otevřený bod |
|---|---|---|---|
| 16 | Lokální BCS/LME telefonickou cestu použít jen pro whitelisted V2 zákazníka. | V4 zákazník není směrován touto lokální asistovanou cestou. | Bez přímého protějšku v porovnané sadě. Potřebný provozní whitelist, jeho správa a ověření nejsou uzavřeným kontraktem. |
| 17 | LME identifikuje zákazníka a kontext a zaznamená výsledek v SNOW. | Výsledek asistované podpory zůstane přiřazen správnému zákazníkovi. | Bez přímého protějšku v porovnané sadě. BCS je kanál a LME lidská role; neodvozovat z UC nový aplikační systém. |
| 18 | Pokud nelze vyřešit lokálně, předat či eskalovat dle provozního modelu. | Eskalace se nevykáže jako vyřešený zákaznický požadavek. | Bez přímého protějšku v porovnané sadě. Přesné resolver skupiny, routing a fallback při nedostupnosti nejsou potvrzené. |

### UC009

| Ř. | Chování ze zdroje – parafráze | Návrh ověření | Kandidáti v Book1 a otevřený bod |
|---|---|---|---|
| 19 | Plné ukončení zahájit pro správného zákazníka a subscription cestou Frontline/Siebel do ICT Hub/Provisioning. | Identifikace předchází ukončení; SH se neprohlásí za nový prodejní či termination vstup. | Bez přímého protějšku v porovnané sadě. Chybí atomický FREQ pro tuto hranici procesu v porovnávané sadě. |
| 20 | Následné ukončení vést přes Marketplace a SNOW/MSO. | Nepotvrzené předání se neprezentuje jako dokončené ukončení. | Bez přímého protějšku v porovnané sadě. Detailní payload, routing, efektivní datum a zotavení při selhání nejsou uzavřené. |
| 21 | Zachovat subscription mimo vymezený termination scope. | Ukončení Atlas nezpůsobí ukončení nesouvisející subscription. | Bez přímého protějšku v porovnané sadě. Downgrade se zachováním M365 patří do UC004; neslučovat jej s plným ukončením UC009. |

### UC010

| Ř. | Chování ze zdroje – parafráze | Návrh ověření | Kandidáti v Book1 a otevřený bod |
|---|---|---|---|
| 22 | Získávat ze SNOW support requesty odpovídající aktivnímu oprávněnému CRM kontextu. | Seznam neobsahuje požadavek jiného kontextu. | F-REQ-IAM-40 (ř.62), F-REQ-IAM-41 (ř.63). IAM-41 all tickets ani IAM-42 not current user nepovažovat za potvrzení rozsahu všech druhů SNOW ticketů. |
| 23 | Umožnit načtení detailu a aktuálního stavu přístupného požadavku. | Požadavek mimo oprávněný kontext nelze otevřít v detailu. | F-REQ-IAM-40 (ř.62). Přesná pole, status mapping, sorting/filtering a pagination nejsou potvrzené. |
| 24 | Při přepnutí CRM ID nahradit seznam i detail odpovídajícím kontextem. | Po přepnutí z A na B nezůstane obsah A jako obsah B. | F-REQ-IAM-26 (ř.48), F-REQ-IAM-28 (ř.50), F-REQ-IAM-51 (ř.73). Obecnou dynamickou aktualizaci rozpadnout na seznam/detail; časové a cache pravidlo otevřené. |
| 25 | Prázdný seznam odlišit od nedostupného SNOW výsledku. | Nedostupnost se neprezentuje jako ověřená absence požadavků. | F-REQ-IAM-49 (ř.71), F-REQ-IAM-50 (ř.72). Konkrétní UX a retry politika neověřena. |

### UC011

| Ř. | Chování ze zdroje – parafráze | Návrh ověření | Kandidáti v Book1 a otevřený bod |
|---|---|---|---|
| 26 | Změnu povolit pouze pro přístupný požadavek aktivního CRM kontextu. | Požadavek cizího kontextu nelze změnit. | F-REQ-IAM-18 (ř.40), F-REQ-IAM-19 (ř.41), F-REQ-IAM-26 (ř.48). Nezaměnit oprávněný company scope za pouhé porovnání emailu. |
| 27 | Získat aktuální stav a oprávnění k operaci ze SNOW. | SH nabízí jen operace povolené pro aktuální stav a oprávnění. | F-REQ-IAM-19 (ř.41), F-REQ-IAM-51 (ř.73). Povolené operace, pole, komentáře, attachments a status transitions nejsou specifikované. |
| 28 | Validovat změnu a neodesílat neplatnou či nepovolenou operaci. | Neplatná změna nedorazí jako update do SNOW. | Bez přímého protějšku v porovnané sadě. Chybí konkrétní atomický FREQ a potvrzená validační pravidla. |
| 29 | Úspěch změny zobrazit až po potvrzení SNOW. | Odmítnutá či nepotvrzená změna se nevykáže jako úspěšná. | Bez přímého protějšku v porovnané sadě. Chybí atomický FREQ. Technické kódy, retry a souběh změn nejsou uzavřené. |
| 30 | Při změně CRM kontextu nebo stavu znovu vyhodnotit oprávnění a operace. | Zastaralá oprávnění ani starý kontext nezaloží update. | F-REQ-IAM-26 (ř.48), F-REQ-IAM-28 (ř.50), F-REQ-IAM-51 (ř.73). IAM-51 je širší obecný požadavek; doplnit konkrétní aktualizační scénář. |

## Návaznost na SREQ a EA

`Kontrolni_matice.json` obsahuje původní text a GUID každého FREQ kandidáta a všechny nalezené řádky existujícího FREQ mapping, které jeho ID obsahují. Tyto vazby jsou inventura stávajícího workbooku, nikoli nově schválená sémantická shoda nebo EA konektor. Prázdné EA GUID u historického SREQ se nedoplňuje odhadem. Stejné historické IAM číslo v jiném zdroji může znamenat jiný požadavek.

Další revize musí pro každou podmínku rozhodnout reuse/úpravu/doplnění podle významu a konkrétní odpovědnosti. U otevřených API detailů se nejprve ověří primární kontrakt. Bez něj nelze dopsat pole, konkrétní operace, error/retry pravidla, stavové přechody nebo SNOW identity payload. UC001–004 a UC012 tímto dokumentem nejsou atomicky dokončeny.
