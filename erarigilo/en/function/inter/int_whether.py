from erarigilo.en.util.rule import (
        PlainWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhetherRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whether'

    def __init__(self):
        super().__init__(
                ['which', 'what', 'that', 'how',
                    'whatever', 'whatsoever', 'if'])
        self.target_word = 'whether'

