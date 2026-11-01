# Výsledek Confluence agenta – načteno 1. 11. 2026

Celá zobrazená odpověď byla přečtena. Jde o sekundární výsledek agenta nad exporty Confluence DOCX (UniversalSearch), nikoli přímou kontrolu aktuálních stránek. VDI pouze čtením.

## Co agent našel

- ServiceNow Drop 2, PR25_0749, verze 2, uvedená úprava 13. 8. 2026. Agent cituje poskytování customer users a rolí do ServiceHub přes DXL TMF691, synchronizaci V2 rolí ONSC IMR → DXL a rozhodnutí AD01. To podporuje rozlišení datových vazeb/rolí od portálové navigace. Přímý zdroj nebyl v této kontrole otevřen.
- IDaaS, verze 2, 23. 10. 2025: použití V4/WSC/MVA i V2/ONSC a SSO ONSC. Není to důkaz aktuálního MVP scope Atlas.
- VFID 01.08 MVA12 ↔ WSC WebView, verze 3, 23. 5. 2025: předání identity, rolí a zákaznického kontextu, token exchange přes DXL/AuthX. Agent sám přiznává, že stránka neobsahuje Atlas. Tento vzor nelze přenést jako potvrzené rozhraní Atlas.
- TMF629 Customer Management: vyhledání přes Siebel CA nebo MS CRM ID a zákazníci dostupní podle userAssets. Přiřazení ke Customer Selector je závěr agenta, nikoli doložená implementace aktuálního UC005.
- Marketplace Microsoft licences: WSC → GraphQL → DXL → Vodafone Group DXL → Marketplace/AppDirect; nákupní cesta ve WSC. Tato starší marketplace cesta sama nedokazuje standalone přístupový model Atlas; závěr agenta o jeho podpoře je příliš silný.

## Co agent nenašel / omezení

- Přímou projektovou stránku PR25_0837, říjnový BRD, Use Case Specification a Requirements.xlsx.
- Přímé dokumenty, komentáře ani rozhodnutí Martina Dostála.
- Přímou specifikaci Customer Selector ani Atlas eligibility pravidla.
- Pozdější říjnové rozhodnutí měnící model; nejpozdější uváděný relevantní AD01 je ze srpna 2026.
- Některé vnořené SharePoint/Jira/Confluence odkazy neotevřel. Nenalezení v indexu není důkaz neexistence.

## Použití pro další analýzu

Uchovat jako seznam zdrojů k ověření pro role, identity a API. Nepřebírat finální tabulku aplikací agenta jako ověřený model: směšuje aplikace, rozhraní/API a architektonické vrstvy (např. DXL TMF691). Neodvozovat z ní nové fyzické komponenty ani SREQ. Současný MVP scope nadále opírat o přímo přečtený říjnový BRD/UC a odděleně dohledané projektové rozhodnutí.

Čekáme na další informace uživatele; nebyly zadány další dotazy ani změněna data ve VDI.
