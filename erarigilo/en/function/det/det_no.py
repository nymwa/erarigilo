from .rule import DetCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class NoRule(
        TrgEqCondRule,
        DetCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'det_no'

    def __init__(self):
        super().__init__(['not', 'non', 'any'])
        self.target_word = 'no'

