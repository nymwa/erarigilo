from erarigilo.module.rule import Rule
from erarigilo.module.module import TokenWiseBetaModule
from erarigilo.module.factory import Factory
from erarigilo.util.sampler import UniformSampler

quot = chr(0x2019)

class ContrRule(Rule):

    name = 'contr'

    def __init__(self, delete_ratio):
        super().__init__()
        self.delete_ratio = delete_ratio
        self.sampler = UniformSampler()

    def cond(self, token):
        word = token.word()
        return (token.pos != 'PUNCT') and ("'" in word or quot in word)

    def make_error(self, token):
        word = token.word()
        if (word not in {q + x for x in ['m', 's', 'd', 've', 're'] for q in ["'", quot]}
                or self.sampler() > self.delete_ratio):
            error = word.replace("'", '').replace(quot, '')
        else:
            error = ''
        return error

    def __call__(self, token):
        token.src = self.make_error(token)
        token.left_space = False
        token = self.add_history(token)
        return token


class ContrFactory(Factory):

    def __init__(self):
        self.rule_class = ContrRule
        self.name = self.rule_class.name

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        delete_ratio = dct.get('delete_ratio', 0.25)
        rule = self.rule_class(delete_ratio)
        module = TokenWiseBetaModule(mean, std, rule)
        return module

