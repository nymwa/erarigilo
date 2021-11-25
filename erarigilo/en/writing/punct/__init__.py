from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory,
        IndexWiseModuleFactory)

from .comma import CommaRule
from .ins_left_comma import InsLeftCommaRule
from .ins_right_comma import InsRightCommaRule
from .period import PeriodRule
from .hyphen import HyphenRule
from .two_hyphens import TwoHyphensRule
from .ins_hyphen import InsHyphenRule
from .quot import QuotRule
from .colon import ColonRule
from .semicolon import SemicolonRule
from .hatena import HatenaRule
from .bang import BangRule

register(TokenWiseModuleFactory(CommaRule))
register(IndexWiseModuleFactory(InsLeftCommaRule))
register(IndexWiseModuleFactory(InsRightCommaRule))
register(TokenWiseModuleFactory(PeriodRule))
register(TokenWiseModuleFactory(HyphenRule))
register(TokenWiseModuleFactory(TwoHyphensRule))
register(IndexWiseModuleFactory(InsHyphenRule))
register(TokenWiseModuleFactory(QuotRule))
register(TokenWiseModuleFactory(ColonRule))
register(TokenWiseModuleFactory(SemicolonRule))
register(TokenWiseModuleFactory(HatenaRule))
register(TokenWiseModuleFactory(BangRule))

