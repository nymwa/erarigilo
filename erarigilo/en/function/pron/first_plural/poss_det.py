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

    name = '1plu_poss'

    def __init__(self):
        super().__init__([
            '',
            'we',
            'us',
            'ours',
            'a',
            'the',
            'an',
            'theirs',
            'its',
            'my'])
        self.target_word = 'our'

