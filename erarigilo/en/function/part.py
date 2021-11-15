from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRule)

class PartRule(
        ChoiceSamplableRule,
        TokenWiseRule):

    name = 'part'

    def __init__(self):
        super().__init__(
                ['', 'out', 'up', 'down', 'about', 'on', 'in', 'off'],
                p = [0.65] + [0.05] * 7)

    def cond(self, token):
        return (token.dep == 'prt') and (token.tag == 'RP')

