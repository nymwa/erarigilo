from erarigilo.module.rule import TokenWiseRule

class UncaseRule(TokenWiseRule):

    name = 'uncase'

    def word_cond(self, token):
        word = token.word()
        return (
            (not word.islower())
            and
            (not word.isdigit())
            and
            word.isalnum())

    def cond(self, token):
        return (token.ent_iob == 'O') and self.word_cond(token)

    def make_error(self, token):
        return token.word().lower()

