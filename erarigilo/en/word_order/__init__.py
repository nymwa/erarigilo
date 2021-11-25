from erarigilo.module.factory import register

from .adv_wo import AdvWOFactory
from .an_wo import ANWOFactory
from .of_wo import OfWOFactory
from .pp_wo import PPWOFactory
from .wh_wo import WhWOFactory
from .norm_wo import NormWOFactory

register(AdvWOFactory())
register(ANWOFactory())
register(OfWOFactory())
register(PPWOFactory())
register(WhWOFactory())
register(NormWOFactory())

