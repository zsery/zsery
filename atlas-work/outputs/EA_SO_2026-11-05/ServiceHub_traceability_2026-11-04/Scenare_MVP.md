# ServiceHub – logické scénáře MVP

Pracovní funkční návrh, 4. 11. 2026. Vychází z primárních UC005–UC011 zaznamenaných v kontrolní matici a tokenového návrhu emailu „RE: ServiceHub - DXL“, 15. 10. 2026. Diagramy vyjadřují odpovědnosti a pořadí podmínek; neurčují nepotvrzené API endpointy, payloady, role enumy ani produkční oprávnění. Čísla podmínek odkazují na EA_UC_traceability.json. Nejde o potvrzení nasazení.

## UC005 – přihlášení a kontext (podmínky 1–7)

```mermaid
sequenceDiagram
    actor U as Uživatel
    participant SH as ServiceHub / BFF
    participant ID as VFID / IDaaS
    participant AX as APIX
    participant AUTH as AuthX
    participant DX as VFCZ DXL
    U->>SH: Vstup přes samostatnou URL
    SH->>ID: Přihlášení
    alt Přihlášení selhalo
        ID-->>SH: Neúspěch
        SH-->>U: Přístupový tok ukončen
    else Přihlášení úspěšné
        ID-->>SH: IDaaS token
        SH->>AX: Token exchange – subject_token
        AX->>AUTH: Předání požadavku
        AUTH->>ID: /oidc/introspect
        ID-->>AUTH: Výsledek validace
        Note over AUTH,SH: Pouze validní výsledek může založit použitelný DXL token
        AUTH-->>AX: DXL access token
        AX-->>SH: DXL access token
        SH->>DX: Autorizované role, vztahy a CRM ID
        DX-->>SH: Dostupná data nebo chyba
        alt Chybí role nebo oprávněný CRM kontext
            SH-->>U: Obecný obsah bez zákaznických dat
        else Dostupný oprávněný kontext
            SH->>SH: Automatická volba jednoho dostupného CRM ID
            SH-->>U: Zákaznický obsah a selector
            U->>SH: Přepnutí na dostupné CRM ID
            SH->>SH: Znovu vyhodnotit obsah a akce
        end
    end
```

Priorita první volby je otevřená. Nedostupný kontext se nesmí aktivovat; při jeho ztrátě se obnoví selector. Technická chyba DXL se nesmí vydávat za úspěšně zjištěnou absenci vztahů. VFID sub ↔ příslušný ONSC/WSC user je 1:1; více CRM kontextů je samostatný vztah. TMF691 poskytuje CRM_ID; potřebné customer name je samostatný lookup TMF629. Holding payload není doplněn odhadem.

## UC006 – Atlas služby (podmínky 8–11)

```mermaid
flowchart TD
    A[Aktivní oprávněný CRM kontext z UC005] --> B[Načíst odpovídající Marketplace data]
    B --> C{Výsledek načtení}
    C -->|Chyba| D[Zobrazit nedostupnost dat]
    C -->|Úspěch| E[Filtrovat Atlas managed služby v MVP]
    E --> F{Dostupná služba}
    F -->|Ano| G[Zobrazit služby aktivního kontextu]
    F -->|Ne| H[Zobrazit ověřený prázdný stav]
    G --> I[Při přepnutí CRM ID znovu načíst a vyhodnotit]
    H --> I
```

Konkrétní převod CRM ID na Marketplace company UUID, pole a subscription stavy vyžadují kontrakt. Žádný automatický Siebel prefill ani ONSC/WSC navigační handover není tímto zaveden.

## UC007 – vytvoření support requestu (podmínky 12–15)

```mermaid
flowchart TD
    A[Role, Atlas služba a aktivní kontext] --> B{Operace povolena a SNOW user/company připraveny}
    B -->|Ne| C[Nevytvářet požadavek]
    B -->|Ano| D[Vyplnit požadavek]
    D --> E{Povinné vstupy platné a kontext stále aktuální}
    E -->|Ne| F[Opravit vstupy nebo znovu vyhodnotit kontext]
    E -->|Ano| G[Odeslat potvrzenou integrační cestou do SNOW]
    G --> H{SNOW potvrdil vytvoření}
    H -->|Ano| I[Zobrazit potvrzený úspěch a identifikaci]
    H -->|Ne nebo bez výsledku| J[Nezobrazovat nepotvrzený úspěch]
```

Konkrétní mandatory fields, routing, assignment, timeout, retry a ochrana proti duplicitám zůstávají technickým návrhem k potvrzení. V4 customer/admin onboarding je manuální MVP; není novou automatickou provisioning sekvencí.

## UC008 – asistovaná podpora (podmínky 16–18)

```mermaid
flowchart TD
    A[Telefonický BCS/LME kanál] --> B{Whitelisted V2 zákazník}
    B -->|Ne| C[Nepoužít tuto lokální asistovanou cestu]
    B -->|Ano| D[LME ověří zákazníka a kontext]
    D --> E[Zaznamenat výsledek v SNOW]
    E --> F{Lokálně vyřešeno}
    F -->|Ano| G[Zaznamenat skutečné řešení]
    F -->|Ne| H[Předat nebo eskalovat dle provozního modelu]
```

BCS je kanál a LME lidská role. Diagram nezavádí novou aplikaci. Správa whitelistu, resolver skupiny a fallback se musí doložit provozním postupem.

## UC009 – úplné ukončení (podmínky 19–21)

```mermaid
sequenceDiagram
    participant FL as Frontline / Siebel
    participant ICT as ICT Hub / Provisioning
    participant MP as Marketplace
    participant SN as SNOW / MSO
    FL->>FL: Ověřit zákazníka a subscription scope
    FL->>ICT: Zahájit úplné ukončení
    ICT->>MP: Následné zpracování ukončení
    MP->>SN: Následná SNOW / MSO činnost
    Note over FL,SN: Nepotvrzené předání není dokončené ukončení
    Note over FL,SN: Zachovat subscription mimo vymezený scope
```

Jde o logický procesní směr, nikoli specifikaci přímých API volání. ServiceHub se nestává novým prodejním ani termination vstupem. Downgrade se zachováním M365 je UC004, neslučuje se s úplným ukončením UC009. Efektivní datum a zotavení po selhání vyžadují kontrakt.

## UC010 – seznam a detail (podmínky 22–25)

```mermaid
flowchart TD
    A[Aktivní oprávněný CRM kontext] --> B[Získat odpovídající support requesty ze SNOW]
    B --> C{Výsledek}
    C -->|Chyba| D[Odlišit nedostupnost od prázdného seznamu]
    C -->|Úspěch| E[Zobrazit oprávněný seznam]
    E --> F[Detail pouze přístupného požadavku]
    F --> G[Při přepnutí kontextu nahradit seznam i detail]
    E --> G
```

Obecné „all tickets“ neprokazuje oprávnění ke všem SNOW typům nebo všem společnostem. Detail musí podléhat stejnému customer scope jako seznam. Pagination, sorting, status mapping a cache nejsou odhadovány.

## UC011 – změna požadavku (podmínky 26–30)

```mermaid
flowchart TD
    A[Přístupný požadavek aktivního kontextu] --> B[Získat aktuální stav a oprávnění k operaci]
    B --> C{Operace povolena}
    C -->|Ne| D[Neodeslat změnu]
    C -->|Ano| E[Validovat vstupy a aktuálnost kontextu]
    E --> F{Platná změna}
    F -->|Ne| D
    F -->|Ano| G[Odeslat povolenou změnu do SNOW]
    G --> H{SNOW potvrdil změnu}
    H -->|Ano| I[Zobrazit potvrzený nový stav]
    H -->|Ne nebo bez výsledku| J[Nezobrazovat nepotvrzený úspěch]
    B --> K[Při změně kontextu nebo stavu znovu vyhodnotit]
    K --> B
```

Company scope není porovnání emailu. Povolené update operace, komentáře, attachments, stavové přechody a souběh změn musí určit příslušný SNOW kontrakt. Diagram je nevymýšlí.

## Akceptační a modelová návaznost

Všech 30 kontrolovatelných podmínek, návrhy jejich ověření a původní FREQ GUIDy jsou v EA_UC_traceability.json. Prázdná množina kandidátů je viditelná mezera v porovnávané sadě, nikoli automatické nové FREQ/SREQ ID. Existující obecný požadavek na refresh neprokazuje splnění konkrétního submit/update scénáře. Návrh proto nesmí generovat úplné realization vztahy jen podle shody čísel.
