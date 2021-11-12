from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory)
from .delete import Delete
from .mask import MaskFactory
register(TokenWiseModuleFactory(Delete))
register(MaskFactory())

