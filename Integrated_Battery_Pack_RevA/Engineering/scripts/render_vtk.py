import sys,json,numpy as np

import vtk
from vtk.util.numpy_support import numpy_to_vtk
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
root=Path(__file__).resolve().parents[2];cache=root/'Engineering/RenderCache';cache.mkdir(exist_ok=True);mesh=json.loads((root/'Engineering/cad_mesh.json').read_text())
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
for name,exploded in [('01_Assembly_Isometric',False),('02_Exploded_Assembly',True),('08_Cell_Tray',False)]:
 ren=vtk.vtkRenderer();ren.SetBackground(.957,.965,.98)
 for m in mesh:
  if name=='08_Cell_Tray' and (m['group'] in ['pcb','electronics','connector','fasteners'] or 'Fishpaper' in m['name']):continue
  verts=np.array(m['vertices'],dtype=float)
  if exploded and m['group'] in ['pcb','electronics','connector','fasteners']:verts[:,2]+=19
  if exploded and m['group']=='insulation':verts[:,2]+=7
  pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(verts,deep=True));cells=vtk.vtkCellArray()
  for f in m['faces']:
   cells.InsertNextCell(3)
   for k in f:cells.InsertCellPoint(int(k))
  poly=vtk.vtkPolyData();poly.SetPoints(pts);poly.SetPolys(cells)
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(poly)
  actor=vtk.vtkActor();actor.SetMapper(mapper);pr=actor.GetProperty();pr.SetColor(*m['color']);pr.SetAmbient(.28);pr.SetDiffuse(.72);pr.SetSpecular(.18);pr.SetSpecularPower(24)
  ren.AddActor(actor)
 win=vtk.vtkEGLRenderWindow();win.SetOffScreenRendering(1);win.AddRenderer(ren);win.SetSize(1800,1100);win.SetMultiSamples(8)
 cam=ren.GetActiveCamera();cam.SetPosition(125,-135,120);cam.SetFocalPoint(37,21,21 if exploded else 14);cam.SetViewUp(0,0,1);cam.ParallelProjectionOn();cam.SetParallelScale(47 if exploded else 43)
 ren.ResetCameraClippingRange();win.Render()
 capture=vtk.vtkWindowToImageFilter();capture.SetInput(win);capture.Update()
 wr=vtk.vtkPNGWriter();wr.SetFileName(str(cache/(name+'.png')));wr.SetInputConnection(capture.GetOutputPort());wr.Write();win.Finalize()
 scene=Image.open(str(cache/(name+'.png'))).convert('RGB')
 page=Image.new('RGB',(2040,1480),(244,246,250));page.paste(scene,(120,210));dr=ImageDraw.Draw(page)
 dr.text((110,55),'Entegre 2S batarya paketi',font=ImageFont.truetype(bold,54),fill='#1b304d')
 dr.text((110,135),'2 × 18650  •  BMS PCB  •  sabit 4 kontak  •  10 kΩ NTC',font=ImageFont.truetype(font,28),fill='#48607d')
 dr.text((110,1320),'Patlatılmış montaj — ayrılma mesafeleri gösterim içindir' if exploded else ('Pil grubu, nikel bağlantılar ve taşıyıcı — PCB kaldırılmıştır' if name=='08_Cell_Tray' else 'Birleşik montaj — CAD geometrisinden alınan görünüm'),font=ImageFont.truetype(font,25),fill='#485973')
 dr.text((110,1370),'74 × 42 × yaklaşık 29,2 mm  |  Rev A — TASARIMCIYA AKTARIM / ÜRETİM ONAYI YOK',font=ImageFont.truetype(font,23),fill='#485973')
 path=root/'Views'/str(name+'.png');page.save(path)
 pdf=canvas.Canvas(str(path.with_suffix('.pdf')),pagesize=(842,611));pdf.drawImage(ImageReader(page),0,0,width=842,height=611);pdf.showPage();pdf.save()
 print('Rendered',name,flush=True)
