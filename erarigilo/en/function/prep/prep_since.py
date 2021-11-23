from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ReplacableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepSinceRule(
        TrgEqCondRule,
        PrepCond,
        ReplacableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_since'

    def __init__(self):
        super().__init__('from')
        self.target_word = 'since'

