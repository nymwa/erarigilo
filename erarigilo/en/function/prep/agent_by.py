from .rule import AgentCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class AgentByRule(
        TrgEqCondRule,
        AgentCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'agent_by'

    def __init__(self):
        super().__init__(['', 'of', 'from', 'with', 'on'])
        self.target_word = 'by'

