from .rule import DetCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class EachRule(
        TrgEqCondRule,
        DetCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'det_each'

    def __init__(self):
        super().__init__(['', 'all', 'both', 'every'])
        self.target_word = 'each'

