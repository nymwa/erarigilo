from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhenRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_when'

    def __init__(self):
        super().__init__(['where', 'until', 'that', 'what', 'for', 'in'])

    def cond(self, token):
        return token.lower == 'when'

