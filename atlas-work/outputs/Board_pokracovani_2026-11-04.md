# Pokračování čtení Board scope, 4. 11. 2026

Aktuálně ověřeno otevřené VDI okno AOProd W11. Edge zobrazuje OneDrive SharePoint Immersive Reader; textový nadpis „Prezentace pro Architecture Board“, „Atlas – Project Scope“. Celý název souboru a verze nebyly na této obrazovce znovu ověřeny; předání tento reader identifikuje jako závazný Board dokument. Níže jsou přímo přečtené části, nikoli nové schválení verze dokumentu. Zdrojová data nebyla upravena.

Viditelný úvod uvádí páteční dohodu Františka Kožíška a Alexandry Staňkové a Variantu 2 jako MVP, nikoli rozdělení projektu do dropů.

In scope: ServiceHub standalone portál přes dedicated URL; Atlas pro cílový segment V4; interní manuální onboarding V4 zákazníků/uživatelů do SNOW. CustomerSelector pro V2 i V4: Group dodávka funkčnosti V2 s více CA; lokálně se definuje jednodušší RBAC a jeho test scénáře. ServiceHub support flow směrem k SNOW má dodávku Group a projektu SNOW. Autentizace přes Vodafone ID, lokální autorizace ServiceHub → VFCZ DXL. Další odrážka pouze obecně uvádí IVR a CZ Business portal; nepřidává detailní kontrakt.

Out of scope: ONSC/WSC ↔ ServiceHub integration, včetně CustomerContext propagation z ONSC/WSC do ServiceHubu a bidirectional integration. Automatizovaný onboarding V4 zákazníků/uživatelů do SNOW. Další managed services a budoucí ServiceHub enhancements.

Dopad: právě přečtený text podporuje dosavadní oddělení standalone MVP, manuálního V4 onboardingu a Group CustomerSelector dependency. Není podkladem k vymyšlení DXL token kontraktu, holding payloadu ani konkrétní Atlas role eligibility. Zákaz portálové integrace nevyvrací upstream ONSC/WSC role vstupy přes DXL.

Poslední čitelný bod: nadpis Rizika. Následující obsah rizik nebyl v tomto kroku přečten. Vložené diagramy a úplný dokument nejsou tímto ověřeny. Copilot nebyl v tomto krátkém pokračování použit; před rozsáhlým dalším průzkumem ověřit dostupný Teams Copilot a Confluence Agent dle pokynů. Book1, EA a SO tento krok nemění.

Dřívější timeout nástroje je historický výsledek předchozího pokusu. Není důkazem, že VDI není otevřené nebo dostupné nyní. Aktuální snímky a přepnutí na Edge úspěšně proběhly.
