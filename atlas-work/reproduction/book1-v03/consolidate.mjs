import fs from 'node:fs/promises';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const require=createRequire('C:/Users/zsery/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/package.json');
const {FileBlob,SpreadsheetFile}=await import(pathToFileURL(require.resolve('@oai/artifact-tool')).href);
const dir='work/book1-consolidation';
const plan=JSON.parse(await fs.readFile(`${dir}/changes.json`,'utf8'));
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('outputs/book1-v02/Book1_Atlas_pracovni_v02_2026-11-01.xlsx'));
console.log('Imported v02, sheets:',wb.worksheets.items.length);
for(const [name,start,end,lastCol,styleRow] of [['Postup revize',35,47,'D',34],['Revize MVP',20,26,'C',19]]){
 const s=wb.worksheets.getItem(name);
 for(let r=start;r<=end;r++)s.getRange(`A${r}:${lastCol}${r}`).copyFrom(s.getRange(`A${styleRow}:${lastCol}${styleRow}`),'all');
 s.getRange(`A${start}:${lastCol}${end}`).format.wrapText=true;
 s.getRange(`A${start}:${lastCol}${end}`).format.verticalAlignment='top';
 s.getRange(`A${start}:${lastCol}${end}`).format.rowHeight=105;
}
for(const [name,changes] of Object.entries(plan.operations)){
 const s=wb.worksheets.getItem(name);
 for(const [ref,value] of Object.entries(changes))s.getRange(ref).values=[[value]];
 console.log('Updated',name,Object.keys(changes).length);
}
wb.worksheets.getItem('Cover').getRange('A13:B19').format.rowHeight=80;
wb.worksheets.getItem('Cover').getRange('A13:B19').format.wrapText=true;
wb.worksheets.getItem('Revize MVP').getRange('A20:C26').format.font.size=11;
wb.worksheets.getItem('Revize MVP').getRange('A20:A26').format.fill='#174A70';
wb.worksheets.getItem('Revize MVP').getRange('A20:A26').format.font.color='#FFFFFF';
wb.worksheets.getItem('Revize MVP').getRange('A20:A26').format.font.bold=true;
for(const [name,row,end] of [['Functionalities',315,'L'],['FREQ mapping',49,'W'],['SREQ Aplikační role',49,'W']]){
 wb.worksheets.getItem(name).getRange(`A${row}:${end}${row}`).format.rowHeight=150;
}
for(const row of [4,12,17,18])wb.worksheets.getItem('Interfaces').getRange(`A${row}:K${row}`).format.rowHeight=150;
await wb.recalculate();
for(const [name,changes] of Object.entries(plan.operations)){
 const s=wb.worksheets.getItem(name);
 for(const [ref,expected] of Object.entries(changes)){
  const actual=s.getRange(ref).values[0][0];if(actual!==expected)throw new Error(`Value mismatch ${name}!${ref}`);
 }
}
const inspected=await wb.inspect({kind:'table',range:"'Revize MVP'!A20:C26",include:'values,formulas',tableMaxRows:7,tableMaxCols:3,maxChars:2200});
await fs.writeFile(`${dir}/artifact-inspection.ndjson`,inspected.ndjson);
await (await SpreadsheetFile.exportXlsx(wb)).save(`${dir}/authored.xlsx`);
console.log('Exported authored changes; native preservation follows.');
for(const [name,range,slug] of [
 ['Cover','A13:B19','cover'],['Postup revize','A35:D37','identity-controls'],
 ['Postup revize','A38:D40','sources-controls'],['Business a FREQ','I161:J166','uc005'],
 ['Business a FREQ','P9:Q11','text-conflicts'],['EA SREQ','I22:L22','ea-identity'],
 ['Revize MVP','A20:C26','revision'],['Interfaces','I4:K4','interface'],
 ['FREQ mapping','K49:N49','freq-identity'],['SREQ Aplikační role','L49:N49','sreq-identity'],
 ['Functionalities','J315:L315','function-identity']]){
 const png=await wb.render({sheetName:name,range,scale:1,format:'png'});
 await fs.writeFile(`${dir}/${slug}.png`,new Uint8Array(await png.arrayBuffer()));
 console.log('Rendered',slug);
}
console.log('Artifact authoring and value verification completed:',plan.summary.changedCells);
