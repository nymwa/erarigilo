from .rule import DetCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class SomeRule(
        WordEqCondRule,
        DetCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'det_some'

    def __init__(self):
        super().__init__(
                ['', 'a', 'an', 'the', 'those', 'these',
                    'few', 'little', 'something', 'somewhere', 'much', 'many', 'so'],
                p = [0.4, 0.05, 0.05, 0.05, 0.05, 0.05,
                    0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])
        self.target_word = 'some'

