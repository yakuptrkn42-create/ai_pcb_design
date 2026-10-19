from pathlib import Path
import json,xml.etree.ElementTree as ET
import pcbnew as p
root=Path(__file__).resolve().parents[1]
b=p.LoadBoard(str(root/'Project/BatteryPack_RevA.kicad_pcb'))
fps={f.GetReference():f for f in b.GetFootprints()}
def n(ref,pad):return next(q.GetNetname() for q in fps[ref].Pads() if q.GetNumber()==str(pad))
expected={('J1',1):'PACK_PLUS',('J1',2):'PACK_PLUS_AUX',('J1',3):'HOST_NTC',('J1',4):'PACK_MINUS',('F1',1):'PROTECTED_PLUS',('F1',2):'PACK_PLUS',('R40',1):'PACK_PLUS',('R40',2):'AUX_PRE_FUSE',('F2',1):'AUX_PRE_FUSE',('F2',2):'PACK_PLUS_AUX',('TH1',1):'BMS_TS',('TH1',2):'CELL_MINUS',('TH2',1):'HOST_NTC',('TH2',2):'PACK_MINUS',('PAD7','PAD'):'CELL_PLUS',('PAD1','PAD'):'CELL_MID',('PAD8','PAD'):'CELL_MINUS',('R5',1):'CELL_MINUS',('R5',2):'PACK_MINUS',('U2',4):'BMS_TS',('Q2',1):'PROTECTED_PLUS'}
for pair,name in expected.items():assert n(*pair)==name,(pair,n(*pair),name)
assert n('J1',4)!=n('PAD8','PAD')
assert n('J1',1)!=n('PAD7','PAD')
netlist=ET.parse(root/'Verification/Recovered_Netlist.xml').getroot()
xml={(node.get('ref'),node.get('pin')):net.get('name') for net in netlist.findall('./nets/net') for node in net.findall('node')}
board={(f.GetReference(),q.GetNumber()):q.GetNetname() for f in b.GetFootprints() if not f.GetAttributes()&p.FP_BOARD_ONLY for q in f.Pads() if q.GetNumber()}
assert board==xml,[(k,board.get(k),xml.get(k)) for k in board.keys()|xml.keys() if board.get(k)!=xml.get(k)]
erc=json.loads((root/'Verification/ERC_RevA.json').read_text());assert all(not s['violations'] for s in erc['sheets'])
drc=json.loads((root/'Verification/DRC_RevA.json').read_text());assert not drc['violations'] and not drc['unconnected_items'] and not drc['schematic_parity']
result={'interface_assertions_passed':len(expected),'unique_pad_net_pairs_matched':len(board),'schematic_components':len(netlist.findall('./components/comp')),'physical_DRC_violations':0,'unconnected_items':0,'schematic_parity_issues':0,'ERC_violations':0,'scope':'Recovered passive pad symbols; functional IC ratings, firmware, battery performance and medical safety are NOT validated'}
(root/'Verification/Independent_Connectivity_Check.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
