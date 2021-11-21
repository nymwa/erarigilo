from .rule import PrepCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepOutRule(
        WordEqCondRule,
        PrepCond,
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_out'

    def __init__(self):
        super().__init__()
        self.target_word = 'out'

