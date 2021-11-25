from erarigilo.module.rule import (
        ChoiceSamplableRule,
        IndexWiseRule)
from erarigilo.en.util.token import EnToken

class InsRightCommaRule(
        ChoiceSamplableRule,
        IndexWiseRule):

    name = 'ins_right_comma'

    def __init__(self):
        super().__init__([
            ',',
            ', ,',
            '.',
            ';',
            ':'],
            p = [
                0.9,
                0.025,
                0.025,
                0.025,
                0.025])

    def centr_cond_1(self, sent, index):
        return sent[index].tag in {
                'NN',
                'NNS',
                'NNP',
                'NNPS'}

    def centr_cond_2_1(self, sent, index):
        return sent[index].tag in {
                'RB',
                'RBR',
                'RBS'}

    def centr_cond_2_2(self, sent, index):
        return sent[index].pos == 'ADV'

    def centr_cond_2(self, sent, index):
        return (
            self.centr_cond_2_1(sent, index)
            and
            self.centr_cond_2_2(sent, index))

    def centr_cond(self, sent, index):
        return (
            self.centr_cond_1(sent, index)
            or
            self.centr_cond_2(sent, index))

    def right_cond(self, sent, index):
        return sent[index + 1].tag in {
                'VB',
                'VBD',
                'VBG',
                'VBN',
                'VBP',
                'VBZ'}

    def cond(self, sent, index):
        if index < len(sent) - 1:
            return (
                self.centr_cond(sent, index)
                and
                self.right_cond(sent, index))
        return False

    def make_error(self, sent, index):
        sent[index].addition.append(
                EnToken(
                    index = sent[index].index + 0.5,
                    src = self.sampler()))
        return sent

