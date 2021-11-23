class PlainWordCond:

    def cond(self, token):
        return self.word_cond(token)


class PlusWordCond:

    def cond(self, token):
        return self.word_cond(token) and self.plus_cond(token)


class WordEqCondRule:

    def word_cond(self, token):
        return token.word().lower() == self.target_word


class WordInCondRule:

    def word_cond(self, token):
        return token.word().lower() in self.target_set


class TrgEqCondRule:

    def word_cond(self, token):
        return token.lower == self.target_word


class TrgInCondRule:

    def word_cond(self, token):
        return token.lower in self.target_set

