from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepOutRule(
        TrgEqCondRule,
        PrepCond,
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_out'

    def __init__(self):
        super().__init__()
        self.target_word = 'out'

