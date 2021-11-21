from pathlib import Path
from erarigilo.module.rule import (
        DeletingRule,
        TokenWiseRule)

class Delete(
        DeletingRule,
        TokenWiseRule):

    name = 'del'

    def __init__(self):
        super().__init__()

        with open(Path(__file__).parent.resolve()
                / 'delete_list.txt') as f:
            tokens = [x.strip() for x in f]
        self.token_set = set(tokens)

    def cond(self, token):
        return token.word().lower() in self.token_set

