from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class ThatRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_that'

    def __init__(self):
        super().__init__(['which', 'who', 'how', 'what'])

    def cond(self, token):
        return (token.lower == 'that') and (token.tag == 'WDT')

