"""Read-only engineering audit; run native DRC/ERC first. All dimensions in mm."""
from pathlib import Path
import os,sys,json,math,hashlib,csv,collections,xml.etree.ElementTree as ET,tempfile
for k,s in [('XDG_CONFIG_HOME','config'),('XDG_CACHE_HOME','cache'),('XDG_DATA_HOME','data')]:
 os.environ.setdefault(k,str(Path(tempfile.gettempdir())/'kicad-r2-audit'/s));Path(os.environ[k]).mkdir(parents=True,exist_ok=True)
import pcbnew as P
root=Path(__file__).resolve().parents[1];name='STM32F469_DISEN_RevJ_Prep1';p=root/'Project';v=root/'Verification';b=P.LoadBoard(str(p/f'{name}.kicad_pcb'));src=P.LoadBoard(str(root/'Original/Project'/f'{name}.kicad_pcb'));fps={x.GetReference():x for x in b.GetFootprints()};oldfps={x.GetReference():x for x in src.GetFootprints()}
def norm(n):return n.removeprefix('/Backlight / external power/')
def xy(q):return [P.ToMM(q.x),P.ToMM(q.y)]
def xml(path):
 r=ET.parse(path).getroot();ns={(a.attrib['ref'],a.attrib['pin']):norm(n.attrib['name']) for n in r.findall('./nets/net') for a in n};comps={c.attrib['ref']:c for c in r.findall('./components/comp')};return ns,comps
expected,cs=xml(v/'Source_netlist.xml');actual,fc=xml(v/'Final_netlist.xml');assert expected==actual
assert set(fps)==set(oldfps)==set(cs)==set(fc) and len(fps)==53
padmap={(f.GetReference(),q.GetNumber()):norm(q.GetNetname()) for f in b.GetFootprints() for q in f.Pads() if q.GetNumber()};assert all(padmap[k]==val for k,val in expected.items())
placement=[];parts=[]
for ref,f in sorted(fps.items()):
 o=oldfps[ref];assert f.m_Uuid.AsString()==o.m_Uuid.AsString() and f.GetPath().AsString()==o.GetPath().AsString(),ref
 assert f.GetValue()==fc[ref].findtext('value') and f.GetFPID().GetUniStringLibId()==fc[ref].findtext('footprint'),ref
 if ref.startswith('H'):assert f.GetPosition()==o.GetPosition() and next(iter(f.Pads())).GetDrillSize().x==P.FromMM(3.5)
 if f.GetPosition()!=o.GetPosition() or f.GetOrientationDegrees()!=o.GetOrientationDegrees():placement.append({'ref':ref,'before_xy':xy(o.GetPosition()),'after_xy':xy(f.GetPosition()),'before_rotation':o.GetOrientationDegrees(),'after_rotation':f.GetOrientationDegrees()})
 parts.append({'ref':ref,'value':f.GetValue(),'footprint':str(f.GetFPID().GetUniStringLibId()),'x_from_left_mm':P.ToMM(f.GetPosition().x)-115.5,'y_from_top_mm':P.ToMM(f.GetPosition().y)-70,'rotation_deg':f.GetOrientationDegrees(),'side':f.GetLayerName(),'population':'DNP' if 'DNP' in f.GetValue() else 'FIT'})
assert b.GetCopperLayerCount()==4 and P.ToMM(b.GetDesignSettings().GetBoardThickness())==1.6
pro=json.loads((p/f'{name}.kicad_pro').read_text());oldpro=json.loads((root/'Original/Project'/f'{name}.kicad_pro').read_text());assert pro['board']['design_settings']==oldpro['board']['design_settings'];assert not pro['board']['design_settings'].get('drc_exclusions')
d=json.loads((v/'DRC_Final.json').read_text());e=json.loads((v/'ERC_Final.json').read_text());assert not (d['violations'] or d['unconnected_items'] or d['schematic_parity']);assert not [a for s in e['sheets'] for a in s['violations']]
traces=[t for t in b.GetTracks() if type(t).__name__!='PCB_VIA'];vias=[t for t in b.GetTracks() if type(t).__name__=='PCB_VIA'];grounds=[t for t in vias if t.GetNetname()=='GND'];dsi=[];projection=[]
plane={P.F_Cu:[z for z in b.Zones() if not z.GetIsRuleArea() and z.GetNetname()=='GND' and z.IsOnLayer(P.In1_Cu)],P.B_Cu:[z for z in b.Zones() if not z.GetIsRuleArea() and z.GetNetname()=='GND' and z.IsOnLayer(P.In2_Cu)]};assert all(len(x)==1 for x in plane.values())
for net in ['DSI_CLK_P','DSI_CLK_N','DSI_D0_P','DSI_D0_N','DSI_D1_P','DSI_D1_N']:
 ts=[t for t in traces if t.GetNetname()==net];vs=[t for t in vias if t.GetNetname()==net];length=sum(P.ToMM(t.GetLength()) for t in ts);assert length<=50 and len(vs)<=2
 # Endpoint graph: no branches, a single J1-to-J2 path, matched layer transitions.
 graph=collections.defaultdict(set)
 def key(q,lay):return (round(P.ToMM(q.x),4),round(P.ToMM(q.y),4),lay)
 for t in ts:
  a=key(t.GetStart(),t.GetLayer());c=key(t.GetEnd(),t.GetLayer());graph[a].add(c);graph[c].add(a)
 for t in vs:
  a=key(t.GetPosition(),P.F_Cu);c=key(t.GetPosition(),P.B_Cu);graph[a].add(c);graph[c].add(a)
 ends=[next(q for q in fps[ref].Pads() if q.GetNetname()==net) for ref in ['J1','J2']];a=key(ends[0].GetPosition(),P.F_Cu);c=key(ends[1].GetPosition(),P.F_Cu);seen={a};todo=[a]
 while todo:
  q=todo.pop()
  for n in graph[q]-seen:seen.add(n);todo.append(n)
 assert c in seen and len(seen)==len(graph) and all(len(x)<=2 for x in graph.values()),net
 nearest=[min(math.dist(xy(q.GetPosition()),xy(g.GetPosition())) for g in grounds) for q in vs]
 record={'net':net,'planar_length_mm':length,'through_vias':len(vs),'nominal_total_barrel_length_mm':len(vs)*1.565,'layer_lengths_mm':dict(collections.Counter({P.LayerName(l):sum(P.ToMM(t.GetLength()) for t in ts if t.GetLayer()==l) for l in [P.F_Cu,P.B_Cu]})),'widths_mm':sorted({P.ToMM(t.GetWidth()) for t in ts}),'nearest_GND_return_via_mm':nearest,'graph_single_unbranched_path':True};dsi.append(record)
 for t in ts:
  la=P.In1_Cu if t.GetLayer()==P.F_Cu else P.In2_Cu;poly=plane[t.GetLayer()][0].GetFilledPolysList(la);a=xy(t.GetStart());c=xy(t.GetEnd());count=max(1,math.ceil(math.dist(a,c)/.05));checked=skipped=0;missing=[]
  for i in range(count+1):
   q=[a[j]+(c[j]-a[j])*i/count for j in [0,1]]
   if any(math.dist(q,xy(z.GetPosition()))<=.55 for z in vs):skipped+=1;continue
   checked+=1
   if not poly.Contains(P.VECTOR2I(P.FromMM(q[0]),P.FromMM(q[1]))):missing.append(q)
  projection.append({'net':net,'layer':P.LayerName(t.GetLayer()),'checked':checked,'own_via_antipad_samples_exempt':skipped,'missing_centerline_reference':missing})
assert not [q for r in projection for q in r['missing_centerline_reference']]
# Measure overlapping, parallel N/P main segments; fanout/tuning gaps are reported separately.
gaps=[]
for lane in ['CLK','D0','D1']:
 left=[t for t in traces if t.GetNetname()=='DSI_'+lane+'_P' and abs(P.ToMM(t.GetWidth())-.14)<1e-6]
 right=[t for t in traces if t.GetNetname()=='DSI_'+lane+'_N' and abs(P.ToMM(t.GetWidth())-.14)<1e-6]
 for t in left:
  a=xy(t.GetStart());c=xy(t.GetEnd());ll=math.dist(a,c)
  if ll<.05:continue
  u=[(c[i]-a[i])/ll for i in [0,1]];distances=[]
  for q in right:
   if q.GetLayer()!=t.GetLayer():continue
   e0=xy(q.GetStart());e1=xy(q.GetEnd());ql=math.dist(e0,e1)
   if ql<.05:continue
   du=[(e1[i]-e0[i])/ql for i in [0,1]]
   if abs(u[0]*du[1]-u[1]*du[0])>.0001:continue
   d0=sum((e0[i]-a[i])*u[i] for i in [0,1]);d1=sum((e1[i]-a[i])*u[i] for i in [0,1]);overlap=min(ll,max(d0,d1))-max(0,min(d0,d1))
   if overlap>.05:distances.append(abs((e0[0]-a[0])*u[1]-(e0[1]-a[1])*u[0])-.14)
  if distances:gaps.append({'lane':lane,'segment_planar_mm':ll,'nearest_parallel_gap_mm':min(distances),'nominal_018_gap_match':abs(min(distances)-.18)<.00001})
assert gaps and min(q['nearest_parallel_gap_mm'] for q in gaps)>=.15-.00001
(v/'DSI_Parallel_Gap_Check.json').write_text(json.dumps({'scope':'Overlapping parallel 0.14mm main-line N/P segments only; excludes nonparallel corners, fanout and 3D coupling','segments':gaps,'nominal_018_matches':sum(q['nominal_018_gap_match'] for q in gaps)},indent=2))
pairs={}
for lane in ['CLK','D0','D1']:
 ns=[x for x in dsi if x['net'].startswith('DSI_'+lane+'_')];skew=abs(ns[0]['planar_length_mm']-ns[1]['planar_length_mm']);assert skew<=.1;pairs[lane]={'planar_skew_mm':skew,'via_counts_equal':ns[0]['through_vias']==ns[1]['through_vias']}
spread=max(x['planar_length_mm'] for x in dsi)-min(x['planar_length_mm'] for x in dsi);assert spread<=1.
def signature(t):
 ends=sorted(tuple(round(x,6) for x in xy(q)) for q in [t.GetStart(),t.GetEnd()]);w=P.ToMM(t.GetWidth(P.F_Cu)) if type(t).__name__=='PCB_VIA' else P.ToMM(t.GetWidth());return str((type(t).__name__,norm(t.GetNetname()),t.GetLayer(),ends,round(w,6)))
finalsig={signature(t) for t in b.GetTracks()};preserved=[t for t in src.GetTracks() if signature(t) in finalsig]
power=[]
for net in ['EXT_5V','FUSED_5V','BL_5V','BL_POWER','BL_SW','BL_LEDA','BL_LEDK','HOST_3V3','LCD_VCI','TP_VDD','HOST_TP_3V3']:
 ts=[t for t in traces if norm(t.GetNetname())==net];power.append({'net':net,'total_branch_length_mm':sum(P.ToMM(t.GetLength()) for t in ts),'widths_mm':sorted({P.ToMM(t.GetWidth()) for t in ts}),'via_count':sum(norm(t.GetNetname())==net for t in vias),'all_branches_in_series_copper_R20_mohm_upper_bound':sum(.017241*P.ToMM(t.GetLength())/(P.ToMM(t.GetWidth())*.035) for t in ts)})
limits={'footprints':53,'numbered_pin_memberships':len(expected),'net_count':len(set(expected.values())),'copper_layers':4,'board_mm':[55,45],'board_thickness_mm':1.6,'tracks':len(traces),'vias':len(vias),'GND_vias':len(grounds),'physical_DRC_violations':0,'unconnected_items':0,'parity_issues':0,'ERC_errors':0,'ERC_warnings':0,'source_pin_memberships_preserved':True,'source_component_UUID_and_paths_preserved':True,'physical_rules_and_exclusions_preserved':True,'source_copper_objects':len(src.GetTracks()),'source_copper_objects_preserved_geometrically':len(preserved),'placement_changes':len(placement),'DSI_planar_spread_mm':spread,'DSI_reference_sample_count':sum(q['checked'] for q in projection),'DSI_uncovered_centerline_samples_excluding_own_vias':0,'DSI_max_GND_return_via_distance_mm':max(y for x in dsi for y in x['nearest_GND_return_via_mm']),'manufacturer_stackup_confirmed':False,'impedance':'Nominal 2D only; no manufactured coupon, mask/3D/via/FPC/channel verification','board_sha256':hashlib.sha256((p/f'{name}.kicad_pcb').read_bytes()).hexdigest()}
for fn,obj in [('Validation_Summary.json',limits),('Placement_Changes.json',placement),('DSI_Routes.json',{'conductors':dsi,'pairs':pairs,'maximum_planar_spread_mm':spread}),('DSI_Reference_Projection.json',projection),('Power_Geometry.json',power)]: (v/fn).write_text(json.dumps(obj,indent=2))
with (root/'Engineering/Component_Placement.csv').open('w',newline='') as out:
 w=csv.DictWriter(out,fieldnames=list(parts[0]));w.writeheader();w.writerows(parts)
print(json.dumps(limits,indent=2));print(json.dumps(pairs,indent=2))
