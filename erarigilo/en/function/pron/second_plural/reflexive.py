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

    name = '2plu_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'to yourselves',
            'of yourselves',
            'for yourselves',
            'by yourselves',
            'with yourselves',
            'yourself',
            'to yourself',
            'of yourself',
            'for yourself',
            'by yourself',
            'with yourself',
            'you',
            'your',
            'yours',
            'themselves',
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
        self.target_word = 'yourselves'
        self.target_dep_set = {
                'dobj',
                'conj',
                'nsubj',
                'nsubjpass',
                'npadvmod',
                'dative',
                'attr'}

