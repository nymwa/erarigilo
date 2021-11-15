from tabulate import tabulate
from .row import Row

class Table:

    def __init__(self, cond, sent):

        self.row_list = []
        for token in sent:
            self.row_list.append(Row(cond, token))
            self.row_list += [Row(cond, x) for x in token.addition]

        self.col_list = [
            'i',
            'shift',
            'src',
            'trg',
            'cond',
            'l_space',
            'r_space',
            'tag',
            'pos',
            'dep',
            'lemma',
            'norm',
            'ent_type',
            'ent_iob',
            'history']

    def __call__(self):
        tab = [x() for x in self.row_list]
        return tabulate(tab, self.col_list, tablefmt = 'psql')
