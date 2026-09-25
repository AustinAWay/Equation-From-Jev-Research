"""Local numerical text measurements for equation discovery.

The only inputs are source text and a reading-step's UTF-16 offsets. Parsing
always stops at that step's end: later source text never enters the parser.
No API calls, teacher judgments, student outcomes, corpus identifiers or split
labels are used. These measurements are proxies, not cognitive quantities.
"""
import math
import re
import threading
from collections import Counter
from functools import lru_cache
from typing import Dict

FEATURE_VERSION = 'local-prefix-features-v3-reference-frequency'
PARSER_MODEL = 'en_core_web_sm'
WORDFREQ_VERSION = '3.1.1'
_LOCK = threading.RLock()
_WORDS = re.compile(r"[^\W_]+(?:['’][^\W_]+)*", re.UNICODE)
_CONTENT_POS = {'NOUN', 'PROPN', 'VERB', 'ADJ', 'ADV'}
_NOMINAL_POS = {'NOUN', 'PROPN'}
_POS = ('NOUN', 'PROPN', 'PRON', 'VERB', 'AUX', 'ADJ', 'ADV', 'ADP', 'CCONJ', 'SCONJ', 'NUM', 'DET')
_SUBORDINATE = {'advcl', 'ccomp', 'xcomp', 'relcl', 'acl', 'csubj', 'csubjpass'}
_CONDITIONAL = {'if', 'unless', 'provided', 'whenever'}
_CAUSAL = {'because', 'therefore', 'hence', 'thus', 'consequently'}
_NEGATION = {'no', 'not', 'never', 'neither', 'nor', 'without', "n't"}
_COMPARISON = {'than', 'more', 'less', 'fewer', 'most', 'least', 'same', 'different', 'equal', 'equals'}
_TEMPORAL = {'before', 'after', 'then', 'while', 'until', 'during', 'once', 'first', 'next', 'finally'}
_DEMONSTRATIVE = {'this', 'that', 'these', 'those'}
_DEFINITION = re.compile(r'\b(?:means|denotes|is called|are called|is defined as|are defined as|refers to|is the|are the)\b', re.I)
_ACTION_CATEGORIES = {
    'compare': {'compare', 'contrast', 'distinguish', 'differ', 'match'},
    'order': {'arrange', 'order', 'sort', 'rank', 'sequence'},
    'connect': {'connect', 'link', 'relate', 'join', 'associate', 'pair'},
    'track': {'track', 'trace', 'follow', 'record', 'note', 'identify', 'label', 'mark'},
    'calculate': {'calculate', 'count', 'add', 'subtract', 'multiply', 'divide', 'total'},
    'select': {'choose', 'select', 'pick', 'retain', 'exclude', 'include', 'keep'},
    'define': {'define', 'mean', 'denote', 'represent', 'refer', 'call'},
    'manipulate': {'move', 'place', 'put', 'lift', 'turn', 'open', 'close', 'fold',
                   'draw', 'attach', 'remove', 'replace', 'rotate', 'press', 'pull',
                   'push', 'bring', 'set', 'return', 'shift', 'transfer'},
}
_SUBJECT_DEPS = {'nsubj', 'nsubjpass', 'csubj', 'csubjpass', 'expl'}
_OBJECT_DEPS = {'dobj', 'obj', 'dative'}
_ARGUMENT_NOMINAL_POS = {'NOUN', 'PROPN', 'PRON', 'NUM'}
_SPATIAL = {'above', 'across', 'against', 'along', 'around', 'at', 'behind',
            'below', 'beneath', 'beside', 'between', 'beyond', 'down', 'from',
            'in', 'inside', 'into', 'near', 'on', 'onto', 'out', 'outside',
            'over', 'through', 'to', 'toward', 'towards', 'under', 'underneath',
            'up', 'upon', 'within'}
_REFERENCE_WORDS = ('both', 'each', 'every', 'same', 'equal', 'different', 'other',
                    'another', 'between', 'either', 'neither', 'together',
                    'separately', 'respectively', 'former', 'latter')


@lru_cache(maxsize=1)
def _parser():
    import spacy
    # Fail explicitly if unavailable; switching parser silently changes features.
    return spacy.load(PARSER_MODEL)


@lru_cache(maxsize=128)
def _parse_prefix(prefix):
    with _LOCK:
        return _parser()(prefix)


def _mean(values):
    return sum(values) / len(values) if values else 0.0


def _ratio(numerator, denominator):
    return numerator / denominator if denominator else 0.0


def _syllables(word):
    """Small English vowel-group heuristic; intentionally not a pronunciation model."""
    word = re.sub('[^a-z]', '', word.lower())
    if not word:
        return 0
    count = len(re.findall('[aeiouy]+', word))
    if word.endswith('e') and not word.endswith(('le', 'ye')) and count > 1:
        count -= 1
    if word.endswith('es') and not word.endswith(('ses', 'xes', 'zes', 'ches', 'shes')) and count > 1:
        count -= 1
    return max(1, count)


def _lemma(token):
    return (token.lemma_ or token.text).lower()


@lru_cache(maxsize=1)
def _frequency_lookup():
    from importlib.metadata import version
    from wordfreq import zipf_frequency
    if version('wordfreq') != WORDFREQ_VERSION:
        raise RuntimeError(f'Expected wordfreq=={WORDFREQ_VERSION}; changing its word list changes features')
    return zipf_frequency


@lru_cache(maxsize=8192)
def _english_zipf(lemma):
    return float(_frequency_lookup()(lemma, 'en', wordlist='best', minimum=0.0))


def _inside(token, left, right):
    return token.idx >= left and token.idx + len(token.text) <= right


def _candidate_spans(doc):
    """Local noun/predicate/value occurrences, inspired by Passage's parser rules.

    No semantic grouping is performed. This independent prefix parser does not
    promise identical candidates to Passage, which parses the full source.
    """
    spans = {(chunk.start_char, chunk.end_char, 'concept') for chunk in doc.noun_chunks}
    for token in doc:
        covered = any(a <= token.idx and token.idx + len(token) <= b for a, b, _ in spans)
        if token.pos_ in {'NOUN', 'PROPN', 'PRON'} and not covered:
            spans.add((token.idx, token.idx + len(token), 'concept'))
        if token.pos_ in {'VERB', 'AUX'} and token.dep_ not in {'aux', 'auxpass'}:
            if not (token.dep_ == 'amod' and covered):
                spans.add((token.idx, token.idx + len(token), 'relation'))
    for token in doc:
        state = token.dep_ in {'acomp', 'attr', 'oprd'} or token.dep_ == 'advmod' and token.head.lemma_ == 'be'
        if token.pos_ in {'ADJ', 'NUM'} or token.pos_ in {'ADV', 'ADP'} and state:
            if not any(a <= token.idx and token.idx + len(token) <= b for a, b, _ in spans):
                spans.add((token.idx, token.idx + len(token), 'concept'))
    return spans


def _scope(doc, left, right, spans):
    text = doc.text[left:right]
    tokens = [token for token in doc if _inside(token, left, right) and not token.is_space]
    words = _WORDS.findall(text)
    word_tokens = [token for token in tokens if any(ch.isalnum() for ch in token.text)]
    content = [token for token in tokens if token.pos_ in _CONTENT_POS and not token.is_stop]
    lemmas = [_lemma(token) for token in content]
    nominal = [_lemma(token) for token in tokens if token.pos_ in _NOMINAL_POS]
    pos = Counter(token.pos_ for token in tokens)
    lower = [token.lower_ for token in tokens]
    syllables = [_syllables(word) for word in words]
    lengths = [len(word) for word in words]
    distances = [abs(token.i - token.head.i) for token in tokens if token.head != token]
    internal_distances = [abs(token.i - token.head.i) for token in tokens if token.head != token and _inside(token.head, left, right)]
    depths = [len(list(token.ancestors)) for token in word_tokens]
    noun_chunks = [chunk for chunk in doc.noun_chunks if chunk.start_char >= left and chunk.end_char <= right]
    entities = [entity for entity in doc.ents if entity.start_char >= left and entity.end_char <= right]
    current_spans = [(a, b, kind) for a, b, kind in spans if a >= left and b <= right]
    sentences = [sentence for sentence in doc.sents if sentence.end_char > left and sentence.start_char < right]
    nwords = len(words)
    nsentences = len(sentences)
    clause_heads = [token for token in tokens if token.dep_ in _SUBORDINATE or token.dep_ == 'ROOT' or token.dep_ == 'conj' and token.pos_ in {'VERB', 'AUX'}]
    subtree_depths = [sum(ancestor.dep_ in _SUBORDINATE for ancestor in token.ancestors) for token in word_tokens]
    nominal_modifiers = [sum(child.dep_ in {'amod', 'compound', 'nummod', 'poss', 'acl', 'relcl'} for child in token.children) for token in tokens if token.pos_ in _NOMINAL_POS]
    result = {
        'characters': len(text), 'words': nwords, 'syllables': sum(syllables),
        'mean_word_length': _mean(lengths), 'max_word_length': max(lengths, default=0),
        'mean_syllables': _mean(syllables), 'polysyllabic_words': sum(n >= 3 for n in syllables),
        'long_words': sum(n >= 7 for n in lengths), 'short_words': sum(n <= 3 for n in lengths),
        'sentences': nsentences, 'words_per_sentence': _ratio(nwords, nsentences),
        'content_words': len(content), 'unique_content_lemmas': len(set(lemmas)),
        'content_density': _ratio(len(content), nwords),
        'repeated_lemma_ratio': 1 - _ratio(len(set(lemmas)), len(lemmas)) if lemmas else 0,
        'unique_nominal_lemmas': len(set(nominal)),
        'repeated_nominal_mentions': len(nominal) - len(set(nominal)),
        'unique_proper_lemmas': len({_lemma(t) for t in tokens if t.pos_ == 'PROPN'}),
        'stopword_ratio': _ratio(sum(t.is_stop for t in word_tokens), len(word_tokens)),
        'noun_chunks': len(noun_chunks), 'mean_noun_chunk_tokens': _mean([len(c) for c in noun_chunks]),
        'max_noun_chunk_tokens': max([len(c) for c in noun_chunks], default=0),
        'max_nominal_modifiers': max(nominal_modifiers, default=0),
        'named_entities': len(entities), 'unique_named_entities': len({e.text.lower() for e in entities}),
        'person_entities': sum(e.label_ == 'PERSON' for e in entities),
        'quantity_entities': sum(e.label_ in {'QUANTITY', 'CARDINAL', 'PERCENT', 'MONEY', 'ORDINAL'} for e in entities),
        'numeric_tokens': sum(t.like_num for t in tokens),
        'candidate_concepts': sum(kind == 'concept' for _, _, kind in current_spans),
        'candidate_relations': sum(kind == 'relation' for _, _, kind in current_spans),
        'candidate_total': len(current_spans),
        'clause_heads': len(clause_heads), 'subordinate_clauses': sum(t.dep_ in _SUBORDINATE for t in tokens),
        'relative_clauses': sum(t.dep_ == 'relcl' for t in tokens),
        'coordinated_predicates': sum(t.dep_ == 'conj' and t.pos_ in {'VERB', 'AUX'} for t in tokens),
        'coordinated_nominals': sum(t.dep_ == 'conj' and t.pos_ in {'NOUN', 'PROPN', 'PRON'} for t in tokens),
        'mean_syntax_depth': _mean(depths), 'max_syntax_depth': max(depths, default=0),
        'max_subordinate_depth': max(subtree_depths, default=0),
        'mean_dependency_distance': _mean(distances), 'max_dependency_distance': max(distances, default=0),
        'long_dependencies': sum(distance >= 5 for distance in distances),
        'internal_dependency_distance_sum': sum(internal_distances),
        'conditional_markers': sum(word in _CONDITIONAL for word in lower),
        'causal_markers': sum(word in _CAUSAL for word in lower),
        'negation_markers': sum(word in _NEGATION for word in lower),
        'comparison_markers': sum(word in _COMPARISON for word in lower),
        'temporal_markers': sum(word in _TEMPORAL for word in lower),
        'demonstrative_markers': sum(word in _DEMONSTRATIVE for word in lower),
        'definition_cues': len(_DEFINITION.findall(text)),
        'passive_subjects': sum(t.dep_ in {'nsubjpass', 'csubjpass'} for t in tokens),
        'modal_verbs': sum(t.tag_ == 'MD' for t in tokens),
        'commas': text.count(','), 'semicolons': text.count(';'), 'colons': text.count(':'),
        'parenthesis_pairs': min(text.count('('), text.count(')')),
        'question_marks': text.count('?'),
        'flesch_kincaid_grade': 0.39 * _ratio(nwords, nsentences) + 11.8 * _ratio(sum(syllables), nwords) - 15.59 if nwords else 0,
        'flesch_reading_ease': 206.835 - 1.015 * _ratio(nwords, nsentences) - 84.6 * _ratio(sum(syllables), nwords) if nwords else 0,
    }
    result.update({f'pos_{name.lower()}': pos[name] for name in _POS})
    return result


def _imperative_root(token):
    """Conservative parser cue, not a semantic classification of instructions."""
    return (token.dep_ == 'ROOT' and token.pos_ == 'VERB' and token.tag_ == 'VB'
            and not any(child.dep_ in _SUBJECT_DEPS for child in token.children)
            and not any(child.lower_ == 'to' and child.dep_ in {'aux', 'mark'}
                        for child in token.children))


def _imperative_predicate(token):
    if _imperative_root(token):
        return True
    if token.pos_ != 'VERB' or token.tag_ != 'VB':
        return False
    current = token
    while current.dep_ == 'conj':
        if any(child.dep_ in _SUBJECT_DEPS for child in current.children):
            return False
        current = current.head
    return _imperative_root(current)


def _coordinated_items(head, left, right):
    """Return a nominal argument and coordinated peers present in this scope."""
    candidates = (head, *head.conjuncts)
    return {token.i for token in candidates
            if token.pos_ in _ARGUMENT_NOMINAL_POS and _inside(token, left, right)}


def _action_features(doc, left, right):
    """Twenty preregistered, step-local action/argument proxies for revision v2.

    The document is already a prefix parse. Earlier sentence context can identify
    an inherited imperative or an available condition, but arguments are counted
    only when their own tokens occur within the current reading step.
    """
    tokens = [token for token in doc if _inside(token, left, right)]
    predicates = [token for token in tokens if token.pos_ in {'VERB', 'AUX'}]
    categories = {
        name: [token for token in predicates if _lemma(token) in lexicon]
        for name, lexicon in _ACTION_CATEGORIES.items()
    }
    categories['define'].extend(
        token for token in predicates if _lemma(token) == 'be'
        and any(child.dep_ == 'attr' and child.pos_ in _NOMINAL_POS
                and _inside(child, left, right) for child in token.children)
    )
    action_ids = {token.i for group in categories.values() for token in group}
    actions = [token for token in predicates if token.i in action_ids]
    object_heads = []
    object_groups = []
    nominal_by_action = {token.i: set() for token in actions}
    for action in actions:
        for child in action.children:
            if child.dep_ in _OBJECT_DEPS and child.pos_ in _ARGUMENT_NOMINAL_POS and _inside(child, left, right):
                object_heads.append(child)
                items = _coordinated_items(child, left, right)
                object_groups.append(items)
                nominal_by_action[action.i].update(items)

    def owner(token):
        return next((ancestor for ancestor in token.ancestors if ancestor.pos_ in {'VERB', 'AUX'}), None)

    prepositions = []
    prep_object_items = set()
    spatial = []
    for token in tokens:
        governing = owner(token)
        if governing is None or governing.i not in action_ids:
            continue
        if token.dep_ == 'prep' and token.pos_ == 'ADP':
            prepositions.append(token)
            for child in token.children:
                if child.dep_ == 'pobj' and child.pos_ in _ARGUMENT_NOMINAL_POS and _inside(child, left, right):
                    items = _coordinated_items(child, left, right)
                    prep_object_items.update(items)
                    nominal_by_action[governing.i].update(items)
        if token.lower_ in _SPATIAL and token.dep_ in {'prep', 'advmod', 'prt'}:
            spatial.append(token)
    direct_items = set().union(*object_groups) if object_groups else set()
    result = {
        'imperative_roots': sum(_imperative_root(token) for token in predicates),
        'imperative_predicates': sum(_imperative_predicate(token) for token in predicates),
        **{f'action_{name}_verbs': len(group) for name, group in categories.items()},
        'action_category_count': sum(bool(group) for group in categories.values()),
        'action_lexical_verbs': len(action_ids),
        'action_conditional_selections': sum(
            any(item.lower_ in _CONDITIONAL for item in token.sent)
            for token in categories['select']),
        'action_direct_object_heads': len(object_heads),
        'action_direct_object_items': len(direct_items),
        'action_max_object_group': max((len(items) for items in object_groups), default=0),
        'action_prepositional_arguments': len(prepositions),
        'action_prepositional_object_items': len(prep_object_items),
        'action_spatial_arguments': len(spatial),
        'action_max_nominal_arguments': max((len(items) for items in nominal_by_action.values()), default=0),
    }
    assert len(result) == 20
    return {f'step_{name}': value for name, value in result.items()}


def _utf16_prefix(passage, start, end):
    if not isinstance(passage, str):
        raise TypeError('passage must be a string')
    if not isinstance(start, int) or isinstance(start, bool) or not isinstance(end, int) or isinstance(end, bool):
        raise TypeError('start and end must be integer UTF-16 offsets')
    if start < 0 or end < start:
        raise ValueError('offsets must satisfy 0 <= start <= end')
    # Scan only to end; suffix contents cannot affect even Unicode validation.
    consumed = 0
    start_character = 0 if start == 0 else None
    end_character = 0 if end == 0 else None
    for index, char in enumerate(passage):
        if consumed >= end:
            break
        if 0xD800 <= ord(char) <= 0xDFFF:
            raise ValueError('unpaired surrogate within inspected prefix')
        consumed += 2 if ord(char) > 0xFFFF else 1
        if consumed == start:
            start_character = index + 1
        if consumed == end:
            end_character = index + 1
    if end_character is None or start_character is None:
        raise ValueError('offset lies outside source or splits a UTF-16 surrogate pair')
    return passage[:end_character], start_character


def extract_features(passage: str, start: int, end: int) -> Dict[str, float]:
    """Return a fresh dictionary of finite features for UTF-16 range [start, end).

    Parsing uses only passage[:end]. Scope prefixes: ``step`` is [start,end),
    ``prefix`` is [0,end), ``sentence`` is the last parsed sentence in that
    prefix (the sentence containing the reading point). All values are floats.
    """
    prefix, left = _utf16_prefix(passage, start, end)
    doc = _parse_prefix(prefix)
    right = len(prefix)
    spans = _candidate_spans(doc)
    sentences = list(doc.sents)
    sentence_left = sentences[-1].start_char if sentences else 0
    result = {}
    for label, a, b in (('step', left, right), ('prefix', 0, right), ('sentence', sentence_left, right)):
        result.update({f'{label}_{name}': value for name, value in _scope(doc, a, b, spans).items()})
    result.update(_action_features(doc, left, right))
    prior = [t for t in doc if t.idx + len(t) <= left and not t.is_space]
    current = [t for t in doc if _inside(t, left, right) and not t.is_space]
    prior_content = [t for t in prior if t.pos_ in _CONTENT_POS and not t.is_stop]
    current_content = [t for t in current if t.pos_ in _CONTENT_POS and not t.is_stop]
    prior_by_lemma = {}
    for token in prior_content:
        prior_by_lemma.setdefault(_lemma(token), []).append(token)
    # Frequency is an installed English word-list lookup, never a teacher call.
    # The dictionary can contain many words; only current prefix lemmas are used.
    content_frequencies = [(_lemma(token), _english_zipf(_lemma(token))) for token in current_content]
    current_words = Counter(token.lower_ for token in current)
    result.update({f'step_reference_word_{word}': current_words[word] for word in _REFERENCE_WORDS})
    result.update({
        'step_content_zipf_mean': _mean([frequency for _, frequency in content_frequencies]),
        'step_content_zipf_min': min((frequency for _, frequency in content_frequencies), default=0.0),
        'step_rare_content_mentions': sum(frequency < 3.0 for _, frequency in content_frequencies),
        'step_new_rare_content_lemmas': len({lemma for lemma, frequency in content_frequencies
                                             if frequency < 3.0 and lemma not in prior_by_lemma}),
    })
    seen = [t for t in current_content if _lemma(t) in prior_by_lemma]
    recency = [t.i - prior_by_lemma[_lemma(t)][-1].i for t in seen]
    mention_counts = [len(prior_by_lemma[_lemma(t)]) for t in seen]
    cross_edges = [t for t in doc if t.head != t and (t.idx < left) != (t.head.idx < left)]
    nominal_prior = [t for t in prior if t.pos_ in _NOMINAL_POS]
    pronoun_distances = []
    antecedent_counts = []
    for token in current:
        if token.pos_ == 'PRON':
            available = [t for t in doc if t.i < token.i and t.pos_ in _NOMINAL_POS]
            if available:
                pronoun_distances.append(token.i - available[-1].i)
            antecedent_counts.append(len(available))
    result.update({
        'prior_words': len(_WORDS.findall(prefix[:left])),
        'prior_sentences': sum(sentence.end_char <= left for sentence in sentences),
        'prior_definition_cues': len(_DEFINITION.findall(prefix[:left])),
        'prior_unique_nominal_lemmas': len({_lemma(t) for t in nominal_prior}),
        'step_content_mentions_seen_before': len(seen),
        'step_content_mentions_new': len(current_content) - len(seen),
        'step_seen_content_ratio': _ratio(len(seen), len(current_content)),
        'step_mean_mention_recency_tokens': _mean(recency),
        'step_max_mention_recency_tokens': max(recency, default=0),
        'step_mean_previous_mentions': _mean(mention_counts),
        'cross_step_dependency_edges': len(cross_edges),
        'cross_step_dependency_distance_sum': sum(abs(t.i - t.head.i) for t in cross_edges),
        'cross_step_dependency_distance_max': max([abs(t.i - t.head.i) for t in cross_edges], default=0),
        'step_mean_nearest_nominal_distance': _mean(pronoun_distances),
        'step_max_nearest_nominal_distance': max(pronoun_distances, default=0),
        'step_mean_available_nominal_antecedents': _mean(antecedent_counts),
        'step_words_before_in_sentence': len(_WORDS.findall(prefix[sentence_left:left])) if left >= sentence_left else 0,
        'reading_point_sentence_index': len(sentences) - 1 if sentences else 0,
    })
    values = {name: float(value) for name, value in result.items()}
    if not all(math.isfinite(value) for value in values.values()):
        raise ValueError('feature extraction produced a nonfinite value')
    return values
