from erarigilo.module.rule import (
        ChoiceSamplableRule,
        IndexWiseRule)
from erarigilo.en.util.token import EnToken

class InsDetRule(
        ChoiceSamplableRule,
        IndexWiseRule):

    name = 'ins_det'

    def __init__(self):
        super().__init__(
                ['a', 'an', 'the', 'this', 'that', 'these', 'those'],
                p = [0.3, 0.3, 0.3, 0.025, 0.025, 0.025, 0.025])

    def c1(self, sent, index):
        return (
            (index == 0)
            and
            (sent[index].tag in {'NN', 'NNS', 'JJ', 'JJN', 'JJS'}))

    def c2(self, sent, index):
        return (
            (0 < index < len(sent))
            and
            (sent[index - 1].tag in {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'IN'})
            and
            (sent[index].tag in {'NN', 'NNS', 'JJ', 'JJN', 'JJS'}))


    def cond(self, sent, index):
        return self.c1(sent, index) or self.c2(sent, index)

    def preprocess(self, sent, index):
        if (index == 0):
            if (sent[index].src is None):
                sent[index].src = sent[index].trg
            sent[index].src = sent[index].src.lower()
        return sent

    def get_error(self, sent, index):
        error = self.sampler()
        if (index == 0):
            error = error.title()
        return error

    def add_error(self, sent, index, error):
        sent[index].addition = [
                EnToken(
                    index = sent[index].index - 0.5,
                    src = error)
                ] + sent[index].addition
        return sent

    def make_error(self, sent, index):
        sent = self.preprocess(sent, index)
        error = self.get_error(sent, index)
        sent = self.add_error(sent, index, error)
        return sent

