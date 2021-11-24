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

    name = '2nd_subj'

    def __init__(self):
        super().__init__([
            'u',
            'yo',
            'your',
            'yours',
            'me',
            'they'])
        self.target_word = 'you'
        self.target_dep_set = {
                'nsubj',
                'nsubjpass',
                'conj',
                'appos',
                'nmod',
                'compound',
                'attr'}

