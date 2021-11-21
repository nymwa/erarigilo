from .rule import PrepCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ReplacableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepSinceRule(
        WordEqCondRule,
        PrepCond,
        ReplacableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_since'

    def __init__(self):
        super().__init__('from')
        self.target_word = 'since'

