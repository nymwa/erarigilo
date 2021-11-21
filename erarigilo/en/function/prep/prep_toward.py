from .rule import PrepCond
from erarigilo.en.util.rule import WordInCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class PrepTowardRule(
        WordInCondRule,
        PrepCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_toward'

    def __init__(self):
        super().__init__(['to', 'with', 'of', 'for', 'in', 'into'])
        self.target_set = {'toward', 'towards'}

