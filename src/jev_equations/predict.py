"""Replay frozen equations on a reading step using only visible text."""
import argparse
import json
import sys
from pathlib import Path
import numpy as np
from . import features, text_counts, spline_runtime
from .structure import connection_measurements

ROOT = Path(__file__).resolve().parents[2]
STRUCTURAL_KEYS = [
    'step_noun_chunks', 'step_clause_heads', 'step_subordinate_clauses',
    'step_max_syntax_depth', 'step_mean_dependency_distance',
    'step_long_dependencies', 'step_pos_pron', 'struct_unfinished_peak',
    'struct_new_entities', 'struct_intervening_information_sum',
    'struct_cross_step_connections',
]


def extract(text, start=0, end=None):
    length = len(text.encode('utf-16-le')) // 2
    end = length if end is None else end
    if not 0 <= start < end <= length:
        raise ValueError('Require 0 <= start < end <= text length in UTF-16 units.')
    expanded = features.extract_features(text, start, end)
    prefix, left = features._utf16_prefix(text, start, end)
    structure = connection_measurements(features._parse_prefix(prefix), left)
    measured = text_counts.measurements(text, start, end)
    measured.update({k: expanded[k] if k in expanded else float(structure[k])
                     for k in STRUCTURAL_KEYS})
    for name, value in expanded.items():
        if name in measured and measured[name] != value:
            raise ValueError('Inconsistent shared measurement: ' + name)
        measured[name] = value
    if not all(np.isfinite(v) for v in measured.values()):
        raise ValueError('Nonfinite input measurement')
    return measured


def kernel_predict(model, X):
    """The saved Gaussian/polynomial arithmetic; no fitting or remote calls."""
    transform = model['transform']
    z = (X - np.asarray(transform['mean'])) / np.asarray(transform['std'])
    if transform['kind'] == 'gaussian':
        columns = [np.exp(-np.sum((z - center) ** 2, axis=1) /
                          (2 * z.shape[1] * transform['length'] ** 2))
                   for center in np.asarray(transform['centers'])]
        basis = np.column_stack([z] + columns)
    elif transform['degree'] == 1:
        basis = z
    elif transform['degree'] == 2:
        basis = np.column_stack([z] + [z[:, i] * z[:, j]
                for i in range(z.shape[1]) for j in range(i, z.shape[1])])
    else:
        raise ValueError('Unsupported polynomial degree')
    basis = (basis - np.asarray(transform['basis_mean'])) / np.asarray(transform['basis_std'])
    logits = np.einsum('ni,ki->nk', basis, np.asarray(model['coefficients'])) + model['intercept']
    if logits.shape[1] == 1:
        logits = np.column_stack([np.zeros(len(logits)), logits[:, 0]])
    exp = np.exp(logits - logits.max(axis=1, keepdims=True))
    prob = exp / exp.sum(axis=1, keepdims=True)
    if not np.isfinite(prob).all():
        raise ValueError('Nonfinite prediction')
    return np.asarray(model['classes'])[np.argmax(logits, axis=1)], prob


def predict_matrix(kind, X):
    model = json.loads((ROOT / 'models' / (kind + '.json')).read_text())
    if kind in ('gaussian', 'polynomial'):
        return kernel_predict(model, X[:, model['feature_indices']])
    if kind in ('spline', 'word-count'):
        return spline_runtime.predict(model, X), spline_runtime.probabilities(model, X)
    if kind == 'linear':
        names = json.loads((ROOT / 'data/features.json').read_text())['names']
        raw = np.full(len(X), model['intercept'], dtype=float)
        for term in model['terms']:
            raw += term['coefficient'] * np.prod(X[:, [names.index(k) for k in term['features']]], axis=1)
        return np.maximum(0, np.floor(raw + .5)).astype(int), None
    raise ValueError('Unknown equation: ' + kind)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument('--text')
    group.add_argument('--text-file', type=Path)
    p.add_argument('--start', type=int, default=0, help='Step start, UTF-16 code units')
    p.add_argument('--end', type=int, help='Step end, UTF-16 code units; default is text end')
    p.add_argument('--model', choices=['gaussian', 'polynomial', 'spline', 'word-count', 'linear'], default='gaussian')
    args = p.parse_args()
    text = args.text if args.text is not None else args.text_file.read_text(encoding='utf-8')
    # Local prediction must never call an API, even through an imported dependency.
    import socket
    def denied(*args, **kwargs):
        raise RuntimeError('Network access is disabled during prediction')
    socket.socket.connect = denied
    socket.create_connection = denied
    try:
        measured = extract(text, args.start, args.end)
        names = json.loads((ROOT / 'data/features.json').read_text())['names']
        X = np.asarray([[measured[k] for k in names]])
        scores, probability = predict_matrix(args.model, X)
        result = {'score': int(scores[0]), 'model': args.model,
                  'target': 'Approximation of the fixed Jev-based app score; not a human measurement',
                  'start_utf16': args.start, 'end_utf16': args.end if args.end is not None else len(text.encode('utf-16-le')) // 2,
                  'measured_inputs': measured}
        if probability is not None:
            classes = json.loads((ROOT / 'models' / (args.model + '.json')).read_text())['classes']
            result['model_class_probabilities'] = {str(c): float(v) for c, v in zip(classes, probability[0])}
            result['probability_note'] = 'Model outputs, not calibrated certainty about people or future accuracy.'
        print(json.dumps(result, indent=2, allow_nan=False))
    except (ValueError, UnicodeError) as e:
        p.error(str(e))

if __name__ == '__main__':
    main()
