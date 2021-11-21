from .rule import PrepCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepAboutRule(
        WordEqCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_about'

    def __init__(self):
        super().__init__(['', 'in', 'on', 'of', 'to', 'at'])
        self.target_word = 'about'

