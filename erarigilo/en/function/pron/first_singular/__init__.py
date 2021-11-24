from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory)

from .subj import SubjRule
from .obj import ObjRule
from .dobj import DobjRule
from .pobj import PobjRule
from .dative import DativeRule
from .poss import PossRule
from .poss_det import PossDetRule

from .reflexive import ReflexiveRule
from .appos_reflexive import ApposReflexiveRule
from .pobj_reflexive import PobjReflexiveRule

register(TokenWiseModuleFactory(SubjRule))
register(TokenWiseModuleFactory(ObjRule))
register(TokenWiseModuleFactory(DobjRule))
register(TokenWiseModuleFactory(PobjRule))
register(TokenWiseModuleFactory(DativeRule))
register(TokenWiseModuleFactory(PossRule))
register(TokenWiseModuleFactory(PossDetRule))

register(TokenWiseModuleFactory(ReflexiveRule))
register(TokenWiseModuleFactory(ApposReflexiveRule))
register(TokenWiseModuleFactory(PobjReflexiveRule))

