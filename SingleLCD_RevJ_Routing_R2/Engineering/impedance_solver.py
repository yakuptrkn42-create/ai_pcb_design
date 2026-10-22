"""2D electrostatic finite-volume estimate. No soldermask/etch or 3D launch model."""
from pathlib import Path
import json,math
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
EPS0=8.8541878128e-12;C=299792458.
def solve(w=.14,g=.18,h=.1,t=.035,er=4.2,step=.005,domain=(2.,.7),single=False):
 nx,ny=(round(d/step) for d in domain);x=(np.arange(nx)+.5)*step-domain[0]/2;y=(np.arange(ny)+.5)*step
 metal=np.zeros((ny,nx),np.int8)
 masky=(y>=h-1e-8)&(y<h+t-1e-8)
 if single:metal[np.ix_(masky,abs(x)<w/2)]=1
 else:
  metal[np.ix_(masky,(x>=g/2-1e-8)&(x<g/2+w-1e-8))]=1
  metal[np.ix_(masky,(x>=-g/2-w+1e-8)&(x<-g/2+1e-8))]=-1
 fixed=metal!=0;fixed[0,:]=fixed[-1,:]=True;fixed[:,0]=fixed[:,-1]=True
 voltage=metal.astype(float);uid=np.full((ny,nx),-1,np.int32);uid[~fixed]=np.arange(np.count_nonzero(~fixed));n=uid.max()+1
 def cap(diel):
  eps=np.where(y[:,None]<h,diel,1.)*np.ones((ny,nx));rr=[];cc=[];vv=[];rhs=np.zeros(n);diag=np.zeros(n)
  for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
   y0=slice(max(0,-dy),min(ny,ny-dy));x0=slice(max(0,-dx),min(nx,nx-dx));y1=slice(max(0,dy),min(ny,ny+dy));x1=slice(max(0,dx),min(nx,nx+dx));a=uid[y0,x0];b=uid[y1,x1];ea=eps[y0,x0];eb=eps[y1,x1];k=2*ea*eb/(ea+eb);valid=a>=0;av=a[valid];bv=b[valid];kv=k[valid];diag[av]+=kv
   # Metal faces are half a grid cell from adjacent dielectric centers.
   is_metal=metal[y1,x1][valid]!=0;kv[is_metal]=2*ea[valid][is_metal];diag[av]+=kv-k[valid]
   free=bv>=0;rr.append(av[free]);cc.append(bv[free]);vv.append(-kv[free]);rhs[av[~free]]+=kv[~free]*voltage[y1,x1][valid][~free]
  rr.append(np.arange(n));cc.append(np.arange(n));vv.append(diag);A=coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),shape=(n,n)).tocsr();u=voltage.copy();u[~fixed]=spsolve(A,rhs)
  q=0.
  for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
   y0=slice(max(0,-dy),min(ny,ny-dy));x0=slice(max(0,-dx),min(nx,nx-dx));y1=slice(max(0,dy),min(ny,ny+dy));x1=slice(max(0,dx),min(nx,nx+dx));sel=(metal[y0,x0]==1)&(metal[y1,x1]!=1);ea=eps[y0,x0];eb=eps[y1,x1];k=2*eb;q+=np.sum(k[sel]*(1-u[y1,x1][sel]))
  return q*EPS0
 c=cap(er);c0=cap(1.);z=(1 if single else 2)/(C*math.sqrt(c*c0));return {'width_mm':w,'gap_mm':None if single else g,'h_mm':h,'copper_mm':t,'Er':er,'grid_mm':step,'domain_mm':domain,'single_ended':single,'Z_ohm':z,'Codd_F_per_m':c,'Codd_vacuum_F_per_m':c0,'epsilon_eff':c/c0,'velocity_mm_per_ns':C/math.sqrt(c/c0)/1e6}
if __name__=='__main__':
 out={'method':'2D finite-volume electrostatic odd-mode; rectangular copper, air above FR4, finite grounded domain','manufacturer_stackup_confirmed':False,'target_differential_ohm':100,'excludes':['soldermask','etch trapezoid','dispersion','glass weave','vias','connectors','FPC'],'cases':[]}
 for kw in [{'step':.005},{'step':.0025},{'h':.09},{'h':.11},{'er':3.9},{'er':4.5},{'w':.17,'single':True}]:
  a=solve(**kw);out['cases'].append(a);print(a,flush=True)
 (Path(__file__).resolve().parents[1]/'Verification/Impedance_Calculation.json').write_text(json.dumps(out,indent=2))
