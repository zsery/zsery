"""Add a separate analytical review layer; never infer realization/approval."""
from pathlib import Path
from lxml import etree as E
from collections import defaultdict, Counter
import uuid, re, json, hashlib, copy

src=Path('work/ea-revision/Atlas_MVP_review_2026-11-04.xml')
raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='fb0cfe908c40bf58928d5b8a837760bce19304d9293d1f331377183a268a21a6'
X='{http://schema.omg.org/spec/XMI/2.1}'
parser=E.XMLParser(resolve_entities=False,no_network=True,huge_tree=True)
r=E.fromstring(raw,parser);ext=r.find(X+'Extension')
els={e.get(X+'idref'):e for e in ext.find('elements')}
matrix=json.loads(Path('outputs/ServiceHub_traceability_2026-11-04/EA_UC_traceability.json').read_text(encoding='utf-8'))
ns=uuid.UUID('a013a7f9-3679-4326-bf44-e89c9fa416e0')
def guid(key,prefix='EAID_'): return prefix+str(uuid.uuid5(ns,'Atlas UC review 2026-11-04 '+key)).upper().replace('-','_')
def node(tag,attrs=None,**kw):
    return E.Element(tag,dict(attrs or {},**{k:str(v) for k,v in kw.items()}))
def sub(parent,tag,attrs=None,**kw):
    el=node(tag,attrs,**kw);parent.append(el);return el
def serialize(e): return E.tostring(e,encoding='ascii',with_tail=False)
def block(data): return b'<!--ATLAS_UC_REVIEW_BEGIN-->'+data+b'<!--ATLAS_UC_REVIEW_END-->'
parent=r.find('.//packagedElement');parent_id=parent.get(X+'id')
pid=guid('package','EAPK_')
pkg=node('packagedElement',{X+'type':'uml:Package',X+'id':pid,'name':'Atlas MVP - UC review 2026-11-04 [PROPOSED]','visibility':'public'})
locals_used=[int(v) for e in r.iter() for k,v in e.attrib.items() if k in ['ea_localid','localID'] and v.isdigit()]
next_local=max(locals_used)+1
def local():
    global next_local
    v=next_local;next_local+=1;return str(v)
new_elements=[];new_connectors=[];new_diagrams=[];target_links=defaultdict(list);manifest=[]
pe=node('element',{X+'idref':pid,X+'type':'uml:Package','name':pkg.get('name'),'scope':'public'})
sub(pe,'model',package=parent_id,tpos='0',ea_localid=local(),ea_eleType='package')
sub(pe,'properties',documentation='Analytical UC005-UC011 review layer. Nodes are review artifacts, not new approved FREQ/SREQ. Candidate trace links do not assert fulfillment. See Scenare_MVP.md and EA_UC_traceability.json. Original model elements, source texts and relationships are retained.',sType='Package',nType='0',scope='public')
sub(pe,'project',author='Codex',version='0.1',phase='Review',status='Proposed',created='2026-11-04 19:00:00',modified='2026-11-04 19:00:00')
new_elements.append(pe)
by_uc=defaultdict(list)
for rule in matrix['rules']: by_uc[rule['uc']].append(rule)
for uc,rules in by_uc.items():
    dg=node('diagram',{X+'id':guid(uc+' diagram')})
    sub(dg,'model',package=pid,localID=local(),owner=pid,tpos='0')
    sub(dg,'properties',name=uc+' - review conditions and candidate FREQ [PROPOSED]',type='Logical')
    sub(dg,'project',author='Codex',version='0.1',created='2026-11-04 19:00:00',modified='2026-11-04 19:00:00')
    sub(dg,'style1',value='ShowNotes=1;HideRelationships=0;Locked=0;HideAtts=1;HideOps=1;ShowTags=0;UseAlias=0;')
    sub(dg,'style2',value='MDGDgm=;ShowNotes=1;Theme=:119;')
    diagram_elements=sub(dg,'elements');right={}
    for i,rule in enumerate(rules):
        rid=guid('condition '+str(rule['review_row']))
        label=f"{uc} review {rule['review_row']:02d} - "+rule['rule']
        sub(pkg,'packagedElement',{X+'type':'uml:Artifact',X+'id':rid,'name':label,'visibility':'public'})
        el=node('element',{X+'idref':rid,X+'type':'uml:Artifact','name':label,'scope':'public'})
        lid=local();sub(el,'model',package=pid,tpos=str(i),ea_localid=lid,ea_eleType='element')
        documentation='PROPOSED ANALYTICAL REVIEW CONDITION; NOT AN APPROVED NEW REQUIREMENT.\n'+rule['rule']+'\nAcceptance proposal: '+rule['proposed_acceptance']+'\nOpen point: '+rule['gap']+'\nBasis: recorded primary UC005-UC011 reading, 3-4 Nov 2026. Candidate links use original GUIDs. Historical workbook references are not current OneDrive row evidence.'
        sub(el,'properties',documentation=documentation,sType='Artifact',nType='0',scope='public')
        sub(el,'project',author='Codex',version='0.1',phase='Review',status='Proposed',created='2026-11-04 19:00:00',modified='2026-11-04 19:00:00')
        sub(el,'style',appearance='BackColor=16777215;BorderColor=8421504;BorderWidth=1;FontColor=0;')
        links=sub(el,'links')
        sub(diagram_elements,'element',geometry=f'Left=30;Top={30+i*190};Right=470;Bottom={190+i*190};',subject=rid,seqno=str(i+1),style='fontsz=100;')
        for candidate in rule['candidates']:
            target=candidate['guid'];assert target in els
            cid=guid('trace '+rid+' '+target)
            sub(pkg,'packagedElement',{X+'type':'uml:Dependency',X+'id':cid,'name':'candidate trace - not fulfillment','visibility':'public','supplier':target,'client':rid})
            link=node('Dependency',{X+'id':cid,'start':rid,'end':target})
            links.append(copy.deepcopy(link));target_links[target].append(link)
            c=node('connector',{X+'idref':cid})
            for tag,g,ea_id,name,typ in [('source',rid,lid,label,'Artifact'),('target',target,els[target].find('model').get('ea_localid'),els[target].get('name'),'Requirement')]:
                end=sub(c,tag,{X+'idref':g});sub(end,'model',ea_localid=ea_id,type=typ,name=name)
                sub(end,'role',visibility='Public',targetScope='instance');sub(end,'type',aggregation='none',containment='Unspecified')
                sub(end,'constraints');sub(end,'modifiers',isOrdered='false',changeable='none',isNavigable='true' if tag=='target' else 'false')
                sub(end,'style');sub(end,'documentation');sub(end,'xrefs');sub(end,'tags')
            sub(c,'model',ea_localid=local())
            sub(c,'properties',ea_type='Dependency',direction='Source -> Destination',stereotype='trace')
            sub(c,'documentation',value='Candidate trace from a proposed analytical UC condition to an existing FREQ. Not an implementation realization, approval, or assertion of full semantic coverage.')
            sub(c,'appearance',linemode='3',linecolor='-1',linewidth='0',seqno='0',headStyle='0',lineStyle='0')
            sub(c,'extendedProperties');sub(c,'style');sub(c,'xrefs');sub(c,'tags')
            new_connectors.append(c)
            if target not in right: right[target]=len(right)
            manifest.append({'connector_guid':cid,'review_artifact_guid':rid,'uc':uc,'condition':rule['review_row'],'candidate_freq_id':candidate['id'],'candidate_freq_guid':target,'relationship':'candidate trace only'})
        new_elements.append(el)
    for g,i in right.items():
        sub(diagram_elements,'element',geometry=f'Left=700;Top={30+i*190};Right=1140;Bottom={190+i*190};',subject=g,seqno=str(len(rules)+i+1),style='fontsz=100;')
    new_diagrams.append(dg)

# Add fragments only; every original byte can be recovered by removing marked blocks.
out=raw
parent_open=re.search(rb'<packagedElement\b[^>]*xmi:id="'+parent_id.encode()+rb'"[^>]*>',out)
assert parent_open
out=out[:parent_open.end()]+block(serialize(pkg))+out[parent_open.end():]
for target,links in target_links.items():
    pattern=rb'(<element\s+xmi:idref="'+target.encode()+rb'"[^>]*>)(.*?)(</element>)'
    matches=list(re.finditer(pattern,out,re.S));assert len(matches)==1
    m=matches[0];inside=m.group(2)
    data=b''.join(serialize(l) for l in links)
    if b'</links>' in inside:
        inside=inside.replace(b'</links>',block(data)+b'</links>',1)
    else: inside+=block(b'<links>'+data+b'</links>')
    out=out[:m.start(2)]+inside+out[m.end(2):]
for close,items in [(b'</elements>',new_elements),(b'</connectors>',new_connectors),(b'</diagrams>',new_diagrams)]:
    # First closing elements is the top-level EA elements collection, before diagrams.
    pos=out.index(close,out.index(b'<xmi:Extension'))
    out=out[:pos]+block(b''.join(serialize(e) for e in items))+out[pos:]
stripped=re.sub(rb'<!--ATLAS_UC_REVIEW_BEGIN-->.*?<!--ATLAS_UC_REVIEW_END-->',b'',out,flags=re.S)
assert stripped==raw,'Original bytes changed outside the additive review layer'
new=E.fromstring(out,parser);newext=new.find(X+'Extension')
old_guids=set(els);all_els={e.get(X+'idref') for e in newext.find('elements')}
assert old_guids<=all_els
children=lambda section: [e for e in newext.find(section) if isinstance(e.tag,str)]
assert len(children('elements'))==len(ext.find('elements'))+31
assert len(children('connectors'))==len(ext.find('connectors'))+65
assert len(children('diagrams'))==len(ext.find('diagrams'))+7
for c in new_connectors:
    assert c.find('source').get(X+'idref') in all_els
    assert c.find('target').get(X+'idref') in all_els
for d in new_diagrams:
    for el in d.find('elements'): assert el.get('subject') in all_els
for section in ['connectors','diagrams']:
    assert [E.tostring(e) for e in ext.find(section)]==[E.tostring(e) for e in children(section)][:len(ext.find(section))]
dest=Path('work/ea-review-layer');dest.mkdir(exist_ok=True)
(dest/'Atlas_UC_review_2026-11-04.xml').write_bytes(out)
report={'status':'Proposed analytical review layer, not approved requirements or native EA import validation','source_sha256':hashlib.sha256(raw).hexdigest(),'output_sha256':hashlib.sha256(out).hexdigest(),'new_review_package':pid,'new_review_artifacts':30,'new_candidate_trace_dependencies':65,'new_review_diagrams':7,'all_input_bytes_recoverable_by_removing_added_blocks':True,'all_original_connectors_and_diagrams_unchanged':True,'native_EA_import_verified':False,'links':manifest}
(dest/'Kontrola_UC_review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='links'},ensure_ascii=False,indent=2))
