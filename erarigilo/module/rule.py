from erarigilo.util.sampler import ChoiceSampler

class Rule:

    def __init__(self, name):
        self.name = name

    def add_history(self, token):
        token.history.append(self.name)
        for additional_token is token.addition:
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
            error = error.title()
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


class WordConditionableRule:

    def word_cond(self, token):
        raise NotImplementedError


class ChoiceSampleableRule(SamplableRule):

    def __init__(self, name, choice_list, p = None, buffer_size = None):
        super().__init__(name)
        self.sampler = ChoiceSampler(choice_list, p = p, buffer_size = buffer_size)


class WordConditionedChoiceSamplableRule(WordConditionableRule, ChoiceSampleableRule):

    def __init__(self, name, choice_list, word_cond, p = None, buffer_size = None):
        super().__init__(name, choice_list, p = p, buffer_size = buffer_size)
        self.word_cond = word_cond


class ReplacableRule:

    def __init__(self, name, target):
        super().__init__(name)
        self.target = target


class WordConditionedReplacableRule(ReplacableRule):

    def __init__(self, name, target, word_cond):
        super().__init__(name, target)
        self.word_cond = word_cond

