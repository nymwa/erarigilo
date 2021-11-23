from erarigilo.en.util.rule import (
        PlusWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class ThatRule(
        TrgEqCondRule,
        PlusWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_that'

    def __init__(self):
        super().__init__(['which', 'who', 'how', 'what'])
        self.target_word = 'that'

    def plus_cond(self, token):
        return token.tag == 'WDT'

