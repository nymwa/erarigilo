from erarigilo.en.function.pron.rule import PronCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PossRule(
        TrgEqCondRule,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '3sng_fem_poss'

    def __init__(self):
        super().__init__([
            '',
            'she',
            'her',
            'theirs',
            'his',
            'they',
            'yours'])
        self.target_word = 'hers'

