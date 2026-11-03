import fs from 'node:fs/promises';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const req=createRequire('C:/Users/zsery/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/package.json');
const {FileBlob,SpreadsheetFile}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const dir='work/book1-consolidation';
const plan=JSON.parse(await fs.readFile(`${dir}/changes.json`,'utf8'));
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('outputs/Book1_2026-11-03/Book1_Atlas_konsolidovany_2026-11-03.xlsx'));
let cells=0;
if(wb.worksheets.items.length!==14)throw new Error('Expected 14 sheets');
for(const [name,changes]of Object.entries(plan.operations))for(const [ref,value]of Object.entries(changes)){
 if(wb.worksheets.getItem(name).getRange(ref).values[0][0]!==value)throw new Error(`Reimport mismatch ${name}!${ref}`);cells++;
}
for(const [name,range,slug]of [['Cover','A13:B19','final-cover'],['Revize MVP','A20:C22','final-identity']]){
 const blob=await wb.render({sheetName:name,range,scale:1,format:'png'});
 await fs.writeFile(`${dir}/${slug}.png`,new Uint8Array(await blob.arrayBuffer()));
}
const result={reimportedFinalWorkbook:true,sheets:14,verifiedAuthoredCells:cells,nativeExcelRecalculation:false};
await fs.writeFile(`${dir}/reimport-qa.json`,JSON.stringify(result,null,2));
console.log(JSON.stringify(result));
