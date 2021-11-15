from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhereRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_where'

    def __init__(self):
        super().__init__(['when', 'wherein', 'whereas', 'whereby'])

    def cond(self, token):
        return token.lower == 'where'

