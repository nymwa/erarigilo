from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhenceRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whence'

    def __init__(self):
        super().__init__(['when', 'whither', 'where', 'what'])

    def cond(self, token):
        return token.lower == 'whence'

