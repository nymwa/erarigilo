from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepByRule(
        TrgEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_by'

    def __init__(self):
        super().__init__(
                ['', 'in', 'on', 'at', 'for', 'with',
                    'of', 'from', 'through', 'until', 'till'])
        self.target_word = 'by'

