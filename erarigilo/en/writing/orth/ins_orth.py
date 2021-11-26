from erarigilo.module.rule import TokenWiseRule
from erarigilo.module.module import TokenWiseBetaModule
from erarigilo.module.factory import Factory
from ortobruilo.ortobruilo import OrtoBruilo

class InsOrthRule(TokenWiseRule):

    name = 'ins_orth'

    def __init__(self, dict_path, penalty):
        super().__init__()
        self.noiser = OrtoBruilo(dict_path, penalty)

    def cond(self, token):
        return True

    def make_error(self, token):
        word = token.word()
        error = self.noiser(word)
        if error == word:
            error = None
        return error


class InsOrthFactory(Factory):

    name = InsOrthRule.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        penalty = dct.get('penalty', 0.8)
        dict_path = self.replace_environment_variable(dct['dict_path'])
        rule = InsOrthRule(dict_path, penalty)
        module = TokenWiseBetaModule(mean, std, rule)
        return module

