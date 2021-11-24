from erarigilo.en.function.pron.rule import (
        PronCond,
        DepEqCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class DobjRule(
        TrgEqCondRule,
        DepEqCond,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '3sng_inan_dobj'

    def __init__(self):
        super().__init__([
            '',
            'its',
            'them',
            'him',
            'her',
            'this',
            'that',
            'which',
            'for it',
            'to it',
            'on it',
            'in it',
            'at it',
            'of it'])
        self.target_word = 'it'
        self.target_dep_label = 'dobj'

