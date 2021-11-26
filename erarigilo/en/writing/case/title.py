from erarigilo.module.rule import TokenWiseRule

class TitleRule(TokenWiseRule):

    name = 'title'

    def cond(self, token):
        word = token.word()
        return (
            word.islower()
            and
            (not word.isdigit())
            and
            word.isalnum())

    def make_error(self, token):
        return token.word().capitalize()

