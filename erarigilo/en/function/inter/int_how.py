from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class HowRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_how'

    def __init__(self):
        super().__init__(
                ['what', 'that', 'who', 'which'],
                p = [0.6, 0.2, 0.1, 0.1])

    def cond(self, token):
        return token.lower == 'how'

