import sys
import json
from .util.form import form_src, form_trg

def en_form():
    for sent in sys.stdin:
        sent = sent.strip()
        sent = json.loads(sent)
        sent = EnSent.decode(sent, token_class = EnToken)

        src = form_src(sent)

        if sent.trg is None:
            trg = form_trg(sent)
        else:
            trg = sent.trg['text']

        out = src + '\t' + trg
        print(out)

