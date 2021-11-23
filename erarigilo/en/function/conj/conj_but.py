from erarigilo.en.util.rule import (
        TrgEqCondRule,
        PlainWordCond)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class ButRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'conj_but'

    def __init__(self):
        super().__init__(
                ['', 'and'],
                p = [0.9, 0.1])
        self.target_word = 'but'

