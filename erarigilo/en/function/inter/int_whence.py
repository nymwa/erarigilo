from erarigilo.en.util.rule import (
        PlainWordCond,
        TrgEqCondRule)
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class WhenceRule(
        TrgEqCondRule,
        PlainWordCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'int_whence'

    def __init__(self):
        super().__init__(['when', 'whither', 'where', 'what'])
        self.target_word = 'whence'

