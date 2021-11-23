from .rule import PcompCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PcompForRule(
        TrgEqCondRule,
        PcompCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'pcomp_for'

    def __init__(self):
        super().__init__(
                ['to', 'at', 'in', 'on'],
                p = [0.4, 0.2, 0.2, 0.2])
        self.target_word = 'for'

