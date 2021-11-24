class PronCond:

    def dep_cond(self, dep):
        return True

    def cond(self, token):
        return (
            self.word_cond(token)
            and
            # O.K., i, You
            # N.G., I, YOU
            (not token.word().isupper())
            and
            (token.pos == 'PRON')
            and
            (self.dep_cond(token.dep)))


class UpperPronCond(PronCond):

    def cond(self, token):
        return (
            self.word_cond(token)
            and
            (token.pos == 'PRON')
            and
            (self.dep_cond(token.dep)))


class DepEqCond:

    def dep_cond(self, dep):
        return dep == self.target_dep_label


class DepInCond:

    def dep_cond(self, dep):
        return dep in self.target_dep_set

