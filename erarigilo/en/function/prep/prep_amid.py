from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepAmidRule(
        TrgEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_amid'

    def __init__(self):
        super().__init__(['', 'in', 'on', 'at', 'about', 'between', 'among'])
        self.target_word = 'amid'

