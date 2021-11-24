from erarigilo.en.function.pron.rule import (
        PronCond,
        DepInCond)
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class ReflexiveRule(
        TrgEqCondRule,
        DepInCond,
        PronCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = '1plu_reflexive'

    def __init__(self):
        super().__init__([
            '',
            'to ourselves',
            'of ourselves',
            'for ourselves',
            'by ourselves',
            'with ourselves',
            'ourself',
            'to ourself',
            'of ourself',
            'for ourself',
            'by ourself',
            'with ourself',
            'us',
            'our',
            'ours',
            'yourselves',
            'myself'],
            p = [
                0.2,
                0.1,
                0.1,
                0.1,
                0.1,
                0.1,
                0.02,
                0.02,
                0.02,
                0.02,
                0.02,
                0.02,
                0.1,
                0.02,
                0.02,
                0.02,
                0.02])
        self.target_word = 'ourselves'
        self.target_dep_set = {
                'dobj',
                'conj',
                'nsubj',
                'nsubjpass',
                'npadvmod',
                'dative',
                'attr'}

