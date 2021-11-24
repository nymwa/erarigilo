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

    name = '1sng_poss'

    def __init__(self):
        super().__init__([
            'my',
            'me',
            'ours',
            'his',
            'hers'])
        self.target_word = 'mine'

