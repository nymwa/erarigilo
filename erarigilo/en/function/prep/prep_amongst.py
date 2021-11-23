from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepAmongstRule(
        TrgEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_amongst'

    def __init__(self):
        super().__init__(['', 'in', 'on', 'at', 'about', 'between', 'amidst'])
        self.target_word = 'amongst'

