from .rule import PcompCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PcompOfRule(
        TrgEqCondRule,
        PcompCond,
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'pcomp_of'

    def __init__(self):
        super().__init__()
        self.target_word = 'of'

