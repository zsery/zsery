# Reprodukce a ověření 5. listopadu 2026

Použij vlastní aktuální Python s lxml, python-docx a dokumentový skill. Cesty k původnímu pracovnímu repozitáři v audit_traceability.py nahraď vlastním checkoutem; původní XML má vstupní SHA ověřený ve skriptech. Nepoužívej skripty naslepo na novější živý model.

1. Předchozí revise_ea.py vytvoří osmipolovou dokumentační revizi ze zdrojového Atlas.xml. audit_traceability.py vytvoří audit původních GUIDů proti uložené historické UC matici.
2. build_ea_review_layer.py čte tuto konkrétní revizi a přidá oddělenou navrženou analytickou vrstvu: 30 Artifact, 65 candidate trace, 7 diagramů. Nejde o schválené FREQ/SREQ ani realization. Všechny vstupní bajty jsou obnovitelné odstraněním označených aditivních bloků.
3. add_authx_evidence.py doplní primárně ověřený Confluence kontrakt do jediného AD-02 documentation pole. Všechny ostatní bajty zachová. Nejnovější model SHA: dc3eb22fb5469726f475b416efeddb58a8976512954ff1ed6788d0bbe5e3ba8a. Nativní import EA neověřen.
4. build_so.py vytvoří čtyřstránkové změnové kapitoly, nikoli náhradu celého SO. export_so_text.py vytvoří jejich Markdown. K vydání DOCX je nutné použít původní render_docx.py a prohlédnout všechny stránky. Doklady zde proběhlé kontroly jsou v qa-so-zmenove-kapitoly.

Na tomto Windows chyběl LibreOffice. Oficiální MSI 26.8.2 x64 má SHA256 ff4b911403b67ee9e6249f820f9782c44bb32c94fdaa45b0da53a8e419e5307a; zdroj a hash viz Confluence_AuthX_overeni není zdroj runtime, runtime zdroj je https://download.documentfoundation.org/libreoffice/stable/26.8.2/win/x86_64/LibreOffice_26.8.2_Win_x86-64.msi.mirrorlist. Administrativní msiexec extract skončil 1601, služba Installer nebyla dostupná. Následně 7-Zip rozbalil soubory MSI do work/lo-flat a extract_lo_layout.py přečetl pouze File/Component/Directory databázové tabulky přes msi.dll a zrekonstruoval layout do work/libreoffice; 19427 souborů, žádný chybějící. Installer custom actions se nespouštějí. Programový adresář se přidá na PATH pouze procesu rendereru. Na jiném PC preferuj vlastní funkční LibreOffice/bundled renderer. MSI a rozbalený runtime se do Git nedávají.

Checkpoint skripty jsou evidence provedeného přenosu, ne obecné instalační nástroje; obsahují původní lokální cesty a historický stav. Aktuální pokračování řídí STATE_2026-11-05.md. Přihlašovací údaje nejsou součástí předání.
