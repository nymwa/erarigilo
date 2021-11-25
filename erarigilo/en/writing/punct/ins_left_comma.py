from erarigilo.module.rule import (
        ChoiceSamplableRule,
        IndexWiseRule)
from erarigilo.en.util.token import EnToken

class InsLeftCommaRule(
        ChoiceSamplableRule,
        IndexWiseRule):

    name = 'ins_left_comma'

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

    def left_cond_1_1(self, sent, index):
        return sent[index - 1].tag in {
                'NN',
                'NNS',
                'NNP',
                'NNPS'}

    def left_cond_1_2_1(self, sent, index):
        return sent[index - 1].tag in {
                'RB',
                'RBR',
                'RBS'}

    def left_cond_1_2_2(self, sent, index):
        return sent[index - 1].pos == 'ADV'

    def left_cond_1_2(self, sent, index):
        return (
            self.left_cond_1_2_1(sent, index)
            and
            self.left_cond_1_2_2(sent, index))

    def left_cond_1(self, sent, index):
        return (
            self.left_cond_1_1(sent, index)
            or
            self.left_cond_1_2(sent, index))

    def cent_cond_1(self, sent, index):
        return sent[index].tag in {
                'CC',
                'DT',
                'IN',
                'WDT',
                'WP',
                'WP$',
                'WRB'}

    def cond_1(self, sent, index):
        return (
            self.left_cond_1(sent, index)
            and
            self.cent_cond_1(sent, index))

    def left_cond_2(self, sent, index):
        return sent[index - 1].tag in {
                'NN',
                'NNS',
                'NNP',
                'NNPS'}

    def cent_cond_2_1(self, sent, index):
        return sent[index].tag in {
                'RB',
                'RBR',
                'RBS'}

    def cent_cond_2_2(self, sent, index):
        return sent[index].pos == 'ADV'

    def cent_cond_2(self, sent, index):
        return (
            self.cent_cond_2_1(sent, index)
            and
            self.cent_cond_2_2(sent, index))

    def cond_2(self, sent, index):
        return (
            self.left_cond_2(sent, index)
            and
            self.cent_cond_2(sent, index))

    def cond(self, sent, index):
        if 0 < index < len(sent):
            return (
                self.cond_1(sent, index)
                or
                self.cond_2(sent, index))
        return False

    def make_error(self, sent, index):
        sent[index].addition = [
                EnToken(
                    index = sent[index].index - 0.5,
                    src = self.sampler())
                ] + sent[index].addition
        return sent

