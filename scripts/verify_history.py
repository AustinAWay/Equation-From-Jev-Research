from pathlib import Path
from collections import defaultdict
import json,csv,statistics,sys,hashlib
import argparse
parser=argparse.ArgumentParser(description='Recompute historical arithmetic and raw fresh100 medians from extracted archives.')
parser.add_argument('research_root', type=Path)
args=parser.parse_args()
root=args.research_root.resolve();repo=Path(__file__).resolve().parents[1];sys.path.insert(0,str(repo/'scripts'))
from verify_results import metrics

def rows(f):return [json.loads(s) for s in f.read_text().splitlines() if s.strip()]
checks={}
for folder,predfile,resultfile in [
 ('working-memory-equation','final_predictions.jsonl','final_results.json'),
 ('working-memory-equation-round2','final_predictions.jsonl','final_results.json'),
 ('working-memory-equation-round3','all-final-predictions.csv','final-results.json'),
 ('working-memory-equation-round4','all-final-predictions.jsonl','final-results.json')]:
 p=root/'outputs'/folder;f=p/predfile
 if f.suffix=='.csv':
  data=list(csv.DictReader(f.open()))
  for r in data:
   for k in ['target','prediction','raw_prediction']:r[k]=float(r[k])
 else:data=rows(f)
 original=json.loads((p/resultfile).read_text());groups=defaultdict(list)
 for r in data:groups[r.get('model','selected')].append(r)
 checked={}
 for model,batch in groups.items():
  result=metrics(batch,[r['prediction'] for r in batch]);expected=original['metrics'] if model=='selected' else original['metrics'][model]
  for k,v in result.items():assert abs(v-expected[k])<1e-12,(folder,model,k,v,expected[k])
  assert len({(r['id'],r['segment_id']) for r in batch})==len(batch)
  if 'repeat_targets' in batch[0]:
   for r in batch:assert r['target']==statistics.median(r['repeat_targets'].values())
  checked[model]=result
 checks[folder]={'models_checked':len(groups),'prediction_rows':len(data),'metrics':checked}
# Check raw repeated responses against all 910 comparison targets.
reference={};raw_paths=[]
for f in (root/'work/fresh100-20260924/reference/raw').glob('*.json'):
 d=json.loads(f.read_text());rid=d['record']['id'];rep=str(d['repeat']);raw_paths.append(f)
 for s in d['scores']['rows']:
  key=(rid,s['segment_id'],rep);assert key not in reference
  reference[key]=s['target']
comparison=rows(repo/'data/comparison.jsonl')
for r in comparison:
 for rep,target in r['repeat_targets'].items():assert reference[(r['id'],r['segment_id'],rep)]==target
 assert statistics.median([reference[(r['id'],r['segment_id'],str(rep))] for rep in [1,2,3]])==r['target']
checks['fresh100_raw_reference']={'raw_analyses':len(raw_paths),'step_repeat_scores_checked':len(reference),'median_rows_checked':len(comparison)}
assert len(raw_paths)==300 and len(reference)==2730
# Raw-score distribution and freeze dates are evidence recorded by the experiment.
fresh=json.loads((root/'outputs/working-memory-fresh100/results.json').read_text())
checks['fresh100_reference_flags']={k:sum(bool(r[k]) for r in comparison) for k in ['inconsistent','provisional','coverage_limited']}
for k,v in {'inconsistent':267,'provisional':880,'coverage_limited':910}.items():assert checks['fresh100_reference_flags'][k]==v
report={'status':'passed','checks':checks,'scope':'Arithmetic reproduction and saved raw-score consistency. No fresh service collection, retraining or human validation.'}

print(json.dumps({k:{t:v for t,v in d.items() if t!='metrics'} for k,d in checks.items()},indent=2))
