# Book1: analýza aktualizace

## Výsledek

Book1 lze aktualizovat proti aktuálnímu scope a doloženým požadavkům. Dosavadní čtení prokazuje konkrétní změny níže. Úplná aktualizace ještě není provedena: celý zdrojový sešit nebyl souborově načten, všechny jeho řádky a závislosti nebyly přečteny a EA/XMI zatím není k dispozici. Nový soubor nesmí být označen za úplný aktuální Book1, dokud tyto podmínky nejsou splněny.

Uživatel potvrdil dokument Atlas CZ Launch – Architecture Board Confirmation of Phased Implementation Approach jako poslední závazný projektový scope. Ten má přednost při vyhodnocování starších návrhů. Aktuální detailní BRD/UC a MVP Requirements doplňují požadavky v jeho hranicích; případné rozpory se označí k vyřešení, neodstraní se přepisem historie.

## SSO je součást MVP

Uživatel doplnil závazný technický záměr: uživatel se přihlásí do ServiceHub; ServiceHub specifickým voláním vyjedná token pro CZ DXL; získaný token zpracuje a vloží do hlaviček následujících volání do VFCZ DXL. Toto není portálový handover ONSC/WSC, který board scope vylučuje.

Přesný protokol ještě nebyl přímo ověřen. Obecná VFID dokumentace o shared-code exchange ho sama nepotvrzuje. Doplnit konkrétní endpoint/metodu, klienta a cílovou audience, grant/exchange, scopes, claims, expiraci/obnovu, validaci tokenu, přesný název a formát hlavičky, autorizaci ke CRM ID/company, chyby a jejich zpracování. Nevymýšlet JWT formát, OAuth grant ani Authorization Bearer bez kontraktu.

Pro pozdější diagramy sledovat odděleně: uživatel → ServiceHub → Vodafone Identity; ServiceHub → CZ DXL tokenové rozhraní; ServiceHub → CZ DXL business API s tokenem; DXL → lokální zdrojové aplikace. Trust boundaries, ochranu tokenů a vazbu na zákaznický kontext doplnit podle technických podkladů.

## Konkrétní změnová matice

| Oblast / známé řádky Book1 FREQ mapping | Zjištění | Návrh změny |
|---|---|---|
| 203, CHM-05 → SREQ-SH-66 | Standalone ServiceHub zůstává. | Zachovat; určit, zda SREQ znamená Group dependency, CZ konfiguraci nebo lokální implementační změnu. |
| 204–207, CHM-14 až 17 → SH-67 až 70 | Odkazy ONSC/WSC a nová okna jsou starý návrh. | Posoudit vůči board vyloučení portálové integrace; ponechat historii, vyřadit nepodloženou MVP implementaci. |
| 210–212, CHM-06 až 08 → PORTAL-10/11, SH-73 | Předání portálového kontextu/cookie je mimo současný scope. | Oddělit jako historický návrh mimo MVP. Nepřepsat stejný SREQ na SSO token exchange; jde o jiný požadavek. |
| 213–214, CHM-18/19 → SH-74/75 | Staré větvení podle počtu kontextů se liší od aktuálního UC005. | Upravit význam na automatickou volbu jednoho dostupného CRM ID a následné přepínání. Pravidlo priority výběru zatím nedoloženo. |
| 208–209, CHM-22/25 a service eligibility | Staré společné označení eligibility spojuje více podmínek. | Rozdělit autentizaci, admin oprávnění, přípustná CRM ID a dostupnost Atlas subscription. Nevytvářet nová business ID bez zdroje. |
| 218, CHM-21 → PORTAL-07 | Entry point všem autentizovaným je starý portálový požadavek. | V rámci současného MVP neimplementovat portálový entry point; neodvozovat z něj přístup všem do standalone ServiceHub. |
| 219–220, IAM-39 → PORTAL-12/13 | Přímý Requirements zdroj používá IAM-39 pro customer selection, ne portálovou visibility. | Označit chybný nebo verzově nedoložený odkaz. Opravit až podle skutečného textu a zdrojové verze, ne podle názvu ID. |
| IAM-30/31/32 | Zdrojový Requirements.xlsx opakuje ID s odlišným obsahem. | Uchovat původní ID, přidat zdrojový list/řádek/text a označit duplicitu. Nepřečíslovávat svévolně. |
| Marketplace company readiness | MVP Requirements ponechává minimum dat a vylučuje automatický Siebel retrieval/population bez reconfirmation. | Oddělit manuální/data readiness od dřívějšího automatického lookupu z AppImpacts. |
| SSO / token pro CZ DXL | MVP funkce potvrzená uživatelem; přesný kontrakt ještě nedoložen. | Zachovat jako povinnou oblast. Identifikovat existující SREQ a rozhraní v Book1/EA; chybějící vazbu označit, nevyrobit neověřené ID. |
| V4 onboarding do SNOW | Board scope stanovuje manuální onboarding. | Automatizaci označit mimo aktuální dodávku; zachovat požadavky na výsledek, oprávnění, vstupy a případné acceptance. |

Zdrojové řádky Requirements.xlsx, list Functional Requirements: CHM-05 ř. 26; CHM-06/07/08 ř. 27–29; CHM-09 ř. 31; CHM-14 až 17 ř. 36–39; CHM-18 až 20 ř. 40–42; CHM-21 až 27 ř. 44–50; IAM-29 ř. 84; IAM-39 ř. 94; opakovaná IAM-30/31/32 ř. 85–87 a 107–109. Obsah byl přímo čten ve VDI. Jde o původní draft; současný scope se určuje výše uvedenými novějšími zdroji. Druhá odpověď Copilotu chybně přiřadila některá ID a není kanonickým mapováním.

## Jak upravit sešit

Zachovat původní listy a obsah potřebný pro dohledatelnost. U revize Functionalities, FREQ mapping a SREQ Aplikační role doplnit: původní text; navržený aktuální text; stav v MVP; druh odpovědnosti (CZ implementace / data či proces / Group dependency); konkrétní zdroj a verzi; důvod změny; stav ověření proti EA. Nevyužívat jediný stav SHODA pro současně platnost scope, pokrytí požadavku a soulad modelu.

FREQ a SREQ mají vztah N:M; jedna aplikace není automaticky jeden SREQ. Rozhraní je samostatná identita s providerem a consumerem. Group funkce může být podmínkou E2E acceptance, aniž by byla CZ implementační změnou. Chybějící AS-IS nesmí být označen za potvrzený delta dopad.

Před předáním aktualizace ověřit všechny zdrojové řádky, duplicity, osiřelé odkazy, změny scope, obousměrné pokrytí FREQ/SREQ a zachování vzorců/listů. EA shoda zůstává „neověřeno“, dokud nepřijde modelový export. Nesoulad v EA se neopravuje přejmenováním ID v Excelu bez zachování historie.

## Co bude následovat po XMI

Kontrolovat GUID a stabilní identifikátory EA, stereotypy, typy prvků, směry a význam vztahů. Z diagramů neodvozovat nové entity jen podle polohy/barvy. Prověřit business (žlutou) → application (modrou) vrstvu, funkce/služby/rozhraní a datové objekty, doménový model, integrační class model a sekvence. Propojit CustomerContext a ostatní logické pojmy s fyzickými datovými kontrakty a jejich autoritativními zdroji. Každá sekvence musí odpovídat rozhraním a odpovědnostem v modelu i SREQ.

## Marketplace V2/V4: analýza čištění a párování

Následující postup je návrh k rozpracování, nikoli doložený schválený projektový požadavek nebo povolení měnit produkční data:

1. Dohledat existující export/report Marketplace pro company, lokální customer identifier, segment V2/V4, stav, subscription a potřebné role. Nezaměňovat billing transactions report s company/customer inventurou. Získat srovnatelný referenční report ze Siebel a případně dalšího autoritativního V2 zdroje.
2. Ověřit sémantiku identifikátorů. CRM ID, Siebel CA/BA, company UUID, subscription UUID a billing BAN nejsou zaměnitelné. Určit autoritativní systém pro každý atribut a pravidla normalizace.
3. Propojit podle potvrzeného stabilního klíče. Název firmy sám nestačí. Oddělit jednoznačnou shodu, chybějící/neplatný klíč, žádný match, více matchů, duplicity a existující vazbu s rozdílnými atributy.
4. Při platném klíči a rozdílu dat ponechat vazbu k prověření; nepárovat automaticky jinam podle názvu a nepřepisovat hromadně zvoleným zdrojem. Porovnat konkrétní pole a jejich vlastníka, rozlišit opožděnou synchronizaci, změnu názvu/adresy, nesprávné přiřazení nebo chybný master záznam.
5. Pro opravu stanovit konkrétní cílový systém, vlastníka, schválený mechanismus (ručně/API/import), auditní stopu a kontrolu dopadu na subscription, fakturaci a oprávnění. Po opravě opakovat report a prokázat výsledek. Rozhodnout případ po případu podle schválených pravidel.

Chybí přesný report a sloupce, autoritativní V2/V4 klíče, směry synchronizace, pravidla survivorship, přípustný způsob aktualizace, vlastníci výjimek a provozní akceptace. Tyto body musí být doplněny ze zdrojů; nelze je prohlásit za implementované nebo schválené jen z tohoto návrhu.
