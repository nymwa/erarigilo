from .rule import PcompCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PcompToRule(
        TrgEqCondRule,
        PcompCond,
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'pcomp_to'

    def __init__(self):
        super().__init__()
        self.target_word = 'to'

