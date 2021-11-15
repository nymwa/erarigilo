from erarigilo.module.rule import (
        ReplacableRule,
        TokenWiseRule)

class AuxpassRule(ReplacableRule, TokenWiseRule):

    name = 'auxpass'

    def __init__(self):
        super().__init__('')

    def cond(self, token):
        return token.dep == 'auxpass'

