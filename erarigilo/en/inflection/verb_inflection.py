from erarigilo.util.sampler import (
        UniformSampler,
        ChoiceSampler)
from erarigilo.en.util.token import EnToken
from erarigilo.module.rule import Rule
from erarigilo.module.module import IndexWiseBetaModule
from erarigilo.module.factory import Factory
import random as rd
from lemminflect import (
        getInflection,
        getAllInflections,
        getAllInflectionsOOV)

def get_word(sent, index):
    if sent[index].src is not None:
        word = sent[index].src
    else:
        word = sent[index].lemma
    return word


class VerbInflectionRule(Rule):

    name = 'verb_infl'
    tag_list = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}
    contr_haves = [q + x for x in ['ve', 's', 'd'] for q in ["'", chr(0x2019)]]
    vbg_list = contr_haves + [
            'have',
            'has',
            'had',
            'have been',
            'have be',
            'have being',
            'has been',
            'has be',
            'has being',
            'had been',
            'had be',
            'had being',
            'be',
            'am',
            'is',
            'are',
            'was',
            'were']
    vbn_list = contr_haves + [
            'have been',
            'have be',
            'have being',
            'has been',
            'has be',
            'has being',
            'had been',
            'had be',
            'had being',
            'be',
            'am',
            'is',
            'are',
            'was',
            'were']

    def __init__(self, aux_ratio):
        super().__init__()
        self.aux_ratio = aux_ratio
        self.sampler = UniformSampler()
        self.vbg_sampler = ChoiceSampler(self.vbg_list)
        self.vbn_sampler = ChoiceSampler(self.vbn_list)

    def cond(self, sent, index):
        return sent[index].tag in self.tag_list

    def make_error(self, target, target_tag):
        error = None
        if target != '':
            tag_list = [source_tag for source_tag in self.tag_list if source_tag != target_tag]
            tag = rd.choice(tag_list)
            error_list = getInflection(target, tag)
            if error_list == []:
                error_list = getAllInflectionsOOV(target, upos = 'VERB').values()
            if len(error_list) > 0:
                error = rd.choice(error_list)
        return error

    def additional_cond_1(self, sent, index):
        return index >= 1 and (sent[index - 1].pos != 'AUX')

    def additional_cond_2(self, sent, index):
        return index >= 2 and (sent[index - 2].pos != 'AUX')

    def additional_cond(self, sent, index):
        return (
            self.additional_cond_1(sent, index)
            and
            self.additional_cond_2(sent, index)
            and
            (self.sampler() < self.aux_ratio))

    def make_sent(self, sent, index, error):
        sent[index].src = error
        # 直前にAUXがないVBG,VBNに対して，その直前に"have (been)"の変化を挿入する
        if self.additional_cond(sent, index):
            target_tag = sent[index].tag
            if target_tag == 'VBG':
                sent[index].addition.append(
                        EnToken(
                            index = sent[index].index - 0.25,
                            src = self.vbg_sampler()))
            elif target_tag == 'VBN':
                sent[index].addition.append(
                        EnToken(
                            index = sent[index].index - 0.25,
                            src = self.vbn_sampler()))
        sent[index] = self.add_history(sent[index])
        return sent

    def __call__(self, sent, index):
        word = get_word(sent, index)
        error = self.make_error(
                word.lower(),
                sent[index].tag)
        if error is not None:
            if word.istitle():
                error = error.title()
            sent = self.make_sent(sent, index, error)
        return sent


class VerbInflectionFactory(Factory):

    def __init__(self):
        super().__init__()
        self.name = VerbInflectionRule.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        aux_ratio = dct.get('aux_ratio', 0.2)
        rule = VerbInflectionRule(aux_ratio)
        module = IndexWiseBetaModule(mean, std, rule)
        return module

