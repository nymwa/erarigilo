import random as rd
from nltk.corpus import wordnet as wn
from erarigilo.module.rule import Rule

def synsets(word):
    synonym_set = {
            synonym
            for synset in wn.synsets(word)
            for synonym in synset.lemma_names()
            if synonym.isalpha()}
    synonym_set = synonym_set - {word}
    return synonym_set


class SynonymRule(Rule):

    name = 'synonym'
    tag_set = {
            'JJ',
            'JJR',
            'JJS',
            'NN',
            'NNS',
            'RB',
            'RBR',
            'RBS',
            'VB',
            'VBD',
            'VBG',
            'VBN',
            'VBP',
            'VBZ'}

    def cond(self, token):
        return token.tag in self.tag_set

    def __call__(self, token):
        word = token.word()
        synonyms = synsets(word)

        if len(synonyms) > 0:
            error = rd.choice(list(synonyms))
            if word.istitle():
                error = error.title()
            token.src = error
            token = self.add_history(token)
        return token

