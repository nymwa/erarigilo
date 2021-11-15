from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhoeverRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whoever'

    def __init__(self):
        super().__init__(['whatever', 'whichever', 'however', 'who'])

    def cond(self, token):
        return token.lower == 'whoever'

