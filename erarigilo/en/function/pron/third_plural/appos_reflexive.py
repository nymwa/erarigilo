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

    name = '3plu_appos_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'they',
            'them',
            'themself',
            'them selves',
            'for themselves',
            'by themselves',
            'by himselves',
            'herself',
            'himself'])
        self.target_word = 'themselves'
        self.target_dep_label = 'appos'

