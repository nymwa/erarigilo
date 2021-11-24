from erarigilo.en.function.pron.rule import PronCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PossDetRule(
        TrgEqCondRule,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '1sng_poss_det'

    def __init__(self):
        super().__init__([
            '',
            'I',
            'me',
            'mine',
            'a',
            'an',
            'the',
            'its',
            'his',
            'her',
            'their'])
        self.target_word = 'my'

