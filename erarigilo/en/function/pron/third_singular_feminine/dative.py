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

    name = '3sng_fem_dative'

    def __init__(self):
        super().__init__([
            '',
            'she',
            'him',
            'for her',
            'to her',
            'on her',
            'in her',
            'at her'],
            p = [
                0.1,
                0.05,
                0.05,
                0.3,
                0.35,
                0.05,
                0.05,
                0.05])
        self.target_word = 'her'
        self.target_dep_label = 'dative'

