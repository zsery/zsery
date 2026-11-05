from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from pathlib import Path

d=Document(); s=d.sections[0]
s.page_width=Inches(8.5);s.page_height=Inches(11)
s.top_margin=s.bottom_margin=Inches(.72);s.left_margin=s.right_margin=Inches(.8)
for name in ['Normal','Title','Subtitle','Heading 1','Heading 2']:
    st=d.styles[name];st.font.name='Calibri';st.font.color.rgb=RGBColor(0,0,0)
d.styles['Normal'].font.size=Pt(11)
d.styles['Normal'].paragraph_format.space_after=Pt(7)
d.styles['Normal'].paragraph_format.line_spacing=1.08
d.styles['Title'].font.size=Pt(23)
d.styles['Heading 1'].font.size=Pt(16)
d.styles['Heading 1'].paragraph_format.space_before=Pt(12)
d.styles['Heading 2'].font.size=Pt(12)
def p(text):return d.add_paragraph(text)
def h(text):return d.add_heading(text,1)
def sub(text):return d.add_heading(text,2)
def table(headers,rows,widths):
    t=d.add_table(rows=1,cols=len(headers));t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
    for i,w in enumerate(widths):t.columns[i].width=Inches(w)
    for i,x in enumerate(headers):t.rows[0].cells[i].text=x
    repeat=OxmlElement('w:tblHeader');t.rows[0]._tr.get_or_add_trPr().append(repeat)
    for row in rows:
        for c,x in zip(t.add_row().cells,row):c.text=x
    for ri,row in enumerate(t.rows):
        for ci,c in enumerate(row.cells):
            c.width=Inches(widths[ci]);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            pr=c._tc.get_or_add_tcPr();b=OxmlElement('w:tcBorders')
            for edge in ['top','left','bottom','right']:
                e=OxmlElement('w:'+edge);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'4');e.set(qn('w:color'),'D9D9D9');b.append(e)
            pr.append(b)
            mar=OxmlElement('w:tcMar')
            for edge in ['top','left','bottom','right']:
                e=OxmlElement('w:'+edge);e.set(qn('w:w'),'90');e.set(qn('w:type'),'dxa');mar.append(e)
            pr.append(mar)
            sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'234E65' if ri==0 else ('F1F5F7' if ri%2 else 'FFFFFF'));pr.append(sh)
            for pp in c.paragraphs:
                pp.paragraph_format.space_after=Pt(3);pp.paragraph_format.line_spacing=1.03
                for r in pp.runs:
                    r.font.size=Pt(10)
                    if ri==0:r.bold=True;r.font.color.rgb=RGBColor(255,255,255)
            no_split=OxmlElement('w:cantSplit');row._tr.get_or_add_trPr().append(no_split)
    d.add_paragraph().paragraph_format.space_after=Pt(0)
    return t
def page():d.add_page_break()

d.add_paragraph('ServiceHub Atlas CZ',style='Title')
d.add_paragraph('Změnové kapitoly Solution Overview',style='Subtitle')
p('4. listopadu 2026 | Scope MVP a integrační odpovědnosti')
h('Introducing')
p('Aktuální MVP používá samostatný ServiceHub přes vlastní URL, autentizaci Vodafone ID a lokální autorizaci s VFCZ DXL. V4 customer a user/admin onboarding do SNOW probíhá interním manuálním postupem. Tato aktualizace sjednocuje rozsah, odpovědnosti a doloženou část tokenového toku pro revizi Solution Overview.')
p('Závazným rozsahem je uživatelem určený dokument Atlas CZ Launch – Architecture Board Confirmation of Phased Implementation Approach. Aktuální Book1 slouží pro traceability a odlišení aplikační schopnosti od prokázané implementační změny. Existence funkce v katalogu ani absence detailu v UC sama neurčuje novou změnu nebo odstranění schopnosti.')
h('Architecture and Solution Description')
table(['Součást','Odpovědnost v návrhu'],[
('Vodafone Identity a IDaaS','Autentizace a identity claims. Nerozhoduje samo o přístupu k zákaznickému obsahu SH.'),
('ServiceHub a BFF','Zahájí vyjednání lokálního DXL tokenu, získá oprávněné kontexty, zvolí dostupné CRM ID a řídí zobrazení a přepínání kontextu.'),
('VFCZ DXL','Zpřístupní autorizované upstream vztahy, role a customer údaje. Oddělit identity data, customer data a tokenový kontrakt.'),
('Marketplace','Zdroj relevantních produktových a subscription dat. SH nese odpovědnost za Atlas filtraci a zobrazení.'),
('SNOW a provozní cesta','Ticket doména a manuální V4 onboarding podle vymezeného MVP. Přesná platforma a rozhraní musí odpovídat potvrzenému kontraktu.')
],[1.58,5.32])
p('Mimo MVP zůstává ONSC/WSC navigační integrace, bidirectional customer-context propagation a automatizovaný V4 onboarding do SNOW. Upstream ONSC/WSC role a vztahy přes DXL zůstávají použitelné i bez portálové navigace. Group dodávka sama neznamená nový vývoj VFCZ.')

page();h('Functional Design')
sub('Autentizace a vyjednání DXL tokenu')
p('Primární email RE: ServiceHub - DXL ze dne 15. října 2026 popisuje následující návrh. Jde o doložený integrační směr; email nenahrazuje verzovaný wire kontrakt ani důkaz nasazení.')
steps=[
'Uživatel se autentizuje přes Vodafone Identity a ServiceHub BFF získá IDaaS access token.',
'SH BFF volá DXL OAuth2 Token Exchange endpoint přes APIX a předá IDaaS access token jako subject_token.',
'APIX předá požadavek do AuthX. AuthX validuje IDaaS token vůči IDaaS /oidc/introspect.',
'AuthX vytvoří DXL access token a vrátí jej ServiceHubu. SH jej použije pro další volání chráněných DXL API.',
'Pro UserInfo je v přečtené specifikaci TMF691 doložena hlavička Authorization: Bearer a scope TMF691_FEDERATED_IDENTITY_ALL. Přidělení konkrétnímu Atlas klientovi se musí ověřit samostatně.'
]
for x in steps:d.add_paragraph(x,style='List Number')
p('Přesná URL token exchange endpointu, grant a úplné parametry, client authentication, audience, vydávané claims, expirace, refresh, chyby a produkční oprávnění zůstávají k doložení. Nonce/state z referenčního VFCZ diagramu se nesmí automaticky prezentovat jako existující chování SH nebo nový požadavek na DXL.')
sub('Identita a zákaznický kontext')
p('VFID sub odpovídá právě jednomu příslušnému ONSC/WSC userovi. Email je atribut a neslouží jako stabilní párovací klíč. Jeden uživatel může mít více oprávněných customer kontextů; to je jiný vztah než user identity a cílová TMF691 holding parent–child relace.')
p('UC005 vyžaduje automatickou volbu jednoho dostupného CRM ID a následné přepínání mezi dostupnými kontexty. Priorita počáteční volby není doložená. Chybějící role nebo CRM ID vede k obecnému obsahu; ztráta aktuálního CRM ID vyžaduje obnovu selectoru bez přepnutí na nedostupný kontext.')
p('Email z 15. října výslovně rozlišuje customer identifier z TMF691 a customer name získávaný přes TMF629. Není tím doloženo oprávnění libovolného klienta k jakémukoli customer lookupu. V2 se v přečtené TMF691 specifikaci žádá explicitně a má omezený root-level rozsah.')

page();h('System Impacts')
p('Aktuální Book1 ponechává původní CRM schopnosti a označuje neověřenou AS-IS deltu. Revize proto rozlišuje požadovaný výsledek, jeho aplikačního vlastníka a doloženou změnu implementace.')
table(['Oblast','Doložená hranice','Co nelze převzít automaticky'],[
('CRM a Siebel','CRM-03 poskytuje separation data; CRM-04 hierarchy a vztahy. Aktuální list rolí je váže k IAM-24 a IAM-25.','Nový CRM vývoj, přesný holding payload nebo plnou realizaci chování SH jednou datovou službou.'),
('IDaaS a DXL','Book1 F166 rozlišuje IDaaS claims, DXL retrieval vztahů/rolí/CRM ID a SH content eligibility.','Vlastnictví všech eligibility rozhodnutí IDaaS podle historického názvu Determine Access Eligibility.'),
('Marketplace','Potřebná data readiness a Atlas produktová/subscription data.','Automatický Siebel retrieval/prefill/population nebo zaměnění order acceptance za aktivaci.'),
('SH a SNOW','UC vymezují logické ticket operace. Aktuální Interfaces rozlišuje logickou hranici a nepotvrzenou technickou realizaci.','Že Local DXL/TMF621, SNOW EVE, GSNOW a CSD označují jedinou potvrzenou implementační trasu.'),
('ONSC a WSC','Upstream role a customer vztahy jsou oddělené od navigace.','Handover, návratovou URL nebo bidirectional propagaci jako současné MVP.')
],[1.12,2.8,2.98])
sub('Technické rozhraní SNOW')
p('Copilot dohledal DXL-TMF621 Trouble Ticket API Specification SNOW Integration 250926. Otevřený primární PDF má 74 stran. Ověřený obsah rozlišuje case request, incident, service request a obecné trouble tickets; kapitola Accessing Vodafone APIs popisuje Mutual TLS a klientské certifikáty pro VBPS API. Tato část sama nepotvrzuje použití dokumentu pro ServiceHub Atlas ani vyřešení identity/company scope.')
p('Samostatný SnowConnector návrh PR25_0749 popisuje middleware, provisioning a ticket integraci se systémy Foris, V2DB a Remedy. Bez dalšího dokladu není Atlas PR25_0837 kontraktem. Nově nalezené technické podklady se musí přiřadit ke skutečnému směru volání a platformě před doplněním sekvencí a polí.')

page();h('Other Requirements')
p('Datové kontrakty musí rozlišovat VFID sub, lokální user ID, platformu V2/V4, Siebel CA, V2 MSCRM GUID, BA/wallet a Marketplace company UUID. Názvy CRM ID nebo customer samy neopravňují tyto identifikátory sloučit. Konkrétní cleansing a reconciliation postup, žádný/více matchů a řešení existujících nesouhlasících vazeb zůstávají samostatnou součástí návrhu.')
p('Pracovní XML revize mění pět dokumentačních polí AD-05, ASS-06, AD-07, ASS-03 a upřesnění SREQ-ID-07. Zachovává GUIDy a všechny konektory a diagramy. Původní znění je uloženo v kontrolním manifestu. Revize dokumentace modelu neprokazuje nasazení aplikací ani schválení baseline.')
h('Open Points')
table(['Bod','Podmínka uzavření'],[
('DXL token exchange','Verzovaný request/response kontrakt, URL prostředí, client auth, scopes, expiry/refresh a chyby; potvrdit konkrétní SH klient.'),
('SNOW ticket integrace','Ověřit platformu a trasu, create/read/update operace, required fields, user/company identifikaci, status transitions a oprávnění.'),
('Role a holding','Potvrdit Atlas eligible role enum a holding parent–child payload; historický allow/deny rozpor SH-07 neřešit podle samotného ID.'),
('Traceability a model','Dokončit křížovou kontrolu FREQ mapping, funkcí a původních EA konektorů. Ověřit XML import a vizuální podobu dotčených diagramů.'),
('V4 provozní proces','Doložit provozní vlastnictví, přesný manuální postup a relevantní privacy/security podmínky. Neoznačovat budoucí automatizaci za hotové MVP.')
],[1.54,5.36])
sub('Podklady pro změnu')
p('Závazný Board scope určený uživatelem; přímé čtení UC a DXL specifikací zaznamenané 3.–4. listopadu; aktuální OneDrive Book1 ze 4. listopadu, zejména SREQ Aplikační role F166 a Interfaces H4 až K7 a A22; primární email RE: ServiceHub - DXL, Zdeněk Šerý, 15. října 2026 16:35. Nalezená TMF621 specifikace je ověřena pouze ve výše uvedeném rozsahu. Schválení jejího použití pro Atlas není doloženo.')

d.core_properties.title='ServiceHub Atlas CZ změnové kapitoly Solution Overview'
d.core_properties.subject='MVP scope, integration responsibilities and verified token-flow evidence'
d.core_properties.author=''
dest=Path('outputs/ServiceHub_SO_zmenove_kapitoly_2026-11-04.docx');d.save(dest)
print(dest)
