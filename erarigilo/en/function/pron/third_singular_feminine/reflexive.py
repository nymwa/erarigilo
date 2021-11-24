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

    name = '3sng_fem_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'to herself',
            'of herself',
            'for herself',
            'by herself',
            'with herself',
            'herselves',
            'to herselves',
            'of herselves',
            'for herselves',
            'by herselves',
            'with herselves',
            'themself',
            'to themself',
            'of themself',
            'for themself',
            'by themself',
            'with themself',
            'she',
            'her',
            'hers',
            'himself'],
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
        self.target_word = 'herself'
        self.target_dep_set = {
                'dobj',
                'conj',
                'nsubj',
                'nsubjpass',
                'npadvmod',
                'dative',
                'attr'}

