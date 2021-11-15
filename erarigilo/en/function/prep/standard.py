from .rule import PrepCond
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class StandardRule(
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'standard_prep'

    def __init__(self):
        super().__init__(
                ['', 'of', 'to', 'in', 'for', 'on', 'with', 'by', 'at'])

    def word_cond(self, token):
        assert False
        return token

