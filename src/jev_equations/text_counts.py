"""Deterministic measurements from current and preceding visible text only."""
import re
from collections import Counter

WORDS = re.compile(r"[^\W_]+(?:['’][^\W_]+)*", re.UNICODE)
PRONOUNS = set('he she it they him her them his their its this that these those'.split())
CONDITIONS = set('if unless when whenever provided'.split())
CONNECTORS = set('and or but because although while whereas therefore however'.split())
NEGATION = set('not no never neither nor without'.split())

def syllables(word):
    w = re.sub('[^a-z]', '', word.lower())
    if not w:
        return 0
    n = len(re.findall('[aeiouy]+', w))
    if w.endswith('e') and not w.endswith(('le', 'ye')) and n > 1:
        n -= 1
    if w.endswith('es') and not w.endswith(('ses', 'xes', 'zes', 'ches', 'shes')) and n > 1:
        n -= 1
    return max(1, n)

def visible_parts(passage, start, end):
    # Saved reading-step offsets are UTF-16 code units, not Python indices.
    b = passage.encode('utf-16-le')
    return b[:2*start].decode('utf-16-le'), b[2*start:2*end].decode('utf-16-le')

def measurements(passage, start, end):
    prior, current = visible_parts(passage, start, end)
    w = [v.lower() for v in WORDS.findall(current)]
    old = [v.lower() for v in WORDS.findall(prior)]
    syll = [syllables(v) for v in w]
    n = len(w)
    sentences = max(1, len([v for v in re.split(r'[.!?]+', current) if WORDS.search(v)]))
    last = {v:i for i,v in enumerate(old)}
    repeated = [v for v in w if v in last]
    gaps = [len(old)-last[v] for v in repeated]
    out = {
        'words': n,
        'letters': sum(ch.isalpha() for ch in current),
        'vowels': sum(ch in 'aeiou' for ch in current.lower()),
        'syllables': sum(syll),
        'sentences': sentences,
        'words_per_sentence': n/sentences,
        'syllables_per_word': sum(syll)/max(n,1),
        'letters_per_word': sum(ch.isalpha() for ch in current)/max(n,1),
        'long_words': sum(len(v)>=7 for v in w),
        'three_syllable_words': sum(v>=3 for v in syll),
        'unique_words': len(set(w)),
        'repeated_words': n-len(set(w)),
        'commas': current.count(','),
        'semicolons': current.count(';'),
        'colons': current.count(':'),
        'pronoun_markers': sum(v in PRONOUNS for v in w),
        'condition_markers': sum(v in CONDITIONS for v in w),
        'connectors': sum(v in CONNECTORS for v in w),
        'negations': sum(v in NEGATION for v in w),
        'number_tokens': sum(any(ch.isdigit() for ch in v) for v in w),
        'previous_words': len(old),
        'previous_unique_words': len(set(old)),
        'words_seen_before': len(repeated),
        'new_word_types': len(set(w)-set(old)),
        'words_seen_recently': sum(v in set(old[-40:]) for v in w),
        'mean_repeat_gap': sum(gaps)/max(len(gaps),1),
        'max_repeat_gap': max(gaps,default=0),
    }
    return {k:float(v) for k,v in out.items()}

def predict(equation, passage, start, end, grammar=None):
    f=measurements(passage,start,end)
    if grammar: f.update(grammar)
    raw=equation['intercept']
    contributions=[]
    for term in equation['terms']:
        value=1.0
        for name in term['features']:
            value*=f[name]
        amount=term['coefficient']*value
        contributions.append(dict(term, value=value, contribution=amount))
        raw+=amount
    import math
    return {'raw':raw,'score':max(0,math.floor(raw+.5)), 'measurements':f,'contributions':contributions}
