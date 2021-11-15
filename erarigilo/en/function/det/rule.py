class DetCond:

    def cond(self, token):
        return self.word_cond(token) and (token.tag == 'DT')

class DetPlusCond:

    def cond(self, token):
        return self.word_cond(token) and (token.tag == 'DT') and self.plus_cond(token)

