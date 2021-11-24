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

    name = '1sng_appos_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'me',
            'myselves',
            'my self',
            'for myself',
            'by myself'])
        self.target_word = 'myself'
        self.target_dep_label = 'appos'

