from erarigilo.en.util.rule import (
        PlainWordCond,
        WordEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class SuchRule(
        WordEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'such'

    def __init__(self):
        super().__init__(['', 'so', 'very'])
        self.target_word = 'such'

