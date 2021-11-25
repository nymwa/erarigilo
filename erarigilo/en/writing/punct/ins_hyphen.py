from erarigilo.module.rule import (
        ChoiceSamplableRule,
        IndexWiseRule)
from erarigilo.en.util.token import EnToken

class InsHyphenRule(
        ChoiceSamplableRule,
        IndexWiseRule):

    name = 'ins_hyphen'

    def __init__(self):
        super().__init__([
            '-',
            '--',
            '---',
            '- -'],
            p = [
                0.7,
                0.25,
                0.025,
                0.025])

    def c1(self, sent, index):
        return sent[index].tag in {
                'JJ',
                'JJR',
                'JJS',
                'NN',
                'NNS',
                'RB',
                'CD'}

    def r1(self, sent, index):
        return sent[index + 1].tag in {
                'JJ',
                'JJR',
                'JJS',
                'NN',
                'NNS',
                'VBN',
                'VBG'}

    def c2(self, sent, index):
        return sent[index].tag in {
                'JJ',
                'JJR',
                'JJS',
                'CD',
                'NN',
                'NNS'}

    def r2(self, sent, index):
        return sent[index + 1].tag == 'RB'

    def c3(self, sent, index):
        return sent[index].tag == 'CD'

    def r3(self, sent, index):
        return sent[index + 1].tag == 'CD'

    def c4(self, sent, index):
        return sent[index].tag in {
                'VB',
                'VBG',
                'VBN',
                'NN',
                'NNS'}

    def r4(self, sent, index):
        return sent[index + 1].tag == 'RP'

    def cond(self, sent, index):
        if index < len(sent) - 1:
            return (
                (self.c1(sent, index) and self.r1(sent, index))
                or
                (self.c2(sent, index) and self.r2(sent, index))
                or
                (self.c3(sent, index) and self.r3(sent, index))
                or
                (self.c4(sent, index) and self.r4(sent, index)))
        return False

    def make_error(self, sent, index):
        sent[index].addition.append(
                EnToken(
                    index = sent[index].index + 0.5,
                    src = self.sampler()))
        return sent

