from pathlib import Path
import zipfile
from lxml import etree as E
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
for label,source in [('before',HERE/'canonical-before.xlsx'),('after',ROOT/'outputs/Book1_2026-11-03/Book1_Atlas_konsolidovany_2026-11-03.xlsx')]:
    with zipfile.ZipFile(source) as z,zipfile.ZipFile(HERE/(label+'-visible.xlsx'),'w',zipfile.ZIP_DEFLATED) as out:
        for name in z.namelist():
            data=z.read(name)
            if name.startswith('xl/worksheets/') and name.endswith('.xml'):
                root=E.fromstring(data)
                for row in root.findall('.//{*}sheetData/{*}row'):
                    row.attrib.pop('hidden',None)
                data=E.tostring(root,encoding='utf-8',xml_declaration=True)
            out.writestr(name,data)
print('Temporary preview copies only; delivered hidden states unchanged.')
