from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhetherRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whether'

    def __init__(self):
        super().__init__(
                ['which', 'what', 'that', 'how', 'whatever', 'whatsoever', 'if'])

    def cond(self, token):
        return token.lower == 'whether'

