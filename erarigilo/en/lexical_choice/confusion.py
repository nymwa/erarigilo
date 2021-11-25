import pickle
import random as rd
from erarigilo.module.rule import Rule
from erarigilo.module.module import TokenWiseBetaModule
from erarigilo.module.factory import Factory

class ConfusionRule(Rule):

    name = 'confusion'

    def __init__(self, model_path):
        super().__init__()
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def cond(self, token):
        return token.tag in {
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

    def __call__(self, token):
        word = token.word()
        if (word in self.model) and (len(self.model[word]) > 0):
            error = rd.choice(self.model[word])
            if word.istitle():
                error = error.title()
            token.src = error
            token = self.add_history(token)
        return token


class ConfusionFactory(Factory):

    def __init__(self):
        super().__init__()
        self.name = ConfusionRule.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        model_path = self.replace_environment_variable(dct['model_path'])
        rule = ConfusionRule(model_path)
        module = TokenWiseBetaModule(mean, std, rule)
        return module

