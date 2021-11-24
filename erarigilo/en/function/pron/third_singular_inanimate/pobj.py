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

    name = '3sng_inan_pobj'

    def __init__(self):
        super().__init__([
            'its',
            'them',
            'him',
            'her',
            'this',
            'that',
            'which'])
        self.target_word = 'it'
        self.target_dep_label = 'pobj'

