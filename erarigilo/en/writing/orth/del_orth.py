from erarigilo.module.rule import Rule

class DelOrthRule(Rule):

    name = 'del_orth'

    def cond(self, sent, index):
        return True

    def __call__(self, sent, index):
        if index < len(sent) - 1:
            left = sent[index].word()
            right = sent[index + 1].word()
            if left.isalnum() and right.isalnum():
                sent[index].right_space = ''
                sent[index] = self.add_history(sent[index])
        return sent

