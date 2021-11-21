import sys
from erarigilo.en.util.sent import EnSent
from .util.form import (
        decode,
        form_src,
        form_trg)

def en_form(capitalize = False):
    for sent in sys.stdin:
        sent = decode(sent)

        src = form_src(sent, capitalize = capitalize)

        if sent.trg is None:
            trg = form_trg(sent)
        else:
            trg = sent.trg['text']

        out = src + '\t' + trg
        print(out)

