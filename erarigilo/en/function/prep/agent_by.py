from .rule import AgentCond
from erarigilo.en.util.rule import WordEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class AgentByRule(
        WordEqCondRule,
        AgentCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'agent_by'

    def __init__(self):
        super().__init__(['', 'of', 'from', 'with', 'on'])
        self.target_word = 'by'

