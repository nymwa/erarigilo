from .rule import PrepCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepAfterRule(
        WordEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_after'

    def __init__(self):
        super().__init__(['for', 'by', 'over', 'from', 'when'])
        self.target_word = 'after'

