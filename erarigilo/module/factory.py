import os
from .module import (
        TokenWiseBetaModule,
        IndexWiseBetaModule,
        SpanWiseBetaModule)

registory = {}

def register(name):

    def _register(factory_function):
        assert name not in registory
        registory[name] = factory_function
        return factory_function

    return _register


def replace_environment_variable(path):
    if 'SGE_LOCALDIR' in os.environ:
        path = path.replace(
            '${SGE_LOCALDIR}',
            os.environ['SGE_LOCALDIR'])
    return path


class Factory:

    def __init__(self, rule_class):
        self.rule_class = rule_class


class MeanStdFactory(Factory):

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        rule = self.rule_class()
        module = make_module(mean, std, rule)
        return module


class TokenWiseModuleFactory(MeanStdFactory):

    def make_module(self, mean, std, rule):
        return TokenWiseBetaModule(mean, std, rule)


class IndexWiseModuleFactory(MeanStdFactory):

    def make_module(self, mean, std, rule):
        return IndexWiseBetaModule(mean, std, rule)


class SpanWiseModuleFactory(MeanStdFactory):

    def make_module(self, mean, std, rule):
        return SpanWiseBetaModule(mean, std, rule)


class ChoiceSamplingModuleFactory(Factory):

    def make_module(self, name, word_cond, choice_list, p, buffer_size):
        rule = self.rule_class(
                name,
                choice_list,
                word_cond = word_cond,
                p = p,
                buffer_size = buffer_size)
        return TokenWiseBetaModule(mean, std, rule)

    def __call__(self, dct, name, word_cond, choice_list, p = None):
        mean = dct['mean']
        std = dct['std']
        buffer_size = dct.get('buffer_size', None)
        return self.make_module(name, word_cond, choice_list, p, buffer_size)


class ChoiceSamplingSetCondModuleFactory(Factory):

    def __call__(self, dct, name, source_set, target):
        mean = dct['mean']
        std = dct['std']
        word_cond = lambda token : token.word().lower() in source_set
        rule = self.rule_class(name, target, word_cond)
        return TokenWiseBetaModule(mean, std, rule)

