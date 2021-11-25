from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class TwoHyphensRule(
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'two_hyphens'

    def __init__(self):
        super().__init__([
            '',
            '-',
            '---',
            '- -'],
            p = [
                0.2,
                0.7,
                0.05,
                0.05])

    def cond(self, token):
        return token.trg == '--'

