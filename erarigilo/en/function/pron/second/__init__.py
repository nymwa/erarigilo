from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory)

from .subj import SubjRule
from .pobj import PobjRule
from .dobj import DobjRule
from .dative import DativeRule
from .poss import PossRule
from .poss_det import PossDetRule

register(TokenWiseModuleFactory(SubjRule))
register(TokenWiseModuleFactory(PobjRule))
register(TokenWiseModuleFactory(DobjRule))
register(TokenWiseModuleFactory(ObjRule))
register(TokenWiseModuleFactory(DativeRule))
register(TokenWiseModuleFactory(PossRule))
register(TokenWiseModuleFactory(PossDetRule))

