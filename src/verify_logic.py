"""Independent connectivity/Boolean check. This does not invoke Logisim."""
from pathlib import Path
from itertools import product
import xml.etree.ElementTree as ET
import csv

base=Path(__file__).resolve().parents[1]
c=ET.parse(base/'src/automatic_street_light.circ').find('./circuit')
def pt(v): return tuple(map(int,v.strip('()').split(',')))
def attrs(comp): return {a.get('name'):a.get('val') for a in comp.findall('a')}
parent={}
def find(a):
    parent.setdefault(a,a)
    if parent[a]!=a: parent[a]=find(parent[a])
    return parent[a]
def join(a,b): parent[find(a)]=find(b)
for wire in c.findall('wire'): join(pt(wire.get('from')),pt(wire.get('to')))
pins={}; gates=[]; leds=[]
for comp in c.findall('comp'):
    a=attrs(comp); loc=pt(comp.get('loc')); name=comp.get('name')
    if name=='Pin': pins[a['label']]=(loc,a.get('output')=='true')
    elif name=='LED': leds.append(loc)
    elif name.endswith('Gate'):
        assert a.get('facing','east')=='east'
        x,y=loc
        if name=='NOT Gate':
            assert a['size']=='30'
            inputs=[(x-30,y)]
        else:
            assert a['size']=='50' and a['inputs']=='2'
            inputs=[(x-50,y-20),(x-50,y+20)]
        gates.append((name,loc,inputs))
    else: raise ValueError('Unsupported component '+name)
assert set(pins)=={'E','D','M','L'}
assert all(not pins[k][1] for k in ('E','D','M')) and pins['L'][1]
assert len(gates)==3 and len(leds)==1
assert find(leds[0])==find(pins['L'][0])
expected={tuple(int(r[k]) for k in ['E','D','M']):int(r['Expected_L']) for r in csv.DictReader((base/'data/expected_truth_table.csv').open())}
lines=['Independent circuit connectivity and Boolean verification','Not a Logisim simulation run.','E D M | Calculated L | Expected L']
for e,d,m in product(range(2),repeat=3):
    signals={find(pins[k][0]):v for k,v in zip(('E','D','M'),(e,d,m))}
    pending=gates[:]
    while pending:
        progress=False
        for gate in pending[:]:
            name,out,inputs=gate
            if all(find(i) in signals for i in inputs):
                v=[signals[find(i)] for i in inputs]
                result=(1-v[0]) if name=='NOT Gate' else (int(any(v)) if name=='OR Gate' else int(all(v)))
                node=find(out)
                assert node not in signals, 'Multiple drivers'
                signals[node]=result;pending.remove(gate);progress=True
        assert progress,'Disconnected or cyclic gate inputs'
    actual=signals[find(pins['L'][0])]
    assert actual==expected[(e,d,m)]
    lines.append(f'{e} {d} {m} |      {actual}       |      {expected[(e,d,m)]}')
lines.append('PASS: all 8 combinations agree with the expected table.')
report='\n'.join(lines)+'\n'
print(report)
(base/'results/independent_verification.txt').write_text(report,encoding='utf-8')
