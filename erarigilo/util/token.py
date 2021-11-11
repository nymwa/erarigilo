class Token:

    def __init__(self,
            index,
            shift = 0,
            src = None,
            trg = None,
            addition = None,
            history = None):

        self.index = index
        self.shift = shift
        self.src = src
        self.trg = trg

        if addition is None:
            self.addition = []
        else:
            self.addition = addition

        if history is None:
            self.history = []
        else:
            self.history = history

    def word(self):
        if self.src is not None:
            word = self.src
        else:
            word = self.trg
        return word

    def encode(self):
        dct = {
                'i': self.index,
                'shift': self.shift,
                'src': self.src,
                'trg': self.trg,
                'addition': [token.encode() for token in self.addition],
                'history': self.history,
                }
        return dct

    @classmethod
    def decode(cls, dct):
        index = dct['i']
        shift = dct['shift']
        src = dct['src']
        trg = dct['trg']
        addition = [cls.decode(x) for x in dct['addition']]
        history = dct['history']

        token = cls(
            index,
            shift = shift,
            src = src,
            trg = trg,
            addition = addition,
            history = history)
        return token

