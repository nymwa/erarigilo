from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class CommaRule(
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'comma'

    def __init__(self):
        super().__init__([
            '',
            '.',
            '. .',
            ';'],
            p = [
                0.90,
                0.05,
                0.025,
                0.025])

    def cond(self, token):
        return token.trg == ','

