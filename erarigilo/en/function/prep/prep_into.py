from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepIntoRule(
        TrgEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_into'

    def __init__(self):
        super().__init__(
                ['', 'in', 'to', 'toward', 'towards'],
                p = [0.2, 0.3, 0.3, 0.1, 0.1])
        self.target_word = 'into'

