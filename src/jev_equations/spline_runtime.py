"""Frozen direct-text equation; requires NumPy/SciPy, not scikit-learn.

Each raw measurement enters a clipped cubic B-spline, then class-specific
weighted sums and exp produce a probability. The selected class is the score.
"""
import json
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline


def basis_matrix(model, X):
    X = np.asarray(X, dtype=np.float64)
    assert np.isfinite(X).all(), "Non-finite text measurement"
    blocks = []
    for item in model['splines']:
        t = np.asarray(item['knots'], dtype=np.float64)
        k = item['degree']
        count = len(t) - k - 1
        if t[k] == t[-k - 1]:
            # A feature constant throughout fitting has zero-width knots.
            # Its entire dropped-bias basis is zero under the fitted transform.
            blocks.append(np.zeros((len(X), count - 1)))
        else:
            b = BSpline(t, np.eye(count), k, extrapolate=False)
            z = np.clip(X[:, item['feature_index']], t[k], t[-k - 1])
            blocks.append(b(z)[:, :-1])
    raw = np.concatenate(blocks, axis=1)
    scaled = (raw - np.asarray(model['basis_mean'])) / np.asarray(model['basis_scale'])
    assert np.isfinite(scaled).all(), "Non-finite spline measurement"
    return scaled


def probabilities(model, X):
    basis = basis_matrix(model, X)
    logits = np.einsum('nj,kj->nk', basis, np.asarray(model['coefficients']))
    logits += np.asarray(model['intercepts'])
    if len(model['classes']) == 2 and logits.shape[1] == 1:
        logits = np.column_stack([np.zeros(len(logits)), logits[:, 0]])
    exponentials = np.exp(logits - np.max(logits, axis=1, keepdims=True))
    p = exponentials / np.sum(exponentials, axis=1, keepdims=True)
    assert np.isfinite(p).all(), "Non-finite output probability"
    return p


def predict(model, X):
    p = probabilities(model, X)
    return np.asarray(model['classes'])[np.argmax(p, axis=1)]


def load_model(path):
    return json.loads(Path(path).read_text())
