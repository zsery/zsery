from pathlib import Path
import shutil,hashlib,json
root=Path('C:/Users/zsery2/Documents/Codex/2026-11-03/pokra-uj-v-pr-ci-atlas/zsery/atlas-work')
out=root/'outputs/EA_SO_2026-11-05';out.mkdir(exist_ok=True)
for name in ['Confluence_AuthX_overeni_2026-11-05.md','ServiceHub_SO_zmenove_kapitoly_2026-11-05.md','ServiceHub_SO_zmenove_kapitoly_2026-11-05.docx','Atlas_UC_AuthX_review_2026-11-05.7z']:
    shutil.copy2(Path('outputs')/name,out/name)
shutil.copy2('work/ea-authx-review/Kontrola_AuthX_doplneni.json',out/'Kontrola_AuthX_doplneni.json')
repro=root/'reproduction/uc-review-2026-11-05'
for name in ['build_so.py','export_so_text.py','add_authx_evidence.py','extract_lo_layout.py','checkpoint_2026_11_05.py','checkpoint_verified_2026_11_05.py']:
    shutil.copy2(Path('work')/name,repro/name)
qa=out/'qa-so-zmenove-kapitoly';qa.mkdir(exist_ok=True)
for n in range(1,5):shutil.copy2(Path('work/so-render-final2')/f'page-{n}.png',qa/f'page-{n}.png')
doc=out/'ServiceHub_SO_zmenove_kapitoly_2026-11-05.docx'
report={'document':doc.name,'sha256':hashlib.sha256(doc.read_bytes()).hexdigest(),'renderer':'Original documents skill render_docx.py, unchanged','backend':'LibreOffice 26.8.2 x64, extracted locally from official MSI without executing installer actions','backend_msi_sha256':'ff4b911403b67ee9e6249f820f9782c44bb32c94fdaa45b0da53a8e419e5307a','pages':4,'all_pages_visually_inspected':True,'visual_result':'No clipping, overlapping text, truncated tables or missing glyphs observed','scope':'Change chapters only; not the full 32-page SO in OneDrive','date':'2026-11-05'}
(qa/'Kontrola_DOCX.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
(repro/'README.md').write_text('''# Reprodukce a ověření 5. listopadu 2026

Použij vlastní aktuální Python s lxml, python-docx a dokumentový skill. Cesty k původnímu pracovnímu repozitáři v audit_traceability.py nahraď vlastním checkoutem; původní XML má vstupní SHA ověřený ve skriptech. Nepoužívej skripty naslepo na novější živý model.

1. Předchozí revise_ea.py vytvoří osmipolovou dokumentační revizi ze zdrojového Atlas.xml. audit_traceability.py vytvoří audit původních GUIDů proti uložené historické UC matici.
2. build_ea_review_layer.py čte tuto konkrétní revizi a přidá oddělenou navrženou analytickou vrstvu: 30 Artifact, 65 candidate trace, 7 diagramů. Nejde o schválené FREQ/SREQ ani realization. Všechny vstupní bajty jsou obnovitelné odstraněním označených aditivních bloků.
3. add_authx_evidence.py doplní primárně ověřený Confluence kontrakt do jediného AD-02 documentation pole. Všechny ostatní bajty zachová. Nejnovější model SHA: dc3eb22fb5469726f475b416efeddb58a8976512954ff1ed6788d0bbe5e3ba8a. Nativní import EA neověřen.
4. build_so.py vytvoří čtyřstránkové změnové kapitoly, nikoli náhradu celého SO. export_so_text.py vytvoří jejich Markdown. K vydání DOCX je nutné použít původní render_docx.py a prohlédnout všechny stránky. Doklady zde proběhlé kontroly jsou v qa-so-zmenove-kapitoly.

Na tomto Windows chyběl LibreOffice. Oficiální MSI 26.8.2 x64 má SHA256 ff4b911403b67ee9e6249f820f9782c44bb32c94fdaa45b0da53a8e419e5307a; zdroj a hash viz Confluence_AuthX_overeni není zdroj runtime, runtime zdroj je https://download.documentfoundation.org/libreoffice/stable/26.8.2/win/x86_64/LibreOffice_26.8.2_Win_x86-64.msi.mirrorlist. Administrativní msiexec extract skončil 1601, služba Installer nebyla dostupná. Následně 7-Zip rozbalil soubory MSI do work/lo-flat a extract_lo_layout.py přečetl pouze File/Component/Directory databázové tabulky přes msi.dll a zrekonstruoval layout do work/libreoffice; 19427 souborů, žádný chybějící. Installer custom actions se nespouštějí. Programový adresář se přidá na PATH pouze procesu rendereru. Na jiném PC preferuj vlastní funkční LibreOffice/bundled renderer. MSI a rozbalený runtime se do Git nedávají.

Checkpoint skripty jsou evidence provedeného přenosu, ne obecné instalační nástroje; obsahují původní lokální cesty a historický stav. Aktuální pokračování řídí STATE_2026-11-05.md. Přihlašovací údaje nejsou součástí předání.
''',encoding='utf-8')
state=root/'STATE_2026-11-05.md';text=state.read_text(encoding='utf-8')
banner='''
## Aktualizace po ověření rendereru a Confluence 5. 11. 2026

- Předchozí checkpoint 6736f5cbedd1c1bf070651c067a5dfd306277ec8 byl úspěšně pushnut a remote SHA ověřeno. Projektový skill prošel quick_validate.py s Python UTF-8 režimem; PyYAML bylo doplněno jen do lokálního work/python-deps.
- Confluence přihlášení je aktivní. Přímo přečten TS - AuthX - authx-ts, část 3.2.1, stránka last modified 4.6.2026. Nově doloženo POST /OAuth2TokenExchangeGrant/v2/token, APIX scopes OAUTH2_TOKEN_EXCHANGE_GRANT a TMF691_FEDERATED_IDENTITY_ALL, form-urlencoded grant_type, subject_token_type, subject_token a povinný subject_token_iss. Response UserInfo assets jsou i v tokenu; token opravňuje jen k assets odpovědi. Kompletní ověření a hranice důkazů v outputs/EA_SO_2026-11-05/Confluence_AuthX_overeni_2026-11-05.md.
- Nejnovější pracovní model je Atlas_UC_AuthX_review_2026-11-05.7z, XML SHA dc3eb22fb5469726f475b416efeddb58a8976512954ff1ed6788d0bbe5e3ba8a. Obsahuje předchozí review vrstvu a přesné doplnění AD-02 podle Confluence. Nativní import/diagram QA stále neověřené.
- LibreOffice bylo lokálně rozbaleno z oficiálního a hashově ověřeného MSI; původní render_docx.py už funguje. Nové ServiceHub_SO_zmenove_kapitoly_2026-11-05.docx prošly renderem i přímou vizuální kontrolou všech čtyř stran, bez pozorovaných vad. DOCX a kontrolní PNG/JSON jsou v outputs/EA_SO_2026-11-05. Tento dokument je dodatek se změnovými kapitolami, není plný nový SO z OneDrive.
- V AI kopii Book1 Copilot vytvořil Audit_2026_11_05, rozsah A1:F32, s 26 nálezy, přesnými buňkami, podpůrnými odkazy, vysvětlením a omezeními. Ohlásil zachování ostatních listů; nový tab byl přímo viditelný. Nejde o potvrzení pravdivosti každého nálezu ani provedení všech oprav.
- Uživatel v této VDI relaci aktivně píše do Copilotu; nezasahuj do rozpracovaného vstupu. Nové komentáře a komunikace piš česky; původní anglické requirement texty zachovej.
- Celý 32stránkový SO v AI a jeho Word Copilot audit ještě nejsou obsahově/vizuálně uzavřené. Vrať se k nim po dokončení uživatelského vstupu. Nativní EA import a role/SNOW klientské kontrakty také nesmějí být prohlášeny za hotové. Starší části níže popisují historii; zejména nedostupnost rendereru je už vyřešená.

Další krok: v AI Book1 přímo otevřít nový Audit_2026_11_05, ověřit skutečné buňky pro nálezy a provést jen podložené analytické opravy. Poté přečíst dokončenou Word Copilot kontrolu celého AI SO, doplnit nové Confluence AuthX poznatky do pracovní kopie a ověřit technické SNOW detaily přes Confluence / Teams Confluence agenta. Zachovat zdroje a správné změny Copilota.
'''
if '## Aktualizace po ověření rendereru a Confluence 5. 11. 2026' not in text:
    first,rest=text.split('\n',1);state.write_bytes((first+'\n'+banner+'\n'+rest).encode('utf-8'))
manifest=root/'SHA256SUMS.txt';files=sorted(p for p in root.rglob('*') if p.is_file() and p!=manifest)
manifest.write_bytes(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(root).as_posix()+'\n' for p in files).encode('utf-8'))
print('Verified checkpoint:',len(files),'files')
