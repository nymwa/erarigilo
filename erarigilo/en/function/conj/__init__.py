from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory)

from .conj_and import AndRule
from .conj_but import ButRule

register(TokenWiseModuleFactory(AndRule))
register(TokenWiseModuleFactory(ButRule))

