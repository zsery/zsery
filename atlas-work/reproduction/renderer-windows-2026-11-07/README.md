# Původní renderer na této Windows instanci

Použit původní render_docx.py z dokumentového skillu beze změny. Windows balík skillu LibreOffice neobsahoval; připraven oddělený runtime z oficiálního LibreOffice 26.8.2 x86-64 MSI, bez systémové instalace.

Zdroj: https://download.documentfoundation.org/libreoffice/stable/26.8.2/win/x86_64/LibreOffice_26.8.2_Win_x86-64.msi
SHA256: ff4b911403b67ee9e6249f820f9782c44bb32c94fdaa45b0da53a8e419e5307a

Administrativní msiexec extrakce selhala 1601 / 0x80070005. Standardní 7-Zip extrakce uspěla. reconstruct_msi.py čte MSI databázi pouze pro čtení a sestaví jména souborů z tabulek Directory, Component a File. Výsledek 19427 souborů, 0 chybějících. Vyžaduje Python s msilib (zde dodaný runtime Python 3.11).

Postup: rozbalit MSI přes 7z x do samostatné pracovní složky, spustit reconstruct_msi.py MSI EXTRACTED DESTINATION a přidat DESTINATION/LibreOffice/program na PATH pouze procesu rendereru. Potom spustit původní render_docx.py INPUT --output_dir QA_DIR --emit_pdf. Binární runtime ani MSI nepatří do GitHubu.

Smoke test na historickém ServiceHub_SO_zmenove_kapitoly_2026-11-05.docx uspěl: čtyři PNG a PDF 155824 B, exit 0. Jde pouze o test runtime, nikoli vizuální QA plného SO.

Plný SO získaný 7. listopadu je chráněný soubor (OLE magic d0cf11e0a1b11ae1, ve Wordu Restricted Access), nikoli přímo ZIP OOXML. Původní renderer dosud nevytvořil stránky. Ochrana se neměnila; na uživateli je příprava firemně povolené renderovatelné kopie. Samotný úspěšný přenos není obsahová ani vizuální validace.
