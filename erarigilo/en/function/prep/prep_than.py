from .rule import PrepCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepThanRule(
        WordEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_than'

    def __init__(self):
        super().__init__(
                ['', 'to', 'from', 'over', 'beyond'],
                p = [0.2, 0.4, 0.2, 0.1, 0.1])
        self.target_word = 'than'

