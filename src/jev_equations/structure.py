"""Unchanged structural feature function, separated from unused training imports."""
from .features import _lemma

DEPENDENCIES = {'nsubj', 'nsubjpass', 'csubj', 'csubjpass', 'dobj', 'obj', 'iobj',
                'ccomp', 'xcomp', 'relcl', 'acl', 'advcl', 'pobj', 'attr', 'oprd'}

def connection_measurements(doc, left):
    """Simplified unfinished-connection and intervening-information measurements.

    Only edges parsed in the available prefix count. These are not an exact
    implementation of a psychological theory; prefix parsing can revise edges.
    """
    current = [t for t in doc if t.idx >= left and not t.is_space]
    old_lemmas = {_lemma(t) for t in doc if t.idx < left and t.pos_ in {'NOUN', 'PROPN'}}
    novel = set()
    seen = set(old_lemmas)
    for t in current:
        if t.pos_ in {'NOUN', 'PROPN'}:
            lemma = _lemma(t)
            if lemma not in seen:
                novel.add(t.i)
            seen.add(lemma)
    finite = {t.i for t in doc if t.pos_ in {'VERB', 'AUX'} and 'Fin' in t.morph.get('VerbForm')}
    edges = [(min(t.i, t.head.i), max(t.i, t.head.i), t.dep_)
             for t in doc if t.head != t and t.dep_ in DEPENDENCIES]
    active = [sum(a <= t.i < b for a, b, _ in edges) for t in current]
    completions = [(a, b, dep) for a, b, dep in edges if doc[b].idx >= left]
    novelty_costs = [sum(a < j < b for j in novel) + sum(a < j < b for j in finite)
                     for a, b, _ in completions]
    return {
        'struct_unfinished_peak': max(active, default=0),
        'struct_unfinished_sum': sum(active),
        'struct_unfinished_mean': sum(active) / max(1, len(active)),
        'struct_new_entities': len(novel),
        'struct_completed_connections': len(completions),
        'struct_intervening_information_sum': sum(novelty_costs),
        'struct_intervening_information_max': max(novelty_costs, default=0),
        'struct_cross_step_connections': sum(doc[a].idx < left <= doc[b].idx for a, b, _ in edges),
    }
