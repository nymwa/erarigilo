from .rule import PcompCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PcompOnRule(
        WordEqCondRule,
        PcompCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'pcomp_on'

    def __init__(self):
        super().__init__(['at', 'in', 'of'])
        self.target_word = 'on'

