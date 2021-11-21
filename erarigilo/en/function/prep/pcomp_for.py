from .rule import PcompCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PcompForRule(
        WordEqCondRule,
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

