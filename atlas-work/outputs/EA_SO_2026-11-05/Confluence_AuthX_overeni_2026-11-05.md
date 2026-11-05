# AuthX token exchange – primární ověření Confluence

Přímo otevřeno a přečteno 5. listopadu 2026 v přihlášeném VDI. Zdroj: [TS - AuthX - authx-ts](https://confluence-agile.oskarmobil.cz/display/DCP/TS+-+AuthX+-+authx-ts), kapitola **3.2.1 Exchange Vodafone ID Access Token For DXL Access Token**. Hlavička stránky uvádí poslední změnu 4. června 2026. Nejde o potvrzení Atlas klientské konfigurace ani produkčního nasazení.

## Přímo doložený platformní kontrakt

- `POST /OAuth2TokenExchangeGrant/v2/token`.
- Pro volání přes APIX musí API key mít scopes `OAUTH2_TOKEN_EXCHANGE_GRANT` a `TMF691_FEDERATED_IDENTITY_ALL`.
- `Accept: application/json`; `Content-Type: application/x-www-form-urlencoded`.
- `grant_type=urn:ietf:params:oauth:grant-type:token-exchange`.
- `subject_token_type=urn:vodafone:params:oauth:token-type:vodafone_id`.
- `subject_token` obsahuje platný Vodafone ID access token.
- Povinný `subject_token_iss` určuje vydávající VFID prostředí, aby AuthX ověřil opaque subject token proti správnému prostředí. Stránka má samostatné hodnoty DEV, STAGINGREF a PROD; hodnotu pro konkrétní SH prostředí je třeba přiřadit podle skutečného token issueru.

Odpověď obsahuje standardní OAuth atributy a TMF691-kompatibilní UserInfo se seznamem autorizačních assets uživatele. Stejné assets jsou vložené do vydaného access tokenu; jeho použití pro další DXL API neopravňuje k assets mimo seznam odpovědi. Příklad response uvádí HTTP 200, JSON, `access_token`, `issued_token_type` = `urn:ietf:params:oauth:token-type:access_token`, `token_type` = `Bearer`, `expires_in`, `expires_at`, `scope`, `refresh_token`, `refresh_expires_at`, `refresh_expires_in` a `user_info`.

Číselné hodnoty expirace v příkladu nejsou důkazem pevné produkční životnosti Atlas tokenu. Nejsou přebírány žádné tokeny, emaily ani uživatelské identifikátory z příkladu. Request zde neprokazuje konkrétní APIX auth header nebo client secret mechanismus; ty se nesmí domyslet.

## Dopad na návrh ServiceHub

Emailový návrh SH BFF → APIX → AuthX má nyní primární technickou oporu pro relativní endpoint a uvedené request parametry. SH musí předat issuer prostředí spolu se subject tokenem. Vyhodnocování customer content v SH a získávání upstream vztahů/rolí zůstávají oddělené odpovědnosti. TMF691-kompatibilní UserInfo uvnitř token exchange odpovědi samo nepotvrzuje, zda musí Atlas pro svůj úplný kontext provést další samostatný UserInfo lookup.

Přidělení scopes konkrétnímu Atlas API key, URL prostředí, klientská autentizace, přesné životnosti, error/refresh kontrakt, úplný payload a nasazení zůstávají k ověření. Prohlédnutý rozsah není celá stránka AuthX, odkazovaná VFID 01.01 specifikace ani SNOW integrační kontrakt. Datum stránky není approval Atlas.

Přístup do Confluence byl při této kontrole aktivní. Pokud vyprší, požádat uživatele o ruční přihlášení. Technické ověřování provádět v Confluence nebo přes Teams agenta Confluence; ostatní práci přes Copilot podle přenosného skillu v repozitáři.
