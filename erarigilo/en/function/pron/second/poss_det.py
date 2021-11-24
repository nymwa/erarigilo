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

    name = '2nd_poss_det'

    def __init__(self):
        super().__init__([
            '',
            'you',
            'yours',
            'their',
            'a',
            'an',
            'the',
            'its',
            'they'])
        self.target_word = 'your'

