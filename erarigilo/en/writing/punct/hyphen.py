from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class HyphenRule(
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'hyphen'

    def __init__(self):
        super().__init__([
            '',
            '--',
            '---',
            '- -'],
            p = [
                0.85,
                0.10,
                0.025,
                0.025])

    def cond(self, token):
        return token.trg == '-'

