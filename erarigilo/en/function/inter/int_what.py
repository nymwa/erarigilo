from erarigilo.en.util.rule import (
        PlainWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhatRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_what'

    def __init__(self):
        super().__init__(
                ['how', 'that', 'which', 'who'],
                p = [0.6, 0.2, 0.1, 0.1])
        self.target_word = 'what'

