import random as rd
from erarigilo.util.sampler import NormalSampler
from erarigilo.module.rule import Rule
from erarigilo.module.module import BetaModule
from erarigilo.module.factory import Factory

def extract_adv(sent):
    i = 0
    wh_list = []
    for i in range(len(sent)):
        if sent[i].pos == 'ADV':
            wh_list.append(i)
    return wh_list


class AdvWORule(Rule):

    name = 'adv_wo'

    def __init__(self, scale):
        super().__init__()
        self.sampler = NormalSampler(loc = 0.0, scale = scale)

    def make_error(self, sent, index):
        shift = round(self.sampler())
        if 0 <= index + shift < len(sent):
            sent[index].shift += shift
            for token in sent[index].addition:
                token.shift += shift
        return sent

    def __call__(self, sent, index):
        sent = self.make_error(sent, index)
        sent[index] = self.add_history(sent[index])
        return sent


class AdvWOApplier:

    def apply(self, sent, lottery):
        adv_list = extract_adv(sent)
        for index in adv_list:
            if lottery():
                sent = self.rule(sent, index)
        return sent


class AdvWOModule(AdvWOApplier, BetaModule):

    pass


class AdvWOFactory(Factory):

    name = AdvWORule.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        scale = dct.get('scale', 1.5)
        rule = AdvWORule(scale)
        module = AdvWOModule(mean, std, rule)
        return module

