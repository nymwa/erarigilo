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

    name = '3sng_masc_appos_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'him',
            'themself',
            'him self',
            'for himself',
            'by himself',
            'herself'])
        self.target_word = 'himself'
        self.target_dep_label = 'appos'

