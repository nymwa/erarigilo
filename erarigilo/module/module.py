from erarigilo.util.sampler import (
        UniformSampler,
        BetaSampler)
from .applier import (
        TokenWiseApplier,
        IndexWiseApplier,
        SpanWiseApplier)

class Module:

    def __init__(self, rule):
        self.rule = rule

    def __call__(self, sent):
        sent = self.noise(sent)
        sent.history.append({'name' : self.mistaker.name})
        return sent


class BetaModule(Module):

    def __init__(self, mean, std, rule):
        super().__init__(rule)
        self.uniform_sampler = UniformSampler()
        self.beta_sampler = BetaSampler(mean, std)

    def get_threshold(self):
        threshold = self.beta_sampler()
        return threshold

    def __call__(self, sent):
        threshold = self.get_threshold()
        lottery = lambda : self.uniform_sampler() < threshold
        sent = self.apply(sent, lottery)
        sent.history.append({
            'name' : self.mistaker.name,
            'threshold' : round(threshold, 2)})
        return sent


class TokenWiseBetaModule(TokenWiseApplier, BetaModule):
    pass


class IndexWiseBetaModule(IndexWiseApplier, BetaModule):
    pass


class SpanWiseBetaModule(SpanWiseApplier, BetaModule):
    pass

