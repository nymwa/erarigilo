class Conds:

    def __init__(self,
            color = None,
            trg = None,
            tag = None,
            pos = None,
            dep = None,
            remove_identical = False):

        self.color = color
        self.trg = trg
        self.tag = tag
        self.pos = pos
        self.dep = dep
        self.remove_identical = remove_identical

    def is_free(self):
        return ((self.trg is None)
            and (self.tag is None)
            and (self.pos is None)
            and (self.dep is None))

    def is_ok(self, token):
        return (((self.trg is None) or (self.trg == token.trg))
            and ((self.tag is None) or (self.tag == token.tag))
            and ((self.pos is None) or (self.pos == token.pos))
            and ((self.dep is None) or (self.dep == token.dep)))

    def check(self, sent):
        if (self.remove_identical
                and all(len(token.history) == 0 for token in sent)):
            return False
        if self.is_free():
            return True
        return any(self.is_ok(token) for token in sent)

