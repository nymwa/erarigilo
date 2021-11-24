from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory)

from .subj import SubjRule
from .pobj import PobjRule
from .dobj import DobjRule
from .obj import ObjRule
from .dative import DativeRule
from .poss import PossRule

from .reflexive import ReflexiveRule
from .appos_reflexive import ApposReflexiveRule
from .pobj_reflexive import PobjReflexiveRule

register(TokenWiseModuleFactory(SubjRule))
register(TokenWiseModuleFactory(PobjRule))
register(TokenWiseModuleFactory(DobjRule))
register(TokenWiseModuleFactory(ObjRule))
register(TokenWiseModuleFactory(DativeRule))
register(TokenWiseModuleFactory(PossRule))

register(TokenWiseModuleFactory(ReflexiveRule))
register(TokenWiseModuleFactory(ApposReflexiveRule))
register(TokenWiseModuleFactory(PobjReflexiveRule))

