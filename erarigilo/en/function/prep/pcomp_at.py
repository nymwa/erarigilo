from .rule import PcompCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PcompAtRule(
        TrgEqCondRule,
        PcompCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'pcomp_at'

    def __init__(self):
        super().__init__(['on', 'in', 'of'])
        self.target_word = 'at'

