from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class HatenaRule(
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'hatena'

    def __init__(self):
        super().__init__([
            '',
            '.',
            ',',
            '!'],
            p = [
                0.1,
                0.75,
                0.1,
                0.05])

    def cond(self, token):
        return token.trg == '?'

