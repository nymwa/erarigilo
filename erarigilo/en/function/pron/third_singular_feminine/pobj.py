from erarigilo.en.function.pron.rule import (
        PronCond,
        DepEqCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PobjRule(
        TrgEqCondRule,
        DepEqCond,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '3sng_fem_pobj'

    def __init__(self):
        super().__init__([
            'she',
            'hers',
            'their',
            'them',
            'herself',
            'him'])
        self.target_word = 'her'
        self.target_dep_label = 'pobj'

