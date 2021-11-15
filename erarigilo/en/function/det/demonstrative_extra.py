from .rule import DetPlusCond
from erarigilo.en.util.rule import WordInCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class DemonstrativeExtraRule(
        WordInCondRule,
        DetPlusCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'demonstrative_extra'

    def __init__(self):
        super().__init__(
                ['', 'this', 'that', 'these', 'those'])
        self.target_set = {'this', 'that', 'these', 'those'}

    def plus_cond(self, token):
        return (
            (token.dep in {
                'nsubj', 'nsubjpass', 'pobj', 'dobj', 'conj', 'appos',
                'attr', 'advmod', 'ROOT', 'quantmod', 'npadvmod'})
            and
            (token.tag != 'WDT'))

