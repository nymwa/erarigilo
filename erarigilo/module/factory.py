import os
from .module import (
        TokenWiseBetaModule,
        IndexWiseBetaModule,
        SpanWiseBetaModule)

registory = {}

def register(factory):
    name = factory.name
    assert name not in registory, name
    registory[name] = factory


class Factory:

    def __call__(self, dct):
        raise NotImplementedError

    def replace_environment_variable(self, path):
        if 'SGE_LOCALDIR' in os.environ:
            path = path.replace(
                '${SGE_LOCALDIR}',
                os.environ['SGE_LOCALDIR'])
        return path


class RuleInitFactory(Factory):

    def __init__(self, rule_class):
        self.rule_class = rule_class
        self.name = rule_class.name


class MeanStdFactory(RuleInitFactory):

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        rule = self.rule_class()
        module = self.make_module(mean, std, rule)
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

