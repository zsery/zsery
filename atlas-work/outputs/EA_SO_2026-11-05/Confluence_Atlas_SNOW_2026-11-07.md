# Atlas / SNOW – cílené primární čtení 7. 11. 2026

Přímo čteno v Chrome ve VDI po ručním přihlášení uživatele. Jde o podklad pro dokončení SO, nikoli samostatný audit nebo potvrzení implementace.

## PR25_0749 Servicenow (Snow) drop 2

Primární stránka: https://confluence-agile.oskarmobil.cz/display/IAG/PR25_0749+Servicenow+%28Snow%29+drop+2#tab-Solution+description

Hlavička: created by Dana Košťálová, Vodafone; last modified 13. srpna 2026. AB Summary uvádí request type Acknowledgment; pole výsledku a schvalujících jsou zástupný text. To není důkaz schválení.

Přímo přečtená část Solution description:

- UC03.04 Synchronize Customer Users požaduje zákaznické uživatele a role pro V2 i V4 provisionovat do ServiceNow a poskytovat ServiceHub přes DXL TMF691; uvádí souvislost s Atlas projektem.
- Následující odstavec popisuje návrh DXL udržovat vztah a roli uživatele k nejvyššímu spravovatelnému assetu. Úplná autorizace má být dopočtena při požadavku; pro holding nebo VPN association se mají dohledat údaje ze zdrojového OneNet Foris. Obdobné chování je navržené pro Snow Connector při provisioningu uživatele/role do ServiceNow.
- Schéma UC03.04 obsahuje poznámku o IDaaS email jako vstupu. Je to historické schéma návrhu; nepotvrzuje email jako stabilní identitní klíč. Závazné uživatelské pravidlo VFID sub ↔ příslušný ONSC/WSC USER 1:1 zůstává zachované.
- UC03.07 popisuje integrační tok CZ Remedy přes V4 Tibco a Snow Connector do ServiceNow. Příchozí požadavek ze ServiceNow má přijímat CZ DXL, value mapping dělat Snow Connector dle konfigurace a V4 Tibco mapovat TMF621 API na Remedy API. Je to kontext toku Remedy, nikoli potvrzení ServiceHub klientského API nebo ticket entitlement filtru Atlas.

Dopad pro SO: tyto pasáže mohou doložit původ návrhu upstream rolí a hierarchie. Nepotvrzují aktuální Atlas klientskou konfiguraci, role enum, technický kontrakt ticketů ani nasazení. Automatický V4 onboarding z historického návrhu nepřebírat do aktuálního manuálního MVP. Otevřené OP-03/OP-07 a Atlas kontrakt se tím neuzavírají.

## Atlas (SNOW + ServiceHub) User Access Management

Primární stránka: https://confluence-agile.oskarmobil.cz/pages/viewpage.action?pageId=254764081

Hlavička last modified 5. června 2026. Přímo čtené AB Summary obsahuje prázdné zástupné hodnoty výsledku/schválení; Solution description obsahuje pouze šablonové instrukce. Tyto dvě záložky nedokládají schválení ani technický kontrakt. Ostatní záložky a přílohy při tomto kroku nebyly přečteny; závěr se na ně nevztahuje.
