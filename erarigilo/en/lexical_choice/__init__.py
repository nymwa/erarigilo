from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory)

from .confusion import ConfusionFactory
from .synonym import SynonymRule

register(ConfusionFactory())
register(TokenWiseModuleFactory(SynonymRule))

