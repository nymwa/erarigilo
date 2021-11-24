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

    name = '3plu_dobj'

    def __init__(self):
        super().__init__([
            '',
            'they',
            'her',
            'him',
            'for them',
            'to them',
            'on them',
            'in them',
            'at them',
            'of them'],
            p = [
                0.05,
                0.05,
                0.05,
                0.05,
                0.2,
                0.2,
                0.1,
                0.1,
                0.1,
                0.1])
        self.target_word = 'them'
        self.target_dep_label = 'dobj'

