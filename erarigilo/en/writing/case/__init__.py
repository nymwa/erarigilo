from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory,
        IndexWiseModuleFactory)

from .ent import EntFactory
from .title import TitleRule
from .uncase import UncaseRule

register(EntFactory())
register(TokenWiseModuleFactory(TitleRule))
register(TokenWiseModuleFactory(UncaseRule))

