from pathlib import Path
from lxml import etree as E
from xml.sax.saxutils import escape
import hashlib,json,re
src=Path('work/ea-revision/Atlas_MVP_review_2026-11-04.xml');raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='fb0cfe908c40bf58928d5b8a837760bce19304d9293d1f331377183a268a21a6'
guid='EAID_D9B354CD_C458_4e36_8399_B2F2A72A4314'
pat=rb'(<element\s+xmi:idref="'+guid.encode()+rb'"[^>]*>.*?<properties\s+documentation=")([^"]*)(")'
matches=list(re.finditer(pat,raw,re.S));assert len(matches)==1;m=matches[0]
old=E.fromstring(b'<x d="'+m.group(2)+b'"/>').get('d')
addition='\n\nPrimary technical verification 5 November 2026: Confluence TS - AuthX - authx-ts, section 3.2.1, last modified 4 June 2026, documents POST /OAuth2TokenExchangeGrant/v2/token. The API key used via APIX needs OAUTH2_TOKEN_EXCHANGE_GRANT and TMF691_FEDERATED_IDENTITY_ALL scopes. The form-urlencoded request includes grant_type=urn:ietf:params:oauth:grant-type:token-exchange, subject_token_type=urn:vodafone:params:oauth:token-type:vodafone_id, a valid subject_token and mandatory subject_token_iss identifying the issuing VFID environment. The response contains a Bearer DXL access token and TMF691-compliant user_info authorization assets; the token grants access only to the assets listed in that response. Example expiry/refresh values are not an Atlas production lifetime guarantee. This platform specification closes the relative endpoint and listed request-parameter evidence gaps, but does not prove Atlas API key configuration, environment URL, complete client authentication/error/refresh contract or deployment. Source: https://confluence-agile.oskarmobil.cz/display/DCP/TS+-+AuthX+-+authx-ts'
new=old+addition
encoded=escape(new,{'"':'&quot;','\n':'&#10;','\r':'&#13;','\t':'&#9;'}).encode('ascii')
out=raw[:m.start(2)]+encoded+raw[m.end(2):]
assert re.sub(pat,lambda x:x.group(1)+b'FIELD'+x.group(3),raw,flags=re.S)==re.sub(pat,lambda x:x.group(1)+b'FIELD'+x.group(3),out,flags=re.S)
E.fromstring(out,E.XMLParser(resolve_entities=False,no_network=True,huge_tree=True))
dest=Path('work/ea-mvp-so');dest.mkdir(exist_ok=True)
(dest/'Atlas_MVP_SO_2026-11-05.xml').write_bytes(out)
report={'status':'Working review model; native EA import not verified','source_sha256':hashlib.sha256(raw).hexdigest(),'output_sha256':hashlib.sha256(out).hexdigest(),'guid':guid,'field':'AD-02 properties.documentation','all_other_bytes_preserved':True,'before':old,'after':new,'evidence':'outputs/Confluence_AuthX_overeni_2026-11-05.md'}
(dest/'Kontrola_AuthX_doplneni.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['before','after']},indent=2))
