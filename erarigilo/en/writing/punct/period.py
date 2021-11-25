from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class PeriodRule(
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'period'

    def __init__(self):
        super().__init__([
            '',
            ',',
            '. .',
            '..',
            ':',
            ';',
            '!',
            '?'],
            p = [
                0.5,
                0.3,
                0.05,
                0.05,
                0.025,
                0.025,
                0.025,
                0.025])

    def cond(self, token):
        return token.trg == '.'

