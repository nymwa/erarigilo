from .rule import DetCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class EachRule(
        WordEqCondRule,
        DetCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'det_each'

    def __init__(self):
        super().__init__(['', 'all', 'both', 'every'])
        self.target_word = 'each'

