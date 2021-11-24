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

    name = '1sng_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'to myself',
            'of myself',
            'for myself',
            'by myself',
            'with myself',
            'myselves',
            'to myselves',
            'of myselves',
            'for myselves',
            'by myselves',
            'with myselves',
            'me',
            'my',
            'mine',
            'yourself',
            'ourselves'],
            p = [
                0.2,
                0.1,
                0.1,
                0.1,
                0.1,
                0.1,
                0.02,
                0.02,
                0.02,
                0.02,
                0.02,
                0.02,
                0.1,
                0.02,
                0.02,
                0.02,
                0.02])
        self.target_word = 'myself'
        self.target_dep_set = {
                'dobj',
                'conj',
                'nsubj',
                'nsubjpass',
                'npadvmod',
                'dative',
                'attr'}

