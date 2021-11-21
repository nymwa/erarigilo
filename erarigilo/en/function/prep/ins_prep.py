from erarigilo.module.rule import (
        ChoiceSamplableRule,
        IndexWiseRule)
from erarigilo.en.util.token import EnToken

class InsPrepRule(
        ChoiceSamplableRule,
        IndexWiseRule):

    name = 'post_vb_prep'

    def __init__(self):
        super().__init__(['to', 'in', 'on', 'at', 'by', 'for', 'with', 'of'])

    def cond_1(self, sent, index):
        return sent[index].tag in {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

    def cond_2(self, sent, index):
        return sent[index].dep in {'acl', 'advcl', 'xcomp', 'pcomp'}

    def cond_3_1(self, sent, index):
        return sent[index + 1].pos in {'NOUN', 'DET', 'ADJ', 'PROPN'}

    def cond_3_2(self, sent, index):
        return (
            (sent[index + 1].pos == 'SCONJ')
            and
            (sent[index + 1].dep == 'mark'))

    def cond_3(self, sent, index):
        return self.cond_3_1(sent, index) or self.cond_3_2(sent, index)

    def cond(self, sent, index):
        return (
            (index < len(sent) - 1)
            and
            self.cond_1(sent, index)
            and
            self.cond_2(sent, index)
            and
            self.cond_3(sent, index))

    def add_error(self, sent, index, error):
        sent[index].addition.append(
                EnToken(
                    index = sent[index].index + 0.5,
                    src = error))
        return sent

    def make_error(self, sent, index):
        error = self.sampler()
        sent = self.add_error(sent, index, error)
        return sent

