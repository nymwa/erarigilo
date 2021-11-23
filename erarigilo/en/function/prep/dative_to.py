from .rule import DativeCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class DativeToRule(
        TrgEqCondRule,
        DativeCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'dative_to'

    def __init__(self):
        super().__init__(
                ['', 'for'],
                p = [0.4, 0.6])
        self.target_word = 'to'

