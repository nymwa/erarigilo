from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory)

from .reflexive import ReflexiveRule
from .appos_reflexive import ApposReflexiveRule
from .pobj_reflexive import PobjReflexiveRule

register(TokenWiseModuleFactory(ReflexiveRule))
register(TokenWiseModuleFactory(ApposReflexiveRule))
register(TokenWiseModuleFactory(PobjReflexiveRule))

