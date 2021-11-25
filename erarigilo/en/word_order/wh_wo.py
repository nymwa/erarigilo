from erarigilo.util.sampler import NormalSampler
from erarigilo.module.rule import Rule
from erarigilo.module.module import BetaModule
from erarigilo.module.factory import Factory

def extract_wh(sent):
    i = 0
    wh_list = []
    for i in range(len(sent)):
        if sent[i].word().lower() in {
                'how',
                'what',
                'who',
                'which',
                'whose',
                'when',
                'where',
                'whither',
                'whence',
                'why',
                'whether'}:
            wh_list.append(i)
    return wh_list


class WhWORule(Rule):

    name = 'wh_wo'

    def __init__(self, loc, scale):
        super().__init__()
        self.sampler = NormalSampler(loc = loc, scale = scale)

    def make_error(self, sent, index):
        shift = round(self.sampler())
        if 0 <= (index + shift) < len(sent):
            sent[index].shift += shift
            for token in sent[index].addition:
                token.shift += shift
        return sent

    def __call__(self, sent, index):
        sent = self.make_error(sent, index)
        sent[index] = self.add_history(sent[index])
        return sent


class WhWOApplier:

    def apply(self, sent, lottery):
        wh_list = extract_wh(sent)
        for index in wh_list:
            if lottery():
                sent = self.rule(sent, index)
        return sent


class WhWOModule(WhWOApplier, BetaModule):

    pass


class WhWOFactory(Factory):

    name = WhWORule.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        loc = dct.get('loc', 1.5)
        scale = dct.get('scale', 1.0)
        rule = WhWORule(loc, scale)
        module = WhWOModule(mean, std, rule)
        return module

