from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory)

from .int_how import HowRule
from .int_that import ThatRule
from .int_what import WhatRule
from .int_whatever import WhateverRule
from .int_when import WhenRule
from .int_whenever import WheneverRule
from .int_whence import WhenceRule
from .int_where import WhereRule
from .int_wherever import WhereverRule
from .int_whether import WhetherRule
from .int_which import WhichRule
from .int_whichever import WhicheverRule
from .int_whither import WhitherRule
from .int_who import WhoRule
from .int_whoever import WhoeverRule
from .int_whose import WhoseRule
from .int_why import WhyRule

register(TokenWiseModuleFactory(HowRule))
register(TokenWiseModuleFactory(ThatRule))
register(TokenWiseModuleFactory(WhatRule))
register(TokenWiseModuleFactory(WhateverRule))
register(TokenWiseModuleFactory(WhenRule))
register(TokenWiseModuleFactory(WheneverRule))
register(TokenWiseModuleFactory(WhenceRule))
register(TokenWiseModuleFactory(WhereRule))
register(TokenWiseModuleFactory(WhereverRule))
register(TokenWiseModuleFactory(WhetherRule))
register(TokenWiseModuleFactory(WhichRule))
register(TokenWiseModuleFactory(WhicheverRule))
register(TokenWiseModuleFactory(WhitherRule))
register(TokenWiseModuleFactory(WhoRule))
register(TokenWiseModuleFactory(WhoeverRule))
register(TokenWiseModuleFactory(WhoseRule))
register(TokenWiseModuleFactory(WhyRule))

