"""Recompute results and replay five frozen equations without network access."""
from pathlib import Path
from collections import defaultdict
import argparse, hashlib, json, statistics, sys
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from jev_equations.predict import predict_matrix, extract

def rows(path):
    return [json.loads(s) for s in path.read_text().splitlines() if s.strip()]

def metrics(data, predictions):
    families = defaultdict(list)
    for r, p in zip(data, predictions):
        d = abs(float(p) - r['target'])
        families[r['family']].append((d == 0, d, d <= 1))
    return {k: statistics.mean(statistics.mean(r[j] for r in f) for f in families.values())
            for j, k in enumerate(['exact', 'mae', 'within_one'])}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--features', action='store_true', help='Re-extract all 910 comparison steps from raw text.')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    import socket
    def denied(*a, **kw): raise RuntimeError('Network disabled for reproduction')
    socket.socket.connect = denied
    socket.create_connection = denied
    comparison = rows(ROOT / 'data/comparison.jsonl')
    development = rows(ROOT / 'data/development.jsonl')
    features = np.load(ROOT / 'data/comparison-features.npz', allow_pickle=False)
    train = np.load(ROOT / 'data/train.npz', allow_pickle=False)
    names = json.loads((ROOT / 'data/features.json').read_text())['names']
    assert (len(development),len(comparison)) == (4726,910)
    assert (len({r['id'] for r in development}),len({r['family'] for r in development})) == (688,344)
    assert (len({r['id'] for r in comparison}),len({r['family'] for r in comparison})) == (100,50)
    for key in ['id','family']:
        assert not {r[key] for r in development} & {r[key] for r in comparison}
    for data, matrix in [(development,train),(comparison,features)]:
        assert len({(r['id'],r['segment_id']) for r in data}) == len(data)
        assert list(zip(matrix['id'],matrix['segment_id'])) == [(r['id'],r['segment_id']) for r in data]
        assert np.isfinite(matrix['X']).all()
        for r in data:
            repeat=list(r['repeat_targets'].values())
            assert len(repeat)==3 and r['target']==statistics.median(repeat)
    assert np.array_equal(train['y'],[r['target'] for r in development])
    assert 'y' not in features
    folds=json.loads((ROOT/'data/folds.json').read_text())['folds']
    coverage=np.zeros(len(train['X']),dtype=int)
    for f in folds:
        tr,va=f['train_indices'],f['validation_indices']
        assert not set(tr)&set(va)
        assert set(tr)|set(va)==set(range(len(train['X'])))
        assert not set(train['family'][tr])&set(train['family'][va])
        coverage[va]+=1
    assert np.all(coverage==1)
    result_path=ROOT/'results/nonlinear-text-equation-20260924'
    saved=json.loads((result_path/'comparison-predictions.json').read_text())
    expected=json.loads((result_path/'results.json').read_text())
    assert [(r['id'],r['segment_id'],r['target']) for r in saved]==[(r['id'],r['segment_id'],r['target']) for r in comparison]
    checked={}
    for name in saved[0]['predictions']:
        checked[name]=metrics(comparison,[r['predictions'][name] for r in saved])
        for k,v in checked[name].items():assert abs(v-expected['metrics'][name][k])<1e-12,(name,k)
    mapping={'gaussian':'gaussian','polynomial':'polynomial','spline':'spline','word-count':'word_count_spline','linear':'previous_32_term_formula'}
    for kind,column in mapping.items():
        prediction,probability=predict_matrix(kind,features['X'])
        assert np.array_equal(prediction,[r['predictions'][column] for r in saved]),kind
        if probability is not None:
            assert np.isfinite(probability).all()
            assert np.allclose(probability.sum(axis=1),1,atol=1e-12)
    count=0
    if args.features:
        for i,r in enumerate(comparison):
            measured=extract(r['passage'],r['start'],r['end'])
            assert np.array_equal([measured[k] for k in names],features['X'][i]),('features',i)
            if i%97==0:
                prefix=r['passage'].encode('utf-16-le')[:r['end']*2].decode('utf-16-le')
                assert measured==extract(prefix+' An unrelated ending about seventeen planets.',r['start'],r['end'])
            count+=1
    selection=json.loads((result_path/'selection.json').read_text())
    assert hashlib.sha256((ROOT/'models/gaussian.json').read_bytes()).hexdigest()==selection['selected_equation_sha256']
    assert selection['selected_kind']=='gaussian' and selection['comparison_labels_used_for_selection'] is False
    report={'status':'passed','development_passages':688,'development_steps':4726,'comparison_passages':100,
            'comparison_steps':910,'families':50,'model_replays':5,'replayed_predictions':4550,
            'raw_text_feature_rows_checked':count,'family_folds_checked':len(folds),
            'median_reference_rows_checked':len(development)+len(comparison),'metrics':checked,
            'scope':'Computational reproduction on saved data; no retraining, new Jev calls or human validation.'}
    text=json.dumps(report,indent=2,allow_nan=False)+'\n'
    if args.output:args.output.write_text(text)
    print(text)
if __name__=='__main__':main()
