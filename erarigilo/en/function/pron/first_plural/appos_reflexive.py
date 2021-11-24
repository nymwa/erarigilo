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

    name = '1plu_appos_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'us',
            'ourself',
            'our selves',
            'for ourselves',
            'by ourselves'])
        self.target_word = 'ourselves'
        self.target_dep_label = 'appos'

