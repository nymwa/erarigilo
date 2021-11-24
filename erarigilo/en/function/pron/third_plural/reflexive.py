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

    name = '3plu_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'to themselves',
            'of themselves',
            'for themselves',
            'by themselves',
            'with themselves',
            'themself',
            'to themself',
            'of themself',
            'for themself',
            'by themself',
            'with themself',
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
            'they',
            'them',
            'their'],
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
                0.06,
                0.06,
                0.06])
        self.target_word = 'themselves'
        self.target_dep_set = {
                'dobj',
                'conj',
                'nsubj',
                'nsubjpass',
                'npadvmod',
                'dative',
                'attr'}

