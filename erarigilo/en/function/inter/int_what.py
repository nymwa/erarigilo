from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhatRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_what'

    def __init__(self):
        super().__init__(
                ['how', 'that', 'which', 'who'],
                p = [0.6, 0.2, 0.1, 0.1])

    def cond(self, token):
        return token.lower == 'what'

