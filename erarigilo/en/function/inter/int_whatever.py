from erarigilo.en.util.rule import (
        PlainWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhateverRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whatever'

    def __init__(self):
        super().__init__(
                ['what', 'however', 'whichever', 'whoever'],
                p = [0.4, 0.2, 0.2, 0.2])
        self.target_word = 'whatever'

