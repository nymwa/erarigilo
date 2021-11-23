from erarigilo.en.util.rule import (
        PlainWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhichRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_which'

    def __init__(self):
        super().__init__(
                ['that', 'who', 'what', 'how'],
                p = [0.3, 0.3, 0.2, 0.2])
        self.target_word = 'which'

