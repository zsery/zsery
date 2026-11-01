# Revize Excelu ServiceHub + Atlas – první ověřené nálezy

Datum: 1. 11. 2026. Práce ve VDI pouze čtením; žádné buňky, soubory ani projektová data nebyly upraveny. Tento lokální dokument je návrhem pro další revizi, nikoli aktualizovaným sešitem ani schválenou změnou scope.

**Doplnění po přímé kontrole SharePointu:** CHM-05 až 27 v Support_Material/Requirements.xlsx významově odpovídají přečteným CHM vazbám Book1; druhá odpověď Copilotu je přiřadila chybně. U IAM je nutná oprava: IAM-39 ve zdroji ř. 94 znamená customer selection, nikoli viditelnost portálového odkazu z Book1 ř. 219–220. Zdroj navíc opakuje IAM-30 až 32 s odlišnými texty. Říjnový MVP Requirements byl přímo přečten (scope a dekompozice). Podrobnosti viz sharepoint-cz-local-pruzkum.md. Následující tabulka je stále návrh revize Book1, nikoli schválená baseline.

## Výchozí podklady

| Zdroj | Co bylo přímo přečteno | Omezení |
|---|---|---|
| Otevřený Book1.xlsx | Listy Functionalities, FREQ mapping a SREQ Aplikační role; konkrétní řádky uvedené níže. | Celý sešit nebyl kompletně přečten. Úplné cloudové umístění a závazná verze nejsou potvrzeny. |
| PR25_0837_ServiceHub_Atlas_BRD.docx | Titulní verze 0.1; rozsah MVP na stranách 7–8 a 12; reference na Use Case Specification na str. 5; kapitola 2.2 Requirements Matrix. | V seznamu souborů datum změny 23. října. Datum změny samo nedokládá schválení. V zobrazené kapitole 2.2.1 jsou prázdné šablonové řádky, nikoli potřebný detailní seznam FREQ. |
| PR25_0837_ServiceHub_Atlas_Use_Case_Specification.docx | Titulní verze 0.1, Last Update 14 October 2026, autor Martin Dostál; Executive Introduction / MVP Access Model na str. 3; začátek UC001 na str. 4. | V knihovně uvedena změna před dvěma dny. Titulní datum a metadata změny se liší. Aktuálně zobrazený obsah je jiný než starší červnová specifikace. |
| PR25_0837_ServiceHub_Atlas_Traceability_Decomposition.xlsx | Struktura CJ → UC → Process → Value Stream → Capability → Sub-capability a popisy úvodních položek. | Není to detailní tabulka FREQ/SREQ. Nelze ji zaměnit za zdrojový Requirements.xlsx. |
| Confluence: Copilot Agent – SO Traceability review (BRD<->SO review) | Metodika dokazování pokrytí a reverse traceability. | Metodický zdroj IN TESTING, nikoli projektové požadavky. |

Projektové dokumenty byly otevřeny přes Atlas Programme → 2. Portfolio → Atlas Expansion – Czech → Interlock-Pack → CZ local folder → Business Requirements Document; specifikace je v podsložce Use Cases.

## Zásadní zjištění: aktuální MVP je standalone

BRD na stranách 7–8 popisuje ServiceHub jako samostatný zákaznický portál přes vlastní URL. Integrace, embedding, přímá navigace a kontextový handover z ONSC/WSC nejsou součástí MVP. Strana 12 omezení opakuje.

Aktuálně otevřená Use Case Specification na straně 3 v oddílu MVP Access Model nezávisle potvrzuje samostatnou URL a vyloučení ONSC/WSC integrace z MVP. Současně říká, že ServiceHub a Atlas produktová funkcionalita zůstává vlastnictvím Vodafone Group; CZ dodává lokální vstupy, data readiness, integrační podmínky a procesní změny. Group funkcionalita popsaná jako end-to-end závislost se tím automaticky nestává CZ implementačním požadavkem.

**Důsledek pro revizi:** existující řádky související s portály nelze pouze hromadně přemapovat nebo označit jako pokryté. Je nutné rozlišit práci mimo MVP, zachovaný standalone přístup, autentizaci a zákaznický kontext a případné budoucí rozšíření. Následující návrhy jsou podmíněné potvrzením platné projektové baseline a absencí pozdějšího rozhodnutí měnícího scope.

## Konkrétní kandidáti změn v Book1.xlsx

Čísla řádků níže platí pro list FREQ mapping při kontrole. ID i čísla řádků před aplikací změn znovu ověřit. Původní ID zachovat; nic bez schválení nemažte ani nepřečíslovávejte.

| Řádek | Stávající vazba | Přečtený význam | Návrh k revizi | Důkaz / co ještě ověřit |
|---|---|---|---|---|
| 203 | F-REQ-CHM-05 → SREQ-SH-66 | Standalone portál ServiceHub. | Zachovat jako kandidáta MVP; doložit vyhovující funkcionalitu a správné rozhraní místo závěru jen z vazby ID. | BRD str. 7–8, UC specifikace str. 3. Přesné znění SREQ-SH-66 je nutné přečíst celé. |
| 204 | F-REQ-CHM-14 → SREQ-SH-67 | ONSC navigační odkaz v ServiceHub. | Prověřit vyřazení z aktuální MVP baseline / odložení; zachovat historii. | Aktuální přístupový model je standalone. Zvlášť ověřit, zda konkrétní outbound odkaz není výslovně požadován jiným schváleným zdrojem. |
| 205 | F-REQ-CHM-15 → SREQ-SH-68 | WSC navigační odkaz v ServiceHub. | Stejná kontrola jako u předchozího řádku. | Neodvozovat rozsah outbound odkazů jen z obecné věty o ONSC/WSC integraci. |
| 206 | F-REQ-CHM-16 → SREQ-SH-69 | Otevření ONSC v novém okně. | Kandidát mimo MVP, do potvrzení ponechat jako otevřený scope bod. | Ověřit explicitní zdroj outbound navigace. |
| 207 | F-REQ-CHM-17 → SREQ-SH-70 | Otevření WSC v novém okně. | Kandidát mimo MVP, do potvrzení ponechat jako otevřený scope bod. | Ověřit explicitní zdroj outbound navigace. |
| 210 | F-REQ-CHM-06 → SREQ-PORTAL-10; IF_ONSC_03 | ONSC poskytuje aktivní zákaznický kontext do ServiceHub. | Oddělit od MVP; neuvádět jako povinnou MVP integraci bez novějšího rozhodnutí. | BRD str. 7–8 vylučuje kontextový handover; UC specifikace str. 3 vylučuje ONSC/WSC integraci. |
| 211 | F-REQ-CHM-07 → SREQ-PORTAL-11; IF_WSC_01 | WSC poskytuje aktivní zákaznický kontext do ServiceHub. | Stejná změna jako řádek 210. | Stejné zdroje. |
| 212 | F-REQ-CHM-08 → SREQ-SH-73; IF_SH_04 | Převzetí zabezpečeného kontextu z portálového cookie jako počátečního execution context. | Oddělit konkrétní mechanismus portálového cookie od obecné potřeby bezpečného zákaznického kontextu. Portálový mechanismus nemodelovat jako MVP změnu bez dalšího důkazu. | BRD str. 7–8; UC specifikace str. 3. Standalone autentizace a customer-context resolution vyžadují vlastní detailní podklad. |
| 213 | F-REQ-CHM-18 → SREQ-SH-74 | Výběr zákaznického kontextu při přímé URL a více kontextech. | Nepřesouvat automaticky mimo MVP; přečíst aktuální UC005 a ověřit konkrétní způsob výběru. | Standalone URL je v MVP, ale tento detail zatím nebyl z aktuálního UC005 doložen. |
| 214 | F-REQ-CHM-19 → SREQ-SH-75 | Přímé otevření při jediném vyřešeném kontextu. | Stejně jako řádek 213 vyžaduje samostatné ověření, nikoli automatické odstranění. | Aktuální UC005. |
| 218 | F-REQ-CHM-21 → SREQ-PORTAL-07 | WSC/ONSC mají zobrazit vstup do ServiceHub všem autentizovaným uživatelům. | Pro MVP označit konflikt scope a odložit portálovou implementaci. Neřešit jen přepisem na „všichni uživatelé“ versus role-based visibility. | BRD str. 7–8 a 12; UC specifikace str. 3. |
| 219 | F-REQ-IAM-39 → SREQ-PORTAL-12; IF_ONSC_02 | Lokální role a eligibility řídí viditelnost odkazu ONSC. | Oddělit portálovou viditelnost mimo MVP od oprávnění uvnitř standalone ServiceHub. | Stejné zdroje. Poznámka v pracovním Excelu o rozhodnutí role-based access sama není nezávislý důkaz. |
| 220 | F-REQ-IAM-39 → SREQ-PORTAL-13; IF_WSC_02 | Lokální role a eligibility řídí viditelnost odkazu WSC. | Stejně jako řádek 219. | Stejné zdroje. |

Řádky 208–209 (eligibility po vstupu a zákaz service-specific funkcí při nesplnění eligibility) nejsou automaticky zrušeny tím, že portálové vazby nejsou v MVP. Jejich přesné podmínky a aplikační odpovědnost je nutné doložit z aktuálního UC005/UC006 a požadavkového sešitu.

## Další korekce struktury modelu

- **FREQ není automaticky SREQ jedné aplikace.** Group závislost a lokální implementační změna musí mít rozdílný status. Stejně tak obchodní pravidlo nemusí znamenat nový interface.
- **Funkce není důkaz delta změny.** List SREQ Aplikační role už u řady položek uvádí chybějící AS-IS. Tyto řádky nemají být prezentovány jako potvrzený dopad do aplikace.
- **Neodvozovat změny CRM z názvu UC.** Aktuální UC001 na str. 4 popisuje obchodní prodej přes CRM a příslušný sales tool (BidBot pro V2, OfferTool pro V4) a v úvodu odlišuje komerční výsledek od vytvoření Marketplace customer/order/subscription. Staré lead-management funkcionality je třeba porovnat s celým aktuálním tokem, nikoli hromadně schválit nebo odstranit.
- **Zachovat reference na zdroj i verzi.** Stávající označení SHODA, CHYBÍ V SO a poznámky „opraveno podle Martina“ nezastupují konkrétní odkaz na zdrojový řádek, kapitolu a verzi.
- **Traceability Decomposition je samostatná vrstva.** CJ, UC, proces a capability se nesmějí zaměnit za atomický FREQ nebo SREQ. Aktuálně zobrazená dekompozice obsahuje například UC005 Customer Accesses Service Hub a UC012 Customer Is Onboarded to Atlas Managed Service.

## Co zbývá pro úplnou aktualizaci

1. Dohledat přesný aktuální soubor ServiceHub+Atlas – Requirements.xlsx, na který odkazují pracovní poznámky. Jeho obsah v této kontrole ještě nebyl otevřen.
2. Potvrdit rozhodnutí měnící scope po zveřejnění aktuálního BRD/specifikace v e-mailech, Teams a přepisech schůzek.
3. Doplnit UC006 a související requirements pro produktovou eligibility a dostupnost Atlas služeb; UC005 byl následně přečten, viz doplnění níže.
4. Projít všechny platné řádky původního sešitu a připravit lokální změnovou matici: původní ID, původní text, návrh textu, aplikace, funkcionalita, rozhraní, změna scope, důvod, zdroj a jistota.

## Copilot

Vyhledávací dotaz nebyl odeslán: při vložení se zobrazila kontrola Microsoft Purview a pole zůstalo prázdné. Uživatel byl požádán o ruční zadání nebo externí Copilot. Z odpovědi Copilotu nebyl odvozen žádný nález.

## Doplnění: ověřený UC005, strany 19–21

Aktuální UC005 rozlišuje přístupové oprávnění od dostupnosti konkrétní služby Atlas:

- Zákazník otevírá vlastní URL ServiceHub a autentizuje se přes Vodafone Identity.
- ServiceHub získává z DXL uživatele, zákaznické vztahy, ONSC/WSC role a dostupná CRM ID. ONSC/WSC administrativní role zůstávají autorizačním vstupem i při standalone přístupu.
- Pro oprávněného administrátora ServiceHub automaticky zvolí právě jedno dostupné CRM ID jako aktivní kontext. Neříká, že výběr probíhá jen při jediném dostupném CRM ID.
- Customer Selector umožňuje následně přepnout na jiné CRM ID dostupné podle DXL. Při již nedostupném vybraném CRM ID se na ně nepřepne a obnoví seznam.
- Autentizovaný uživatel bez způsobilé administrativní role dostane obecnou stránku bez zákaznicky specifického obsahu. Při chybě autentizace nevznikne autentizovaná session; při chybějícím CRM ID nebo nedostupném DXL se zákaznicky specifický obsah nezobrazí.
- Úspěšný UC005 sám nepotvrzuje dostupnost Atlas služeb: ta se řeší v UC006 v aktivním zákaznickém kontextu.

**Upřesnění návrhu pro řádky 213–214:** zachovat potřebu aktivního kontextu, ale prověřit starou logiku „více kontextů → povinný úvodní selector“ a „jeden kontext → přímé otevření“. Aktuální UC005 popisuje automatickou volbu jednoho dostupného CRM ID a až následné přepínání. Bez Requirements.xlsx nelze doplnit nové atomické FREQ/SREQ ani označit přesné pokrytí.

**Upřesnění pro řádky 208–209 a 219–220:** neztotožňovat administrativní oprávnění, produktovou eligibility, dostupnost služby a viditelnost portálového odkazu. UC005 dokládá první oblast, UC006 řeší dostupnost Atlas; portálová navigace je podle aktuálního MVP mimo scope.
