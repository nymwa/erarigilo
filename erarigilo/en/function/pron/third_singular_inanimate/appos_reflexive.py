from erarigilo.en.function.pron.rule import (
        PronCond,
        DepEqCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class ApposReflexiveRule(
        TrgEqCondRule,
        DepEqCond,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '3sng_inan_appos_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'it',
            'they',
            'them',
            'themselves',
            'it self',
            'for itself',
            'by itself',
            'themself',
            'herself',
            'himself'])
        self.target_word = 'itself'
        self.target_dep_label = 'appos'

