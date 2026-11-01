# Atlas EA — první revize exportu z 1. 11. 2026

Aktualizace po diskusi s uživatelem: doporučení k opravě CustomerContext v bodu 1 bylo staženo jako nedoložené. Nalezené generalizace jsou faktem exportu, ale samy neprokazují chybu ani potřebu změny. Před případným návrhem změny je nutné respektovat zamýšlený význam děděných definic. Následující původní hodnocení bodu 1 proto není platným doporučením k implementaci.

Export byl syntakticky načten jako XML/XMI 2.1 s vypnutým načítáním externích entit. Zdroj nebyl měněn. SHA-256: `dcc42289f422c120105d791725bb27549238cc8c106812ac1ad36582c1a3861c`.

## Rozsah a omezení

Celý export obsahuje 18,536 záznamů v EA Extension/elements, 14,898 konektorů a 664 diagramů. Projektová větev `01_07_2026_ServiceHub_Atlas_CZ_PR25_0837` obsahuje 2093 záznamů prvků a 55 diagramů. Počty zahrnují pomocné prvky a balíčky, nejsou počtem unikátních business pojmů. Prvky sdílené z jiných balíčků jsou při rozboru diagramu zahrnuty podle GUID. Autor není sám o sobě důkazem vlastnictví nebo aktuálnosti.

Toto je první strukturální a traceability kontrola. Není to úplná sémantická validace ArchiMate/UML, technických kontraktů ani všech 664 diagramů. Přítomnost stereotypu, barva a název diagramu samy nepotvrzují správnost modelu. Závazný projektový scope je nadále Board dokument potvrzený uživatelem; export sám neprokazuje schválení požadavků.

## Nálezy a konkrétní postup

### 1. CustomerContext: identifikátory jsou modelovány jako nadtřídy

Třída `CustomerContext (from http request as well)` má GUID `EAID_F438465B_A411_4fbb_9284_BC3DAA35EC62`. Obsahuje vlastní atributy `language` a `return_uri`. Export obsahuje Generalization z této třídy na `CRM ID` a na `user_id`:

- `EAID_C0509DF1_2245_4fcb_9241_459E0999FD13`: CustomerContext (from http request as well) → IDaaSWebUser; Association.
- `EAID_B7646F10_E87E_458d_B5ED_CD2E1D109050`: Userinfo → CustomerContext (from http request as well); Association.
- `EAID_4CF2F848_3FA2_4c73_8B82_BBF161E72CBF`: CustomerContext (from http request as well) → CRM ID; Generalization.
- `EAID_E568212F_3A03_4125_8C5E_9120C9715A81`: CustomerContext (from http request as well) → user_id; Generalization.

To je konkrétní kandidát k opravě: pokud CRM ID a user_id představují identifikátory, kontext není jejich specializací. Navrhuji logický CustomerContext oddělit od request/navigation údajů; identitu uživatele a vybraný zákaznický identifikátor vyjádřit atributy či asociacemi podle potvrzené sémantiky. Kardinality, seznam přípustných kontextů, aktivní kontext a vztah k roli/subscription je nutné navrhnout; z tohoto exportu je nepovažuji za schválené.

### 2. SSO sekvence nedokládá CZ DXL token flow

Diagram `SSO to ServiceHub`, GUID `EAID_BFC5EACD_2413_9113_9F6C_9678213FD78D`, má deset zobrazovaných prvků. Viditelné modelové účastníky zahrnují ServiceHub, IDaaS, ONSC a WSC, fragment Login obsahuje pojmy SelfCare/OneNet portal. V příslušném exportovaném UML Interaction je nula message a nula lifeline záznamů. Všech sedm projektových UML Interaction má v této části exportu nula message.

To není důkaz, že zprávy neexistují v živém EA; může jít také o obsah či nastavení exportu. Export však neumožňuje potvrdit pořadí volání ani kontrakt vyjednání tokenu. Generické OAuth/token prvky jinde v repozitáři nejsou automaticky CZ DXL kontrakt.

Pro aktuální sekvenci zachovat standalone vstup → VFID přihlášení → specifické vyjednání tokenu SH/CZ DXL → další CZ DXL volání s obdrženým tokenem v hlavičkách. Endpoint, grant, formát hlavičky, expiraci/obnovu a chyby doplnit z potvrzeného kontraktu; nepřevzít je z historického Marketplace D2 SSO diagramu. Portálový login/handover oddělit od MVP. Změny do EA zatím nebyly provedeny.

### 3. Dvě sady aplikačních funkcí se stejnými názvy

Projektová větev obsahuje 228 ArchiMate ApplicationFunction prvků, 110 názvů se opakuje. Jsou přítomny paralelní větve `90.2 Application layer/Functionalities` a `90.2 Application layer/VFCZ/Functionalities`, s různými GUID. Stejný název není totožný prvek.

- Consume Marketplace billing file containing Atlas managed service charges.: `EAID_BD31D5BC_FEB7_E57B_B094_126E8D920E23`, `EAID_BD31D5BC_FEB7_E57B_84C6_897DA01451F0`.
- Configures the service.vodafone.com email address for Atlas product tickets created in Siebel CRM, if this assisted-ticket path is confirmed as applicable.: `EAID_AD41587D_9146_43DE_A17F_A5D6FEE3AAAC`, `EAID_AD41587D_9146_43DE_B08F_7C7A7E15DDC8`.
- Confirms whether Atlas / Type C products are represented in CRM and defines the identification rule used by support and downstream processes.: `EAID_A2858B3D_8E53_FF46_83A3_8D7E67CF1213`, `EAID_A2858B3D_8E53_FF46_AF40_F4A9474DD00F`.

Neprovádět automatické sloučení. Určit, zda jde o záměrné oddělení, pracovní kopii nebo budoucí konsolidaci. Teprve pak zvolit kanonické GUID a přesměrovat vztahy a diagramy. Dvojí realizace téhož požadavku sama nepotvrzuje dvě implementace.

### 4. Book1 a aktuální EA již nejsou totožná sada SREQ

Ze 219 řádků původního Book1 FREQ mapping se SREQ ID našlo v projektových Requirement prvcích u **87 řádků**; u **132 řádků** nebylo nalezeno podle přesného ID. V projektových Requirement prvcích bylo rozpoznáno 110 různých SREQ ID. Hledání používá název/alias a přesné ID, nikoli jen podobnost textu. Nenalezené ID neznamená automaticky chybějící schopnost — mohla být konsolidována či nahrazena.

Konkrétně `SREQ-CRM-09`, GUID `EAID_926888FB_3A02_4d76_9E06_0DA85F47A9F2`, v EA popisuje konfiguraci service.vodafone.com pro Atlas tickets s podmínkou použitelnosti assisted-ticket cesty. To potvrzuje obsahový rozpor vůči lead-create mapování původního Book1; nesmí se označit za shodu pouze podle stejného ID.

Soubor `Book1_EA_vazby.csv` obsahuje všech 219 řádků, odpovídající EA GUID, text požadavku a počet přímo připojených aplikačních funkcí. Nalezené ID ještě není potvrzení scope ani textové ekvivalence. Číslo přímých FREQ/SREQ konektorů je pouze kontrola bezprostředního vztahu, nikoli všech odvozených cest v grafu.

### 5. Co má následovat při aktualizaci

1. Potvrdit kanonickou větev funkcí a aktuální sadu SREQ v EA; historický Book1 nepovažovat za hlavní zdroj ID.
2. Vytvořit změnovou matici původní Book1 → aktuální EA GUID → současný business text → závazný MVP scope; změny a zrušení držet dohledatelné.
3. Rozpracovat logický doménový model nad fyzickými třídami aplikací. Oddělit Customer, identifikátory, vztahy uživatele, zákaznický kontext, subscription a ticket; nové pojmy zatím považovat za návrh.
4. Doplnit SSO sekvenci a integrační kontrakty, potom ověřit návaznost na aplikační funkce/služby/rozhraní, datové objekty a business procesy. Fyzickou aplikaci nezařazovat automaticky do technologické vrstvy jen proto, že je konkrétní.
5. U čištění Marketplace/Siebel dohledat konkrétní reporty, klíče a master jednotlivých atributů; UML entity samy nepotvrzují provozní mechanismus oprav.

Původní revize Book1 zůstává pracovním podkladem před kontrolou EA. Na základě tohoto prvního průchodu ještě nebyla nahrazena novou schválenou verzí. Změny produkčních dat, EA ani zdrojových souborů nebyly provedeny.
