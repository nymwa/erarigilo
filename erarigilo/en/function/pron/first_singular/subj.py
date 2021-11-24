from erarigilo.en.function.pron.rule import (
        UpperPronCond,
        DepInCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class SubjRule(
        TrgEqCondRule,
        DepInCond,
        UpperPronCond,
        ChoiceSamplableRule,
        TokenWiseRule):

    name = '1sng_subj'

    def __init__(self):
        super().__init__([
            '',
            'i',
            'it',
            'me',
            'we'])
        self.target_word = 'I'
        self.target_dep_set = {
                'nsubj',
                'nsubjpass',
                'conj',
                'appos',
                'attr'}

