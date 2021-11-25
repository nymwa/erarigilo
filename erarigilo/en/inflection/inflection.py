from erarigilo.module.rule import Rule
import random as rd
from lemminflect import getInflection

def sample_error(tag_list, target_tag, target):
    tag_list = [source_tag for source_tag in tag_list if source_tag != target_tag]
    source_tag = rd.choice(tag_list)
    error_list = getInflection(target, source_tag)
    error = rd.choice(error_list)
    return error


def get_word(token):
    if token.src is not None:
        word = token.src
    else:
        word = token.lemma
    return word


class InflectionRule(Rule):

    def cond(self, token):
        return token.tag in self.tag_list

    def __call__(self, token):
        word = get_word(token)

        if word != '':
            error = sample_error(
                    self.tag_list,
                    token.tag,
                    word.lower())
            if word.istitle():
                error = error.title()
            token.src = error
            token = self.add_history(token)
        return token


class AdjInflectionRule(InflectionRule):

    name = 'adj_infl'
    tag_list = {'JJ', 'JJR', 'JJS'}


class NounInflectionRule(InflectionRule):

    name = 'noun_infl'
    tag_list = {'NN', 'NNS'}

