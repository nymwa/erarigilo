from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory)

from .inflection import (
        AdjInflectionRule,
        NounInflectionRule)
from .verb_inflection import VerbInflectionFactory

register(TokenWiseModuleFactory(AdjInflectionRule))
register(TokenWiseModuleFactory(NounInflectionRule))
register(VerbInflectionFactory())

