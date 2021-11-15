class PlainWordCond:

    def cond(self, token):
        return self.word_cond(token)


class WordEqCondRule:

    def word_cond(self, token):
        return token.word().lower() == self.target_word


class WordInCondRule:

    def word_cond(self, token):
        return token.word().lower() in self.target_set

