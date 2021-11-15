from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhyRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_why'

    def __init__(self):
        super().__init__(['how', 'when', 'where', 'that', 'what'])

    def cond(self, token):
        return token.lower == 'why'

