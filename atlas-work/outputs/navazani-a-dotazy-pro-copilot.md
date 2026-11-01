# Navázání práce: ServiceHub + Atlas

Uloženo 31. 10. 2026. Pokračování plánováno na 1. 11. 2026 podle dohody v chatu; připomínka nebyla nastavena.

## Kontext a stav

### Závazná pravidla uživatele od 1. 11. 2026

Ve vzdáleném VDI smí agent pouze číst. Nesmí zapisovat, vytvářet ani mazat soubory či data. Jediná výjimka je zadávání textu do vyhledávání v SharePointu, Confluence, Teams, Outlooku a do dotazů Copilotu. Copilot je preferován v Teams a může sloužit k dohledání přepisů schůzek. Nepoužívat jej k vytváření nebo úpravám souborů. Aktualizace starého Excelu se připravují jako lokální návrh mimo VDI, bez zásahů do zdrojového sešitu.

Nově otevřený Excel je v titulku označen Book1.xlsx. Viditelné listy zahrnují Cover, Functionalities, Interfaces, FREQ mapping, EAM App, Siebel EA Export, SREQ Aplikační role, Sheet1 a TA133Arch. FREQ mapping má při navigaci na konec použitou oblast do J220 (to samo o sobě neprokazuje počet platných požadavků). Obsahuje již pracovní poznámky odkazující na Martinův ServiceHub+Atlas – Requirements.xlsx, navržená SREQ ID a označení SHODA / CHYBÍ V SO / ROZPOR TEXTU. Jejich správnost dosud nebyla ověřena proti aktuálním zdrojům.

V listu SREQ Aplikační role jsou sloupce pro kvalitu vazby, doloženost změny a chybějící podklady. Část řádků výslovně upozorňuje, že je popsána cílová odpovědnost, nikoli doložená změna proti AS-IS. Toto rozlišení zachovat.

Otevřená Confluence stránka „Copilot Agent – SO Traceability review (BRD<->SO review)“, pageId 275444785, popisuje přístup k doložení FREQ→SREQ, NFR a reverse traceability. Je to metodický zdroj, nikoli projektová specifikace. Je označena IN TESTING. Deklarované mapování není samo důkaz pokrytí.

Pokus o vložení vyhledávacího dotazu do Teams Copilotu 1. 11. zobrazil Microsoft Purview „Checking information“; po skončení kontroly zůstalo pole prázdné. Dotaz nebyl odeslán. Uživatel byl požádán o ruční zadání nebo externí instanci. Kontrolu neobcházet a výsledek neinterpretovat jako získanou odpověď Copilotu.

Uživatel je Solution Architect, pracuje především s aplikační (modrou) vrstvou ArchiMate. Cílem je získat podklady pro analýzu Vodafone ServiceHub + Atlas, zejména dokumentace analytika Martina Dostála, a identifikovat aplikace, odpovědnosti, integrace, use cases, datové vazby a otevřené otázky.

Průzkum je uložen v souboru `servicehub-pruzkum-podkladu.md` ve stejné složce. Obsahuje soupis 38 záložek větve ServiceHub a jednoho odkazu Projects, dostupnost zdrojů a zjištění. Jde o průzkum využitelnosti, nikoli kompletní analýzu všech dokumentů a příloh. Sousední větve VBTS a SNOW dosud nebyly systematicky zahrnuty.

Přístup: Omnissa Horizon, vzdálená plocha AOProd W11. V prohlížeči je Raindrop se strukturou Vodafone → Projects → ServiceHub → Atlas / Confluence / Group / Tasks. Při pokračování vždy znovu ověřit aktuální okna a obrazovku; nepoužívat staré souřadnice a screenshoty.

Confluence a SharePoint byly přístupné. Skupinová Jira byla přístupná; lokální Jira IDEA vyžadovala přihlášení. Přihlašování provádí uživatel ručně. Přes VDI se při pokusu o zadání dotazu do Copilotu vložil starý obsah schránky místo zadaného textu. Dotaz nebyl odeslán a nesprávný text byl vyčištěn. Copilot odpověď tedy nebyla získána.

Uživatel může dotazy do Copilotu vložit sám a dodat výsledky, případně otevřít Copilot externě nebo v Teams. Další relevantní podklady existují v e-mailech, Teams, SharePointu a v Excelu na OneDrivu; jejich obsah dosud není prověřen.

## Co ověřit při navázání

1. Stanovit platné výchozí verze BRD, Dostálovy Use Case Specification a Solution Overview. Přímá záložka Use cases vedla na červnový dokument, přes BRD nové byla nalezena specifikace Martina Dostála s titulním datem 14. 10. 2026.
2. Dohledat novější rozhodnutí a změny v e-mailech a Teams. Rozlišovat požadavek, návrh, schválené rozhodnutí a implementovaný stav.
3. Získat relevantní Excel z OneDrivu; zjistit účel, listy, vlastníka, datum a vazbu na požadavky, identifikátory nebo integrace. Dosud neznáme jeho název ani obsah.
4. Rozpracovat katalog aplikací a integrační matici s odkazy na konkrétní zdroje.
5. Oddělit segmenty V2/V4 a entity zákazník, CRM účet, Marketplace účet, uživatel, administrátor, tenant a subscription. Kardinality a korelační identifikátory musí být doloženy.
6. Prověřit aktuální podobu onboardingu a životního cyklu uživatelů: některé zdroje popisují automatické kroky, jiné ruční operace nebo nepotvrzený cílový model.
7. Nepřebírat stará rizika jako aktuální: DMM-63200 měl při kontrole stav Done a odkaz na Atlas Subscription Enablement. DMM-63198 a DMM-64918 byly In Progress.

## Dotazy pro Copilot

Dotazy jsou určené k postupnému vložení do pracovního Copilotu s přístupem k firemním zdrojům. Každou odpověď je nutné ověřit v citovaných dokumentech. Pokud konkrétní Copilot nemá přístup ke všem uvedeným zdrojům, má omezení výslovně uvést.

### 1. Nejaktuálnější dokumentace a autorství

> Vyhledej ve zdrojích, ke kterým máš přístup, podklady k Vodafone CZ projektu ServiceHub + Atlas, PR25_0837. Zaměř se na dokumentaci Martina Dostála: BRD, Use Case Specification, procesy, požadavky, workshopy a traceability. Pro každý dokument uveď přesný název, autora, datum poslední změny, uvedenou verzi, stav schválení, pokud je doložen, a přímý odkaz. Rozliš současné dokumenty od starých kopií a exportů. Prověř zejména rozdíl mezi Use Case Specification z 10. 6. 2026 a verzí s titulním datem 14. 10. 2026. Neodhaduj platnost pouze podle data změny souboru. Pokud nelze určit závaznou verzi, napiš, jaký důkaz chybí.

### 2. Rozhodnutí z e-mailů a Teams

> Najdi v dostupných e-mailech a Teams diskusích rozhodnutí a změny k ServiceHub + Atlas / PR25_0837, zejména od 14. 10. 2026 do dneška, a starší zprávy nutné k pochopení kontextu. Zaměř se na Martina Dostála, CZ architekturu, V2/V4 zákazníky, onboarding do SNOW EVE, CRM/Siebel versus Marketplace/AppDirect, Vodafone Identity/CZ IDaaS, ONSC/WSC a DXL. Vytvoř tabulku: datum, téma, přesný závěr parafrází, kdo jej potvrdil, stav (návrh / rozhodnutí / implementace / otevřená otázka), dotčené aplikace a přímý odkaz na zprávu nebo vlákno. Odliš výslovné rozhodnutí od své interpretace. U rozporů zachovej oba zdroje a nevybírej sám vítěznou variantu.

### 3. Aplikace, služby a integrační vazby

> Z doložených podkladů k ServiceHub + Atlas vytvoř katalog aplikací a integrační matici pro Solution Architecta. U aplikací uveď používané názvy a aliasy (např. COSMOS / ServiceHub), účel, odpovědnost, vlastníka, pokud je uveden, a zdroj. U vazeb uveď zdrojovou a cílovou aplikaci, službu/rozhraní/API, směr, spouštěč, přenášené datové objekty a identifikátory, ruční nebo automatický krok, synchronní/asynchronní průběh, segment V2/V4, stav AS-IS / schválené TO-BE / návrh a zdroj. Nevyplňuj chybějící údaje odhadem. Rozliš aplikaci, dodávaný produkt/službu, technologickou platformu a projekt.

### 4. Identita a korelace účtů

> Dohledat a porovnat aktuální pravidla pro CRM Customer/Account ID, Marketplace Company/Account ID, Vodafone Identity/CZ IDaaS User ID, SNOW customer/contact/user, Microsoft tenant ID a subscription ID v ServiceHub + Atlas. Uveď pro každý identifikátor systém původu, systém evidence, kardinality a způsob mapování. Zvlášť zpracuj V2 a V4, více Marketplace účtů k jednomu CRM účtu, primárního a sekundárního administrátora, vytvoření/změnu/deaktivaci uživatele a ukončení posledního Atlas produktu. U každého pravidla cituj dokument nebo konkrétní zprávu. Označ nevyřešené rozpory a nepotvrzené varianty.

### 5. Rizika a jejich aktuální řešení

> Najdi nejnovější podklady a rozhodnutí související s DMM-63198 (Dual CZ Customer Segments with Separate Portals and IT Stacks), DMM-64918 (CZ Architecture Open Points) a DMM-63200 (Marketplace Users Created via G-SNOW Not Present in CZ IDaaS, Blocking SH SSO Access). Při kontrole 31. 10. 2026 byly první dva záznamy In Progress a DMM-63200 Done s odkazem na Atlas Subscription Enablement. Neoznačuj DMM-63200 automaticky za otevřené riziko. Uveď doložené řešení, zbývající závislosti, odpovědnosti a důkazy implementace nebo akceptace. Pokud k Jiře nemáš přístup, napiš to a použij pouze dohledatelné dokumenty/zprávy.

### 6. Excel a traceability

> Najdi relevantní Excel sešity na OneDrivu a SharePointu k ServiceHub + Atlas: požadavky, use cases, traceability, integrační seznamy, zákaznické identifikátory a CZ – Arch & SD requirements. Uveď přesný název, umístění, vlastníka, datum změny, seznam relevantních listů a přímý odkaz. Vysvětli, zda jde o zdroj požadavků, mapovací tabulku, report, rozhodovací log nebo pracovní kopii. Upozorni na duplicitní a zastaralé soubory. Nevymýšlej obsah listů, které nemůžeš číst.

## Jak předat výsledky zpět

Nejprve je nejúčelnější dodat odpovědi na dotazy 1 a 2 včetně zdrojových odkazů. Následně použít dotazy 3–6 podle zjištěných mezer. U dlouhých odpovědí zachovat odkazy a rozlišit text Copilotu od skutečného obsahu zdroje. Výsledky nemusí být upravované ani předem shrnuté.
