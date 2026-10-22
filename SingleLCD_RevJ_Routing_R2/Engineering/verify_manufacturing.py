"""Check native CAM layers and compare every Excellon hit to the board drill geometry."""
from pathlib import Path
import os,json,re,collections,hashlib,tempfile
for k,s in [('XDG_CONFIG_HOME','config'),('XDG_CACHE_HOME','cache'),('XDG_DATA_HOME','data')]:os.environ.setdefault(k,str(Path(tempfile.gettempdir())/'kicad-r2-cam'/s));Path(os.environ[k]).mkdir(parents=True,exist_ok=True)
import pcbnew as P
root=Path(__file__).resolve().parents[1];name='STM32F469_DISEN_RevJ_Prep1';b=P.LoadBoard(str(root/'Project'/f'{name}.kicad_pcb'));g=root/'Manufacturing/Gerber';d=root/'Manufacturing/Drill'
expected=[]
def hit(x,y,diam,plated):return (round(x,4),round(y,4),round(diam,4),plated)
for q in b.GetTracks():
 if type(q).__name__=='PCB_VIA':expected.append(hit(P.ToMM(q.GetPosition().x),P.ToMM(q.GetPosition().y),P.ToMM(q.GetDrill()),True))
for fp in b.GetFootprints():
 for q in fp.Pads():
  s=q.GetDrillSize()
  if s.x:
   assert s.x==s.y,'Slot requires explicit slot parser'
   expected.append(hit(P.ToMM(q.GetPosition().x),P.ToMM(q.GetPosition().y),P.ToMM(s.x),q.GetAttribute()!=P.PAD_ATTRIB_NPTH))
actual=[];toolsum=[]
for f in d.glob('*.drl'):
 s=f.read_text();assert 'METRIC' in s and 'absolute' in s and s.strip().endswith('M30');tools={int(i):float(di) for i,di in re.findall(r'^T(\d+)C([\d.]+)',s,re.M)};tool=None;plated='NonPlated' not in s
 for line in s.splitlines():
  m=re.fullmatch(r'T(\d+)',line)
  if m:tool=int(m[1])
  m=re.fullmatch(r'X(-?[\d.]+)Y(-?[\d.]+)',line)
  if m:assert tool in tools;actual.append(hit(float(m[1]),-float(m[2]),tools[tool],plated))
 toolsum.append({'file':f.name,'plated':plated,'tools_mm':tools,'hits':sum(x[3]==plated for x in actual)})
# Native Excellon decimal format rounds XY to 0.001 mm. Match each hit once.
remaining=actual.copy();maximum_xy_error=0.
for want in expected:
 candidates=[(i,q) for i,q in enumerate(remaining) if q[3]==want[3] and abs(q[2]-want[2])<.00001 and abs(q[0]-want[0])<=.00051 and abs(q[1]-want[1])<=.00051]
 assert len(candidates)==1,(want,candidates)
 i,q=candidates[0];maximum_xy_error=max(maximum_xy_error,abs(q[0]-want[0]),abs(q[1]-want[1]));remaining.pop(i)
assert not remaining

expected_ext={'gtl','g1','g2','gbl','gts','gbs','gto','gbo','gtp','gbp','gm1'};files=list(g.glob('*'));gerbers=[q for q in files if q.suffix!='.gbrjob'];assert {q.suffix[1:] for q in gerbers}==expected_ext
for f in gerbers:
 s=f.read_text();assert '%MOMM*%' in s and s.strip().endswith('M02*'),f
edge=next(q for q in gerbers if q.suffix=='.gm1').read_text();coords=[(int(x)/1e6,-int(y)/1e6) for x,y in re.findall(r'X(-?\d+)Y(-?\d+)D0[12]\*',edge)];assert coords;extents=[min(a[0] for a in coords),min(a[1] for a in coords),max(a[0] for a in coords),max(a[1] for a in coords)];assert extents==[115.5,70.,170.5,115.]
job=json.loads(next(g.glob('*.gbrjob')).read_text());assert len(job['FilesAttributes'])==11
for f in job['FilesAttributes']:assert (g/f['Path']).is_file()
boardhash=hashlib.sha256((root/'Project'/f'{name}.kicad_pcb').read_bytes()).hexdigest();assert boardhash==json.loads((root/'Verification/Validation_Summary.json').read_text())['board_sha256']
report={'passed':True,'copper_layers':4,'gerber_layer_files':11,'Gerber_X2_job_files':1,'all_Gerbers_metric_complete':True,'drill_origin':'absolute; Gerber and drill use same PCB datum; Y restored to PCB orientation in comparison','outline_mm':extents,'board_dimensions_mm':[55,45],'expected_drill_hits':len(expected),'actual_drill_hits':len(actual),'plated_hits':sum(x[3] for x in actual),'NPTH_hits':sum(not x[3] for x in actual),'all_drill_XY_diameters_plating_match_native_board':True,'drill_XY_per_axis_comparison_tolerance_mm':.00051,'maximum_drill_XY_serialization_rounding_mm':maximum_xy_error,'drill_precision_note':'Native Excellon rounds XY to 0.001 mm; electrical DRC constraints are unchanged','native_board_hash_unchanged':boardhash,'manufacturer_DFM_or_impedance_approval':False,'files_sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((root/'Manufacturing').rglob('*')) if f.is_file()}}
(root/'Verification/Manufacturing_Audit.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='files_sha256'},indent=2))
