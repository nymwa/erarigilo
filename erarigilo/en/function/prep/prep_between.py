from .rule import PrepCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepBetweenRule(
        WordEqCondRule,
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

