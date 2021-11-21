from erarigilo.util.sampler import ChoiceSampler

class Rule:

    def add_history(self, token):
        token.history.append(self.name)
        for additional_token in token.addition:
            additional_token.history.append(self.name)
        return token


class TokenWiseRule(Rule):

    def check(self, token, error):
        return token.word() != error

    def preprocess(self, token, error):
        return error

    def __call__(self, token):
        error = self.make_error(token)
        if (error is not None) and self.check(token, error):
            error = self.preprocess(token, error)
            token.src = error
            token = self.add_history(token)
        return token


class TokenWiseRuleCaseFitted:

    def check(self, token, error):
        return token.word().lower() != error.lower()

    def preprocess(self, token, error):
        if token.word().istitle():
            # N.G.: error.title()
            #       'the other' -> 'The Other'
            # O.K.: error.capitalize()
            #       'the other' -> 'The other'
            error = error.capitalize()
        return error


class IndexWiseRule(Rule):

    def __call__(self, sent, index):
        sent = self.make_error(sent, index)
        sent[index] = self.add_history(sent[index])
        return sent


class SpanWiseRule(Rule):

    def __call__(self, sent, span):
        sent = self.make_error(sent, span)
        for index in span:
            sent[index] = self.add_history(sent[index])
        return sent


class SamplableRule:

    def make_error(self, token):
        return self.sampler()


class ChoiceSamplableRule(SamplableRule):

    def __init__(self, choice_list,
            p = None, buffer_size = None):

        super().__init__()
        self.sampler = ChoiceSampler(choice_list, p = p, buffer_size = buffer_size)


class DeletingRule:

    def make_error(self, token):
        return ''


class ReplacableRule:

    def __init__(self, error):
        super().__init__()
        self.error_word = error

    def make_error(self, token):
        return self.error_word

