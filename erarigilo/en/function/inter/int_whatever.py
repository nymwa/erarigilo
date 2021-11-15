from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhateverRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whatever'

    def __init__(self):
        super().__init__(
                ['what', 'however', 'whichever', 'whoever'],
                p = [0.4, 0.2, 0.2, 0.2])

    def cond(self, token):
        return token.lower == 'whatever'

