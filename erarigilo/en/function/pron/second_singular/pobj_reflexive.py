from erarigilo.en.function.pron.rule import (
        PronCond,
        DepEqCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PobjReflexiveRule(
        TrgEqCondRule,
        DepEqCond,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '2sng_pobj_reflexive'

    def __init__(self):
        super().__init__([
            'you',
            'your self',
            'yourselves',
            'your'])
        self.target_word = 'yourself'
        self.target_dep_label = 'pobj'

