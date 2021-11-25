from erarigilo.util.sampler import (
        BetaSampler,
        NormalSampler)
from erarigilo.module.rule import Rule
from erarigilo.module.module import Module
from erarigilo.module.factory import Factory

class NormWORule(Rule):

    name = 'norm_wo'

    def __init__(self, loc, scale):
        super().__init__()
        self.sampler = NormalSampler(loc, scale)

    def __call__(self, ratio, token):
        token.shift += (ratio * self.sampler())
        token = self.add_history(token)
        return token


class NormWOModule(Module):

    def __init__(self, mean, std, rule):
        super().__init__(rule)
        self.beta_sampler = BetaSampler(mean, std)

    def __call__(self, sent):
        ratio = self.beta_sampler()
        for i in range(len(sent)):
            sent[i] = self.rule(ratio, sent[i])
        sent.history.append({'name' : self.rule.name, 'ratio' : round(ratio, 2)})
        return sent


class NormWOFactory(Factory):

    name = NormWORule.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        loc = dct.get('loc', 0.0)
        scale = dct.get('scale', 0.5)
        rule = NormWORule(loc, scale)
        module = NormWOModule(mean, std, rule)
        return module

