from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhereverRule(
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_wherever'

    def __init__(self):
        super().__init__(
                ['where', 'whatever', 'whenever', 'whichever', 'wherein', 'whereas', 'whereby'])

    def cond(self, token):
        return token.lower == 'wherever'

