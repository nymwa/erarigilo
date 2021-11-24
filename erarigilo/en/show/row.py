def o_or_x(p):
    return 'o' if p else 'x'


def blank(x):
    return x if x is not None else '____'


def add_color(x):
    return '\033[31m' + x + '\033[0m'


class Row:

    def __init__(self, cond, token):

        self.token = token
        self.left_space = o_or_x(token.left_space)
        self.right_space = o_or_x(token.right_space)
        self.src = blank(token.src)
        self.trg = blank(token.trg)
        self.tag = blank(token.tag)
        self.pos = blank(token.pos)
        self.dep = blank(token.dep)
        self.lem = blank(token.lemma)
        self.nrm = blank(token.norm)
        self.ent_type = blank(token.ent_type)
        self.ent_iob = blank(token.ent_iob)

        if len(token.history) > 0:
            self.history = ' '.join(['!' + x for x in token.history])
        else:
            self.history = '____'

        if cond.color:
            if (token.trg is not None) and (token.trg == cond.trg):
                self.trg = add_color(self.trg)
            if (token.tag is not None) and (token.tag == cond.tag):
                self.tag = add_color(self.tag)
            if (token.pos is not None) and (token.pos == cond.pos):
                self.pos = add_color(self.pos)
            if (token.dep is not None) and (token.dep == cond.dep):
                self.dep = add_color(self.dep)

        if (not cond.is_free()) and cond.is_ok(token):
            self.p = '*'
        else:
            self.p = ' '

    def __call__(self):
        return (
            str(self.token.index),
            str(self.token.shift),
            self.src,
            self.trg,
            self.p,
            self.left_space,
            self.right_space,
            '_' + self.tag,
            '_' + self.pos,
            '_' + self.dep,
            self.lem,
            self.nrm,
            '_' + self.ent_type,
            '_' + self.ent_iob,
            self.history)

