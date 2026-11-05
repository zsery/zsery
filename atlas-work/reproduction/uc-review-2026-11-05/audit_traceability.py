from pathlib import Path
from lxml import etree as E
from collections import defaultdict, Counter
import json, csv, hashlib

repo=Path('C:/Users/zsery2/Documents/Codex/2026-11-03/pokra-uj-v-pr-ci-atlas/zsery/atlas-work')
src=Path('work/ea-source/Atlas.xml')
X='{http://schema.omg.org/spec/XMI/2.1}'
r=E.parse(str(src),E.XMLParser(resolve_entities=False,no_network=True,huge_tree=True)).getroot()
ext=r.find(X+'Extension')
els={e.get(X+'idref'):e for e in ext.find('elements')}
edges=defaultdict(list)
connectors=[]
for c in ext.find('connectors'):
    a,b=c.find('source'),c.find('target')
    if a is None or b is None: continue
    s,t=a.get(X+'idref'),b.get(X+'idref')
    p=c.find('properties')
    row={'guid':c.get(X+'idref'),'source_guid':s,'target_guid':t,'type':p.get('ea_type','') if p is not None else '', 'stereotype':p.get('stereotype','') if p is not None else ''}
    connectors.append(row);edges[s].append(row);edges[t].append(row)
matrix=json.loads((repo/'outputs/UC_atomicke_podminky_2026-11-04/Kontrolni_matice.json').read_text(encoding='utf-8'))
out=Path('outputs/ServiceHub_traceability_2026-11-04');out.mkdir(exist_ok=True)
rules=[];flat=[]
for rule in matrix['rules']:
    rr={k:rule[k] for k in ['review_row','uc','rule','proposed_acceptance','gap']}
    rr['candidates']=[]
    for f in rule['freq_candidates']:
        guid=f['guid'];el=els.get(guid);incident=edges[guid]
        item={'id':f['id'],'guid':guid,'source_text':f['source_text'],'exists_in_xml':el is not None,'xml_name':el.get('name','') if el is not None else '', 'incident_connectors':incident}
        rr['candidates'].append(item)
        flat.append({'uc':rule['uc'],'condition':rule['review_row'],'freq':f['id'],'guid':guid,'exists_in_xml':el is not None,'incident_connectors':len(incident),'source_text':f['source_text']})
    rr['historical_mapping_rows']=rule['existing_mapping_rows']
    rr['assessment']='Existing source candidates only; no semantic approval or new model links. Current Book1 rows must not be inferred from historical mapping rows.'
    rules.append(rr)
report={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'historical_workbook_sha256':matrix['workbook_sha256'],'scope':'All 30 recorded UC005-UC011 conditions against exact original EA GUIDs. This is a graph inventory, not confirmation of the current seven-sheet OneDrive workbook or implementation.', 'conditions':len(rules),'candidate_occurrences':len(flat),'unique_candidate_guids':len({f['guid'] for f in flat}),'missing_candidate_guids':sorted({f['guid'] for f in flat if not f['exists_in_xml']}),'candidates_with_no_connectors':len({f['guid'] for f in flat if not f['incident_connectors']}),'rules':rules}
(out/'EA_UC_traceability.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
with (out/'EA_UC_traceability.csv').open('w',encoding='utf-8-sig',newline='') as stream:
    w=csv.DictWriter(stream,fieldnames=list(flat[0]));w.writeheader();w.writerows(flat)
lines=['# UC → EA traceability audit','',report['scope'],'',f"Conditions: {len(rules)}; candidate occurrences: {len(flat)}; unique GUIDs: {report['unique_candidate_guids']}; missing GUIDs: {len(report['missing_candidate_guids'])}.",'','Graph adjacency is evidence of a stored connector only. It does not prove that a requirement is semantically fulfilled. The workbook baseline of this matrix predates the latest Copilot changes.','', '| UC | Condition | Existing FREQ candidates | Incident connectors |','|---|---:|---|---:|']
for rule in rules:
    lines.append('| '+rule['uc']+' | '+str(rule['review_row'])+' | '+', '.join(c['id'] for c in rule['candidates'])+' | '+str(sum(len(c['incident_connectors']) for c in rule['candidates']))+' |')
lines+=['','Current Book1 corrections already verified: CRM-04 ↔ IAM-25 and CRM-03 ↔ IAM-24. Do not reapply the historical swap. IAM-12 current row 109 remains an allow/deny conflict. Preserve role wording until business eligibility is decided.','', 'All original XML and workbook files were read only. No EA connector was added from a text match.']
(out/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
assert not report['missing_candidate_guids']
print(json.dumps({k:v for k,v in report.items() if k!='rules'},ensure_ascii=False,indent=2))
