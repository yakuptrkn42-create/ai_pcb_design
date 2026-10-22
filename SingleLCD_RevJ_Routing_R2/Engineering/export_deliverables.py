from pathlib import Path
import os,subprocess,json,tempfile
root=Path(__file__).resolve().parents[1];p=root/'Project';name='STM32F469_DISEN_RevJ_Prep1';board=str(p/f'{name}.kicad_pcb');sch=str(p/f'{name}.kicad_sch');env=os.environ.copy()
for k,s in [('XDG_CONFIG_HOME','config'),('XDG_CACHE_HOME','cache'),('XDG_DATA_HOME','data')]:env.setdefault(k,str(Path(tempfile.gettempdir())/'kicad-r2-exports'/s));Path(env[k]).mkdir(parents=True,exist_ok=True)
steps=[]
def run(args):
 r=subprocess.run(args,cwd=root,env=env,capture_output=True,text=True);steps.append({'command':args,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr});(root/'Verification/Native_Exports.json').write_text(json.dumps(steps,indent=2));assert r.returncode==0,steps[-1];print(args[1:4],'OK',flush=True)
run(['kicad-cli','pcb','drc','--schematic-parity','--exit-code-violations','-o',str(root/'Verification/DRC_Final.txt'),board])
run(['kicad-cli','sch','erc','--exit-code-violations','-o',str(root/'Verification/ERC_Final.txt'),sch])
run(['kicad-cli','sch','export','pdf','-o',str(root/'PDF/Schematic_R2.pdf'),sch])
for name,layers in [('Top','F.Cu,F.Silkscreen,Edge.Cuts'),('Bottom','B.Cu,B.Silkscreen,Edge.Cuts'),('In1_GND','In1.Cu,Edge.Cuts'),('In2_GND','In2.Cu,Edge.Cuts'),('Assembly','F.Fab,Edge.Cuts')]:
 run(['kicad-cli','pcb','export','svg','--mode-single','--layers',layers,'--fit-page-to-board','--exclude-drawing-sheet','-o',str(root/f'Views/{name}.svg'),board])
 run(['inkscape',str(root/f'Views/{name}.svg'),'--export-area-drawing','--export-width=1800',f'--export-filename={root}/Views/{name}.png'])
run(['kicad-cli','pcb','export','gerbers','--layers','F.Cu,In1.Cu,In2.Cu,B.Cu,F.Mask,B.Mask,F.Silkscreen,B.Silkscreen,F.Paste,B.Paste,Edge.Cuts','--subtract-soldermask','-o',str(root/'Manufacturing/Gerber')+'/',board])
run(['kicad-cli','pcb','export','drill','--format','excellon','--drill-origin','absolute','--excellon-units','mm','--excellon-separate-th','--generate-map','--map-format','pdf','-o',str(root/'Manufacturing/Drill')+'/',board])
run(['kicad-cli','pcb','render','--quality','high','--width','1800','--height','1300','--background','opaque','--rotate','325,0,25','-o',str(root/'Views/PCB_3D.png'),board])
