from erarigilo.en.util.rule import (
        PlainWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class ThereRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'there'

    def __init__(self):
        super().__init__(
                ['', 'here', 'they', 'it'],
                p = [0.5, 0.3, 0.1, 0.1])
        self.target_word = 'there'

