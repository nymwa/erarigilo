import random as rd
from erarigilo.util.sampler import UniformSampler
from erarigilo.module.rule import Rule
from erarigilo.module.module import BetaModule
from erarigilo.module.factory import Factory

class AN:

    def __init__(self, a_list, n_list):
        self.a_list = a_list
        self.n_list = n_list

    def check(self, sent):
        for i in self.a_list + self.n_list:
            if not sent[i].word().isalnum():
                return False
        return True


def extract_an(sent):
    i = 0
    an_list = []
    while i < len(sent):
        if sent[i].tag in {'JJ', 'JJR', 'JJS', 'CD'}:
            a_list = [i]
            i += 1
            while i < len(sent) and sent[i].tag in {'JJ', 'JJR', 'JJS', 'CD'}:
                a_list.append(i)
                i += 1
            n_list = []
            while i < len(sent) and sent[i].tag in {'NN', 'NNS'}:
                n_list.append(i)
                i += 1
            an = AN(a_list, n_list)
            if an.check(sent):
                an_list.append(an)
        i += 1
    return an_list


class ANWORule(Rule):

    name = 'an_wo'

    def __init__(self, ratio):
        super().__init__()
        self.ratio = ratio
        self.sampler = UniformSampler()

    def make_error(self, sent, a_list, n_list, prop):
        a_shift = a_list.copy()
        n_shift = [0 for _ in n_list]
        rd.shuffle(a_shift)
        a_shift = [x - y for x, y in zip(a_shift, a_list)]
        if prop:
            a_shift = [x + len(n_list) for x in a_shift]
            n_shift = [x - len(a_list) for x in n_shift]
        for i, shift in zip(a_list + n_list, a_shift + n_shift):
            sent[i].shift += shift
            for token in sent[i].addition:
                token.shift += shift
        return sent

    def __call__(self, sent, a_list, n_list):
        prop = self.sampler() < self.ratio
        sent = self.make_error(sent, a_list, n_list, prop)
        for index in a_list + n_list:
            sent[index] = self.add_history(sent[index])
        return sent


class ANWOApplier:

    def apply(self, sent, lottery):
        an_list = extract_an(sent)
        for an in an_list:
            if lottery():
                sent = self.rule(sent, an.a_list, an.n_list)
        return sent


class ANWOModule(ANWOApplier, BetaModule):

    pass


class ANWOFactory(Factory):

    name = ANWORule.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        ratio = dct.get('ratio', 0.10)
        rule = ANWORule(ratio)
        module = ANWOModule(mean, std, rule)
        return module

