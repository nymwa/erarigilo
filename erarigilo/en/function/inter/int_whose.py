from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhoseRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whose'

    def __init__(self):
        super().__init__(['which', 'who', 'that', 'its', 'his', 'her', 'their'])

    def cond(self, token):
        return token.lower == 'whose'

