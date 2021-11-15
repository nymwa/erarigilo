from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class ToRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'to'

    def __init__(self):
        super().__init__(
                ['', 'by', 'for'],
                p = [0.6, 0.2, 0.2])

    def cond(self, token):
        return (token.tag == 'TO') and (token.word().lower() == 'to')

