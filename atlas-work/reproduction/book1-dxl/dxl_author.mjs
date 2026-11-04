import fs from 'node:fs/promises';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
import os from 'node:os';
import path from 'node:path';
const require=createRequire(process.env.CODEX_NODE_PACKAGE_JSON||path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/package.json'));
const {FileBlob,SpreadsheetFile}=await import(pathToFileURL(require.resolve('@oai/artifact-tool')).href);
const dir='work/book1-consolidation';
const plan=JSON.parse(await fs.readFile(`${dir}/delta.json`,'utf8'));
const mode=process.argv[2]||'before';
const file=process.argv[3]||(mode==='final'?'outputs/Book1_2026-11-03/Book1_Atlas_konsolidovany_2026-11-03.xlsx':`${dir}/canonical-before.xlsx`);
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(file));
console.log('Imported',mode,wb.worksheets.items.length);
if(mode==='edit'){
 for(const [name,cells] of Object.entries(plan.operations)){
  const sheet=wb.worksheets.getItem(name);
  if(name==='Postup revize')sheet.getRange('A57:D57').copyFrom(sheet.getRange('A56:D56'),'all');
  for(const [ref,value]of Object.entries(cells))sheet.getRange(ref).values=[[value]];
  for(const row of new Set(Object.keys(cells).map(r=>Number(r.match(/\d+/)[0])))){
   sheet.getRange(`A${row}`).format.rowHeight=name==='Postup revize'?150:300;
  }
 }
 wb.recalculate();
 await (await SpreadsheetFile.exportXlsx(wb)).save(`${dir}/authored.xlsx`);
}
if(mode!=='before'){
 let count=0;
 for(const [name,cells]of Object.entries(plan.operations))for(const [ref,value]of Object.entries(cells)){
  if(wb.worksheets.getItem(name).getRange(ref).values[0][0]!==value)throw Error(`Mismatch ${name}!${ref}`);count++;
 }
 console.log('Verified',count,'cells');
 if(mode==='final')await fs.writeFile(`${dir}/reimport-qa.json`,JSON.stringify({reimportedFinalWorkbook:true,sheets:wb.worksheets.items.length,verifiedAuthoredCells:count,nativeExcelRecalculation:false},null,2));
}
const targets=mode==='before'?[['Interfaces','I4:K4','interface']]:[
 ['Interfaces','I2:K2','customer'],['Interfaces','I4:K4','identity'],
 ['Postup revize','A55:D57','evidence'],
 ...Object.entries(plan.operations).filter(([s])=>!['Interfaces','Postup revize'].includes(s)).map(([s,c])=>{
  const row=Number(Object.keys(c)[0].match(/\d+/)[0]);
  const cols={'Functionalities':['J','L'],'FREQ mapping':['K','N'],'SREQ Aplikační role':['L','O'],'Business a FREQ':['I','J']}[s];
  return [s,`${cols[0]}${row}:${cols[1]}${row}`,s.replaceAll(' ','-')];
 })];
for(const [sheetName,range,slug]of targets){
 const png=await wb.render({sheetName,range,scale:1,format:'png'});
 await fs.writeFile(`${dir}/${mode}-${slug}.png`,new Uint8Array(await png.arrayBuffer()));
}
