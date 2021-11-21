from .rule import DativeCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class DativeToRule(
        WordEqCondRule,
        DativeCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'dative_to'

    def __init__(self):
        super().__init__(
                ['', 'for'],
                p = [0.4, 0.6])
        self.target_word = 'to'

