from erarigilo.en.util.rule import (
        PlainWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhoRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_who'

    def __init__(self):
        super().__init__(
                ['that', 'which', 'what', 'how'],
                p = [0.3, 0.3, 0.2, 0.2])
        self.target_word = 'who'

