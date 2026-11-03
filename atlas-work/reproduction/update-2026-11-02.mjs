import fs from 'node:fs/promises';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const req=createRequire('C:/Users/zsery/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/package.json');
const {FileBlob,SpreadsheetFile}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const source='outputs/book1-revize/Book1_MVP_revize_2026-11-01.xlsx';
const outDir='outputs/Book1_Solution_2026-11-02';
await fs.mkdir(outDir,{recursive:true});
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(source));
const userSource='U2 — výslovné pravidlo uživatele, 2026-11-02';
const iface=wb.worksheets.getItem('Interfaces');
iface.getRange('L1:M1').values=[['Pravidlo identity potvrzené uživatelem','Zdroj pravidla']];
const irows=iface.getUsedRange().values;
const noteById={
 IF_DXL_01:'Vazba VFID sub ↔ odpovídající ONSC user nebo WSC user je 1:1. E-mail může být atribut identity, není párovacím klíčem. TMF691 nese holding jako parent–child strukturu.',
 IF_ONSC_01:'Každý ONSC user se mapuje na VFID sub v poměru 1:1. E-mail není párovací klíč. Holding se v TMF691 zachycuje parent–child strukturou.',
 IF_IDAAS_02:'VFID sub je identifikátor pro 1:1 vazbu na odpovídající ONSC/WSC user. E-mail je pouze atribut a nelze jej použít jako párovací klíč.',
 IF_WSC_01:'Každý WSC user se mapuje na VFID sub v poměru 1:1. E-mail není párovací klíč. Holding se v TMF691 zachycuje parent–child strukturou.'
};
const touched={interfaces:[]};
for(let r=1;r<irows.length;r++){
 const id=String(irows[r][0]??''); if(noteById[id]){iface.getRange(`L${r+1}:M${r+1}`).values=[[noteById[id],userSource]];touched.interfaces.push(id);}
}
const rev=wb.worksheets.getItem('Revize MVP');
const start=rev.getUsedRange().values.length+1;
const added=[
 ['U2 — identita','VFID sub ↔ ONSC user / WSC user je vždy 1:1.','Výslovné pravidlo uživatele, 2026-11-02. Použít stabilní VFID sub; e-mail není konzistentní a nesmí být párovacím klíčem. Termín „subscriber“ není použit.'],
 ['U2 — holding','TMF691 nese holding jako strukturu parent–child.','Výslovné pravidlo uživatele, 2026-11-02. Udržet strukturu holdingů; nevydávat ji za mapování user identity.'],
 ['U2 — hranice interpretace','Vazba user identity a holding hierarchie jsou dvě různé věci.','VFID sub ↔ ONSC/WSC user 1:1; parent–child je struktura holdingů v TMF691. Detaily kardinality holdingů a konkrétního payloadu musí potvrdit API kontrakt.']
];
rev.getRange(`A${start}:C${start+added.length-1}`).values=added;
rev.getRange(`A${start}:C${start+added.length-1}`).format.wrapText=true;
rev.getRange(`A${start}:C${start+added.length-1}`).format.verticalAlignment='top';
rev.getRange(`A${start}:A${start+added.length-1}`).format={fill:'#174A70',font:{bold:true,color:'#FFFFFF'},wrapText:true};
rev.getRange(`B${start}:C${start+added.length-1}`).format={wrapText:true,verticalAlignment:'top'};
rev.getRange(`A${start}:A${start+added.length-1}`).format.columnWidth=28;
rev.getRange(`B${start}:B${start+added.length-1}`).format.columnWidth=70;
rev.getRange(`C${start}:C${start+added.length-1}`).format.columnWidth=110;
const f=wb.worksheets.getItem('FREQ mapping');
const fvals=f.getUsedRange().values;
const freqRows=[];
for(let r=1;r<fvals.length;r++){
 if(String(fvals[r][0]??'')==='DXL' && String(fvals[r][1]??'')==='F-REQ-IAM-21' && String(fvals[r][5]??'')==='SREQ-ID-06'){
  const cell=f.getRange(`L${r+1}`);cell.values=[[String(cell.values[0][0]??'')+'\nIdentity rule: VFID sub ↔ ONSC/WSC user is 1:1; email is not the mapping key.']];
  f.getRange(`N${r+1}`).values=[[String(f.getRange(`N${r+1}`).values[0][0]??'')+'; '+userSource]];freqRows.push(r+1);
 }
}
const sr=wb.worksheets.getItem('SREQ Aplikační role');
const svals=sr.getUsedRange().values; const sreqRows=[];
for(let r=1;r<svals.length;r++){
 if(String(svals[r][0]??'')==='DXL' && String(svals[r][1]??'')==='SREQ-ID-06'){
  sr.getRange(`M${r+1}`).values=[[String(sr.getRange(`M${r+1}`).values[0][0]??'')+'\nVFID sub ↔ ONSC/WSC user: 1:1. E-mail není párovací klíč.']];
  sr.getRange(`N${r+1}`).values=[[String(sr.getRange(`N${r+1}`).values[0][0]??'')+'; '+userSource]];sreqRows.push(r+1);
 }
}
const fun=wb.worksheets.getItem('Functionalities');
const vals=fun.getUsedRange().values;const functionRows=[];
for(let r=1;r<vals.length;r++){
 if(String(vals[r][4]??'')==='DXL' && /F_DXL_L4 - Resolve VFID identity to User ID/i.test(String(vals[r][1]??''))){
  fun.getRange(`K${r+1}`).values=[[String(fun.getRange(`K${r+1}`).values[0][0]??'')+'\nUser identity key: VFID sub ↔ ONSC/WSC user is 1:1; email is not the mapping key.']];
  fun.getRange(`L${r+1}`).values=[[String(fun.getRange(`L${r+1}`).values[0][0]??'')+' Rule supplied by user 2026-11-02.']];functionRows.push(r+1);
 }
}
await wb.recalculate();
const output=`${outDir}/Book1_Atlas_MVP_revize_2026-11-02.xlsx`;
await (await SpreadsheetFile.exportXlsx(wb)).save(output);
const previews=[];
for(const [sheetName,range,name] of [['Revize MVP',`A${start}:C${start+2}`,'rules'],['Interfaces','L1:M5','interfaces'],['FREQ mapping',`K${freqRows[0]}:N${freqRows[0]}`,'freq'],['SREQ Aplikační role',`L${sreqRows[0]}:N${sreqRows[0]}`,'sreq'],['Functionalities',`J${functionRows[0]}:L${functionRows[0]}`,'functionality']]){
 const blob=await wb.render({sheetName,range,scale:1,format:'png'});const p=`work/book1/updated-${name}.png`;await fs.writeFile(p,new Uint8Array(await blob.arrayBuffer()));previews.push(p);
}
console.log(JSON.stringify({output,sheets:wb.worksheets.items.length,addedRuleRows:added.length,interfaces:touched.interfaces,freqRows,sreqRows,functionRows,previews},null,2));
