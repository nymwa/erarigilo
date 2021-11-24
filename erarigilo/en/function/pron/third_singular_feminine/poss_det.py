from erarigilo.en.function.pron.rule import (
        PronCond,
        DepEqCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PossDetRule(
        TrgEqCondRule,
        DepEqCond,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '3sng_fem_poss_det'

    def __init__(self):
        super().__init__([
            '',
            'she',
            'hers',
            'their',
            'his',
            'a',
            'an',
            'the',
            'its'])
        self.target_word = 'her'
        self.target_dep_label = 'poss'

