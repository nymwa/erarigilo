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

    name = '2sng_appos_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'you',
            'yourselves',
            'your self',
            'for yourself',
            'by yourself'])
        self.target_word = 'yourself'
        self.target_dep_label = 'appos'

