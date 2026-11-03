import fs from 'node:fs/promises';import {createRequire} from 'node:module';import {pathToFileURL} from 'node:url';
const req=createRequire('C:/Users/zsery/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/package.json');
const {FileBlob,SpreadsheetFile}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const w=await SpreadsheetFile.importXlsx(await FileBlob.load('outputs/book1-revize/Book1_MVP_revize_2026-11-01.xlsx'));
const d=JSON.parse(await fs.readFile('work/book1/v02-data.json','utf8'));
const original=JSON.parse(await fs.readFile('work/book1/data.json','utf8'));
const controls=[
 ['BOOK1 — PRACOVNÍ VERZE 02','1. 11. 2026','Přechod na business-first postup a připojení Atlas.xml','Pracovní evidence; není schválená baseline.'],
 ['Směr práce','Analýza Martina Dostála → MVP/FREQ → business vrstva a BPMN → aplikace/SREQ → SO','Pokyn uživatele v tomto chatu','Aktualizovat průběžně po oblastech, bez přeskakování business analýzy.'],
 ['Účel Book1','Evidence zdrojů, požadavků, vazeb, rozhodnutí a postupu','Uživatelské zadání','Výstupy budou podkladem pro úpravu Atlas.xml a následnou aktualizaci SO.'],
 ['Hranice řešení','Integrace Vodafone Group a Vodafone CZ','B1 + zadání uživatele','U každé oblasti určit odpovědnost, data a předání přes hranici Group/CZ.'],
 ['Rozsah v02','159 existujících EA FREQ záznamů + 6 analytických vstupů UC005; 111 EA SREQ prvků; 219 původních mapovacích řádků','E1; U1; původní Book1','Nové listy jsou pracovní; historické listy a ID zůstávají dohledatelné.'],
 ['Zdroje — B1','Atlas CZ Launch – Architecture Board Confirmation of Phased Implementation Approach.docx','Uživatel potvrdil poslední závazný scope','Nejvyšší autorita pro MVP scope.'],
 ['Zdroje — U1','PR25_0837_ServiceHub_Atlas_Use_Case_Specification.docx; verze 0.1; Last Update 14.10.2026','Martin Dostál; přímo čten zejména UC005 s.19–21','Přečtené části nejsou kontrolou celé specifikace; prověřit poslední revizi u zdroje.'],
 ['Zdroje — B2','PR25_0837_ServiceHub_Atlas_BRD.docx; v knihovně změna 23.10.2026','Relevantní části přímo čteny; interní aktuální revize nepotvrzena','Ověřit poslední verzi a úplný obsah před potvrzením business baseline.'],
 ['Zdroje — M1','Service_Hub_Atlas_MVP_Requirements.xlsx; změna v knihovně 19.10.2026','Přímo čteny MVP Scope a MVP Functional Decomposition','Rozlišit CZ lokální změnu, Group dependency a E2E akceptaci.'],
 ['Zdroje — R1','Service Hub+Atlas - Requirements.xlsx / Support_Material; změna 21.8.2026','Starý draft; částečně přímo čten','Historická identifikace a text; nesmí přepsat B1 nebo novější analýzu.'],
 ['Zdroje — E1','Atlas.xml; dodaný export EA','SHA-256: '+d.sha,'Modelová inventura, nikoli automaticky schválený business zdroj.'],
 ['Zdroje — T1','Uživatel: SH vyjedná token s CZ DXL a používá ho v hlavičkách dalších VFCZ DXL volání','Technický záměr potvrzen uživatelem','Povinné SSO MVP; detail kontraktu ověřit z technických podkladů.'],
 ['1 — Aktuální analýza','Sestavit úplnou verzovanou sadu posledních podkladů Martina Dostála','U1, B2 a navazující SharePoint podklady','OTEVŘENO — data změny souborů sama nepotvrzují verzi a schválení.'],
 ['2 — Soulad MVP','Každý požadavek posoudit vůči závaznému B1','B1; M1','PRŮBĚŽNĚ — u rozporu zachovat historii a zaznamenat rozhodnutí.'],
 ['3 — Business a FREQ','Doplnit aktuální text, zdrojovou sekci, FREQ ID a přijetí požadavku','List Business a FREQ','ZALOŽENO — import EA a šest doložených UC005 vstupů; většina čeká na analýzu.'],
 ['4 — Capability a business','Ověřit existující capability, role, služby, procesy a business objekty; doplnit vazby na FREQ','Atlas.xml; analýza','OTEVŘENO — capability a requirement vést podle skutečného typu prvku, ne podle barvy.'],
 ['5 — BPMN','Rozpracovat průběh, rozhodnutí, výjimky a předání Group/CZ','Business podklady; existující BPMN v EA','OTEVŘENO — uchovat zdrojový proces a verzi; stejný název není důkaz shody.'],
 ['6 — Modrá vrstva','Z business potřeby určit aplikační funkce/služby/rozhraní, data a SREQ','Potvrzené FREQ + business/BPMN','ČEKÁ NA BUSINESS BASELINE — EA inventura je připravena.'],
 ['7 — Model EA','Připravit změny podle GUID; zachovat odkazy a zdůvodnění','Potvrzená změnová matice Book1','NYNÍ BEZ ZMĚNY — Atlas.xml zůstává vstupem.'],
 ['8 — SO Word','Aktualizovat Introducing, Architecture, Functional Design, System Impacts, Other Requirements, Open Points','Potvrzený Book1 + EA + aktuální šablona SO','BUDOUCÍ KROK — Word se v této verzi negeneruje.'],
 ['MVP — SSO','Standalone ServiceHub, VFID a specifický CZ DXL token flow','B1; T1','V MVP. Endpoint, grant, audience, hlavička, expirace/obnova a chyby nejsou potvrzeny.'],
 ['MVP — portály','ONSC/WSC navigace a context handover','B1','Mimo současnou integraci MVP; odlišit zdrojové role/data přes DXL.'],
 ['MVP — onboarding V4','Manuální interní onboarding customer/user do SNOW','B1','Nedovozovat automatický onboarding z historických požadavků.'],
 ['MVP — Marketplace/Siebel','Minimum company identifier/data readiness; automatický Siebel prefill jen po opětovném potvrzení','M1, dekompozice ř.14–16','Oddělit potřebný výsledek od staré automatizace.'],
 ['UC005 — kontext','Automatická volba jednoho dostupného CRM ID; možnost následného přepnutí','U1 s.19–21','Priorita volby a všechny produktové podmínky nejsou potvrzeny.'],
 ['Datová připravenost','Dohledat reporty Marketplace/Siebel, klíče, vlastníky atributů a způsob opravy','Business analýza / provozní podklady','OTEVŘENO — žádné opravy produkčních dat nejsou součástí této změny.'],
 ['Rozpor — identifikátory','R1 opakuje IAM-30/31/32 a významy se mezi verzemi liší','R1: ř.85–87 a107–109; původní Book1','Neslučovat pouze podle ID; vyžadovat zdroj, verzi a text.'],
 ['Rozpor — Book1 vs EA','87 mapovacích řádků má SREQ ID v projektové větvi; 132 jej nemá','Přesná kontrola názvu/aliasu proti E1','Nenalezené ID může být nahrazeno; nesmí být automaticky zrušeno ani prohlášeno za chybějící funkci.'],
 ['Rozpor — dvojí funkce','EA má paralelní Functionalities a VFCZ/Functionalities s různými GUID','E1; projektová větev 90.2 Application layer','Určit kanonické použití; automaticky neslučovat.'],
 ['Rozpor — EA poznámka MVP','Některé EA SREQ označené MVP popisují portálové entrypointy','E1 versus B1','Poznámka MVP v EA není schválení scope; ověřit text proti B1.'],
 ['Modelový závěr stažen','CustomerContext: z pouhé generalizace nelze potvrdit potřebu opravy','Upřesnění po diskusi s uživatelem','Bez automatické opravy; záměr děděných definic je nutné respektovat.'],
 ['Změny této verze','Přidány business/FREQ a EA SREQ evidence, řízení postupu a kontrola ID v existujících mapováních','v02 oproti pracovní revizi z 1.11.2026','Původní modelové a business texty nejsou potichu nahrazovány.'],
 ['Další revize záložek','Nejprve Business a FREQ; poté doplnit business vazby, BPMN, FREQ mapping a SREQ','Dohodnuté pořadí práce','Každá změna musí mít dohledatelný zdroj a oddělený stav potvrzení.']
];
function grid(name,headers,rows,widths,color){
 const s=w.worksheets.add(name),r=s.getRangeByIndexes(0,0,rows.length+1,headers.length);r.values=[headers,...rows];r.format.wrapText=true;r.format.verticalAlignment='top';r.format.font.name='Calibri';r.format.font.size=11;
 s.getRangeByIndexes(0,0,1,headers.length).format={fill:color,font:{bold:true,color:'#FFFFFF'},rowHeight:48,wrapText:true};
 for(let j=0;j<headers.length;j++)s.getRangeByIndexes(0,j,rows.length+1,1).format.columnWidth=widths[j]||45;
 s.getRangeByIndexes(1,0,rows.length,headers.length).format.rowHeight=110;
 for(let i=0;i<rows.length;i++)if(i%2===0)s.getRangeByIndexes(i+1,0,1,headers.length).format.fill='#F2F5F7';
 s.freezePanes.freezeRows(1);s.freezePanes.freezeColumns(name==='Postup revize'?1:2);s.showGridLines=false;s.tabColor=color;return s;
}
grid('Postup revize',['Oblast / položka','Pravidlo nebo úkol','Zdroj / podklad','Stav / další krok'],controls,[31,95,75,95],'#174A70');
grid('Business a FREQ',['Původní FREQ ID — nepřečíslováno','Název / oblast','Zdrojový text / analytický vstup','EA GUID','EA cesta','Autor v podkladu','EA modified / datum podkladu','Zdroj vstupu','Stav vstupu / MVP','Aktuální business text — k doplnění','Přímá EA vazba na capability','Přímé EA business vazby','Přímé EA requirement vazby','Odpovědnost Group / CZ','Potvrzený analytický zdroj / sekce','Rozpor / otevřený bod','Stav dalšího kroku'],d.business,[26,64,85,45,65,22,27,60,43,70,75,75,65,60,65,85,60],'#8A6712');
grid('EA SREQ',['SREQ ID','EA GUID','EA název','EA text / dokumentace','Autor EA','EA modified','Přímo připojené aplikační funkce / GUID','Zdroj','Stav baseline','Potvrzené FREQ / zdroj','Odpovědnost Group / CZ','Rozhodnutí / navržená změna'],d.sreq,[25,45,65,100,22,26,100,15,40,65,55,65],'#174A70');
function append(name,start,headers,rows){
 const s=w.worksheets.getItem(name),r=s.getRangeByIndexes(0,start,rows.length+1,headers.length);r.values=[headers,...rows];r.format.wrapText=true;r.format.verticalAlignment='top';
 s.getRangeByIndexes(0,start,1,headers.length).format={fill:'#174A70',font:{bold:true,color:'#FFFFFF'},rowHeight:48,wrapText:true};
 headers.forEach((_,j)=>s.getRangeByIndexes(0,start+j,rows.length+1,1).format.columnWidth=[48,48,65,100,100,55,80][j]);
}
const h=['EA kontrola SREQ — v02','EA SREQ GUID','Aktuální název v EA','Aktuální text v EA','Přímé funkce v EA / GUID','Zdroj kontroly','Další krok / omezení'];append('FREQ mapping',16,h,d.mapping);
const map=new Map(original['FREQ mapping'].values.slice(1).map((r,i)=>[r[0]+'|'+r[5],d.mapping[i]]));
append('SREQ Aplikační role',16,h,original['SREQ Aplikační role'].values.slice(1).map(r=>map.get(r[0]+'|'+r[1])||['Bez spojení','','','','','','Ověřit aplikační klíč/SREQ.']));
w.worksheets.getItem('FREQ mapping').getRange('P2:P220').values=d.mapping.map(r=>[r[0]+'; sémantické potvrzení a AS-IS delta zůstávají otevřené.']);
w.worksheets.getItem('SREQ Aplikační role').getRange('P2:P220').values=original['SREQ Aplikační role'].values.slice(1).map(r=>[(map.get(r[0]+'|'+r[1])?.[0]||'Bez spojení')+'; sémantické potvrzení a AS-IS delta zůstávají otevřené.']);
const fun=w.worksheets.getItem('Functionalities');fun.getRange('L2:L956').values=d.functionNotes.map(text=>[text.replaceAll('NEOVĚŘENO — čeká na EA/XMI','EA export je dostupný; shoda konkrétní funkce zatím není potvrzena')]);
const ints=w.worksheets.getItem('Interfaces');ints.getRange('J2:J55').values=d.interfaceNotes.map(text=>[text.replaceAll('NEOVĚŘENO — čeká na EA/XMI','EA export dostupný; detailní shoda rozhraní neověřena')]);
w.worksheets.getItem('Cover').getRange('A13:B19').values=[['Pracovní verze 02 — 1.11.2026','Začni listem Postup revize; navazuje Business a FREQ.'],['Stav','EA export načten; business baseline se ověřuje z posledních podkladů Martina Dostála v rámci závazného MVP.'],['Originál','Zdrojové Book1 a Atlas.xml beze změny; historické sloupce a ID zachovány.'],['Postup revize','Zdroje, scope, kroky a otevřená rozhodnutí.'],['Business a FREQ','159 modelových FREQ záznamů + 6 UC005 analytických vstupů; čekají na sjednocení s aktuální analýzou.'],['EA SREQ','111 modelových SREQ prvků, jejich GUID a přímé aplikační vazby.'],['Cílový výstup','Potvrzená business → application traceability, aktualizovaný EA model a následně SO Word.']];
const rev=w.worksheets.getItem('Revize MVP');rev.getRange('B17:C17').values=[['EA export dostupný; první kontrola ID dokončena','Viz nové sloupce a Postup revize. Úplná sémantická kontrola vrstev a kontraktů není dokončena.']];rev.getRange('B19:C19').values=[['Dokončit aktuální business baseline z Martinových podkladů','Atlas.xml již načten. Nejprve analýza/MVP/FREQ a business, poté modrá vrstva a SO.']];
w.worksheets.getItem('Cover').getRange('A13:B19').format.wrapText=true;w.worksheets.getItem('Cover').getRange('A13:B19').format.rowHeight=60;
await w.recalculate();
await (await SpreadsheetFile.exportXlsx(w)).save('work/book1/v02-authored.xlsx');
for(const [name,range,file] of [['Postup revize','A1:D5','v02-postup'],['Business a FREQ','A160:C166','v02-business'],['EA SREQ','A1:D4','v02-sreq'],['FREQ mapping','Q6:S8','v02-map'],['SREQ Aplikační role','Q2:S4','v02-role'],['Cover','A13:B19','v02-cover'],['Revize MVP','A17:C19','v02-review'],['Functionalities','L2:L4','v02-functions'],['Interfaces','J2:J4','v02-interfaces']]){
 const p=await w.render({sheetName:name,range,scale:1,format:'png'});await fs.writeFile('work/book1/'+file+'.png',new Uint8Array(await p.arrayBuffer()));
}
console.log(JSON.stringify({authored:true,businessRows:d.business.length,sreqRows:d.sreq.length,mappingRows:d.mapping.length}));
