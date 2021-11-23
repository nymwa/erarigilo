from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepThroughoutRule(
        TrgEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_throughout'

    def __init__(self):
        super().__init__(
                ['in', 'over', 'across', 'into', 'of',
                    'with', 'by', 'through'])
        self.target_word = 'throughout'

