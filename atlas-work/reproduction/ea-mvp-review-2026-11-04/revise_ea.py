from pathlib import Path
from lxml import etree as E
from xml.sax.saxutils import escape
from collections import Counter
import re,json,hashlib

src=Path('work/ea-source/Atlas.xml')
raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='dcc42289f422c120105d791725bb27549238cc8c106812ac1ad36582c1a3861c'
X='{http://schema.omg.org/spec/XMI/2.1}'
parser=E.XMLParser(resolve_entities=False,no_network=True,huge_tree=True)
root=E.fromstring(raw,parser)
ext=root.find(X+'Extension')
elements={e.get(X+'idref'):e for e in ext.find('elements')}
scope='User-designated Architecture Board scope; atlas-work/outputs/Board_pokracovani_2026-11-04.md; direct source reading recorded in atlas-work/outputs/onedrive-servicehub-pruzkum.md.'
changes=[
('EAID_35449BC8_E7BE_40ad_B153_58589875C696','AD-05',
'For the current Atlas CZ MVP, ServiceHub is a standalone portal accessible through its dedicated URL, with Vodafone ID authentication and local authorization using VFCZ DXL. ONSC/WSC portal integration, navigation handover and bidirectional customer-context propagation are outside the current MVP. Upstream ONSC/WSC user roles and customer relationships retrieved through DXL remain distinct from portal navigation. The historical requirement for both V2 and V4 portal entry paths is superseded for this MVP.',scope),
('EAID_A3A663F0_D721_49ec_AB79_45E58A028178','ASS-06',
'The current Atlas CZ MVP uses a standalone ServiceHub access model through a dedicated URL. ONSC/WSC navigation integration and return journeys are future scope and are not prerequisites for standalone access. Vodafone ID authentication and the required VFCZ DXL authorization flow remain in scope. This statement does not exclude upstream ONSC/WSC role and relationship data.',scope),
('EAID_436FF5E3_7559_4a74_845F_38498981CD3F','AD-07',
'The current MVP uses an interim manual process to onboard V4 customers and users/administrators into SNOW. Automated V4 customer/admin onboarding and lifecycle propagation are outside the confirmed MVP. Customer and user presence, the selected company scope, and permissions for each supported ticket operation must be verified against the actual SNOW contract. Historical Atlas-filtered lifecycle propagation and the alternative full-V4 population are future design options, not the current MVP baseline. The implementation route, operational ownership, privacy/security acceptance and eventual removal of the interim process require explicit evidence; this revision does not assert that these conditions are complete.',scope),
('EAID_C6A84687_EFF5_4c33_815C_D3264CD2AC74','ASS-03',
'VFID sub maps one-to-one to the corresponding ONSC/WSC user. Email is an attribute, not the stable identity mapping key. This identity relation is separate from the user\'s multiple authorized customer contexts and from the target TMF691 holding parent-child relation. According to UC005, ServiceHub automatically selects one available CRM ID and allows switching among available contexts; the initial-selection priority remains unconfirmed. Without the required role/context, general content is shown rather than granting customer-specific access. If the selected CRM ID is no longer available, the selector must be refreshed without switching to an unavailable context. Keep service eligibility, customer context, and SNOW company/user scope separate. Specific company cardinalities and holding wire payloads require the relevant contracts.',
'Explicit user identity rule; direct UC005 evidence in atlas-work/outputs/Overeni_zdroju_VDI_2026-11-03.md; current OneDrive Book1 Interfaces!H4:K4 and SREQ Aplikacni role!F166 checked 4 Nov 2026.'),
]
auth_id='EAID_D9B354CD_C458_4e36_8399_B2F2A72A4314'
auth_old=elements[auth_id].find('properties').get('documentation')
changes.append((auth_id,'AD-02',auth_old+'\n\nVerified design clarification 4 November 2026: the primary email RE: ServiceHub - DXL from Zdenek Sery dated 15 October 2026 describes SH BFF obtaining an IDaaS access token, calling DXL OAuth2 Token Exchange through APIX with that token as subject_token, APIX routing to AuthX, and AuthX validating it against IDaaS /oidc/introspect before issuing the DXL access token returned to ServiceHub. The token is used for DXL-protected API calls. The email is design evidence, not a complete versioned wire contract or implementation verification. Endpoint URL, client authentication, full parameters, scopes/audience, expiry/refresh and errors still require the Atlas contract. Reference-diagram nonce/state handling must not be promoted to existing SH behaviour or a new DXL requirement without the Group authentication design.',
'Primary email RE: ServiceHub - DXL, Zdenek Sery, 15 Oct 2026 16:35, opened and read directly from Teams Copilot citation on 4 Nov 2026.'))
changes.append(('EAID_15F4EF2A_14D5_4bca_BA70_DEE9A8FFC46B','ASS-07',
'ServiceHub derives eligible customer scope from upstream role and relationship data and enforces access within the selected authorized context. Distinguish UC005 authentication/role/context handling, UC006 Atlas service visibility using Marketplace data, and UC007/UC010/UC011 ticket operations. Missing eligible role or CRM context leads to general content, not customer-specific access. Active Atlas subscription and SNOW user/company readiness are checked where the relevant service or ticket operation requires them; SNOW presence is not a prerequisite for every item of general ServiceHub content. ServiceHub refreshes or restricts the affected context when upstream eligibility changes. This does not introduce an independent upstream identity or role-provisioning authority in ServiceHub. Exact eligible role enums, per-operation permissions and refresh/error contracts remain subject to confirmation.',
'Direct UC005-UC011 evidence in atlas-work/outputs/Overeni_zdroju_VDI_2026-11-03.md; current Book1 Interfaces!H4:K7 and SREQ Aplikacni role!F166; Board MVP scope.'))
perf_id='EAID_213C4D3B_E083_43c1_B676_5AA96D557C0A'
perf_old=elements[perf_id].find('properties').get('documentation')
changes.append((perf_id,'AD-08',perf_old+'\n\nReview qualification 4 November 2026: retain the preceding paragraph as historical risk/mitigation context, not proof of measured degradation, an approved V2 exclusion or a quantified NFR. The directly read TMF691 specification confirms that V2 must be requested explicitly and returns root-level assets, with southbound limitations; it does not establish an Atlas performance SLO or current measurement. The Atlas rollout/role scope and any mitigation require the applicable MVP decision and accountable owner. Do not infer the target holding parent-child payload from this AS-IS API limitation.',
'Direct source record atlas-work/outputs/DXL_TMF691_overeni_2026-11-03.md; user-designated Board scope.'))
identity_id='EAID_94649FF3_077F_40c7_A722_AA7E5292AA7F'
identity_old=elements[identity_id].find('properties').get('documentation')
changes.append((identity_id,'SREQ-ID-07',identity_old+'\n\nReview clarification 4 November 2026: preserve the Local DXL responsibility above. Vodafone Identity/IDaaS provides authentication and identity-side claims; VFCZ DXL retrieves upstream relationships, roles and CRM context; ServiceHub evaluates access to its customer-specific content. The current Book1 F166 makes this separation explicit. This clarification is a target responsibility statement, not evidence of a new AS-IS implementation or a complete token negotiation contract.',
'Original requirement text retained verbatim; current OneDrive Book1 SREQ Aplikacni role!F166:H166; Interfaces!H4:K4; direct DXL source evidence in atlas-work/outputs/DXL_TMF691_overeni_2026-11-03.md.'))

out=raw
manifest=[]
spans=[]
for guid,name,new,evidence in changes:
    e=elements[guid]
    assert e.get('name')==name
    old=e.find('properties').get('documentation')
    # Replace only the documentation attribute within this unique EA element.
    pat=rb'(<element\s+xmi:idref="'+guid.encode()+rb'"[^>]*>.*?<properties\s+documentation=")([^"]*)(")'
    matches=list(re.finditer(pat,out,re.S))
    assert len(matches)==1,(guid,len(matches))
    m=matches[0]
    encoded=escape(new,{'"':'&quot;','\n':'&#10;','\r':'&#13;','\t':'&#9;'}).encode('utf-8')
    assert E.fromstring(b'<x d="'+m.group(2)+b'"/>').get('d')==old
    out=out[:m.start(2)]+encoded+out[m.end(2):]
    manifest.append(dict(guid=guid,name=name,before=old,after=new,evidence=evidence,field='properties.documentation'))

newroot=E.fromstring(out,parser)
newelements={e.get(X+'idref'):e for e in newroot.find(X+'Extension').find('elements')}
for c in manifest:
    assert newelements[c['guid']].find('properties').get('documentation')==c['after']

def masked(b):
    for guid,_,_,_ in changes:
        pat=rb'(<element\s+xmi:idref="'+guid.encode()+rb'"[^>]*>.*?<properties\s+documentation=")([^"]*)(")'
        b,n=re.subn(pat,lambda m:m.group(1)+b'__REVIEW_FIELD__'+m.group(3),b,flags=re.S)
        assert n==1
    return b
assert masked(raw)==masked(out),'Unplanned byte changes'
ids=lambda r:Counter(e.get(X+'id') for e in r.iter() if e.get(X+'id'))
refs=lambda r:Counter(e.get(X+'idref') for e in r.iter() if e.get(X+'idref'))
assert ids(root)==ids(newroot)
assert refs(root)==refs(newroot)
for section in ['connectors','diagrams']:
    assert E.tostring(ext.find(section))==E.tostring(newroot.find(X+'Extension').find(section))
target=Path('work/ea-revision');target.mkdir(parents=True,exist_ok=True)
dest=target/'Atlas_MVP_review_2026-11-04.xml';dest.write_bytes(out)
report=dict(status='Partial model documentation revision; not a complete architecture baseline or native EA import validation',source_sha256=hashlib.sha256(raw).hexdigest(),output_sha256=hashlib.sha256(out).hexdigest(),changed_documentation_fields=len(manifest),all_other_bytes_preserved=True,all_xmi_ids_and_idrefs_preserved=True,connectors_and_diagrams_byte_identical=True,source_unchanged=src.read_bytes()==raw,changes=manifest)
(target/'Kontrola_EA_revize.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
Path('outputs/Kontrola_EA_revize_2026-11-04.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='changes'},indent=2))
