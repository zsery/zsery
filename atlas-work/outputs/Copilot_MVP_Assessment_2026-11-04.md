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

Následné přímé ověření hledáním pivot (jedna shoda) ukázalo Pedrovu položku **54:45**, která výslovně odděluje selection od dnešního předávání email ID do Gsnow a ptá se, zda je změna nutná. Čas 54:14 v Copilot odpovědi tedy není přesně shodný s časem nalezené položky primárního přepisu. Pankaj 55:03 říká, že současný SNOW i ServiceHub pracují na emailové adrese a použití sub by mělo dopad na oba systémy. Jde o popis tehdejší implementace a diskusi dopadu, nikoli approval používat email jako stabilní VFID mapovací klíč. Následující krátké položky Pedra a Michaela Murphyho obsahují nejasně přepsaný text; z něj nebylo vyvozeno rozhodnutí. Aktuální místo čtení: přepis hledání pivot, kolem 55:11 a následující Pedrovy reakce; původní uvedené místo tmf 2/3 je historické.

## Následný dotaz na aktuální Martinovy podklady

V obecném Teams Copilotu byl správně zadán a odeslán dotaz na nejnovější Martin Dostál Atlas CZ local analysis, odkazy a verze. Copilot uvádí rozdělení analýzy mezi BRD, Use Case Specification a traceability/decomposition. U BRD nabízí odkaz PR25_0837_ServiceHub_Atlas_BRD, modified 3.11.2026 16:21 UTC a editor Martin Dostál. To je vodítko z Copilotu, metadata zatím nebyla nově ověřena na primárním souboru. Nelze z toho tvrdit nové vydání nebo approval. Zbytek odpovědi nebyl dočten.

Historická překážka posunu byla překonána: po ručním posunu uživatelem fungovalo také vlastní tažení svislého posuvníku. Odpověď na Martinův dotaz byla následně dočtena. Nevyžaduje další ruční posun uživatelem.

Další část odpovědi uvádí UC Specification se stejným modified 3.11.2026 16:21 UTC, editor Martin Dostál, cover 0.1 a Last Update 14.10.2026. Traceability je podle odpovědi dokončená CJ→UC→Process→Capability→Subcap matice; verze v odpovědi není. Copilot dále přisuzuje Martinovi zprávu z 2.11., že detailní UC text je hotový a diagramy/review a FREQ následují. Tato zpráva nebyla primárně otevřena, nejde o approval.

Přes nabídnutý odkaz byl otevřen aktuální UC dokument. WordWeb nejprve nabídl Editing; bez psaní do dokumentu bylo přepnuto na Viewing a explicitně otevřen Immersive Reader. Primární cover ukázal Project PR25_0837, verzi 0.1 a Last Update 14 October 2026. Knihovní modified metadata nebyla nově samostatně ověřena; samotný word count neprokazuje revizi.

## Cílený rozbor akceptace UC005–UC011

V Teams Copilotu byl 4.11. odeslán a vizuálně ověřen dotaz `Atlas uc005 to uc011 acceptance rules and gaps with citations`. Odpověděl agent Atlas v rámci Copilotu a citoval aktuální UC Specification, verzi 0.1. Tabulka UC005–UC011 i závěr byly dočteny tažením svislého posuvníku. Odpověď potvrzuje jako mezery přesnou sadu rolí, pravidlo počátečního CRM ID, DXL mapping/chyby/session refresh; Marketplace data contract a viditelné subscription stavy; SNOW pole/validace/routing; asistovaný V2 whitelist a provozní směrování; termination payload/efektivní datum/reconciliation; read ticket pole/status/sorting a zejména update operace/pole/comments/attachments/stavové přechody. Jedná se o analytické shrnutí agenta, ne o nově potvrzené API detaily.

Chování bylo porovnáno s již přímo přečtenými UC poznámkami z 3.11. a aktuálním lokálním Book1. Výsledek je [pracovní rozpad 30 podmínek](UC_atomicke_podminky_2026-11-04/UC_review.md) a strojová matice původních GUID a existujících mapovacích řádků. Návrhy akceptace nejsou schválená baseline. Agent navrhuje prioritu UC011 → UC007 → UC009 → UC005/006 → UC010 → UC008 a sám výslovně označuje toto pořadí za vlastní analýzu; nejde o nové pořadí stanovené uživatelem.

Přepis kolem 55:11 a následná CZ+SNOW diskuse zůstávají k ověření. Celý přepis, Board approval a úplný Group průzkum nejsou dokončené. Kanonický XLSX, Atlas.xml a SO se tímto krokem nezměnily.
