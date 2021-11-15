from erarigilo.en.util.rule import (
        PlainWordCond,
        WordEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class SoRule(
        WordEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'so'

    def __init__(self):
        super().__init__(['', 'such', 'too'])
        self.target_word = 'so'

