from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhitherRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whither'

    def __init__(self):
        super().__init__(['when', 'whence', 'that', 'what'])

    def cond(self, token):
        return token.lower == 'whither'

