# Konkrétní pokračování práce Atlas / ServiceHub

Toto je aktuální prováděcí předání. Určuje následující práci; časové zápisy ve STATE_2026-11-05.md slouží jako historie a evidence. Starší pokyny vytvářet audit, považovat lokální 14listý Book1 za aktuální nebo importovat do připojeného EA jsou překonané.

## Než začne nová instance

Připrav si checkout sám, nepřenášej tuto práci na uživatele. Pokud nemáš vlastní připravenou GitHub autorizaci pro zápis, vygeneruj vyhrazený SSH klíč bez přepsání existujících klíčů; veřejný klíč dej uživateli k autorizaci a soukromý uchovej pouze lokálně. Po autorizaci ověř přístup. Veřejné čtení repozitáře funguje bez klíče; nepotvrzuje zápis. Nespouštěj další agenty na základě otázky či připomínky uživatele. Pokračuj úsporně od doložených výsledků, neopakuj hotové kroky a neoznačuj návrhy nebo rozpracované změny za hotové.

EA prohlížej/exportuj výhradně v `Zdeněk Šerý sandbox / 01_07_2026_ServiceHub_Atlas_CZ_PR25_0837` a podsložkách, ostatní obsah repository není v rozsahu. Zdrojové EA pouze čti. Confluence je v browseru VDI; pokud vyžaduje login, požádej uživatele o ruční přihlášení. Dostupnost konektoru není podmínkou použití browseru.

## Co má agent dodat

Dokončený plný Solution Overview odpovídající potvrzenému MVP a navazující pracovní modelové podklady se zachovanými EA GUID. Zachovat správnou práci Copilota v aktuálním Book1. Připojené EA repository DEV-MODEL-MAIN zůstává beze změn: uživatel dovolil pouze čtení a export. Modelové změny připravovat pouze odděleně od zdrojového repository, v povolených pracovních souborech. Samostatný audit není požadovaný výstup.

## 1. Navázat na aktuální relaci a ověřit export

Aktualizace po skutečném spuštění dalšího agenta: VDI již odemčené; export přímo ověřen jako dokončený, ATLASLIVE.xml 19,0 MB, modified 5.11.2026 18:59. Tento krok znovu neprovádět; zbývá povolený přenos a hash/export v GitHubu. Podrobnosti ve STATE.

- Poslední pozorování VDI: zamčené Windows. Nejprve znovu pozorovat stav. Pokud zůstává zamčené, požádat o ruční odemčení; neautomatizovat přihlášení. Mezitím lze pracovat s uloženými podklady.
- EA už je dostupné, znovu nevyžadovat jeho instalaci nebo cestu. Projekt: Zdeněk Šerý sandbox / 01_07_2026_ServiceHub_Atlas_CZ_PR25_0837.
- Byl spuštěn export celého tohoto balíku do OneDrive Documents/Projects/ServiceHub/AI/ATLASLIVE.xml, formát XMI 2.1. Dokončení nebylo pozorováno. Ověřit dokončení v dialogu EA, existenci a nenulovou velikost souboru. Při chybě opakovat do nového názvu, nepřepisovat existující soubor.
- Žádný import, ukládání modelových změn, úprava elementů, vazeb, diagramů nebo mazání v tomto repository. Business procesy jsou jen orientační; aplikační vrstva a UML entity nedokončené, přibližně správné.
- Je-li dostupný povolený běžný přenos souboru, získat export pro práci a uložit jeho hash. Neobcházet omezení schránky nebo přenosu z VDI. Pokud přenos není dostupný, pokračovat čtením v EA a prací na SO; přesně uvést omezení.

Výsledek kroku: potvrzený aktuální export nebo konkrétní chyba, žádná změna zdrojového modelu.

## 2. Dokončit skutečný plný SO

Aktualizace po pokračování agenta: AuthX podtržítka a scopes doplněné a přímo ověřené v IF01/SREQ-ID-10, Done a Saved. Plný SO nyní 9983 slov, web35stran. Neopakovat stejné doplnění; pokračovat zbývajícími kapitolami a získáním souboru pro původní renderer. Starší počet níže je historie.

- Otevřít Documents/Projects/ServiceHub/AI/Solution_Overview_ServiceHub_Revised_MVP_2026-11-04.docx. Poslední ověřený stav: Saved, 34 stran, 9897 slov. WordWeb Copilot provedl 151 editací a desktop Copilot dalších 11. Počet změn není důkaz správnosti celého dokumentu.
- Přes Word Copilot provést cílenou kontrolu zbývajících rozporů a konkrétní opravy přímo v této pracovní kopii. Nevytvářet další auditní zprávu. Výsledek číst a ověřit v konkrétních kapitolách, neuzavírat práci pouze podle odpovědi Copilota.
- Sjednotit scope, předpoklady, rozhodnutí, funkční návrh, komponenty, rozhraní, identity/autorizaci, onboarding, otevřené body a odkazy na diagramy podle níže uvedených závazných faktů. Staré schválení původního SO neprezentovat jako schválení nové revize. Historické obrázky označit jako historické, pokud neodpovídají MVP; neprohlašovat je za aktualizované.
- Zapracovat přesné doložené AuthX parametry z outputs/EA_SO_2026-11-05/Confluence_AuthX_overeni_2026-11-05.md a primární Confluence stránky. Ověřit, zda je již Copilot zapracoval; nevkládat duplicitně.
- Technické mezery SNOW/Atlas klientského kontraktu dohledat přes Confluence nebo Teams agenta Confluence. Vyžadovat primární URL a verzi/datum. SnowConnector PR25_0749 není automaticky kontrakt Atlas PR25_0837. Nedoložené body ponechat konkrétně otevřené; nevymýšlet payload, role nebo deployment.
- Aktualizovat obsah dokumentu po dokončení editací. Neměnit bezpečnost, oprávnění ani ochranu dokumentu.
- Plný DOCX získat povoleným přenosem, spustit původní render_docx.py a vizuálně projít všechny stránky; opravit skutečné vady a render zopakovat jen po změnách. Word nesmí nahrazovat renderer. Na tomto PC LibreOffice již funguje, návod je v uložené reprodukci; neinstalovat znovu bez potřeby.

Výsledek kroku: plný obsahově a vizuálně ověřený SO, nikoli jen čtyřstránkový dodatek. Pokud bezpečný přenos chybí, uvést, že render plného SO dosud neproběhl.

## 3. Dokončit návaznost požadavků a modelové pracovní soubory

- Vycházet ze závazného Board MVP a nejnovějších UC Martina Dostála, poté aktuálních FREQ/SREQ a skutečného exportu EA. Business procesy nepoužívat jako normativní zdroj.
- V aktuálním modelu číst relevantní aplikační prvky, rozhraní, UML entity a SSO/kontextové diagramy. Porovnat s odpovídajícími UC a odpovědnostmi aplikací; zachovat původní GUID, texty a historii. Samotná existence prvku/vazby není důkaz správnosti.
- Existující pracovní Atlas_MVP_SO_2026-11-05.7z obsahuje pouze osm změněných dokumentačních polí a doplnění AuthX AD-02, XML SHA-256 a91f329d7b9358e791a679870292d60e2d054a6802017c29ca722b54c9b7b278. Není to dokončený strukturální model ani ověřený nativní import. Před dalšími změnami porovnat základ s novým živým exportem; starý soubor nepoužít k přepsání novější práce.
- Potřebné doložené modelové změny připravit v oddělené pracovní kopii/exportu, s přesně identifikovanými původními GUID. Do otevřeného repository je neaplikovat. Pokud nelze bezpečně ověřit nativní strukturu/diagramy bez zásahu do zdroje, ponechat tento konkrétní výstup jako neověřený a uvést potřebný další krok; neoznačit model za hotový.
- Starší balíky Atlas_UC_review a Atlas_UC_AuthX_review obsahují nepožadovanou analytickou review vrstvu. Nejsou finální model, nerozšiřovat je a neimportovat je do repository.

## 4. Zachovat a cíleně uzavřít Book1

- Aktuální zdroj je Documents/Projects/ServiceHub/Atlas/Book1.xlsx po práci Copilota. Pracovní kopie je Documents/Projects/ServiceHub/AI/Book1.xlsx. Starší lokální 14listý XLSX není aktuální baseline; nesmí přepsat současný sešit.
- Zachovat již správné CRM-04 ↔ IAM-25 a CRM-03 ↔ IAM-24 i rozdělení odpovědností ID-07. V AI kopii jsou ověřené D109 = CONFLICT ALLOW/DENY a H109 vysvětlení C109 allow vs J109 deny. To není rozhodnutý role kontrakt; výsledek nesmí zvolit allow/deny odhadem.
- Opravovat pouze konkrétní prokázané rozpory v povolené AI kopii, přes Copilot a s ověřením výsledných buněk. Neprovádět znovu plošný audit. Existující nepožadovaný auditní list nerozšiřovat; nic nemazat.

## Závazné obsahové body

- Standalone ServiceHub s vlastní URL, VFID autentizací a lokální autorizací přes VFCZ DXL.
- ONSC/WSC navigace, handover a obousměrné předávání zákaznického kontextu mimo MVP. Upstream vztahy/role dostupné přes DXL tím nejsou vyloučené.
- V4 SNOW customer/admin onboarding manuální v MVP. Automatický Siebel retrieval/prefill/population není potvrzený MVP; datová připravenost zůstává potřebná.
- VFID sub ↔ příslušný ONSC/WSC USER vždy 1:1; email není klíč. Více dostupných CRM kontextů je samostatný vztah.
- UC005: jediný dostupný CRM kontext automaticky vybrat, přepínání mezi dostupnými kontexty; prioritu více kontextů nevymýšlet. Ztracený kontext odstranit z výběru/obnovit nabídku.
- Chybějící požadovaná role nebo kontext znamená obecný obsah, nikoli plošný zákaz vstupu. Marketplace managed subscriptions a ticket prerequisites rozlišovat.
- AuthX token exchange a TMF691 CRM_ID oddělit od TMF629 customer name. Příklad expirace ve specifikaci není produkční SLA ani schválená konfigurace Atlas.

## 5. Uložit a předat skutečné výsledky

- Po každém věcném milníku uložit změněné pracovní soubory, zdroje, reprodukci, projektový skill a přesný další krok na větev codex/atlas-stav-2026-11-01; ověřit remote SHA. Main neměnit. Nepřenášet klíče/cookies/relace.
- Současný živý export ATLASLIVE.xml a plný aktualizovaný SO zatím nejsou potvrzeně uložené v GitHubu. Nezaměňovat uložení tohoto předání za uložení těchto dvou souborů. Získat a uložit je povolenou cestou, jakmile jsou dostupné.
- Finální předání musí obsahovat odkazy na skutečný plný SO a modelové pracovní soubory, provedené ověření a jen zbývající konkrétní otevřené rozhodnutí/omezení. Dokončení nelze tvrdit na základě samotného zadání Copilotu, změnových kapitol nebo zahájeného exportu.

Podrobnější evidence: STATE_2026-11-05.md. Trvalá pravidla: instructions/skills/follow-explicit-scope/SKILL.md. Starší stav číst cíleně podle potřeby, neopakovat celou již provedenou práci.
