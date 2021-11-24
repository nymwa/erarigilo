from erarigilo.en.function.pron.rule import (
        PronCond,
        DepInCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class ReflexiveRule(
        TrgEqCondRule,
        DepInCond,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '3sng_neut_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'to themself',
            'of themself',
            'for themself',
            'by themself',
            'with themself',
            'themselves',
            'to themselves',
            'of themselves',
            'for themselves',
            'by themselves',
            'with themselves',
            'himself',
            'to himself',
            'of himself',
            'for himself',
            'by himself',
            'with himself',
            'herself',
            'to herself',
            'of herself',
            'for herself',
            'by herself',
            'with herself',
            'she',
            'her',
            'hers',
            'he',
            'him',
            'his'],
            p = [
                0.2,
                0.1,
                0.1,
                0.1,
                0.1,
                0.1,
                0.01,
                0.01,
                0.01,
                0.01,
                0.01,
                0.01,
                0.005,
                0.005,
                0.005,
                0.005,
                0.005,
                0.005,
                0.005,
                0.005,
                0.005,
                0.005,
                0.005,
                0.005,
                0.03,
                0.03,
                0.03,
                0.03,
                0.03,
                0.03])
        self.target_word = 'themself'
        self.target_dep_set = {
                'dobj',
                'conj',
                'nsubj',
                'nsubjpass',
                'npadvmod',
                'dative',
                'attr'}

