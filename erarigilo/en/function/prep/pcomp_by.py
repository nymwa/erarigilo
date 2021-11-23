from .rule import PcompCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PcompByRule(
        TrgEqCondRule,
        PcompCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'pcomp_by'

    def __init__(self):
        super().__init__(['at', 'in', 'on', 'of', 'from'])
        self.target_word = 'by'

