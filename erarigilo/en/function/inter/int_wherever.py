from erarigilo.en.util.rule import (
        PlainWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhereverRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_wherever'

    def __init__(self):
        super().__init__(
                ['where', 'whatever', 'whenever', 'whichever',
                    'wherein', 'whereas', 'whereby'])
        self.target_word = 'whenever'

