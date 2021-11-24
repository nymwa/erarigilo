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

    name = '2nd_pobj'

    def __init__(self):
        super().__init__([
            'u',
            'yo',
            'your',
            'yours',
            'yourself',
            'yourselves'])
        self.target_word = 'you'
        self.target_dep_label = 'pobj'

