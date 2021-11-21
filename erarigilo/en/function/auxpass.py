from erarigilo.module.rule import (
        DeletingRule,
        TokenWiseRule)

class AuxpassRule(
        DeletingRule,
        TokenWiseRule):

    name = 'auxpass'

    def cond(self, token):
        return token.dep == 'auxpass'

