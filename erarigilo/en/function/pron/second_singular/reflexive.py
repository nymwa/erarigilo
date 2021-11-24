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

    name = '2sng_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'to yourself',
            'of yourself',
            'for yourself',
            'by yourself',
            'with yourself',
            'yourselves',
            'to yourselves',
            'of yourselves',
            'for yourselves',
            'by yourselves',
            'with yourselves',
            'you',
            'your',
            'yours',
            'themself',
            'myself'],
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
        self.target_word = 'yourself'
        self.target_dep_set = {
                'dobj',
                'conj',
                'nsubj',
                'nsubjpass',
                'npadvmod',
                'dative',
                'attr'}

