from .rule import PrepCond
from erarigilo.en.util.rule import TrgInCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class StandardPrepRule(
        TrgInCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'standard_prep'

    def __init__(self):
        super().__init__(
                ['', 'of', 'to', 'in', 'for', 'on', 'with', 'by', 'at'])
        self.target_set = {'of', 'to', 'in', 'for', 'on', 'with', 'at'}

