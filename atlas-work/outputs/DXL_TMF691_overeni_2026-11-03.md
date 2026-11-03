# DXL TMF691 – přímé čtení technického zdroje, 3.11.2026

Zdroj ve VDI: `Atlas Programme / 2. Portfolio / Atlas Expansion - Czech / Interlock-Pack / CZ local folder / Architecture / DXL / 29.10.2026 / FS - TMF691 Federated Identity API - federated-identity-fs` (Word). Knihovna uváděla modified před pěti dny, Simona Plevová; export dokumentu 29.10.2026 10:55:13. Viditelná revizní historie únor–duben 2025, autor Ondřej Šebelík, obsahuje doplnění V2, Cache-Control a V4-only GET variant. Datum exportu není schválení nové Atlas implementace.

Dokument otevřen výhradně SharePoint Open → Open in Immersive Reader. Čtecí text prošel od titulku přes všechny kapitoly do posledního odstavce Vodafone Support. Po přepnutí readeru na plnou obrazovku zmizela překryvná karta; příslušný technický text byl čitelný. Změněny jen preference čtecího zobrazení (velikost, spacing, source formatting), nikoli dokument. Vložené obrázky/diagramy reader nepředává, některé očíslované kroky jsou prázdné. Žádná API operace nebyla spuštěna. Následující je shrnutí a dopad pro Atlas, nikoli úplná kopie specifikace.

## Kontrakt doložený dokumentem

| Oblast | Pozorovaný kontrakt |
|---|---|
| Current user | `GET /userInfo`; výchozí varianta vrací V4 assets. `GET /userInfo?userAssets[].assetCategory=MassMarket,Enterprise` požaduje V4 i V2. Samotné MassMarket je V4. |
| Autorizace current user | End-user DXL access token v `Authorization: Bearer …`, scope `TMF691_FEDERATED_IDENTITY_ALL`. Chybějící token → 401; identita nenalezena → 404. Odpověď popsaná jako kolekce UserInfo s jedním aktuálním uživatelem. |
| Rozpor v textu requestu | Current-user část zároveň obsahuje obecné „no query filters/field selection“, přesto výše explicitně vypisuje assetCategory varianty. Před finálním SH kontraktem potvrdit podporované parametry se správcem API; neodstranit V2 parametr jen podle této obecné věty. |
| Stagingref | Reference uvádí `https://eu2.api.vodafone.com/tmf-api/federatedIdentity/v4/userInfo` jako APIX URL (Stagingref). Není tím ověřena produkční base URL, konkrétní SH klient ani jeho přidělené scopes. |
| Flat mode | Volitelný `mode=flat` jen u označených queries; normal mode expanduje spravovatelný strom, flat vrací pouze rootmost asset pro každou roli. Specifikace doporučuje flat při potřebě jen root assets kvůli výkonu; nejde o potvrzení zvolené Atlas varianty. |
| V2 omezení | TMF691 master pouze V4 assets, pro V2 slave ONSC/IMR. V2 se žádá explicitně; vrací pouze root-level assets, flat parametr je pro V2 ignorován. Southbound plný strom podle dokumentu nepodporuje kvůli výkonu ONSC. Změny V2 rolí provádí ONSC, ne TMF691 write API. Budoucí plná správa V2 je cílový stav dokumentu, ne doložená dnešní implementace. |
| By sub | `GET /userInfo/{sub}`, stejné V4/V2 varianty. Sub odpovídá incoming token sub nebo `isTrustedClient()`. Nenalezení → 404. |
| Email/phone lookup | Trusted-client operace se stejným scope, vrací kolekci shod nebo prázdnou kolekci. Email lookup není stabilní párovací identita. Volitelný `Cache-Control: only-if-cached` pro tyto lookup scénáře; nevyvozovat z něj obecné vynechání validace current-user tokenu. |
| Lookup asset/role | Trusted-client filtr entity/id/role, více filtrů se kombinuje OR. Není totožný s current-user oprávněním. |
| User assets endpoint | `GET /userInfo/{sub}/userAssets` vrací interní rootmost assets, nikoli automaticky plný expandovaný strom; V4 default / V4+V2 explicitní varianta. |
| Write katalog | POST identity, PATCH identity, DELETE identity a JSON Patch userAssets jsou interní trusted-client operace. Nejsou tím přidělené ServiceHubu ani schválené pro automatický V4 onboarding. PATCH identity s userAssets nahrazuje celé pole; dílčí změny mají samostatný userAssets endpoint. Pouze přečteno. |

## Identita a role – význam pro doménový / integrační model

- `sub` a také mapované `id` pocházejí z VFID/IDaaS `sub`. Email, phone a locale jsou atributy z IDaaS, ne náhrada identity. Výslovné pravidlo uživatele VFID sub ↔ odpovídající ONSC/WSC **user** vždy 1:1 zůstává platné.
- Interní MongoDB User/authorization-entitlement model není totožný s expandovanou externí UserInfo odpovědí. Interně se ukládá rootmost asset daného oprávnění; external mapping může doplnit jeho strom a relatedAssets.
- V4/MassMarket: owner na CA (`entityType=customer`), admin na BA (`entityType=account`, `assetType=billingAccount`), user na service/product. Owner má CA scope; BA admin automaticky nezískává CA nebo ostatní BA; service user automaticky nezískává ostatní služby. Role není společná vlastnost zákazníka bez rozsahu.
- V2/Enterprise je odlišný a konfigurovatelný model: end user, end user admin (EUA), group level admin (GLA), association level admin (ALA). Podobné názvy V2/V4 nejsou důkaz stejné sémantiky. V2 adapter mapuje customer id, wallet id, ISDN group id a service number; neslučovat je jediným netypovaným „CRM ID“.
- V2 `vodafone support` a neznámé role se v mapovací tabulce ignorují. Poslední odstavec uvádí, že interní Vodafone Support role se v DXL neimplementuje tímto způsobem, interní uživatelé mají jiný přístup přes AD federation. Nevytvářet z ní veřejné SH oprávnění.
- V4 mapping: product relatedAssets obsahuje vlastnící CA i BA, account relatedAssets obsahuje vlastnící CA, customer jej nemá. Dokument používá v různých částech `relatedAsset` a `relatedAssets`; přesný wire schema potvrdit z verzovaného kontraktu, nenormalizovat názvy odhadem.
- V2 association představuje skupinu více firem/zákazníků podobnou holdingu. Tato exportovaná specifikace uvádí Association a Group jako „not currently represented in DXL“, přesto V2 mapovací tabulka obsahuje ISDN group. Jde o omezení/nesoulad dokumentace, nikoli důvod zahodit výslovný cílový požadavek uživatele **TMF691 holding parent–child**. Konkrétní payload tohoto rozšíření není doložen; oddělit AS-IS dokument od cílového Atlas stavu.
- Group ID Gateway projection je další datový kontrakt: lokální UserInfo se přemapuje do Group extended userinfo. `user_account_id` je v CZ mappingu unused; to nevyvrací user identitu 1:1. CA/BA/role a Group subscription/account atributy nemají být směšovány.

## Proces current-user a SSO

Specifikace popisuje: klient předá platný DXL access token; TMF691 z něj rozbalí původní IDaaS access token a zavolá IDaaS `/userinfo`. Odmítnutí IDaaS tokenu odmítne i request. `sub` z ověřených IDaaS claims se použije pro entitlement lookup. Podle asset typu se získávají CA, BA a product údaje z příslušných business API. Dokument dále uvádí cache identity claims, ale pro jednoduché current-user volání vždy čerstvé získání z IDaaS k ověření tokenu. Přesná token serializace/JWT tím není potvrzena.

V2 explicitní větev nejprve volá `DXLAdapter.GetIdaasIdentityStatus` v IMR přes ONSC TIBCO. Stav se krátce cachuje; při `idaasIdentityStatus == 1` následuje `DXLAdapter.GetIdaasIdentity`, V2 assets se cachují v MongoDB a mapují do TMF struktury. Dokument nestanoví přesné krátké TTL či Atlas performance SLO.

Sekce ID Gateway popisuje historický/dočasný mechanismus OAuth2TokenExchange s LM DXL a následné parsování UserInfo pro Group služby, například OneNumber/PPE. Odkazuje na Confluence `CZ subscriptions mapping`. **Není to samo o sobě detailní schválení stejného flow pro Atlas ServiceHub.** Uživatelem zadané specifické vyjednání SH/CZ DXL tokenu zůstává potřebné; jeho endpoint, request, client auth, refresh/expiry a Atlas scopes tím nebyly ověřeny.

## Lifecycle a aktuálnost

Dokument popisuje background asset expiration a user removal jobs. Pro BA se uplatňuje inactiveDate a šestiměsíční interval, pro customer typ/status a existenci, pro product existenci. Procesní část na jiném místě popisuje archivaci/odstranění po šesti měsících při nenalezení; job část popisuje odstranění nenalezeného assetu. Tento rozdíl neuzavírat odhadem. Nejde o ověřený SNOW V4 lifecycle ani o potvrzení nasazení těchto jobů pro Atlas.

## Konkrétní dopad na další práci

1. DXL sekvence může nově uvést doloženou hlavičku a UserInfo token-validaci, odděleně od dosud neověřeného vyjednání tokenu.
2. Před SH akceptací ověřit V2 parametr, root-only odpověď a dopad na seznam dostupných CRM ID/holding parent–child. Samotné default `/userInfo` nepokrývá V2.
3. V modelu oddělit UserIdentity, scoped authorization/asset, Customer/Account/Service a Group projection. Jde o významové role pro review existujících tříd, nikoli pokyn bezpodmínečně zakládat nové GUID nebo měnit CustomerContext generalizace.
4. Potvrdit samostatnou matici Atlas eligible rolí. Technický API seznam rolí není automaticky business eligibility pro UC005.
5. Následuje TMF629 a specifický Atlas token kontrakt; plné SO ani XMI se nesmějí vydávat za aktualizované na základě samotného tohoto čtení.
