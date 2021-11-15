from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhicheverRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whichever'

    def __init__(self):
        super().__init__(['whatever', 'whoever', 'however', 'which'])

    def cond(self, token):
        return token.lower == 'whichever'

