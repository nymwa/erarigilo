from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class ColonRule(
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'colon'

    def __init__(self):
        super().__init__([
            '',
            '.',
            ',',
            ';'],
            p = [
                0.4,
                0.2,
                0.2,
                0.2])

    def cond(self, token):
        return token.trg == ':'

