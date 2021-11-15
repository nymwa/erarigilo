from erarigilo.en.util.rule import (
        PlainWordCond,
        WordEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class OtherRule(
        WordEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'other'

    def __init__(self):
        super().__init__(['another', 'others'])
        self.target_word = 'other'

