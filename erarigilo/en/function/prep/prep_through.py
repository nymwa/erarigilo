from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepThroughRule(
        TrgEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_through'

    def __init__(self):
        super().__init__(
                ['in', 'over', 'across', 'into', 'of',
                    'with', 'by', 'throughout', 'thru'])
        self.target_word = 'through'

