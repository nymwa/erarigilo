from .rule import DetPlusCond
from erarigilo.en.util.rule import TrgInCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class DemonstrativeRule(
        TrgInCondRule,
        DetPlusCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'demonstrative'

    def __init__(self):
        super().__init__(
                ['', 'this', 'that', 'these', 'those', 'a', 'an', 'the'])
        self.target_set = {'this', 'that', 'these', 'those'}

    def plus_cond(self, token):
        return token.dep == 'det'

