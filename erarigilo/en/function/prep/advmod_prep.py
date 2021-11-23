from .rule import AdvmodCond
from erarigilo.en.util.rule import TrgInCondRule
from erarigilo.module.rule import (
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class AdvmodRule(
        TrgInCondRule,
        AdvmodCond,
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'prep_advmod'

    def __init__(self):
        super().__init__()
        self.target_set = {'at', 'as'}

