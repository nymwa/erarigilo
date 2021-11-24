from erarigilo.en.function.pron.rule import (
        PronCond,
        DepInCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class ObjRule(
        TrgEqCondRule,
        DepInCond,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '1sng_nsubj_obj'

    def __init__(self):
        super().__init__([
            '',
            'I',
            'my'])
        self.target_word = 'me'
        self.target_dep_set = {
                'nsubj',
                'nsubjpass',
                'conj',
                'appos',
                'attr'}

