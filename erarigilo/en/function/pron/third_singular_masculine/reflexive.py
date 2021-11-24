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

    name = '3sng_masc_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'to himself',
            'of himself',
            'for himself',
            'by himself',
            'with himself',
            'himselves',
            'to himselves',
            'of himselves',
            'for himselves',
            'by himselves',
            'with himselves',
            'themself',
            'to themself',
            'of themself',
            'for themself',
            'by themself',
            'with themself',
            'he',
            'his',
            'him',
            'herself'],
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
                0.01,
                0.01,
                0.01,
                0.01,
                0.01,
                0.01,
                0.045,
                0.045,
                0.045,
                0.045])
        self.target_word = 'himself'
        self.target_dep_set = {
                'dobj',
                'conj',
                'nsubj',
                'nsubjpass',
                'npadvmod',
                'dative',
                'attr'}

