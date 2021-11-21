from erarigilo.module.factory import (
        register,
        TokenWiseModuleFactory,
        IndexWiseModuleFactory)

from .prep_standard import StandardPrepRule
from .prep_from import PrepFromRule
from .prep_into import PrepIntoRule
from .prep_among import PrepAmongRule
from .prep_amongst import PrepAmongstRule
from .prep_amid import PrepAmidRule
from .prep_amidst import PrepAmidstRule
from .prep_about import PrepAboutRule
from .prep_against import PrepAgainstRule
from .prep_by import PrepByRule
from .prep_since import PrepSinceRule
from .prep_until import PrepUntilRule
from .prep_till import PrepTillRule
from .prep_between import PrepBetweenRule
from .prep_during import PrepDuringRule
from .prep_within import PrepWithinRule
from .prep_after import PrepAfterRule
from .prep_before import PrepBeforeRule
from .prep_as import PrepAsRule
from .prep_like import PrepLikeRule
from .prep_than import PrepThanRule
from .prep_through import PrepThroughRule
from .prep_throughout import PrepThroughoutRule
from .prep_above import PrepAboveRule
from .prep_behind import PrepBehindRule
from .prep_below import PrepBelowRule
from .prep_beyond import PrepBeyondRule
from .prep_over import PrepOverRule
from .prep_across import PrepAcrossRule
from .prep_under import PrepUnderRule
from .prep_upon import PrepUponRule
from .prep_out import PrepOutRule
from .prep_toward import PrepTowardRule

from .mark_standard import StandardMarkRule
from .mark_for import MarkForRule

from .agent_by import AgentByRule
from .agent_between import AgentBetweenRule

from .pcomp_of import PcompOfRule
from .pcomp_to import PcompToRule
from .pcomp_on import PcompOnRule
from .pcomp_for import PcompForRule
from .pcomp_at import PcompAtRule
from .pcomp_by import PcompByRule

from .dative_to import DativeToRule
from .dative_for import DativeForRule

from .advmod_prep import AdvmodRule

from .ins_prep import InsPrepRule

register(TokenWiseModuleFactory(StandardPrepRule))
register(TokenWiseModuleFactory(PrepFromRule))
register(TokenWiseModuleFactory(PrepIntoRule))
register(TokenWiseModuleFactory(PrepAmongRule))
register(TokenWiseModuleFactory(PrepAmongstRule))
register(TokenWiseModuleFactory(PrepAmidRule))
register(TokenWiseModuleFactory(PrepAmidstRule))
register(TokenWiseModuleFactory(PrepAboutRule))
register(TokenWiseModuleFactory(PrepAgainstRule))
register(TokenWiseModuleFactory(PrepByRule))
register(TokenWiseModuleFactory(PrepSinceRule))
register(TokenWiseModuleFactory(PrepUntilRule))
register(TokenWiseModuleFactory(PrepTillRule))
register(TokenWiseModuleFactory(PrepBetweenRule))
register(TokenWiseModuleFactory(PrepDuringRule))
register(TokenWiseModuleFactory(PrepWithinRule))
register(TokenWiseModuleFactory(PrepAfterRule))
register(TokenWiseModuleFactory(PrepBeforeRule))
register(TokenWiseModuleFactory(PrepAsRule))
register(TokenWiseModuleFactory(PrepLikeRule))
register(TokenWiseModuleFactory(PrepThanRule))
register(TokenWiseModuleFactory(PrepThroughRule))
register(TokenWiseModuleFactory(PrepThroughoutRule))
register(TokenWiseModuleFactory(PrepAboveRule))
register(TokenWiseModuleFactory(PrepBehindRule))
register(TokenWiseModuleFactory(PrepBelowRule))
register(TokenWiseModuleFactory(PrepBeyondRule))
register(TokenWiseModuleFactory(PrepOverRule))
register(TokenWiseModuleFactory(PrepAcrossRule))
register(TokenWiseModuleFactory(PrepUnderRule))
register(TokenWiseModuleFactory(PrepUponRule))
register(TokenWiseModuleFactory(PrepOutRule))
register(TokenWiseModuleFactory(PrepTowardRule))

register(TokenWiseModuleFactory(StandardMarkRule))
register(TokenWiseModuleFactory(MarkForRule))

register(TokenWiseModuleFactory(AgentByRule))
register(TokenWiseModuleFactory(AgentBetweenRule))

register(TokenWiseModuleFactory(PcompOfRule))
register(TokenWiseModuleFactory(PcompToRule))
register(TokenWiseModuleFactory(PcompOnRule))
register(TokenWiseModuleFactory(PcompForRule))
register(TokenWiseModuleFactory(PcompAtRule))
register(TokenWiseModuleFactory(PcompByRule))

register(TokenWiseModuleFactory(DativeToRule))
register(TokenWiseModuleFactory(DativeForRule))

register(TokenWiseModuleFactory(AdvmodRule))

register(IndexWiseModuleFactory(InsPrepRule))

