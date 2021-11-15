from .rule import DetCond
from erarigilo.en.util.rule import WordInCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class ArticleRule(
        WordInCondRule,
        DetCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'art'

    def __init__(self):
        super().__init__(
                ['', 'a', 'an', 'the',
                    'this', 'that', 'these', 'those'],
                p = [0.2, 0.2, 0.2, 0.3,
                    0.025, 0.025, 0.025, 0.025])
        self.target_set = {'a', 'an', 'the'}

