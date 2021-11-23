from erarigilo.en.util.rule import (
        TrgEqCondRule,
        PlainWordCond)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class AndRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'conj_and'

    def __init__(self):
        super().__init__(
                ['', 'but'],
                p = [0.95, 0.05])
        self.target_word = 'and'

