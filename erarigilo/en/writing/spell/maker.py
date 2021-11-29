import random as rd
from erarigilo.util.sampler import (
        GeometricSampler,
        ChoiceSampler)
from falsliter.noiser import FalsLiterNoiser

class SpellErrorMaker:

    def __init__(self, char_prob, n, score_path, temp):
        self.n = n
        self.noiser = FalsLiterNoiser(n, score_path, temp)
        self.num_edit_sampler = GeometricSampler(char_prob)
        self.operation_sampler = ChoiceSampler([
            self.delete,
            self.insert,
            self.replace,
            self.swap])

    def delete(self, word):
        if len(word) <= 1:
            return word
        pos = rd.randrange(len(word))
        error = word[:pos] + word[pos + 1:]
        return error

    def swap(self, word):
        if len(word) <= 1:
            return word
        pos = rd.randrange(len(word) - 1)
        error = word[:pos] + word[pos + 1] + word[pos] + word[pos + 2:]
        return error

    def cap(self, word):
        return [self.noiser.vocab.bos] * self.n + list(word) + [self.noiser.vocab.eos] * self.n

    def insert(self, word):
        pos = rd.randrange(len(word) + 1)
        capped = self.cap(word)
        src = capped[pos : pos + self.n] + capped[pos + self.n : pos + self.n * 2]
        pred = self.noiser(src)
        return word[:pos] + pred + word[pos:]

    def replace(self, word):
        if len(word) <= 0:
            return word
        pos = rd.randrange(len(word))
        capped = self.cap(word)
        src = capped[pos : pos + self.n] + capped[pos + self.n + 1 : pos + self.n * 2 + 1]
        trg = capped[pos + self.n]
        pred = self.noiser(src, trg = trg)
        return word[:pos] + pred + word[pos + 1:]

    def __call__(self, word):
        for _ in range(self.num_edit_sampler()):
            sampler = self.operation_sampler()
            word = sampler(word)
        return word

