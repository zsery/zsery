# Confluence Agent: SNOW kontrakt, 4. 11. 2026

Po cíleném hledání v Teams Copilotu s agentem Atlas nebyl vrácen aktuální schválený Atlas SNOW identity decision ani ticket kontrakt. Výsledek hledání není důkazem jejich neexistence. Následně byl přes nabídku `@` vybrán konkrétní **Confluence Agent** a vizuálně ověřen i odeslán dotaz `find servicehub snow ticket api and identity mapping primary urls and versions`.

## Sekundární technická vodítka

Agent uvádí SnowConnector Technical Design, version 158, modified 23.10.2026, a TaaZure APIM documentation, version 33, modified 15.10.2026. Uvádí TMF621 Trouble Ticket API mezi ServiceNow a SnowConnector a cestu `/events/v4/troubleTicket`, s dev App Gateway/APIM/NGINX URL. Tyto endpointy nebyly volány. Samotné v4 v cestě nenahrazuje ověření konkrétního schématu, směru operací ani verze standardu.

Pro identitu agent vrací TMF691 Federated Identity API, swagger `TMF691-FederatedIdentity-v4.0.0.swagger.json` a userInfo endpoint. To není důkaz specifického SNOW identity mappingu, Atlas SH/CZ DXL token negotiation ani schválení emailu jako identity klíče. VFID sub ↔ odpovídající ONSC/WSC user zůstává 1:1.

## Přímo otevřená citace

Citace SnowConnector otevřela WordWeb export v CZConfluenceContentPilot, název souboru `TIB-254750255`. Byl v režimu Viewing a explicitně otevřen Immersive Reader. Viditelný titul: **PR25_0749 - SNOW - DROP1 - SnowConnector - Technical Design**. Metadata obsahují Confluence PageId **254750255**, Confluence URL na doméně `confluence-agile.oskarmobil.cz` ve space TIB a modified `10/23/2026 19:02:43`. Export ukazoval jednu stranu/60 slov; samotné otevření tohoto exportu neznamená přečtení technického návrhu.

Přes skutečný vložený odkaz byla otevřena původní Confluence stránka. Browser se přesměroval na `login.action` s formulářem Username/Password. Přihlášení uživatelovým účtem není aktivní. Přihlašovací formulář nebyl ovládán. Uživatel byl požádán o ruční přihlášení a odpověď „přihlášeno“. Stránka byla ponechána otevřená. Přímý obsah návrhu ani aktuální verze stránky zatím nejsou ověřeny.

## Pokračování

Po ručním přihlášení nejprve znovu pozorovat okno a ověřit přístup ke stránce 254750255. Zaměřit se na skutečnou vazbu SH/SNOW, operace create/read/update, company/user scope, pole, stavová pravidla a identifikátory. PR25_0749 je jiný projekt než Atlas PR25_0837; obecný SnowConnector návrh nelze automaticky prohlásit za Atlas kontrakt. Dále dohledat explicitní rozhodnutí CZ+SNOW navazující na MVP Assessment z 2.11.

Při čekání byla mimo VDI obsahově posouzena celá sada 219 řádků FREQ mapping, viz [výsledky](UC_atomicke_podminky_2026-11-04/SREQ_vsechny_radky.md). Zdrojové dokumenty ve VDI tímto nebyly upraveny. Book1, EA a SO nejsou touto analýzou aktualizované.

## Osobní skill

Projektová kopie závazného skillu je na pracovní GitHub větvi a byla znovu přečtena. Osobní cesta `C:/Users/zsery2/.codex/skills/follow-explicit-scope/SKILL.md` při kontrole neexistovala. Po udělení cíleného filesystem oprávnění nový pokus o vytvoření adresáře skončil systémovým odmítnutím zápisu. Osobní instalace proto není vykazována jako hotová; není důvod žádat další GitHub klíč. Projektová pravidla se při práci nadále uplatňují.
