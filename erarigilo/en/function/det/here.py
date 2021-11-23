from erarigilo.en.util.rule import (
        PlainWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class HereRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'here'

    def __init__(self):
        super().__init__(
                ['', 'there', 'they', 'it'],
                p = [0.5, 0.3, 0.1, 0.1])
        self.target_word = 'here'

