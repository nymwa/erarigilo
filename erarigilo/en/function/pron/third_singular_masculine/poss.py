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

    name = '3sng_masc_poss'

    def __init__(self):
        super().__init__([
            '',
            'he',
            'him',
            'her',
            'a',
            'an',
            'the',
            'its',
            'theirs'])
        self.target_word = 'his'

