from pathlib import Path
import shutil,hashlib,json
root=Path('C:/Users/zsery2/Documents/Codex/2026-11-03/pokra-uj-v-pr-ci-atlas/zsery/atlas-work')
skill=root/'instructions/skills/follow-explicit-scope/SKILL.md'
addition='''
## Přenos práce a zdroje – výslovné pokyny 5. 11. 2026

Technické informace, integrační kontrakty a jejich parametry ověřuj v Confluence. Použij přímou autorizovanou stránku nebo agenta v Teams s názvem **Confluence** (v dřívějším UI Confluence Agent). Vyžádej primární URL a dostupnou verzi či datum. Běžný Copilot není náhradou technické specifikace v Confluence. Pro ostatní vyhledávání, analýzu a práci s dokumenty/sešity používej Copilot. Rozlišuj návrh z emailu, technický kontrakt a potvrzení nasazení.

Pokud Confluence přístup chybí nebo vyprší, požádej uživatele o ruční přihlášení. Přihlášení neautomatizuj a nežádej heslo. Pokračuj nezávislou povolenou prací; technické mezery nevyplňuj odhadem.

Průběžně ukládej na GitHub také vlastní přenosné skills, mezistav, rozhodnutí, zdrojové odkazy, výstupy a reprodukční skripty. Udělej checkpoint po věcném milníku, před předáním a před ukončením práce; pushni pracovní větev a porovnej lokální a vzdálené SHA. Při nedostupné síti uchovej lokální checkpoint a výslovně uveď, že push není potvrzený. Main neměň. Nepřenášej přístupové údaje, SSH klíče, cookies ani přihlášené relace.

Předání musí odlišovat hotové a ověřené změny, rozpracované soubory a skutečné překážky, uvést další konkrétní krok a umístění pracovních kopií v OneDrive. Samotné zadání Copilotu není dokončení; ověř jeho výsledek. Zachovej jeho už provedené správné změny.

Uživatel výslovně zvolil zachování původního render_docx.py. Nepovažuj dřívější číselnou volbu 1 za platný souhlas s nahrazením rendereru Microsoft Wordem; konečné potvrzení bylo „Zachovej původní renderer“.
'''
text=skill.read_text(encoding='utf-8')
if '## Přenos práce a zdroje – výslovné pokyny 5. 11. 2026' not in text:
    skill.write_bytes((text+'\n'+addition).encode('utf-8'))
for name in ['AGENTS.md','AGENT_PROMPT.md','START_HERE.md']:
    p=root/name;t=p.read_text(encoding='utf-8')
    banner='\n## Aktuální checkpoint 5. 11. 2026\n\nPokyny ke zdrojům, přihlášení a průběžnému GitHub ukládání: instructions/skills/follow-explicit-scope/SKILL.md, sekce Přenos práce a zdroje. Nejnovější stav: STATE_2026-11-05.md. Starší časové zápisy níže jsou historie, nikoli současné potvrzení dokončení.\n'
    if '## Aktuální checkpoint 5. 11. 2026' not in t:
        first,rest=t.split('\n',1);p.write_bytes((first+'\n'+banner+'\n'+rest).encode('utf-8'))
out=root/'outputs/EA_SO_2026-11-05';out.mkdir(exist_ok=True)
for name in ['ServiceHub_AI_zmeny_2026-11-04.md']:
    shutil.copy2(Path('outputs')/name,out/name)
shutil.copytree('outputs/ServiceHub_traceability_2026-11-04',out/'ServiceHub_traceability_2026-11-04',dirs_exist_ok=True)
shutil.copy2('work/ea-review-layer/Kontrola_UC_review.json',out/'Kontrola_UC_review.json')
archive=Path('outputs/Atlas_UC_review_2026-11-04.7z')
if archive.exists():shutil.copy2(archive,out/archive.name)
repro=root/'reproduction/uc-review-2026-11-05';repro.mkdir(exist_ok=True)
for name in ['audit_traceability.py','build_ea_review_layer.py','build_so.py','export_so_text.py']:
    shutil.copy2(Path('work')/name,repro/name)
pending=root/'pending/so-render-2026-11-05';pending.mkdir(exist_ok=True)
shutil.copy2('work/ServiceHub_SO_zmenove_kapitoly_neoverene.docx',pending/'ServiceHub_SO_zmenove_kapitoly_NEOVERENO.docx')
state='''# Přenosný stav Atlas / ServiceHub – 5. listopadu 2026

Uživatelský cíl stále platí: zkontrolovat aktuální Book1 po práci Copilota a dokončit navazující EA a vlastní SO bez zničení jeho změn. Pracovní větev codex/atlas-stav-2026-11-01, main beze změny. Toto je věcný mezistav, nikoli tvrzení o úplném dokončení.

## Pravidla pro jiný počítač

Načti AGENTS.md a instructions/skills/follow-explicit-scope/SKILL.md. Technické specifikace Confluence přímo nebo Teams agent Confluence; ostatní Copilot. Při vypršení přístupu požádej o ruční login. Používej vlastní přihlášení a runtime; nepřenášej cookies ani klíče. Změny zdrojů VDI zakázané, výjimka pracovní složka Documents/Projects/ServiceHub/AI. Na jiném PC instaluj potřebné host dovednosti standardní cestou a použij zde uložený vlastní projektový skill. Konkrétní lokální absolutní cesty nejsou podmínkou pokračování.

## Skutečně provedené změny OneDrive

- Aktuální sedmilistý Documents/Projects/ServiceHub/Atlas/Book1.xlsx byl funkcí Copy to zkopírován do Documents/Projects/ServiceHub/AI/Book1.xlsx. Nejde o starý 14listý lokální soubor.
- Excel Copilot v AI kopii změnil pouze FREQ mapping D109 a H109. Přímou kontrolou formula bar ověřeno D109 = CONFLICT ALLOW/DENY; H109 výslovně popisuje C109 allow vs J109 deny a nutnost role rozhodnutí. Zdrojový FREQ, SREQ a funkcionalita se neměnily.
- CRM-04 ↔ IAM-25 a CRM-03 ↔ IAM-24 už Copilot opravil; správné aktuální vazby znovu neměnit.
- Teams Copilot vytvořil celý nový Solution_Overview_ServiceHub_Revised_MVP_2026-11-04.docx. Otevřen ve WordWeb: 32 stran, 8598 slov. Z Documents/Copilot/Created byl přes Move File přemístěn do Documents/Projects/ServiceHub/AI. File menu následně ukázalo Autosaved online to AI. Původní SO zůstal zachovaný. Celková obsahová a vizuální QA nového SO ještě není potvrzená.

## Audit Book1 – dokončená odpověď Copilotu, čtení pokračuje

Excel Copilot uvedl audit všech 219 řádků A2:M220 napříč 9 aplikacemi, bez editace, včetně skutečných textů odkazovaných funkcionalit. Výslovně uvedl, že znovu nevalidoval primární UC dokumenty. Neoznačovat jeho závěr za nezávislý primární audit.

Přečtené nálezy: (1) ř.109 jediný výslovný allow/deny reversal, správně označen; (2–4) ř.105,106,108 úplný deny versus generic page v rolích F105,F106,F108 a Functionalities H517,H518,H520; D stále SHODA; (5) ř.107,110–112 blanket allow role enum neuzavřen proti conditional eligibility; (6) navigace ř.101/218 all authenticated vs role gating, konflikt již poznamenán H101/H218, navigace mimo MVP; (7) ř.121/213 povinná ruční volba vs automaticky založený CRM kontext; (8) ř.88 creation/ACTIVE vs potvrzená downstream aktivace; (9) ř.216 redirect product information vs generic page; (10) CRM ř.22,23,26 stale lookup/context/evaluation label vs CRM data, DXL retrieval, SH evaluation. Tvrzení Copilotu vyžadují cílené ověření před úpravou. Žádné tyto další změny dosud nebyly aplikovány.

Naposledy přečten začátek bodu 11 „DXL resolution — copied label overstates confirmed wiring responsibility“. Zbytek odpovědi je v panelu Excel Copilot na AI kopii Book1. Dokončit čtení, uložit audit do samostatného listu AI kopie, ověřit konkrétní buňky a provést jen podložené analytické změny status/notes. Nerozhodovat neznámé role ani neměnit primární requirement texty podle odhadu.

## Nová lokální modelová a scénářová práce

outputs/EA_SO_2026-11-05 obsahuje audit 30 UC podmínek proti 41 původním GUID (65 výskytů, 0 chybějících GUID). V původním exportu nemá žádný z těchto 41 FREQ incidentní konektor. Historický workbook hash matice není současný OneDrive baseline.

Nová aditivní vrstva Atlas_UC_review_2026-11-04.xml přidává samostatný navržený review package, 30 analytických Artifact uzlů, 65 candidate trace Dependency vazeb a 7 review diagramů. Nejde o nové schválené FREQ/SREQ ani realization. Vychází z předchozí osmipolové dokumentační revize. Každý vstupní bajt lze obnovit odebráním označených přidaných bloků; všechny původní konektory a diagramy ověřeně nezměněné. SHA-256 14f47b8a48f00668e8534a98057b19699265254e8f5ce157160031152ae28fc6. Nativní EA import a jeho vizuální QA neproběhly. Reprodukční skripty jsou přiložené; neaplikovat na jiný živý export naslepo.

Scenare_MVP.md obsahuje sedm logických scénářů UC005–UC011 s chybovými/kontextovými větvemi. API payloady, role enumy, retry, SNOW trasa a produkční oprávnění nejsou domyšleny.

## SO a renderer

Uživatel výslovně potvrdil „Zachovej původní renderer“. Microsoft Word se pro náhradu render_docx.py nepoužije. Lokální změnové kapitoly DOCX zůstávají v pending označené NEOVERENO; nejde o plný nový SO z OneDrive.

Chybějící LibreOffice: stažen oficiální LibreOffice 26.8.2 x64 MSI, 375934976 B, SHA256 ff4b911403b67ee9e6249f820f9782c44bb32c94fdaa45b0da53a8e419e5307a, shodný s oficiálním mirrorlistem https://download.documentfoundation.org/libreoffice/stable/26.8.2/win/x86_64/LibreOffice_26.8.2_Win_x86-64.msi.mirrorlist. Byl zkusen administrativní extract msiexec /a /qn TARGETDIR do work/libreoffice; existence výstupu ještě nepotvrzena. Runtime MSI nepatří do Git; na novém PC použij vlastní renderer/dependency setup. Původní render_docx.py na Windows hledá soffice.exe na PATH.

Word Copilot dostal v novém SO read-only audit celého dokumentu proti standalone MVP, manual V4, no prefill, VFID user1:1 a token exchange plus unsupported approvals a exact sections. Odpověď zatím nebyla přečtena. Nejprve ji dokončit a ověřit nálezy. Technické mezery potvrzovat v Confluence; metadata z emailu nejsou kompletní kontrakt.

## Nejbližší konkrétní kroky

1. Nově pozorovat VDI, otevřít AI Book1 a dočíst audit od bodu 11; uchovat jeho kompletní výsledek v novém audit listu AI kopie. Ověřit a opravit prokazatelné nesprávné status/notes bez změn originálu.
2. Přečíst dokončený audit nového SO, opravit jen AI kopii a provést obsahové i vizuální QA; technické podklady přes Confluence / Teams Confluence agenta, ruční login podle potřeby.
3. Zprovoznit původní render_docx.py doplněním LibreOffice; zkontrolovat všechny stránky před vydáním lokálního DOCX. Nepoužít Word jako náhradu.
4. Ověřit nový XML review import v nativním EA na pracovní kopii, zachovat původní GUIDy. Do té doby označovat jako navržený a neimportně ověřený model.
5. Průběžně aktualizovat tento stav, výstupy a skill, commit/push pracovní větve a ověřit remote SHA. Externí role/kontrakty a implementační approval nelze označit za uzavřené bez důkazu.
'''
(root/'STATE_2026-11-05.md').write_bytes(state.encode('utf-8'))
manifest=root/'SHA256SUMS.txt'
files=sorted(p for p in root.rglob('*') if p.is_file() and p!=manifest)
manifest.write_bytes(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(root).as_posix()+'\n' for p in files).encode('utf-8'))
print('Checkpoint files:',len(files))
