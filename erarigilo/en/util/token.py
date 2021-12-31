from erarigilo.util.token import Token

class EnToken(Token):

    def __init__(self,
            index,
            shift = 0,
            left_space = True,
            right_space = True,
            src = None,
            trg = None,
            tag = None,
            pos = None,
            dep = None,
            lemma = None,
            norm = None,
            lower = None,
            ent_type = None,
            ent_iob = None,
            addition = None,
            history = None):

        super().__init__(
                index,
                shift,
                src,
                trg,
                addition,
                history)

        self.left_space = left_space
        self.right_space = right_space
        self.tag = tag
        self.pos = pos
        self.dep = dep
        self.lemma = lemma
        self.norm = norm

        if (lower is not None) or (trg is None):
            self.lower = lower
        else:
            self.lower = trg.lower()

        self.ent_type = ent_type
        self.ent_iob = ent_iob

    def encode(self):
        dct = super().encode()
        dct['left_space'] = self.left_space
        dct['right_space'] = self.right_space
        dct['tag'] = self.tag
        dct['pos'] = self.pos
        dct['dep'] = self.dep
        dct['lemma'] = self.lemma
        dct['norm'] = self.norm
        dct['lower'] = self.lower
        dct['ent_type'] = self.ent_type
        dct['ent_iob'] = self.ent_iob
        return dct

    @classmethod
    def decode(cls, dct):
        index = dct['i']
        shift = dct['shift']
        left_space = dct['left_space']
        right_space = dct['right_space']

        if 'src' in dct:
            src = dct['src']
        elif 'org' in dct:
            src = dct['org'] # for compatibility of arteraro
        else:
            assert False

        if 'trg' in dct:
            trg = dct['trg']
        elif 'cor' in dct:
            trg = dct['cor'] # for compatibility of arteraro
        else:
            assert False

        tag = dct['tag']
        pos = dct['pos']
        dep = dct['dep']
        lemma = dct['lemma']
        norm = dct['norm']
        lower = dct['lower']
        ent_type = dct['ent_type']
        ent_iob = dct['ent_iob']

        if 'addition' in dct:
            addition = [cls.decode(x) for x in dct['addition']]
        else:
            addition = None

        history = dct['history']

        token = cls(
            index,
            shift = shift,
            left_space = left_space,
            right_space = right_space,
            src = src,
            trg = trg,
            tag = tag,
            pos = pos,
            dep = dep,
            lemma = lemma,
            norm = norm,
            lower = lower,
            ent_type = ent_type,
            ent_iob = ent_iob,
            addition = addition,
            history = history)
        return token

