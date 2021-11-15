from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory)

from .conj import *
from .det import *
from .inter import *
from .prep import *

from .auxpass import AuxpassRule
from .contr import ContrFactory
from .part import PartRule
from .to import ToRule

register(TokenWiseModuleFactory(AuxpassRule))
register(ContrFactory())
register(TokenWiseModuleFactory(PartRule))
register(TokenWiseModuleFactory(ToRule))

