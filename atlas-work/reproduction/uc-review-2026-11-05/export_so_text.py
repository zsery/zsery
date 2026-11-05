from docx import Document
from docx.oxml.ns import qn
from pathlib import Path
d=Document('work/ServiceHub_SO_zmenove_kapitoly_neoverene.docx')
lines=['# ServiceHub Atlas CZ změnové kapitoly Solution Overview','',
'Stav: obsah připravený pro zapracování do původního SO; nejde o úplnou náhradu zdrojového dokumentu. DOCX nebyl vizuálně ověřen, protože dostupnému rendereru chybí LibreOffice.','']
for node in d.element.body:
    if node.tag==qn('w:p'):
        text=''.join(node.itertext())
        # itertext repeats run text in lxml OOXML; use Word paragraph abstraction.
        from docx.text.paragraph import Paragraph
        pp=Paragraph(node,d)
        if not pp.text:continue
        prefix='## ' if pp.style.name.startswith('Heading 1') else '### ' if pp.style.name.startswith('Heading 2') else ''
        if pp.style.name=='Title':continue
        lines.extend([prefix+pp.text,''])
    elif node.tag==qn('w:tbl'):
        from docx.table import Table
        t=Table(node,d)
        for i,row in enumerate(t.rows):
            vals=[c.text.replace('|','/').replace('\n',' ') for c in row.cells]
            lines.append('| '+' | '.join(vals)+' |')
            if i==0:lines.append('| '+' | '.join(['---']*len(vals))+' |')
        lines.append('')
text='\n'.join(lines).replace('pět dokumentačních polí AD-05, ASS-06, AD-07, ASS-03 a upřesnění SREQ-ID-07','osm dokumentačních polí AD-02, AD-05, AD-07, AD-08, ASS-03, ASS-06, ASS-07 a SREQ-ID-07')
Path('outputs/ServiceHub_SO_zmenove_kapitoly_2026-11-04.md').write_text(text,encoding='utf-8')
