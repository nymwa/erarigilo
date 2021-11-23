from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepBetweenRule(
        TrgEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_between'

    def __init__(self):
        super().__init__(
                ['', 'in', 'on', 'at', 'about',
                    'among', 'amongst', 'amid', 'amidst'])
        self.target_word = 'between'

