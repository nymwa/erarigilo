from .rule import DetCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class AnyRule(
        TrgEqCondRule,
        DetCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'det_any'

    def __init__(self):
        super().__init__(
                ['', 'some', 'every', 'a', 'an', 'all', 'anything'],
                p = [0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
        self.target_word = 'any'

