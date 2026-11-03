from pathlib import Path
import json,shutil
root=Path(__file__).resolve().parents[2];here=Path(__file__).resolve().parent
report=json.loads((here/'verification.json').read_text(encoding='utf8'))
state=root/'outputs/Book1_2026-11-03/Stav_Book1_2026-11-03.md'
t=state.read_text(encoding='utf8')
t=t.replace('188 původních mapovacích řádků dostalo pracovní výklad přes shodu konkrétního textu; není tím rozhodnut konflikt identifikátorů ani schválena technická vazba SREQ. Ostatní řádky se nespojují odhadem.','Všech 219 původních mapovacích řádků má pracovní obsahové posouzení: 188 přes konkrétní normalizovaný text a 31 samostatně (sdružené/odlišné texty a historické NFR). Není tím rozhodnut konflikt identifikátorů ani schválena technická vazba SREQ. U sdruženého ONB textu odděleno minimum identifikátoru od vyloučeného auto retrievalu; portálový roundtrip a automatický V4 lifecycle nejsou vydávány za potvrzené MVP.')
t=t.replace('4 289','4 663').replace('30 928','30 554').replace('930e32aa0c83c46940208c250cb282dc0efaffdd533add7b7b2796499952998f',report['sha256'])
t+='\nDalší ověření EA: `../ea-revize/EA_business_revize_2026-11-03.md` a 21řádkový crosswalk s původními GUID. Změna číslování UC je obsahový konflikt, nikoli identita podle čísla.\n'
state.write_text(t,encoding='utf8')
p=root/'outputs/Predani_prace_2026-11-03.md';t=p.read_text(encoding='utf8')
t=t.replace('4 289','4 663').replace('188 mapovacích řádků aktualizováno podle přesného textu','219 mapovacích řádků pracovně posouzeno: 188 přes konkrétní normalizovaný text a 31 samostatně')
t=t.replace('00736584a23fbf1bd043dd0a103f51a3abf5450d','37efb215969adbd034ea45a83d59eae05cb4703c')
t+='\n## Doplnění: kontrola EA a všech mapovacích řádků\n\nVšech 219 mapovacích řádků dostalo aktuální pracovní scope. 188 textových přiřazení a 31 samostatných obsahových posouzení zůstávají odděleny v kontrolním JSON. Zachovány původní ID/text/GUID. Aktualizace pracovního scope neznamená schválení SREQ vazeb.\n\n`outputs/ea-revize/EA_business_revize_2026-11-03.md` dokládá kontrolu 21 původních UC s jiným číslováním než nová specifikace; konkrétní GUID jsou v připojeném crosswalk CSV. AD05/ASS06 jsou v rozporu se standalone MVP; V4 lifecycle cílové předpoklady oddělit od manuálního MVP. Z 228 realizací je 226 na SREQ názvy a 2 na stejný OREQ-CARE-01. Původní XMI se nezměnilo. Pracovní R:S nejsou nově vytvořené EA vztahy.\n'
p.write_text(t,encoding='utf8')
repo=root/'work/github-zsery/atlas-work'
p=repo/'README.md';t=p.read_text(encoding='utf8').replace('188 původních mapovacích řádků aktualizováno přes přesný text','219 mapovacích řádků pracovně posouzeno (188 přes text, 31 samostatně)')
t+='\n- [Kontrola business vrstvy EA a návazností](outputs/ea-revize/EA_business_revize_2026-11-03.md) a [crosswalk 21 původních UC s GUID](outputs/ea-revize/EA_UC_obsahovy_crosswalk_2026-11-03.csv). Nové UC číslování není totožná identita. XMI a SO zatím nezměněny.\n'
p.write_text(t,encoding='utf8')
for src in (root/'outputs/Book1_2026-11-03').glob('*'):
 if src.is_file():shutil.copy2(src,repo/'outputs/Book1_2026-11-03'/src.name)
shutil.copy2(here/'primary-classification.json',root/'outputs/Book1_2026-11-03/Primarni_overeni_klasifikace.json')
shutil.copy2(here/'primary-classification.json',repo/'outputs/Book1_2026-11-03/Primarni_overeni_klasifikace.json')
for src in (root/'outputs/ea-revize').glob('*2026-11-03*'):
 if src.is_file():shutil.copy2(src,repo/'outputs/ea-revize'/src.name)
for name in ['prepare_changes.py','primary_update.py','consolidate.mjs','preserve_and_verify.py','verify_final.mjs','publish_report.py','refresh_delivery.py','changes.json','verification.json','reimport-qa.json']:
 shutil.copy2(here/name,repo/'reproduction/book1-v03'/name)
shutil.copy2(root/'work/ea/review_primary_business.py',repo/'reproduction/review_primary_business.py')
shutil.copy2(root/'outputs/Predani_prace_2026-11-03.md',repo/'PREDANI_2026-11-03.md')
print('Updated current outputs, handoff and reproduction files; original XMI unchanged.')
