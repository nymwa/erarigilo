from .rule import PrepCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepByRule(
        WordEqCondRule,
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

