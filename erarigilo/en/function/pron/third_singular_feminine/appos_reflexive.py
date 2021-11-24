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

    name = '3sng_fem_appos_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'her',
            'themself',
            'her self',
            'for herself',
            'by herself',
            'himself'])
        self.target_word = 'herself'
        self.target_dep_label = 'appos'

