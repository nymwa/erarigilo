from .rule import PcompCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PcompByRule(
        WordEqCondRule,
        PcompCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'pcomp_by'

    def __init__(self):
        super().__init__(['at', 'in', 'on', 'of', 'from'])
        self.target_word = 'by'

