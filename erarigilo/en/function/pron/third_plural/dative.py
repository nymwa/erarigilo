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

    name = '3plu_dative'

    def __init__(self):
        super().__init__([
            '',
            'they',
            'him',
            'her',
            'for them',
            'to them',
            'on them',
            'in them',
            'at them'],
            p = [
                0.05,
                0.05,
                0.05,
                0.05,
                0.3,
                0.35,
                0.05,
                0.05,
                0.05])
        self.target_word = 'them'
        self.target_dep_label = 'dative'

