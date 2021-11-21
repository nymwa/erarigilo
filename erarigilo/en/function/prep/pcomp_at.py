from .rule import PcompCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PcompAtRule(
        WordEqCondRule,
        PcompCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'pcomp_at'

    def __init__(self):
        super().__init__(['on', 'in', 'of'])
        self.target_word = 'at'

