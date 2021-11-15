from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory,
        IndexWiseModuleFactory)

from .article import ArticleRule
from .demonstrative import DemonstrativeRule
from .demonstrative_extra import DemonstrativeExtraRule
from .det_no import NoRule
from .det_any import AnyRule
from .det_some import SomeRule
from .det_all import AllRule
from .det_both import BothRule
from .det_each import EachRule
from .det_every import EveryRule
from .ins_det import InsDetRule
from .so import SoRule
from .such import SuchRule
from .another import AnotherRule
from .other import OtherRule
from .there import ThereRule
from .here import HereRule

register(TokenWiseModuleFactory(ArticleRule))
register(TokenWiseModuleFactory(DemonstrativeRule))
register(TokenWiseModuleFactory(DemonstrativeExtraRule))
register(TokenWiseModuleFactory(NoRule))
register(TokenWiseModuleFactory(AnyRule))
register(TokenWiseModuleFactory(SomeRule))
register(TokenWiseModuleFactory(AllRule))
register(TokenWiseModuleFactory(BothRule))
register(TokenWiseModuleFactory(EachRule))
register(TokenWiseModuleFactory(EveryRule))
register(IndexWiseModuleFactory(InsDetRule))

register(TokenWiseModuleFactory(SoRule))
register(TokenWiseModuleFactory(SuchRule))
register(TokenWiseModuleFactory(AnotherRule))
register(TokenWiseModuleFactory(OtherRule))
register(TokenWiseModuleFactory(ThereRule))
register(TokenWiseModuleFactory(HereRule))

