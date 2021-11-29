from erarigilo.module.rule import TokenWiseRule
from erarigilo.module.module import TokenWiseBetaModule
from erarigilo.module.factory import Factory
from .maker import SpellErrorMaker

class SpellRule(TokenWiseRule):

    name = 'spell'

    def __init__(self, char_prob, n, score_path, temp):
        super().__init__()
        self.maker = SpellErrorMaker(char_prob, n, score_path, temp)

    def cond(self, token):
        word = token.word()
        return all(char in self.maker.noiser.vocab for char in word)

    def make_error(self, token):
        word = token.word()
        error = self.maker(word)
        return error


class SpellFactory(Factory):

    name = SpellRule.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        char_prob = dct.get('char_prob', 0.9)
        n = dct.get('n', 2)
        score_path = self.replace_environment_variable(dct['score_path'])
        temp = dct.get('temp', 2.0)
        rule = SpellRule(char_prob, n, score_path, temp)
        module = TokenWiseBetaModule(mean, std, rule)
        return module

