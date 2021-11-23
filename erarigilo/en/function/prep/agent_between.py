from .rule import AgentCond
from erarigilo.en.util.rule import TrgEqCondRule
from erarigilo.module.rule import (
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule)

class AgentBetweenRule(
        TrgEqCondRule,
        AgentCond,
        ChoiceSamplableRule,
        TokenWiseRuleCaseFitted,
        TokenWiseRule):

    name = 'agent_between'

    def __init__(self):
        super().__init__([
            '', 'by', 'in', 'on', 'at', 'from', 'with',
            'about', 'among', 'amongst', 'amid', 'amidst'])
        self.target_word = 'between'

