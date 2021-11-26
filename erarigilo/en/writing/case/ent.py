from erarigilo.module.rule import SpanWiseRule
from erarigilo.module.module import SpanWiseBetaModule
from erarigilo.module.factory import Factory
from erarigilo.util.sampler import UniformSampler

def extract_ent_span(sent):
    i = 0
    span_list = []
    while i < len(sent):
        if sent[i].ent_iob == 'B':
            span = [i]
            i += 1
            while i < len(sent) and sent[i].ent_iob == 'I':
                span.append(i)
                i += 1
            span_list.append(span)
        else:
            i += 1
    return span_list


class EntRule(SpanWiseRule):

    name = 'ent'

    def __init__(self, ratio, threshold):
        super().__init__()
        self.sampler = UniformSampler()
        self.ratio = ratio
        self.threshold = threshold

    def random_char_uncase(self, char):
        if (self.sampler() < self.threshold):
            char = char.lower()
        return char

    def random_uncase(self, word):
        return ''.join([
            self.random_char_uncase(char)
            for char in word])

    def extract_span(self, sent):
        return extract_ent_span(sent)

    def make_error(self, sent, span):
        cond = (self.sampler() < self.ratio)
        for i in span:
            word = sent[i].word()
            if (not word.islower()) and (not word.isdigit()) and word.isalnum():
                if cond:
                    error = self.random_uncase(word)
                else:
                    error = word.lower()
                if word != error:
                    sent[i].src = error
        return sent


class EntFactory(Factory):

    name = EntRule.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        ratio = dct.get('ratio', 0.2)
        threshold = dct.get('threshold', 0.5)
        rule = EntRule(ratio, threshold)
        module = SpanWiseBetaModule(mean, std, rule)
        return module

