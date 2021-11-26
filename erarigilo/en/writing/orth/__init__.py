from erarigilo.module.factory import (
        register,
        IndexWiseModuleFactory)

from .del_orth import DelOrthRule
from .ins_orth import InsOrthFactory

register(IndexWiseModuleFactory(DelOrthRule))
register(InsOrthFactory())

