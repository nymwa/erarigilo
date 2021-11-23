from .rule import PrepCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepUponRule(
        TrgEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_upon'

    def __init__(self):
        super().__init__(['on', 'up', 'up on', 'over', 'after', 'to'])
        self.target_word = 'upon'

