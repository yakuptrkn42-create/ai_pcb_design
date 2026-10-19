import sys,json,math
from pathlib import Path
sys.path.append('/usr/lib/freecad/lib')
import FreeCAD as A,Part,Import
V=A.Vector
root=Path(__file__).resolve().parents[2];out=root/'Mechanical';models=root/'Project/3D';models.mkdir(exist_ok=True)
doc=A.newDocument('IntegratedPack_Concept_RevA');objects=[];mesh=[]
def box(x,y,z,dx,dy,dz):return Part.makeBox(dx,dy,dz,V(x,y,z))
def cyl(r,h,x,y,z,axis=(0,0,1)):return Part.makeCylinder(r,h,V(x,y,z),V(*axis))
def feature(name,shape,color,group='assembly'):
 o=doc.addObject('Part::Feature',name);o.Label=name;o.Shape=shape
 if hasattr(o,'ViewObject') and o.ViewObject:o.ViewObject.ShapeColor=color
 objects.append(o)
 verts,faces=shape.tessellate(.12)
 mesh.append({'name':name,'group':group,'color':color,'vertices':[[v.x,v.y,v.z] for v in verts],'faces':[list(f) for f in faces]})
 return o
# Dimensions are a visual envelope, not a manufacturer's verified cell specification.
cell1=cyl(9.3,65.2,4.4,11,10.7,(1,0,0))
cell2=cyl(9.3,65.2,4.4,31,10.7,(1,0,0))
feature('Cell_1_18650_3500mAh',cell1,(.12,.43,.78),'cells')
feature('Cell_2_18650_3500mAh',cell2,(.12,.43,.78),'cells')
for x,y in [(69.6,11),(4.05,31)]:feature('Positive_terminal_'+str(y),cyl(3.0,.35,x,y,10.7,(1,0,0)),(.78,.79,.81),'cells')
# Lower carrier: radial seat, open-top end rails, mounting bosses and dock load bridge.
carrier=box(0,0,0,74,42,1.2)
for y in [0,40.8]:carrier=carrier.fuse(box(0,y,1.2,74,1.2,7))
for x in [0,71.2]:carrier=carrier.fuse(box(x,0,1.2,2.8,42,19.2))
# A shallow insulating central rib separates wrappers; straps retain the cells.
carrier=carrier.fuse(box(3,20.4,1.2,68,1.2,3.5))
for x,y in [(2.5,2.5),(71.5,2.5),(2.5,39.5),(71.5,39.5)]:
 carrier=carrier.fuse(cyl(2.4,21.8,x,y,1.2)).cut(cyl(.85,23,x,y,1.0))
for y in [9.01,32.99]:
 carrier=carrier.fuse(box(67,y-2.2,20.7,6.0,4.4,2.3)).cut(cyl(.65,4,68,y,20))
# Vent reliefs in the end rails leave the cell terminal and safety vent zone open.
for x in [0,71.2]:
 for y in [11,31]:carrier=carrier.cut(cyl(5.8,3.0,x-.1,y,10.7,(1,0,0)))
feature('Insulating_carrier_PA66_GF_concept',carrier,(.19,.21,.24),'carrier')
for x in [21,53]:
 strap=box(x,1.2,20.3,4,39.6,.5).fuse(box(x,1.2,7.2,4,.5,13.6)).fuse(box(x,40.3,7.2,4,.5,13.6))
 feature('Foam_pad_'+str(x),box(x,5,20.0,4,32,.3),(.35,.35,.38),'insulation')
 feature('Retention_strap_'+str(x),strap,(.31,.33,.36),'insulation')
# Fishpaper/FR insulation barrier below the electronics, clear of mounting bosses.
ins=box(5,2,21.2,60,38,.4)
for xx,yy,ww in [(3.5,8,8),(3.5,28,8),(56,27,14)]:ins=ins.cut(box(xx,yy,21,ww,7,1))
feature('Fishpaper_barrier_0p4mm',ins,(.73,.64,.40),'insulation')
# Board is above cell crowns; 1 mm thickness leaves 0.8 mm solder-tail protrusion.
pcb=box(2,0,23,70,42,1).fuse(box(0,2,23,74,38,1))
for xx,yy in [(2,2),(72,2),(2,40),(72,40)]:pcb=pcb.fuse(cyl(2,1,xx,yy,23))
for x,y,r in [(2.5,2.5,1.1),(71.5,2.5,1.1),(2.5,39.5,1.1),(71.5,39.5,1.1),(68,9.01,1.0),(68,32.99,1.0)]:pcb=pcb.cut(cyl(r,1.2,x,y,22.9))
feature('BMS_PCB_74x42x1',pcb,(.035,.37,.23),'pcb')
# Fixed, non-spring connector. Land coordinates follow the supplied 2.54 mm drawing.
housing=box(65.45,7.19,24,5.1,27.62,1.1).fuse(box(65.45,10.41,25.1,5.1,21.18,1.8))
for y in [9.01,32.99]:housing=housing.cut(cyl(1,1.3,68,y,23.9))
feature('J1_fixed_contact_housing_nominal',housing,(.12,.13,.15),'connector')
for i,y in enumerate([24.81,22.27,19.73,17.19],1):
 feature('Contact_'+str(i)+'_'+['PACK_PLUS','PACK_PLUS_AUX','NTC','PACK_MINUS'][i-1],cyl(.98 if i in [1,4] else .68,.22,68,y,28.9),(.90,.69,.22),'connector')
for y in [12.7,29.3]:feature('N52_magnet_'+str(y),cyl(2,1.5,68,y,27.4),(.57,.59,.62),'connector')
for x,y,r,h in [(2.5,2.5,.95,1),(71.5,2.5,.95,1),(2.5,39.5,.95,1),(71.5,39.5,.95,1),(68,9.01,.75,1),(68,32.99,.75,1)]:
 feature('Fastener_'+str(x)+'_'+str(y),cyl(r,h,x,y,24 if x!=68 else 25.1),(.65,.67,.70),'fasteners')
# Simplified component envelopes come from the revised PCB placement, not invented circuitry.
parts=json.loads((root/'Engineering/board_parts.json').read_text())
for f in parts:
 ref=f['reference'];val=f['value']
 if f['board_only'] or ref=='J1' or ref.startswith(('Pad','PAD','WIRE')):continue
 if ref.startswith('TH'):continue
 if ref.startswith('U'):dx,dy,dz=(3,4,.9) if ref=='U2' else (3,3,.9)
 elif ref in ['Q2','Q3']:dx,dy,dz=6,5,1.1
 elif ref.startswith('Q'):dx,dy,dz=2.9,1.6,1.0
 elif ref in ['R5','R40','F1','F2']:dx,dy,dz=3.2,1.6,.7
 elif ref.startswith(('R','C')):dx,dy,dz=(1,.5,.5)
 else:dx,dy,dz=2,1,.7
 angle=f['rotation']
 shape=box(-dx/2,-dy/2,0,dx,dy,dz)
 shape.exportStep(str(models/(ref+'.step')))
 if f['side']=='B':shape.rotate(V(0,0,0),V(1,0,0),180)
 shape.rotate(V(0,0,0),V(0,0,1),angle)
 shape.translate(V(f['x'],f['y'],24 if f['side']=='F' else 23))
 feature(ref+'_'+val.split('/')[0].replace(' ','_'),shape,(.19,.20,.22) if not ref.startswith('C') else (.60,.44,.27),'electronics')
# Small isolated beads thermally coupled to wrappers; two independent references.
for name,x,y,c in [('TH1_BMS',34,11,(.8,.4,.12)),('TH2_HOST',43,31,(.85,.32,.12))]:
 feature(name,Part.makeSphere(1.2,V(x,y,20.8)),c,'sensors')
# Nickel current straps shown at the ends; formed tinned solder tabs are nominal.
# Cell 1 positive and cell 2 negative meet at the right-hand series bridge.
series=box(69.95,8.0,7.7,.15,26,6.0).fuse(box(69.95,28,7.7,.15,6,14.1)).fuse(box(56,28,21.8,14.1,6,.15)).fuse(box(69.6,28,7.7,.5,6,.15))
feature('Nickel_series_bridge_B1',series,(.76,.77,.79),'nickel')
for name,y in [('Bminus_cell1',11),('Bplus_cell2',31)]:
 xx=4.25 if y==11 else 3.9
 tab=box(xx,y-3,7.7,.15,6,14.1).fuse(box(xx,y-3,21.8,10.5-xx,6,.15))
 feature('Nickel_'+name,tab,(.76,.77,.79),'nickel')
# PCB-side formed tab tongues pass through the retained PTH solder terminals.
for ref in ['PAD1','PAD7','PAD8']:
 f=next(x for x in parts if x['reference']==ref);x,y=f['x'],f['y']
 feature('Tinned_solder_tab_'+ref,box(x-1.25,y-.075,21.5,2.5,.15,3.3),(.80,.81,.83),'nickel')
(root/'Engineering/cad_mesh.json').write_text(json.dumps(mesh))
# Separately export reusable mechanical objects and the full actual CAD assembly.
doc.recompute()
Import.export(objects,str(out/'Integrated_Battery_Pack_RevA.step'))
doc.saveAs(str(out/'Integrated_Battery_Pack_RevA.FCStd'))
for o in objects:
 if any(tag in o.Name for tag in ['Cell_1','carrier','housing']):o.Shape.exportStep(str(out/(o.Name+'.step')))
# Reference assembly under PCB: exclude the PCB and electronics to avoid duplicate boards.
print('before underbody export',len(objects),len(mesh),flush=True)
under=[o.Shape for o,m in zip(objects,mesh) if m['group'] in ['cells','carrier','insulation','nickel','sensors']]
print('under shapes',len(under),flush=True)
under=Part.Compound(under);under.translate(V(0,0,-24))
print('underbody made',flush=True)
under.exportStep(str(models/'CellCarrier_Reference.step'))
# Connector footprint-local STEP, center of pins on board origin.
conn=Part.Compound([o.Shape for o,m in zip(objects,mesh) if m['group']=='connector']);conn.translate(V(-68,-21,-24));conn.exportStep(str(models/'J1_fixed.step'))
# Standards-compatible WRL files for each STEP (WRL coordinate unit 0.1 inch).
def wrl(shape,path):
 vs,fs=shape.tessellate(.12)
 coords=',\n'.join('%.6f %.6f %.6f'%(v.x/2.54,v.y/2.54,v.z/2.54) for v in vs)
 inds=',\n'.join('%d,%d,%d,-1'%f for f in fs)
 path.write_text('#VRML V2.0 utf8\n# Coordinates in 0.1 inch for KiCad\nShape { appearance Appearance { material Material { diffuseColor 0.6 0.6 0.6 } } geometry IndexedFaceSet { coord Coordinate { point [ '+coords+' ] } coordIndex [ '+inds+' ] } }\n')
wrl(Part.Compound([o.Shape for o in objects]),out/'Integrated_Battery_Pack_RevA.wrl')
for f in models.glob('*.step'):wrl(Part.read(str(f)),f.with_suffix('.wrl'))
(root/'Engineering/cad_mesh.json').write_text(json.dumps(mesh))
# Intentional solid intersections are assembly contacts; report selected critical clearances only.
checks={'cell_diameter_nominal_mm':18.6,'cell_length_envelope_mm':65.2,'cell_to_cell_surface_gap_mm':1.4,'cell_crown_to_pcb_underside_mm':3.0,'cell_crown_to_barrier_mm':1.2,'barrier_to_bottom_component_nominal_mm':.5,'pcb_size_mm':[74,42,1],'connector_fixed_top_nominal_z_mm':29.12,'minimum_mating_spring_stroke_mm':1.0,'mating_height_verified':False,'battery_brand_model_verified':False,'enclosure_release_status':'CONCEPT ONLY'}
(root/'Verification/Mechanical_Assumptions.json').write_text(json.dumps(checks,indent=2))
# Standalone colored assembly uses millimetres; footprint WRLs above use 0.1 inch.
colored=['#VRML V2.0 utf8\n# Full assembly in millimetres\n']
for idx,entry in enumerate(mesh):
 pts=',\n'.join('%.6f %.6f %.6f'%tuple(v) for v in entry['vertices'])
 faces=',\n'.join('%d,%d,%d,-1'%tuple(f) for f in entry['faces'])
 r,g,b=entry['color']
 colored.append('DEF PART_%d Shape { appearance Appearance { material Material { diffuseColor %f %f %f } } geometry IndexedFaceSet { solid FALSE coord Coordinate { point [ %s ] } coordIndex [ %s ] } }\n'%(idx,r,g,b,pts,faces))
(out/'Integrated_Battery_Pack_RevA.wrl').write_text(''.join(colored))
print('CAD saved:',len(objects),'solids/features',flush=True)
