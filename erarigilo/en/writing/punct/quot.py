from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class QuotRule(
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'quot'

    def __init__(self):
        super().__init__([
            '',
            "'",
            '"',
            "''",
            '``'])

    def cond(self, token):
        return token.tag in {
                '``',
                "''"}

