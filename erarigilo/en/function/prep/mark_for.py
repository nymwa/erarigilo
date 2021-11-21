from .rule import MarkCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class MarkForRule(
        WordEqCondRule,
        MarkCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'mark_for'

    def __init__(self):
        super().__init__(
                ['', 'to', 'on', 'in'],
                p = [0.2, 0.6, 0.1, 0.1])
        self.target_word = 'for'

