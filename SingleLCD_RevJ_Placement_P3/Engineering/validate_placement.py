from pathlib import Path
import os,sys,json,math,csv,xml.etree.ElementTree as E,hashlib,itertools,tempfile
for key,leaf in [('XDG_CONFIG_HOME','config'),('XDG_CACHE_HOME','cache'),('XDG_DATA_HOME','data')]:
 os.environ.setdefault(key,str(Path(tempfile.gettempdir())/'kicad-p3-validation'/leaf))
 Path(os.environ[key]).mkdir(parents=True,exist_ok=True)
import pcbnew as P
root=Path(__file__).resolve().parents[1];p=root/'Project';f=p/'STM32F469_DISEN_RevJ_Prep1.kicad_pcb';b=P.LoadBoard(str(f));ox,oy=115.5,70
fps={x.GetReference():x for x in b.GetFootprints()};original=P.LoadBoard(str(root/'Original/Input_PCB.kicad_pcb'));before={x.GetReference():x for x in original.GetFootprints()}
x=E.parse(str(root/'Verification/Schematic_Baseline.xml')).getroot();comps={c.attrib['ref']:c for c in x.findall('./components/comp')};expected={}
for net in x.findall('./nets/net'):
 for n in net:expected[n.attrib['ref'],n.attrib['pin']]=net.attrib['name']
assert len(fps)==53 and set(fps)==set(comps)==set(before)
actual={};placement=[];pa=[]
for ref,fp in sorted(fps.items()):
 assert fp.GetValue()==comps[ref].findtext('value'),ref
 assert fp.GetFPID().GetUniStringLibId()==comps[ref].findtext('footprint'),ref
 assert fp.m_Uuid.AsString()==before[ref].m_Uuid.AsString(),ref
 assert fp.GetPath().AsString()==before[ref].GetPath().AsString(),ref
 for a in fp.Pads():
  if a.GetNumber():actual[ref,a.GetNumber()]=a.GetNetname()
 placement.append({'ref':ref,'x_mm':P.ToMM(fp.GetPosition().x)-ox,'y_mm':P.ToMM(fp.GetPosition().y)-oy,'rotation_deg':fp.GetOrientationDegrees(),'side':fp.GetLayerName(),'value':fp.GetValue()})
 assert fp.GetLayer()==P.F_Cu
for pair,net in expected.items():assert actual[pair]==net,(pair,net,actual.get(pair))
for ref in ['H1','H2','H3','H4']:
 assert fps[ref].GetPosition()==before[ref].GetPosition()
 assert next(iter(fps[ref].Pads())).GetDrillSize().x==P.FromMM(3.5)
for sch in p.glob('*.kicad_sch'):
 hashes=json.loads((root/'Verification/Schematic_SHA256.json').read_text());assert hashlib.sha256(sch.read_bytes()).hexdigest()==hashes[sch.name],sch
assert len(b.GetTracks())==0 and len(b.Zones())==4 and all(z.GetIsRuleArea() for z in b.Zones())
assert b.GetCopperLayerCount()==4
# Mechanical bounds and empty routing / FPC access areas (conservative AABB checks).
def bb(fp):
 z=fp.GetBoundingBox(False,False);return [P.ToMM(z.GetX())-ox,P.ToMM(z.GetY())-oy,P.ToMM(z.GetRight())-ox,P.ToMM(z.GetBottom())-oy]
def intersect(a,c):return a[0]<c[2] and a[2]>c[0] and a[1]<c[3] and a[3]>c[1]
def distance(pt,r):return math.hypot(max(r[0]-pt[0],0,pt[0]-r[2]),max(r[1]-pt[1],0,pt[1]-r[3]))
checks=[]
for ref,fp in fps.items():
 z=bb(fp);assert min(z[0],z[1],55-z[2],45-z[3])>=0,ref
 if not ref.startswith('H'):
  for h in ['H1','H2','H3','H4']:
   c=fps[h].GetPosition();d=distance((P.ToMM(c.x)-ox,P.ToMM(c.y)-oy),z)
   checks.append({'part':ref,'hole':h,'courtyard_bbox_to_hole_center_mm':d,'required_radius_mm':4})
   assert d>=4,(ref,h,d)
areas={'DSI horizontal corridor':[8.9,17,27.1,23.4],'DSI vertical corridor':[23.1,6.5,27.1,23.4],'J1 FPC insertion':[0,13.5,1.6,24.5],'J2 FPC insertion':[17.5,0,32.5,1.6],'J3 FPC insertion':[10.2,0,16.8,1.9]}
for area,rect in areas.items():
 blocked=[r for r,f in fps.items() if r not in ['J1','J2','J3'] and intersect(bb(f),rect)]
 assert not blocked,(area,blocked)
# Tight power/control pad-center distances; these are NOT routed lengths.
def pad(ref,num):return next(a for a in fps[ref].Pads() if a.GetNumber()==num)
def pd(board,a,b):
 fs={x.GetReference():x for x in board.GetFootprints()};pp=[]
 for ref,num in [a,b]:
  q=next(t for t in fs[ref].Pads() if t.GetNumber()==num).GetPosition();pp.append((P.ToMM(q.x),P.ToMM(q.y)))
 return math.dist(*pp)
metrics=[]
for title,a,c in [('L1 SW to U1 SW',('L1','2'),('U1','3')),('D1 anode to U1 SW',('D1','2'),('U1','3')),('C2 VIN bypass to U1 VIN',('C2','1'),('U1','1')),('R7 sense to U1 FB',('R7','1'),('U1','6')),('C9 COMP to U1 COMP',('C9','1'),('U1','5')),('C3 output to D1 cathode',('C3','1'),('D1','1'))]:
 metrics.append({'connection':title,'before_pad_center_distance_mm':pd(original,a,c),'after_pad_center_distance_mm':pd(b,a,c)})
# Geometric alternatives: pin-center lower bounds only, no claim these are routed designs.
variants=[('A uploaded adjacent bottom-right',None,None,'Short chord but scattered hot-loop and FB parts; used as baseline.'),('B opposite left-right',(4,19,-90),(51,19,90),'Reject: long cross-board DSI and added skew/tuning burden.'),('C selected adjacent left-top',(4,19,-90),(25,4,180),'Select: dedicated L corridor, touch outside it, boost at lower right.'),('D same top edge',(18.25,4,180),(38.8,4,180),'Reject: short chord but touch/rail fanout occupies return-turn region; densely packed FPC edge.')]
alternatives=[]
for label,j1,j2,reason in variants:
 fs={r:before[r].Duplicate() for r in ['J1','J2']}
 if j1:
  for ref,(xx,yy,rr) in [('J1',j1),('J2',j2)]:fs[ref].SetOrientationDegrees(rr);fs[ref].SetPosition(P.VECTOR2I(P.FromMM(ox+xx),P.FromMM(oy+yy)))
 lengths=[]
 for net in ['DSI_D0_N','DSI_D0_P','DSI_D1_N','DSI_D1_P','DSI_CLK_N','DSI_CLK_P']:
  a=next(t for t in fs['J1'].Pads() if t.GetNetname()==net).GetPosition();c=next(t for t in fs['J2'].Pads() if t.GetNetname()==net).GetPosition();lengths.append(math.hypot(P.ToMM(a.x-c.x),P.ToMM(a.y-c.y)))
 alternatives.append({'variant':label,'DSI_straight_chord_mean_mm':sum(lengths)/6,'DSI_straight_chord_max_mm':max(lengths),'assessment':reason})
# Reserve candidate via lands without adding any copper to the PCB. Validate circular pad/edge clearances.
signals=[]
for net,y in [('DSI_CLK_N',19.3),('DSI_CLK_P',20.5),('DSI_D1_N',21.6),('DSI_D1_P',22.8)]:signals.append({'name':'J1_'+net,'net':net,'x':7.0,'y':y})
for net,xv,yv in [('DSI_CLK_N',23.2,1.6),('DSI_D1_N',24.4,1.6),('DSI_D0_N',25.6,1.6),('DSI_CLK_P',23.8,6.8),('DSI_D1_P',25.0,6.8),('DSI_D0_P',26.2,6.8),('DSI_D0_N',26.8,10.0),('DSI_D0_P',26.8,11.2)]:signals.append({'name':'J2_'+net+('_transition' if yv>=10 else ''),'net':net,'x':xv,'y':yv})
grounds=[{'name':'GND'+str(i+1),'net':'GND','x':xv,'y':yv} for i,(xv,yv) in enumerate([(7.95,19.9),(7.95,22.2),(22.3,1.6),(25.0,.9),(24.4,7.65),(25.6,7.65),(27.5,10.6)])]
lands=signals+grounds
for a in lands:
 assert min(a['x'],a['y'],55-a['x'],45-a['y'])-.3>=.5-1e-6
 minclear=100
 for ref,fp in fps.items():
  for pad_ in fp.Pads():
   if pad_.GetNetname()==a['net']:continue
   z=pad_.GetBoundingBox();z=[P.ToMM(z.GetX())-ox,P.ToMM(z.GetY())-oy,P.ToMM(z.GetRight())-ox,P.ToMM(z.GetBottom())-oy];d=distance((a['x'],a['y']),z)-.3;minclear=min(minclear,d)
 assert minclear>=.2-1e-6,(a,minclear)
 a['minimum_other_pad_edge_clearance_mm']=minclear
 for c in lands:
  if a is c or a['net']==c['net']:continue
  d=math.hypot(a['x']-c['x'],a['y']-c['y'])-.6
  assert d>=.2-1e-6,(a,c,d)
 if a['net']!='GND':a['nearest_reserved_GND_via_mm']=min(math.hypot(a['x']-c['x'],a['y']-c['y']) for c in grounds)
for path,data in [('Mechanical_Checks.json',checks),('Critical_Distances.json',metrics),('Connector_Alternatives.json',alternatives),('Via_Land_Candidates.json',lands),('Component_Placement.json',placement)]: (root/'Verification'/path).write_text(json.dumps(data,indent=2))
with (root/'Engineering/Component_Placement.csv').open('w') as f_:w=csv.DictWriter(f_,fieldnames=list(placement[0]));w.writeheader();w.writerows(placement)
drc=json.loads((root/'Verification/DRC_Placement.json').read_text());erc=json.loads((root/'Verification/ERC.json').read_text());assert not drc['violations'] and not drc['schematic_parity'];assert not [v for s in erc['sheets'] for v in s.get('violations',[])]
summary={'footprints':53,'circuit_parts':49,'copper_layers':4,'board_mm':[55,45],'thickness_mm':1.6,'tracks':0,'vias':0,'copper_pour_zones':0,'hardware_rule_areas':4,'physical_DRC_violations':len(drc['violations']),'unconnected_items_expected_before_routing':len(drc['unconnected_items']),'schematic_parity_issues':len(drc['schematic_parity']),'ERC_violations':0,'all_schematic_bytes_preserved':True,'all_component_UUIDs_and_paths_preserved':True,'all_component_values_footprint_IDs_and_pin_nets_match_J_SR1':True,'mounting_hole_positions_preserved':True,'reserved_signal_via_lands_not_actual_vias':len(signals),'reserved_GND_via_lands_not_actual_vias':len(grounds),'via_candidate_scope':'Pad and edge clearances only; actual routing and return-via placement must be verified during routing','impedance_scope':'100ohm design target; requires fabricator stackup approval; no routed impedance verified'}
(root/'Verification/Validation_Summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2));print(json.dumps(metrics,indent=2));print(json.dumps(alternatives,indent=2))
