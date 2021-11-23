from .rule import DetCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class EveryRule(
        TrgEqCondRule,
        DetCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'det_every'

    def __init__(self):
        super().__init__(['', 'all', 'both', 'each'])
        self.target_word = 'every'

