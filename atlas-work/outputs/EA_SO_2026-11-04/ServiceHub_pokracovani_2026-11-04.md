# ServiceHub pokračování revize 4. listopadu 2026

## Provedená modelová revize

Vznikla samostatná pracovní kopie Atlas.xml v archivu Atlas_MVP_review_2026-11-04.7z. Původní Atlas.7z a aktuální OneDrive Book1 nebyly přepsány. Změněno osm properties.documentation polí:

| Prvek | Provedená změna |
|---|---|
| AD-02 | K původní autentizační podmínce doplněn primárně ověřený návrh SH BFF → APIX → AuthX → IDaaS introspection → DXL token a meze jeho průkaznosti. |
| AD-05 | Historické povinné ONSC/WSC vstupy nahrazeny aktuálním standalone MVP; upstream role data zůstávají oddělená od navigace. |
| AD-07 | Automatický lifecycle přestal být popsaným MVP baseline; současný V4 onboarding je manuální, budoucí varianty zůstávají budoucími. |
| AD-08 | Zachován historický performance text, doplněna explicitní kvalifikace, že nejde o naměřené SLO nebo schválené vyřazení V2. |
| ASS-03 | Oddělena user identita 1:1, více oprávněných customer kontextů a cílová holding relace; přidána UC005 automatická volba a přepínání dostupného kontextu. |
| ASS-06 | Opravené tvrzení, že direct URL není standalone access model. |
| ASS-07 | Rozlišeny podmínky UC005, UC006 a ticket operací; SNOW presence není plošná podmínka obecného obsahu. |
| SREQ-ID-07 | Původní Local DXL požadavek zachován doslova a doplněno upřesnění IDaaS claims / DXL data / SH eligibility podle aktuálního Book1. |

Kontrola: všechna XMI ID a IDREF zachována, konektory a diagramy bajtově totožné, mimo osm hodnot dokumentace jsou všechny bajty stejné. Výstupní XML SHA-256: fb0cfe908c40bf58928d5b8a837760bce19304d9293d1f331377183a268a21a6. Archiv prošel testem 7-Zip. Původní a nové texty a podklady jsou v Kontrola_EA_revize_2026-11-04.json a v archivu.

Toto je provedená dílčí revize dokumentace modelu. Nativní import do EA a vizuální kontrola jeho diagramů neproběhly; nebyly přidány nové vztahy ani aktualizovány všechny diagramové scénáře. Existující zdrojové texty jsou uchované v manifestu.

## Nově primárně ověřený tokenový návrh

Teams Copilotu byl zadán dotaz na schválené Atlas ServiceHub SNOW API a CZ DXL token negotiation kontrakty s primárními odkazy a daty. Následně byl přímo otevřen email RE: ServiceHub - DXL od Zdeňka Šerého, 15.10.2026 16:35.

Přímo přečteno: po získání IDaaS tokenu volá SH BFF DXL OAuth2 Token Exchange přes APIX a předá token jako subject_token. APIX routuje do AuthX. AuthX validuje token přes IDaaS /oidc/introspect a vytvoří DXL access token vracený do SH pro chráněná DXL API. Nonce/state z původního referenčního VFCZ diagramu se nesmí prezentovat jako existující chování SH ani nový DXL požadavek bez podkladu Group autentizačního návrhu.

Email dále výslovně říká: TMF691 vrací customer identifier CRM_ID, ne customer name. Pokud SH potřebuje customer name, získá jej pro odpovídající CRM_ID přes TMF629. Rozsah přidělených oprávnění a wire detaily tím nejsou doložené.

Copilot uvedl také potvrzení Pedra z 21.10. a sám výslovně uvedl, že nenalezl schválený verzovaný kontrakt konkrétního CZ token exchange endpointu. Email z 21.10. nebyl v tomto kroku přímo ověřen; nejde o nový approval. Endpoint URL, client auth, úplný grant/request/response, audience/scopes, expiry/refresh a chyby zůstávají otevřené.

## SNOW zdroje a jejich hranice

Z citace Copilotu byl otevřen primární PDF DXL-TMF621 Trouble Ticket API Specification SNOW Integration 250926 na SharePoint webu CZ-ServiceNow. Náhled uvádí 74 stran. Přímo čtený obsah rozlišuje case request, incident, service request a generic trouble tickets; část Accessing Vodafone APIs uvádí Mutual TLS a výměnu klientských certifikátů pro VBPS API. Nepřečtený zbytek 74 stran není označen za ověřený. Datum 25.9. a modification 27.10. pocházely ze souhrnu Copilotu a nebyly nezávisle ověřeny jako approval.

Samotný nalezený dokument ani PR25_0749 SnowConnector nejsou důkaz, že jde o definitivní Atlas SH–SNOW implementační kontrakt. Nepřebírat automaticky Remedy trasu, platformu SNOW EVE/GSNOW/CSD, payload identifikace nebo všechny aktualizační operace do Atlas diagramů.

## Aktuální Book1 a uzavřené staré nálezy

FREQ mapping!F4:F5 byl vybrán přes Go To a hodnoty ověřeny interním kopírováním pouze uvnitř VDI do neodeslaného Copilot konceptu. Pozorované hodnoty v pořadí: SREQ-CRM-04, SREQ-CRM-03. Koncept byl vymazán. Nedošlo ke kopírování schránky mimo VDI.

Tím je přímo potvrzena oprava staré záměny CRM-03/04: IAM-25 je hierarchy/CRM-04, IAM-24 separation/CRM-03. Starou navrženou opravu znovu neaplikovat. V aktuálním zobrazení F6:F7 nejsou vyplněná SREQ; historické CRM-09/10 hodnoty ve sloupcích před opravou se nesmějí vydávat za nynější vazby. Samotné zachování aplikačních CRM-09/10 schopností je od mapování FREQ oddělené.

Přímé ověření ID-07 a IF_CRM_02 navazuje na předchozí kontrolní zápis. Zdrojový Book1 se při této práci neměnil.

## Potvrzený zbývající rozpor řádku 109

Aktuální FREQ mapping!B109:J109 byl zpřístupněn přímo přes Go To. Zvolený rozsah byl zkopírován uvnitř VDI do Copilotu s požadavkem Review row 109. To je cílený read-only rozbor, nikoli Apply/Edit.

- B109: F-REQ-IAM-12.
- C109: Service Hub must allow access to V2 users with role End User Admin.
- D109: SHODA.
- F109: SREQ-SH-07.
- H109: tvrzení o obnoveném konzistentním atomickém mapování a neaplikování skupinových rozsahů jako kartézského součinu.
- J109: L4 - Deny access for V2 End User Admin [Functionalities!B521].

Existuje aktuální obsahový allow/deny rozpor, nikoli jen historický nález. Oprava párování řádků tento rozpor neuzavírá. Bez potvrzení business role rozhodnutí nepřepisovat deny na allow ani naopak. Připravená minimální analytická oprava: D109 má rozlišovat KONFLIKT ALLOW / DENY a H109 má výslovně uvést rozpor C109 vůči J109 a nutnost role rozhodnutí. Tato navržená úprava nebyla ve VDI provedena.

Dokončená odpověď Copilotu rozpor výslovně potvrdila a uvedla, že SHODA nemá oporu do vyřešení odlišné polarity. Připomněla také odlišný význam aktuálního SREQ-SH-07 (vyhodnocování přístupu k customer content), nepotvrzené přesné role mapping v UC005 a obecnou stránku pro neeligible uživatele místo úplného odepření portálu. Doporučila označení pro review, prověření vhodné allow/evaluate funkcionality a potvrzení role; pokud má být deny záměrné, musí se změnit FREQ wording. Tato doporučení nejsou novým approval ani provedenou úpravou workbooku.

## SO a zbývající dokončení

Obsah změnových kapitol SO je uložen samostatně v ServiceHub_SO_zmenove_kapitoly_2026-11-04.md. Obsahuje scope, odpovědnosti, ověřenou tokenovou sekvenci, System Impacts a podmínky uzavření otevřených bodů. Není úplnou editací původního SO dokumentu.

DOCX byl vytvořen jako pracovní mezikrok, ale render_docx.py selhal, protože na dostupné cestě není soffice.exe. Po kontrole runtime a troubleshootingu nebyl nalezen zabalený LibreOffice; vizuální QA neproběhlo. Neověřený DOCX zůstal ve work a není finálním výstupem.

Zbývá úplná obsahová kontrola všech aktuálních vazeb, role rozhodnutí, specifické schválené SNOW/token kontrakty, dokončení vztahů a scénářů EA, nativní EA import/diagram QA a zapracování do původního SO včetně Word QA. Tyto části nejsou označené za hotové.

## GitHub synchronizace

Po udělení síťového oprávnění bylo obnoveno spojení a použit existující repo-specific SSH wrapper s již připraveným klíčem a pinned known_hosts. Dílčí revize včetně archivu XML, manifestu, SO textu, tohoto záznamu a aktualizovaného předání je uložena ve větvi codex/atlas-stav-2026-11-01 repozitáře zsery/zsery. Po zápisu byly porovnány lokální HEAD a vzdálené SHA. Main nebyl změněn.
