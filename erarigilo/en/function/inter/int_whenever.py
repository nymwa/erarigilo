from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WheneverRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whenever'

    def __init__(self):
        super().__init__(['when', 'whatever', 'wherever', 'whichever', 'until', 'that', 'what', 'for', 'in'])

    def cond(self, token):
        return token.lower == 'whenever'

