from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepUntilRule(
        TrgEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_until'

    def __init__(self):
        super().__init__(['by', 'for', 'to', 'in', 'up to', 'when'])
        self.target_word = 'until'

