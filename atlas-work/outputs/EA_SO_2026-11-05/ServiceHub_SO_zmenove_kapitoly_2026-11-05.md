# ServiceHub Atlas CZ změnové kapitoly Solution Overview

Stav: změnové kapitoly pro zapracování do plného SO, nikoli náhrada celého dokumentu. DOCX byl vykreslen původním render_docx.py přes LibreOffice a všechny čtyři stránky byly vizuálně zkontrolované.

Změnové kapitoly Solution Overview

5. listopadu 2026 | Scope MVP a integrační odpovědnosti | Změnové kapitoly pro review

## Introducing

Aktuální MVP používá samostatný ServiceHub přes vlastní URL, autentizaci Vodafone ID a lokální autorizaci s VFCZ DXL. V4 customer a user/admin onboarding do SNOW probíhá interním manuálním postupem. Tato aktualizace sjednocuje rozsah, odpovědnosti a doloženou část tokenového toku pro revizi Solution Overview.

Závazným rozsahem je uživatelem určený dokument Atlas CZ Launch – Architecture Board Confirmation of Phased Implementation Approach. Aktuální Book1 slouží pro traceability a odlišení aplikační schopnosti od prokázané implementační změny. Existence funkce v katalogu ani absence detailu v UC sama neurčuje novou změnu nebo odstranění schopnosti.

## Architecture and Solution Description

| Součást | Odpovědnost v návrhu |
| --- | --- |
| Vodafone Identity a IDaaS | Autentizace a identity claims. Nerozhoduje samo o přístupu k zákaznickému obsahu SH. |
| ServiceHub a BFF | Zahájí vyjednání lokálního DXL tokenu, získá oprávněné kontexty, zvolí dostupné CRM ID a řídí zobrazení a přepínání kontextu. |
| VFCZ DXL | Zpřístupní autorizované upstream vztahy, role a customer údaje. Oddělit identity data, customer data a tokenový kontrakt. |
| Marketplace | Zdroj relevantních produktových a subscription dat. SH nese odpovědnost za Atlas filtraci a zobrazení. |
| SNOW a provozní cesta | Ticket doména a manuální V4 onboarding podle vymezeného MVP. Přesná platforma a rozhraní musí odpovídat potvrzenému kontraktu. |

Mimo MVP zůstává ONSC/WSC navigační integrace, bidirectional customer-context propagation a automatizovaný V4 onboarding do SNOW. Upstream ONSC/WSC role a vztahy přes DXL zůstávají použitelné i bez portálové navigace. Group dodávka sama neznamená nový vývoj VFCZ.

## Functional Design

### Autentizace a vyjednání DXL tokenu

Primární email RE: ServiceHub - DXL ze dne 15. října 2026 popisuje následující návrh. Jde o doložený integrační směr; email nenahrazuje verzovaný wire kontrakt ani důkaz nasazení.

Uživatel se autentizuje přes Vodafone Identity a ServiceHub BFF získá IDaaS access token.

SH BFF volá DXL OAuth2 Token Exchange endpoint přes APIX a předá IDaaS access token jako subject_token.

APIX předá požadavek do AuthX. AuthX validuje IDaaS token vůči IDaaS /oidc/introspect.

AuthX vytvoří DXL access token a vrátí jej ServiceHubu. SH jej použije pro další volání chráněných DXL API.

Pro UserInfo je v přečtené specifikaci TMF691 doložena hlavička Authorization: Bearer a scope TMF691_FEDERATED_IDENTITY_ALL. Přidělení konkrétnímu Atlas klientovi se musí ověřit samostatně.

Confluence TS – AuthX – authx-ts, část 3.2.1, primárně přečtená 5. listopadu 2026 (stránka naposledy změněna 4. června 2026), potvrzuje POST /OAuth2TokenExchangeGrant/v2/token. Pro volání přes APIX musí API key mít scopes OAUTH2_TOKEN_EXCHANGE_GRANT a TMF691_FEDERATED_IDENTITY_ALL. Request používá Accept: application/json a Content-Type: application/x-www-form-urlencoded; grant_type=urn:ietf:params:oauth:grant-type:token-exchange a subject_token_type=urn:vodafone:params:oauth:token-type:vodafone_id. Vedle subject_token je povinný subject_token_iss určující prostředí VFID, které token vydalo. Jde o platformní kontrakt, nikoli potvrzení konkrétní konfigurace Atlas klienta.

Odpověď zahrnuje DXL access token a TMF691-kompatibilní user_info s oprávněnými assets. Ty jsou také vložené v tokenu; token opravňuje pouze k assets uvedeným v odpovědi. Příklad uvádí Bearer a pole expirace/refresh, neprokazuje pevné produkční životnosti ani přidělení oprávnění SH. URL prostředí, konfigurace klienta, úplný security/error kontrakt a skutečné nasazení Atlas zůstávají k ověření. Nonce/state z referenčního diagramu není tímto potvrzeno jako existující chování SH.

Primární technický zdroj: https://confluence-agile.oskarmobil.cz/display/DCP/TS+-+AuthX+-+authx-ts, část 3.2.1.

### Identita a zákaznický kontext

VFID sub odpovídá právě jednomu příslušnému ONSC/WSC userovi. Email je atribut a neslouží jako stabilní párovací klíč. Jeden uživatel může mít více oprávněných customer kontextů; to je jiný vztah než user identity a cílová TMF691 holding parent–child relace.

UC005 vyžaduje automatickou volbu jednoho dostupného CRM ID a následné přepínání mezi dostupnými kontexty. Priorita počáteční volby není doložená. Chybějící role nebo CRM ID vede k obecnému obsahu; ztráta aktuálního CRM ID vyžaduje obnovu selectoru bez přepnutí na nedostupný kontext.

Email z 15. října výslovně rozlišuje customer identifier z TMF691 a customer name získávaný přes TMF629. Není tím doloženo oprávnění libovolného klienta k jakémukoli customer lookupu. V2 se v přečtené TMF691 specifikaci žádá explicitně a má omezený root-level rozsah.

## System Impacts

Aktuální Book1 ponechává původní CRM schopnosti a označuje neověřenou AS-IS deltu. Revize proto rozlišuje požadovaný výsledek, jeho aplikačního vlastníka a doloženou změnu implementace.

| Oblast | Doložená hranice | Co nelze převzít automaticky |
| --- | --- | --- |
| CRM a Siebel | CRM-03 poskytuje separation data; CRM-04 hierarchy a vztahy. Aktuální list rolí je váže k IAM-24 a IAM-25. | Nový CRM vývoj, přesný holding payload nebo plnou realizaci chování SH jednou datovou službou. |
| IDaaS a DXL | Book1 F166 rozlišuje IDaaS claims, DXL retrieval vztahů/rolí/CRM ID a SH content eligibility. | Vlastnictví všech eligibility rozhodnutí IDaaS podle historického názvu Determine Access Eligibility. |
| Marketplace | Potřebná data readiness a Atlas produktová/subscription data. | Automatický Siebel retrieval/prefill/population nebo zaměnění order acceptance za aktivaci. |
| SH a SNOW | UC vymezují logické ticket operace. Aktuální Interfaces rozlišuje logickou hranici a nepotvrzenou technickou realizaci. | Že Local DXL/TMF621, SNOW EVE, GSNOW a CSD označují jedinou potvrzenou implementační trasu. |
| ONSC a WSC | Upstream role a customer vztahy jsou oddělené od navigace. | Handover, návratovou URL nebo bidirectional propagaci jako současné MVP. |

### Technické rozhraní SNOW

Copilot dohledal DXL-TMF621 Trouble Ticket API Specification SNOW Integration 250926. Otevřený primární PDF má 74 stran. Ověřený obsah rozlišuje case request, incident, service request a obecné trouble tickets; kapitola Accessing Vodafone APIs popisuje Mutual TLS a klientské certifikáty pro VBPS API. Tato část sama nepotvrzuje použití dokumentu pro ServiceHub Atlas ani vyřešení identity/company scope.

Samostatný SnowConnector návrh PR25_0749 popisuje middleware, provisioning a ticket integraci se systémy Foris, V2DB a Remedy. Bez dalšího dokladu není Atlas PR25_0837 kontraktem. Nově nalezené technické podklady se musí přiřadit ke skutečnému směru volání a platformě před doplněním sekvencí a polí.

## Other Requirements

Datové kontrakty musí rozlišovat VFID sub, lokální user ID, platformu V2/V4, Siebel CA, V2 MSCRM GUID, BA/wallet a Marketplace company UUID. Názvy CRM ID nebo customer samy neopravňují tyto identifikátory sloučit. Konkrétní cleansing a reconciliation postup, žádný/více matchů a řešení existujících nesouhlasících vazeb zůstávají samostatnou součástí návrhu.

Základní pracovní XML revize mění osm dokumentačních polí AD-02, AD-05, AD-07, AD-08, ASS-03, ASS-06, ASS-07 a SREQ-ID-07. Navazující oddělená review vrstva přidává 30 analytických Artifact uzlů, 65 candidate trace vazeb a sedm review diagramů. Původní GUIDy, texty, konektory a diagramy zůstávají zachované; původní a nové znění dokumentace je v manifestu. Candidate trace není realization ani schválení požadavku. Nativní import a vizuální QA v EA dosud nejsou potvrzené.

## Open Points

| Bod | Podmínka uzavření |
| --- | --- |
| DXL token exchange | Platformní endpoint, grant a povinné parametry jsou doložené v Confluence 3.2.1. Potvrdit konkrétní SH klient, URL prostředí, client auth, přidělená oprávnění, životnosti a error/refresh chování. |
| SNOW ticket integrace | Ověřit platformu a trasu, create/read/update operace, required fields, user/company identifikaci, status transitions a oprávnění. |
| Role a holding | Potvrdit Atlas eligible role enum a holding parent–child payload. AI kopie Book1 ř.109 už označuje allow/deny konflikt; oprava klasifikace nenahrazuje business rozhodnutí o roli. |
| Traceability a model | Dokončit křížovou kontrolu FREQ mapping, funkcí a původních EA konektorů. Ověřit XML import a vizuální podobu dotčených diagramů. |
| V4 provozní proces | Doložit provozní vlastnictví, přesný manuální postup a relevantní privacy/security podmínky. Neoznačovat budoucí automatizaci za hotové MVP. |

### Podklady pro změnu

Závazný Board scope určený uživatelem; přímé čtení UC a DXL specifikací zaznamenané 3.–4. listopadu; aktuální OneDrive Book1 ze 4. listopadu, zejména SREQ Aplikační role F166 a Interfaces H4 až K7 a A22; primární email RE: ServiceHub - DXL, Zdeněk Šerý, 15. října 2026 16:35. Nalezená TMF621 specifikace je ověřena pouze ve výše uvedeném rozsahu. Schválení jejího použití pro Atlas není doloženo.
