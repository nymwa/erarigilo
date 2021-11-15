class INCond:

    def cond(self, token):
        return (
            self.word_cond(token)
            and
            (not token.word().isupper())
            and
            (token.tag == 'IN')
            and
            (self.dep_cond(token.dep)))


class PrepCond(INCond):

    def dep_cond(self, dep):
        return dep in {'prep', 'ROOT', 'conj'}


class MarkCond(INCond):

    def dep_cond(self, dep):
        return dep == 'mark'


class AgentCond(INCond):

    def dep_cond(self, dep):
        return dep == 'agent'


class PcompCond(INCond):

    def dep_cond(self, dep):
        return dep == 'pcomp'


class DativeCond(INCond):

    def dep_cond(self, dep):
        return dep == 'dative'


class AdvmodCond(INCond):

    def dep_cond(self, dep):
        return dep == 'advmod'

