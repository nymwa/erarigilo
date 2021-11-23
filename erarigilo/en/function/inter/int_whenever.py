from erarigilo.en.util.rule import (
        PlainWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WheneverRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whenever'

    def __init__(self):
        super().__init__([
            'when', 'whatever', 'wherever', 'whichever',
            'until', 'that', 'what', 'for', 'in'])
        self.target_word = 'whenever'

