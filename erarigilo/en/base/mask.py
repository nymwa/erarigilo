import random as rd
from erarigilo.module.rule import Rule
from erarigilo.module.module import BetaModule
from erarigilo.module.factory import Factory
from erarigilo.util.sampler import (
        UniformSampler,
        BetaSampler,
        GeometricSampler)

char_mask = chr(0x25a1)
word_mask = chr(0x25a8)

class Mask(Rule):

    name = 'mask'

    def cond(self, token):
        return token.word() != ''

    def make_error(self, token):
        token.src = word_mask
        return token

    def __call__(self, token):
        token = self.make_error(token)
        token = self.add_history(token)
        return token


class BetterMask(Mask):

    def __init__(self, p, threshold_mean, threshold_std):
        super().__init__()
        self.beta_sampler = BetaSampler(threshold_mean, threshold_std)
        self.geometric_sampler = GeometricSampler(p)
        self.uniform_sampler = UniformSampler()

    def make_char_masked_word(self, word):
        num_iter = self.geometric_sampler()
        for _ in range(num_iter):
            if len(word) > 1:
                pos = rd.randrange(len(word) - 1)
                word = word[:pos] + char_mask + word[pos+1:]
        return word

    def make_error(self, token, thres):
        if self.uniform_sampler() < thres:
            token.src = self.make_char_masked_word(token.word())
        else:
            token.src = word_mask
        return token

    def __call__(self, token, thres):
        token = self.make_error(token, thres)
        token = self.add_history(token)
        return token


class MaskApplier:

    def apply_original(self, sent, lottery, index):
        # apply for original tokens
        if self.rule.cond(sent[index]) and lottery():
            sent[index] = self.rule(sent[index])
        return sent

    def apply_added(self, sent, lottery, index):
        # apply for added tokens
        for pos in range(len(sent[index].addition)):
            if self.rule.cond(sent[index].addition[pos]) and lottery():
                sent[index].addition[pos] = self.rule(self[index].addition[pos])
        return sent

    def apply(self, sent, lottery):
        # apply mask mistakes
        for index in range(len(sent)):
            sent = self.apply_original(sent, lottery, index)
            sent = self.apply_added(sent, lottery, index)
        return sent


class BetterMaskApplier:

    def apply_original(self, sent, lottery, char_threshold, index):
        # apply for original tokens
        if self.rule.cond(sent[index]) and lottery():
            sent[index] = self.rule(sent[index], char_threshold)
        return sent

    def apply_added(self, sent, lottery, char_threshold, index):
        # apply for added tokens
        for pos in range(len(sent[index].addition)):
            if self.rule.cond(sent[index].addition[pos]) and lottery():
                sent[index].addition[pos] = self.rule(
                        sent[index].addition[pos],
                        char_threshold)
        return sent

    def apply(self, sent, lottery, char_threshold):
        # apply mask mistakes
        for index in range(len(sent)):
            sent = self.apply_original(sent, lottery, char_threshold, index)
            sent = self.apply_added(sent, lottery, char_threshold, index)
        return sent


class MaskModule(MaskApplier, BetaModule):

    pass


class BetterMaskModule(BetterMaskApplier, BetaModule):

    def __call__(self, sent):
        word_threshold = self.get_threshold()
        char_threshold = self.rule.beta_sampler()
        lottery = lambda : self.uniform_sampler() < word_threshold
        sent = self.apply(sent, lottery, char_threshold)
        sent.history.append({
            'name' : self.rule.name,
            'threshold' : round(word_threshold, 2),
            'char_threshold' : round(char_threshold, 2)})
        return sent


class MaskFactory(Factory):

    def __init__(self):
        super().__init__()
        self.name = Mask.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        p = dct.get('p', 0.9)
        threshold_mean = dct.get('threshold_mean', 0.0)
        threshold_std = dct.get('threshold_std', 0.0)

        if threshold_mean == 0.0:
            rule = Mask()
            module = MaskModule(mean, std, rule)
        else:
            rule = BetterMask(p, threshold_mean, threshold_std)
            module = BetterMaskModule(mean, std, rule)
        return module

