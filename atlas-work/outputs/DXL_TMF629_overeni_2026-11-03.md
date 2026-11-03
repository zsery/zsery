# DXL TMF629 – ověřené části pro customer model a data readiness

3.11.2026, read-only VDI SharePoint Immersive Reader. Zdroj: `CZ local folder / Architecture / DXL / 29.10.2026 / FS - TMF629 Customer Management API - customerinformationmanagement-fs`. Knihovna modified před pěti dny Zdeněk Šerý; export 29.10.2026 11:03:49. Revize obsahuje leden/duben 2025 Ondřej Šebelík, září 2025/červen 2026 Mounier Gaballah a červenec/srpen 2026 Martin Hurník. Datum exportu není aktuální Atlas approval.

Přečten titul, obsah, revize/reference, čtecí text Architecture/Integration, bulk/current-user lookup, telefonní lookup a začátek jeho odpovědi, email lookup hlavička, identificationNumber lookup, Get Customer By Id vstupní část a **souvisle obě celé mapping sekce OLC Customer a V2 Customer** do začátku Siebel Create Customer via TIBCO. Některé dlouhé JSON příklady a mezilehlé lookup části byly přeskočeny posuvníkem. Create/patch mapping a procesní kapitoly 6.1/6.2 nebyly dokončeny; není to úplné přečtení dokumentu. Vložené Architecture/Integration diagramy reader nezobrazil. Zachováno source formatting, takže viditelné přeškrtnutí není přehlédnuto.

## Technické poznatky použitelné pro Atlas

| Oblast | Doložený obsah |
|---|---|
| Bulk | `GET /customer?id={id1},{id2},…` pro V4 i V2. Podporuje Siebel CA číslo nebo V2 MSCRM GUID. Limit až 1000 zákazníků, překročení → HTTP 422; APIX URI limit může být nižší a vracet 414. To není potvrzení oprávnění konkrétního Atlas klienta. |
| Single | `GET /customer/{id}` pro V4/V2. Specifikace rozlišuje numeric Siebel CA a GUID MSCRM. Detail routingu do OLC/TIBCO i některé auth predikáty jsou přeškrtnuté; nepoužívat je jako ověřenou nynější implementaci. |
| Scopes | U čtených read operací uvedeny `CZ_GRAPHQL_CUSTOMER_READ`, `TMF629_CUSTOMER_MANAGEMENT_CUSTOMER_READ`, `TMF629_CUSTOMER_MANAGEMENT_ALL`; dokument uvádí také `hasMinLevel('SILVER')`, trusted client a CA access kontroly. Přesná efektivní pravidla/granty SH musí potvrdit kontrakt/owner. Příklad requestu má Authorization Bearer. |
| Current user | `GET /customer` popisuje kolekci dostupných customers/prázdnou kolekci. Vnitřní postup podle userAssets a OLC je přeškrtnutý; neodvozovat z něj aktuální úplnost V2/holding stromu. |
| APIX | Reference je `https://eu2-stagingref.api.vodafone.com/tmf-api/customerManagement/v4`, nikoli ověřená produkční URL. |
| Dokumentační chyba | V obsahu je `Error rendering macro 'toc'` / WstxUnexpectedCharException, unexpected character space / missing name, row,col `[221,35]`. Jde o text exportované stránky; zbytek readeru se načetl. Není to chyba Excelu ani selhání volané API. |

## OLC mapování

`Customer.id` je `$customer.customerAccountNumber`, nikoli Siebel row ID. Název je `$customer.nameAcc`. `status` mapuje A/P/I/Z na active/pending/inactive/anonymized. `characteristic[name=platform].value` je `$customer.channelIdentifier` (V2/V4); nejde o tentýž pojem jako segment consumer/business.

`customerType` je typ CA, `customerSubType` je odlišný podtyp; business typ zahrnuje i variantu bez IČ/DIČ. Proto samotné chybějící IČO není univerzální důkaz chybného customer match. `identificationNumber` je IČO, `taxIdNumber` DIČ. Primary/secondary CA owner login/email/mobile jsou kontaktní atributy a nejsou náhradou VFID `sub` identity či kompletního role modelu.

Kontaktní mapování rozlišuje email včetně verified flag, telefon a GeographicAddressContactMedium z primární aktivní business adresy. `validFor.startDateTime` pochází z customer created. Adresa v API je tedy konkrétní výběr podle source mappingu, ne automaticky libovolná billing/service adresa. Souhrnná shoda názvu/adresy nesmí nahradit ověření typu a identity zákazníka.

## V2 mapování

- Zdroj je `V2 getSubscriberProfile` response. Název této operace neopravňuje přejmenovat modelový **user** na subscriber.
- Výstupní `Customer.id = $customer.siebelCA`. GUID V2 MSCRM je samostatně `characteristic[name=mscrmAccountId].value = $customer.accountId`. Proto input GUID a output CA není přípustné zaměnit v Book1 nebo integrační třídě za stejné netypované pole.
- `customerFORISId` je FORIS CM.ELEMENT row id organization/holding; podle poznámky jen active customer, ne lead. Samotný typ Holding nebo tento identifikátor není payload parent–child hierarchie v TMF691.
- `customerWalletId` je FORIS wallet id určené podle CM subscription vstupního telefonního čísla. Dokument jej omezuje na active customer identifikovaného active incoming phone; pro email/outgoing call není dostupný. Nevyvozovat obecný seznam BA/wallet ze samotného TMF629 customer response.
- V2 `platform` je konstantní V2, `segment` business. `identificationNumber` se mapuje z `ico`. `type` může být Organization/Holding. `accountTypeCode` odlišuje customer/lead. V2 mapping současně uvádí status konstantně active s poznámkou, že getSubscriberProfile vrací pouze active customers; proto tento samotný status nepoužívat jako kompletní lifecycle nebo Atlas subscription eligibility.
- Primary/secondary owner names a primary contact jsou atributy. Nejsou technickým potvrzením eligible ONSC role pro UC005.

## Dopad na cleansing a MVP

Pro report/párování držet odděleně alespoň platformu, Siebel CA číslo, V2 MSCRM GUID, FORIS organization/holding id, BA/wallet id a Marketplace company UUID. Konkrétní Marketplace ExternalCompanyId typ musí být potvrzen jeho source kontraktem; nelze jej určit jen z názvu.

Existence GET API dokládá katalogovou schopnost číst zákaznická data. **Neruší** explicitní MVP vyloučení automatického Siebel retrieval/prefill/population a nedokládá implementovaný reconciliation/dry-run nástroj. Offline srovnávací report a ruční kontrola jsou pracovní návrh, nikoli nové nasazení. Přístup k BA/customer vazbě vyžaduje další ověřený zdroj (např. odpovídající account kontrakt), ne domněnku z CA existence.
