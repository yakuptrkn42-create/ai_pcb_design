from pathlib import Path
import xml.etree.ElementTree as ET,json,sys,csv,math
from sexp_edit import parse
base=Path(__file__).resolve().parents[1];p=base/'Project';out=base/'Verification'
def netlist(path):
 r=ET.parse(path).getroot(); comps={c.attrib['ref']:c for c in r.findall('./components/comp')};nets={n.attrib['name']:frozenset((x.attrib['ref'],x.attrib['pin']) for x in n) for n in r.findall('./nets/net')};pin={pair:name for name,pairs in nets.items() for pair in pairs};return comps,nets,pin
ci,ni,pi=netlist(out/'input.xml');cf,nf,pf=netlist(out/'revised.xml')
assert set(ci)==set(cf),'component set changed'
assert set(ni.values())==set(nf.values()),'physical connectivity changed'
renames=[{'before':a,'after':b} for a,x in ni.items() for b,y in nf.items() if x==y and a!=b]
exp={1:'BL_LEDA',2:'BL_LEDA',3:'BL_LEDK',4:'BL_LEDK',**dict.fromkeys([7,8,9,10],'LCD_VCI'),12:'LCD_RST',13:'LCD_TE',16:'DSI_D0_P',17:'DSI_D0_N',20:'DSI_D1_P',21:'DSI_D1_N',24:'DSI_CLK_P',25:'DSI_CLK_N',30:'TP_VDD',31:'TP_VDD',32:'TP_SCL',33:'TP_SDA',34:'TP_RST',35:'TP_INT',**dict.fromkeys([11,14,15,18,19,22,23,26,27,28,29,36,37],'GND')}
for k in [5,6,38,39]:exp[k]='NC'
rows=[]
for k,v in sorted(exp.items()):
 a=pf[('J2',str(k))];passed=(len(nf[a])==1 and a.startswith('unconnected-')) if v=='NC' else a==v
 rows.append([k,v,a,'PASS' if passed else 'FAIL']);assert passed,(k,v,a)
with (out/'LCD_39_Pin_Audit.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['J2_pin','DISEN_p7_expected','actual_net','result']);w.writerows(rows)
host={1:'NC',2:'GND',3:'GND',4:'GND',5:'HOST_LCD_RST',6:'HOST_3V3',7:'GND',8:'DSI_D0_N',9:'NC',10:'DSI_D0_P',11:'GND',12:'DSI_CLK_N',13:'NC',14:'DSI_CLK_P',15:'GND',16:'DSI_D1_N',17:'NC',18:'DSI_D1_P',19:'GND',20:'NC',21:'HOST_3V3',22:'HOST_TE',23:'NC',24:'NC',25:'GND'}
with (out/'Host_CN10_25_Pin_Audit.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['J1_pin','UM1932_table7_expected_design_net','actual_net','result'])
 for k,v in host.items():
  a=pf['J1',str(k)];ok=(len(nf[a])==1 and a.startswith('unconnected-')) if v=='NC' else a==v;assert ok;w.writerow([k,v,a,'PASS'])
# CN2 order independently read from ST MB1189-C01 sheet 7; pin 5 is intentionally unused.
host_cn2={1:'HOST_TP_3V3',2:'TP_INT',3:'TP_SCL',4:'TP_SDA',6:'GND'}
for k,v in host_cn2.items(): assert pf['J3',str(k)]==v
assert len(nf[pf['J3','5']])==1
with (out/'Host_CN2_6_Pin_Audit.csv').open('w') as f:
 w=csv.writer(f); w.writerow(['J3_pin','MB1189_C01_CN2_signal','actual_net','result'])
 for k in range(1,7):w.writerow([k,host_cn2.get(k,'PH7 reset intentionally NC'),pf['J3',str(k)],'PASS'])
for ref,pin,net in [('J6','1','EXT_5V'),('J6','2','GND'),('J4','1','BL_PWM_RAW'),('J4','2','HOST_TP_RST'),('J4','3','GND'),('U1','1','BL_POWER'),('U1','2','BL_CTRL'),('U1','4','GND'),('U1','6','BL_LEDK'),('U2','1','BL_CTRL'),('U2','2','GND'),('U2','3','OVP_REF'),('U2','5','OVP_REF'),('U2','6','BL_POWER')]:assert pf[ref,pin]==net
assert pf['U1','3']==pf['L1','2']==pf['D1','2']
assert pf['U1','5']==pf['C9','1']
assert pf['U2','4']==pf['R19','2']==pf['R20','1']
# Every physical symbol pin is represented by its assigned footprint pad.
foot=[]
for ref,c in cf.items():
 fp=c.findtext('footprint');lib,name=fp.split(':');assert lib=='Adapter_F469',fp
 f=p/(lib+'.pretty')/(name+'.kicad_mod');assert f.is_file(),f
 r=parse(f.read_text());pads={n.arg() for n in r.all('pad') if n.arg()}
 pins={pin for rr,pin in pf if rr==ref}
 assert pins<=pads,(ref,pins-pads)
 foot.append(dict(reference=ref,footprint=fp,numbered_pads=sorted(pads),symbol_pins=sorted(pins),result='PASS'))
(out/'Footprint_Pin_Audit.json').write_text(json.dumps(foot,indent=2))
for sch in p.glob('*.kicad_sch'):
 r=parse(sch.read_text());lib={n.arg():n for n in r.one('lib_symbols').all('symbol')}
 for sym in r.all('symbol'):
  assert sym.one('lib_id').arg() in lib
  for pr in sym.all('property'):
   if pr.arg()=='Reference' and not pr.arg(2).startswith('#'):
    assert pr.arg(2) in cf
# Core quantitative checks. Vin/efficiency are engineering corners, not measured guarantees.
vfbmax=.204;rmin=5.23*.99;i=vfbmax/rmin;vout=27.2+vfbmax
ipload=i+vout/33000+vout/231000
vin=4.2;eta=.75;L=13.2e-6;fs=1e6;d=1-vin/(vout+.5);di=vin*d/L/fs;iavg=vout*ipload/vin/eta
calc={'led_current_nominal_mA':.2/5.23*1000,'led_current_min_mA':.196/(5.23*1.01)*1000,'led_current_max_mA':i*1000,'R7_power_max_mW':.204**2/rmin*1000,'ack_sink_upper_mA_at_3V6':3.6/(8200*.99)*1000,'ctrl_high_lower_V_at_3V0':3/(1+8200*1.01/(100000*.99)+8200*1.01/400000),'ovp_nominal_V':1.242*(1+221000/10000),'active_payload_Mbps_per_lane_at_60Hz_RGB888':280*1424*24*60/2/1e6,'framebuffer_RGB888_bytes':280*1424*3,'boost_assumed_Vin_min_V':vin,'boost_assumed_efficiency':eta,'boost_assumed_L_min_uH':L*1e6,'boost_assumed_switch_freq_Hz':fs,'boost_estimated_duty':d,'boost_estimated_input_A':iavg,'boost_estimated_ripple_peak_to_peak_A':di,'boost_estimated_peak_inductor_A':iavg+di/2,'tps61165_current_limit_min_A':.96,'tps61165_current_limit_max_A':1.44,'estimated_C3_10uF_discharge_s_to_5V_from_28V69':33000*10e-6*math.log(28.69/5)}
assert calc['ack_sink_upper_mA_at_3V6']<.5
assert calc['ctrl_high_lower_V_at_3V0']>1.2
(out/'Engineering_Calculations.json').write_text(json.dumps(calc,indent=2))
summary={'component_count_including_4_mounting_holes':len(cf),'circuit_components':len(cf)-4,'net_count_including_NC':len(nf),'connected_net_count':sum(len(x)>1 for x in nf.values()),'component_set_preserved':True,'all_physical_net_partitions_preserved':True,'net_scope_renames':renames,'panel_pins_checked':len(exp),'host_CN10_pins_checked':len(host),'footprints_checked':len(foot),'ERC_rules_unchanged':json.loads((p/'STM32F469_DISEN_RevJ_Prep1.kicad_pro').read_text())['erc']==json.loads((base/'Original/input_project_settings.json').read_text())['erc'],'manufacturer_U2_validation':'PASS - TI SBOS300C pinout, 1.65-5.5V, fail-safe, POR Hi-Z, internal hysteresis; transient acceptance still requires bench measurements','physical_CN2_pin_order':'PASS for MB1189-C01 drawing; actual board revision and FPC continuity still require physical confirmation','hardware_measurements':'NOT RUN'}
(out/'Validation_Summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2));print(json.dumps(calc,indent=2))
