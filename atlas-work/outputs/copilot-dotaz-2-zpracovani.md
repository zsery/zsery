# Zpracování druhé odpovědi Teams Copilotu

**Následná přímá kontrola SharePointu opravila podstatnou část této odpovědi.** V Support_Material/Requirements.xlsx CHM-06 znamená předání ONSC kontextu, CHM-20 až 27 existují, IAM-29 znamená předání WSC kontextu a IAM-39 výběr zákazníka. Níže je historický záznam tvrzení Copilotu, nikoli platné kanonické mapování. Viz sharepoint-cz-local-pruzkum.md pro přímo ověřené řádky a duplicity IAM-30 až 32.

1. 11. 2026. Celá druhá odpověď byla přečtena na obrazovce. VDI pouze čtením. Níže jde o tvrzení Copilotu; odkazovaný požadavkový Excel a říjnový MVP Requirements ještě nebyly přímo otevřeny při této kontrole. Nelze tím potvrdit schválenou baseline.

## Kritický nález: nesoulad ID a obsahu

Copilot označuje nalezený Service Hub+Atlas – Requirements za verzi 0.1 / Draft se staršími červencovými požadavky, které říjnové dokumenty mění. Uvádí list Functional Requirements. Přiznává, že index neposkytuje skutečná čísla řádků Excelu.

| ID dle Copilotu v nalezeném zdroji | Význam dle odpovědi |
|---|---|
| F-REQ-CHM-05 | Standalone portál |
| F-REQ-CHM-06 | Přístup přímou URL |
| F-REQ-CHM-07 | Vstup přes WSC |
| F-REQ-CHM-08 | Vstup přes ONSC |
| F-REQ-CHM-14 | Otevření WSC v novém okně nebo záložce |
| F-REQ-CHM-15 | ONSC/WSC entry point všem autentizovaným uživatelům |
| F-REQ-CHM-16 | Vyhodnocení eligibility po vstupu |
| F-REQ-CHM-17 | Service functionality při splnění eligibility |
| F-REQ-CHM-18 | Produktová informační stránka při nesplnění eligibility |
| F-REQ-CHM-19 | Zákaz service functionality při nesplnění eligibility |
| F-REQ-IAM-39 | Lokální vstupní kanály omezují navigaci při nesplnění subscription eligibility |

Tyto významy se liší od vazeb stejných ID pozorovaných v Book1 (např. CHM-06 tam předávání ONSC kontextu, CHM-18 výběr kontextu). **Původní lokální tabulka revize zachycuje obsah Book1, nikoli ověřené kanonické znění FREQ.** Neaplikovat změny mechanicky podle ID. Nutná kontrola původního textu, konkrétní verze a zdrojové buňky. Nelze zatím určit, zda je příčinou jiná verze, chybné mapování Book1 nebo nepřesnost indexu/Copilotu.

CHM-20, CHM-21 a CHM-25 až 27 Copilot v nalezené řadě nedohledal (řada končí CHM-19); to nedokládá zrušení.

## Další využitelné závěry

- Starý IAM-27 umožňuje výběr při více účtech; IAM-29 podle Copilotu vyžaduje výběr před service-specific funkcemi. Nový UC005 naopak automaticky vybere jedno dostupné CRM ID a umožní následné přepínání. Nový tok byl již přímo přečten v UC005 str. 19–21. Původní IAM-29 zůstává k přímému ověření, formální zrušení nebylo doloženo.
- Oddělit autentizaci, administrativní/zákaznickou autorizaci, aktivní CRM kontext a produktovou/subscription dostupnost Atlas. UC006 má číst Marketplace informace pro aktivní CRM ID; podrobnosti UC006 zatím jen z Copilotu.
- CZ/DXL zajišťuje lokální customer relationships, role/permission inputs a CRM ID; Group/ServiceHub autentizační a autorizační chování, Customer Selector a chování aktivního kontextu. Nutné potvrdit přesné hranice z říjnového zdroje.
- ONSC/WSC integrace a context handover mimo MVP odpovídají přímo přečtenému BRD/UC. Portálové cookie není doloženo jako současná integrační potřeba. Samostatný deep link nelze automaticky označit za zrušený.
- Odpověď odkazuje na další dokument „Service Hub Atlas MVP Requirements“, který je nutné přímo otevřít a zjistit verzi, datum a schválení. Jde o potenciálně důležitější zdroj současné dekompozice než starší Requirements draft.

## Stav a další krok

Dotaz č. 2 je zpracován a je možné zadat č. 3 specializovanému agentovi s Confluence indexem. Projektové soubory ani data ve VDI nebyly změněny. Při další kontrole otevřít Requirements draft a říjnový MVP Requirements, doplnit přesné odkazy a vytvořit mapování dle významu, ne pouze shody ID.
