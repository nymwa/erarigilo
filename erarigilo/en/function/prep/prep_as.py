from .rule import PrepCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepAsRule(
        WordEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_as'

    def __init__(self):
        super().__init__(['by', 'of', 'in', 'on', 'at', 'like'])
        self.target_word = 'as'

