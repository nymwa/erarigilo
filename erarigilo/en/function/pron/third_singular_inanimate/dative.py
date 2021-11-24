from erarigilo.en.function.pron.rule import (
        PronCond,
        DepEqCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class DativeRule(
        TrgEqCondRule,
        DepEqCond,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '3sng_inan_dative'

    def __init__(self):
        super().__init__([
            '',
            'its',
            'her',
            'him',
            'them',
            'for it',
            'to it',
            'on it',
            'in it',
            'at it'])
        self.target_word = 'it'
        self.target_dep_label = 'dative'

