# Atlas – kontrola business vrstvy a návaznosti na aplikace, 3.11.2026

Podklad: původní Atlas.xml, SHA-256 `dcc42289f422c120105d791725bb27549238cc8c106812ac1ad36582c1a3861c`, a přímé čtení CZ BRD, UC001–012, říjnových MVP Requirements a Traceability Decomposition zaznamenané v `../Overeni_zdroju_VDI_2026-11-03.md`. Výsledek je změnový podklad. Zdrojové XMI není přepsané a navržené obsahové návaznosti nejsou schválené modelové vztahy.

## UC identita a business vrstva

Projektová větev obsahuje 21 business use case prvků autora SeryZ. Nová specifikace má 12 UC s jiným číslováním a hranicemi. Připojený `EA_UC_obsahovy_crosswalk_2026-11-03.csv` uvádí každý původní GUID, název a pracovní obsahovou návaznost. Například původní UC001 znamená přístup do ServiceHubu (dnešní UC005), původní UC009 MSO řešení (dnešní UC009 je termination), původní UC012 eskalaci (dnešní UC012 onboarding). Přejmenování podle stejného čísla by měnilo význam.

Původní UC002 a UC004 se oba částečně překrývají s dnešní service visibility UC006. UC003 a UC005 rozdělují seznam a detail ticketu, dnes UC010. Tyto prvky nelze automaticky sloučit. UC017/UC018 vyžadují opravu kanálu podle současných UC002/UC009: Marketplace enablement a Frontline/Siebel → ICT Hub/Provisioning → Marketplace → SNOW/MSO termination; SH není potvrzený MVP sales/activation kanál. UC010 Service Desk on behalf není novými UC potvrzený a AD06 jej z MVP vylučuje.

V projektové větvi nebyl nalezen explicitní stereotyp ArchiMate_Capability. Šest takových prvků v plném exportu leží v jiné TA139 větvi. Nelze je použít jen podle názvu. To neznamená absenci celé business vrstvy: projekt obsahuje business procesy a BPMN. Současná zdrojová matice má 26 journey/UC/process/capability/sub-capability návazností; jsou přepsány v Book1 Business a FREQ!167–192. Není to 26 nových FREQ.

## Konkrétní staré předpoklady k opravě

| EA prvek a GUID | Kontrolovaný význam / požadovaná změna |
|---|---|
| AD05 `EAID_35449BC8_E7BE_40ad_B153_58589875C696` | Historické povinné V2/V4 portálové vstupy oddělit od standalone MVP. Nepřenášet portal embedding/handover do nynějšího scope. |
| ASS06 `EAID_A3A663F0_D721_49ec_AB79_45E58A028178` | Tvrzení, že direct URL není standalone access model, je v rozporu s aktuálními UC/MVP. |
| AD07 `EAID_436FF5E3_7559_4a74_845F_38498981CD3F` | Rozlišit cílový V4 SNOW lifecycle a dnešní manuální customer/admin onboarding. Historické create/view/close není potvrzení všech aktuálních ticket oprávnění. |
| AD08 `EAID_213C4D3B_E083_43c1_B676_5AA96D557C0A` | V2 user-info výkonová hypotéza a mitigace vyžadují aktuální měření/kontrakt. Neoznačovat za potvrzenou implementaci nebo kvantifikovaný NFR. |
| ASS03 `EAID_C6A84687_EFF5_4c33_815C_D3264CD2AC74` | User identity 1:1 není počet dostupných CRM/customer/company vztahů. Tyto vztahy neslučovat. |
| ASS07 `EAID_15F4EF2A_14D5_4bca_BA70_DEE9A8FFC46B` | Rozlišit UC005 user/role/context, UC006 Atlas service visibility a UC007/010/011 ticket operace. SNOW presence není automaticky podmínkou přístupu ke všemu SH obsahu. |
| ASS08 `EAID_B457C5A2_0E9C_42e5_B3FE_81E303DB9520` | Před prvním orderem aktuální UC002 konkrétně vyžaduje interní kontrolu VFID/admin v Logins. Nevyvozovat automatický SNOW onboarding. |
| ASS09 `EAID_F0523E6E_D1D2_4c7f_A356_7946B384377F`, LIM01 `EAID_CF970416_8ACB_42d7_BC89_7A46583EAA12` | Cílový lifecycle/otevřené technické varianty ponechat odlišné od výslovného manuálního MVP. |

Ostatní AD/ASS mají širší smysl VFID, Marketplace subscription source a SNOW ticket source; tím ještě není ověřen konkrétní payload, konzistence všech polí nebo technická implementace. Původní constraint záznamy jsou v `EA_constraints_zdroj_2026-11-03.json`.

## Návaznost do modré vrstvy

V projektu je 228 ApplicationFunction a 228 Realization konektorů, všechny ApplicationFunction → ArchiMate_Requirement. Z toho 226 konektorů směřuje na názvy začínající SREQ-, dva na stejný OREQ-CARE-01 `EAID_79402BF1_669A_41ec_9713_E4D8C1D78EDD`. Dvojí realizace není důkaz dvou implementací. OREQ care/IVR provozní směrování samo není potvrzení správného modelového typu aplikační funkce.

Exportní index nenalezl incidentní konektory na původních FREQ ani na 21 uvedených business UC. Proto 228 realizací nedokládá business UC → FREQ → SREQ → aplikační funkce průchod. Jde o výsledek dodaného exportu/indexu, nikoli tvrzení o kompletním živém EA. Přímé EA vazby v Book1 zůstaly zachovány; pracovní capability/UC přiřazení je oddělené v R:S.

Padesát pět projektových diagramů odkazuje také mimo projektovou větev: mimo jiné na 23 sdílených ApplicationComponent, 44 UML Class a 10 uml:Sequence prvků. Pro kontrolu aplikací a integračního modelu je nutné zahrnout tyto odkazované GUID; samotný podstrom projektu není úplná modrá architektura. Paralelní sady funkcí s různými GUID se neslučují podle názvu.

## SSO a doménový model

SSO diagram `EAID_BFC5EACD_2413_9113_9F6C_9678213FD78D` má deset odkazovaných prvků; v této množině nebyl nalezen DXL účastník ani indexovaný konektor s oběma konci v množině. Obsahuje Customer, IDaaS, ONSC, WSC, ServiceHub a Login fragment/pomocné texty. Export tak nepotvrzuje detailní CZ DXL token sekvenci; neprokazuje absenci zpráv v živém EA.

Výslovně zadaný cílový tok: VFID přihlášení → SH specificky vyjedná token s CZ DXL → obdržený token použije v hlavičce dalších CZ DXL volání. Endpoint, grant, typ tokenu, přesná hlavička, expirace a chybové kódy se nepřebírají odhadem. VFID sub ↔ příslušný ONSC/WSC user vždy 1:1, email není párovací klíč. TMF691 holding parent–child je samostatný vztah.

CustomerContext generalizace nebyly změněny ani označeny za chybu. Dědičnost definic tříd nevyžaduje instanci. Původní nedoložené doporučení první revize zůstává stažené.

## Stav

Dokončena tato strukturální a obsahová kontrola 21 UC a uvedených omezení, nikoli implementace nových EA vztahů. Přesná GUID business prvků/capabilities, atomické FR a schválení, kanonická sada funkcí a technické kontrakty zůstávají pro řízenou aktualizaci modelu. Žádné nové GUID nebyly vytvořeny jen z podobnosti názvu. Původní Atlas.xml a SO nebyly touto kontrolou změněny.
