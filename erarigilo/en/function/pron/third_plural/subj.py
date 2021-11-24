from erarigilo.en.function.pron.rule import (
        PronCond,
        DepInCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class SubjRule(
        TrgEqCondRule,
        DepInCond,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '3plu_subj'

    def __init__(self):
        super().__init__([
            'them',
            'their',
            'he',
            'him',
            'she',
            'her',
            'themself',
            'themselves'])
        self.target_word = 'they'
        self.target_dep_set = {
                'nsubj',
                'nsubjpass',
                'conj',
                'appos',
                'nmod',
                'compound',
                'attr'}

