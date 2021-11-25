from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class BangRule(
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'bang'

    def __init__(self):
        super().__init__([
            '',
            '.',
            ',',
            '?'],
            p = [
                0.4,
                0.2,
                0.2,
                0.2])

    def cond(self, token):
        return token.trg == '!'

