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

    name = '1plu_subj'

    def __init__(self):
        super().__init__([
            'I',
            'us',
            'our',
            'me',
            'they',
            'you'])
        self.target_word = 'we'
        self.target_dep_set = {
                'nsubj',
                'nsubjpass',
                'conj',
                'appos',
                'nmod',
                'compound',
                'attr'}

