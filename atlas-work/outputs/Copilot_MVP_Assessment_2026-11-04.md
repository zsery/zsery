# Teams Copilot a primární přepis MVP Assessment, 4. 11. 2026

Práce ve VDI AOProd W11, Teams. Zdrojová data pouze čtena. Cílený dotaz o Atlas/ServiceHub Board MVP scope, odkazech a verzích byl úspěšně zadán přímými klávesami a odeslán. Clipboard input přenášel starší text; koncept byl vymazán a správný dotaz před odesláním vizuálně ověřen. Pro další krátké dotazy funguje press_key po znacích. Nejde o obcházení outbound clipboard omezení.

## Vodítka z Copilotu – dosud nejsou novým schválením

Copilot uvedl jednání Architecture board 20.10.2026 12:30–14:30 a podmíněné schválení limitovaného MVP s evidencí rizik, vlastněným technickým dluhem a roadmapou. Tento přepis Board jednání zatím nebyl přímo ověřen.

Copilot nabídl tři soubory Atlas CZ Launch – Architecture Board Confirmation of Phased Implementation Approach, další s příponou 1 a 2, s modified 19., 21. a 23.10.2026. Samotné modified datum a tvrzení Copilotu nedokládají approval ani kanonickou identitu. Přímé URL nebyly přepsány; odkazy zůstávají v odpovědi Teams Copilotu. Uživatelův závazný Board scope se tímto nepřebíjí.

Copilot dále nalezl schůzku CZ Atlas+SH: MVP Assessment z 2.11.2026. Přes odkaz byla otevřena její primární Teams stránka: pondělí 2.11.2026 12:00–12:45, organizátorka Esther de Gracia Corrales. Je dostupný záznam 01:02:01 a přepis. Recap ukazuje No files were shared. Meeting Copilot byl použit na shrnutí přepisu před jeho cíleným ověřováním.

Meeting Copilot uvádí V2 i V4 v MVP, manuální/interim V4, V2 závislost na ServiceNow for Business; standalone SH bez navigačního propojení s CZ portály, VFID/OIDC; single-account picker; hledání, favorites/default account konfiguraci, přejmenování a agregované parent/child pohledy mimo MVP. Tyto body jsou zatím shrnutí Copilotu, nikoli všechny přímo ověřené výroky přepisu.

## Přímo přečtené úseky přepisu

- Vyhledání parent v přepisu ukázalo 28 shod. První část navazuje na Dan England 4:56 a popisuje nabídku parent i child accounts; následující shody popisují výběr jednoho účtu a viditelnost zvoleného účtu. Jde o počáteční popis, nikoli automaticky závěrečné rozhodnutí schůzky.
- Vyhledání tmf ukázalo tři shody. Zdeněk Šerý 18:29 zpochybňuje možnost přejít z child na parent a říká, že přes TMF691 pravděpodobně nepřijde struktura parent–child, pouze array bez struktury; ptá se, odkud vztah pochází. Čtené znění je automatický přepis, obsahuje neobratné formulace a není samostatný API kontrakt.
- Kapil Jain 19:23 reaguje, že vztah by nejprve musel přijít v 691 array; následný Zdeňkův výrok 19:38 opět rozlišuje ploché pole bez parent–child relace. Celý následný úsek ještě nebyl dočten.
- Zdeněk Šerý 49:34 odmítá identifikaci uživatele emailem, protože email není unikátní ID a user má jiné ID. Navazující text říká, že user ID vrací TMF691 a email k němu nemusí být 1:1, jiné ID může mít stejný email. Toto se týká vztahu email–user ID, nikoli popření pravidla VFID sub ↔ příslušný ONSC/WSC user 1:1. V další viditelné položce Esther de Gracia Corrales 50:15. Návazná odpověď nebyla přečtena.

## Dopad a další přesné místo

Dodatečné přímé čtení: Esther 50:15 bere poznámku na vědomí. Pankaj Bhadauria 50:41 se ptá na email/password login přes Vodafone ID. Zdeněk 51:03 odpovídá o interně diskutované kombinaci CRM ID a Vodafone ID pro určení uživatele; přepis následně uvádí formulaci o více users se stejným Vodafone ID. Bez určení významu lokálního „user“ a následného kontextu se tento automatický přepis nesmí zaměnit za změnu závazného VFID sub ↔ ONSC/WSC user 1:1. Vyžaduje další čtení, nikoli automatickou změnu kardinality v Book1 nebo EA.

Výslovný cílový požadavek uživatele na TMF691 holding parent–child zůstává zachován. Přečtený přepis podporuje potřebu oddělit AS-IS omezení a cílové rozšíření. Není důvod měnit CustomerContext generalizace ani vytvářet konkrétní payload.

Další cílený dotaz meeting Copilotu na diskusi po minutě 51 vrátil tyto citované časy (dosud kontrolováno v odpovědi Copilotu, nikoli znovu v odpovídajících místech primárního přepisu): Pedro Melo Pereira 51:36 a 52:27–52:38 se ptá na používání email ID pro vytváření/získávání SNOW ticketů. V 53:02 navrhuje offline diskusi se SNOW týmem. V 53:36 popisuje OIDC sub a více CRM účtů na jedny credentials. V 54:14 odděluje account selection od předávání identity do SNOW. V 54:46 upozorňuje, že samotný přechod na sub nemusí problém vyřešit a je nutná diskuse s CZ a SNOW. Tato část neobsahuje mnou ověřené definitivní rozhodnutí o SNOW payloadu. Další text odpovědi dosud nepřečten.

Pracovní integrační review proto musí mít oddělené otázky: ověřená autentizace/VFID sub; odpovídající lokální ONSC/WSC user; seznam oprávněných CRM kontextů; SNOW company/user identifikace pro konkrétní ticket operaci. Jde o rozlišení k prověření existujících kontraktů, nikoli nové kardinality, nové GUID nebo potvrzení emailového párování. Uzavření poslední otázky závisí na primárním dokladu o dořešení CZ+SNOW.

Živý stav na konci záznamu: Teams → CZ Atlas+SH: MVP Assessment → Recap → Transcript, hledání tmf, shoda 2/3; obraz ukazuje začátek výroku Zdeňka 49:34. Pokračovat tímto úsekem a návaznou reakcí, poté ověřit ostatní Copilot závěry. Neprohlašovat celý přepis, Board verze ani úplný Group průzkum za dokončené. Book1, Atlas.xml a SO tímto krokem nebyly změněny.
