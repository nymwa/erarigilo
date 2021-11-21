from .rule import MarkCond
from erarigilo.en.util.rule import WordInCondRule
from erarigilo.module.rule import (
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class StandardMarkRule(
        WordInCondRule,
        MarkCond,
        DeletingRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'standard_mark'

    def __init__(self):
        super().__init__()
        self.target_set = {
                'as', 'if', 'because', 'so', 'whether',
                'while', 'since', 'although', 'than', 'though',
                'once', 'whereas', 'whilst', 'like', 'except'}

