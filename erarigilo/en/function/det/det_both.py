from .rule import DetCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class BothRule(
        WordEqCondRule,
        DetCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'det_both'

    def __init__(self):
        super().__init__(['', 'all', 'each', 'every'])
        self.target_word = 'both'

