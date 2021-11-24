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

    name = '1plu_dative'

    def __init__(self):
        super().__init__([
            '',
            'we',
            'for us',
            'to us',
            'on us',
            'in us',
            'at us'],
            p = [
                0.1,
                0.1,
                0.3,
                0.35,
                0.05,
                0.05,
                0.05])
        self.target_word = 'us'
        self.target_dep_label = 'dative'

