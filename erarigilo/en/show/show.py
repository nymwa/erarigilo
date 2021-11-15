import sys
import json
from erarigilo.en.util.token import EnToken
from erarigilo.en.util.sent import EnSent
from erarigilo.en.util.form import form_src, form_trg
from .conds import Conds
from .table import Table

def decode(sent):
    sent = sent.strip()
    sent = json.loads(sent)
    sent = EnSent.decode(sent, token_class = EnToken)
    return sent


def show_sents(sent):
    if sent.trg is None:
        print('src: ' + form_src(sent))
        print('trg: ' + form_trg(sent))
    else:
        print('src    : ' + form_src(sent))
        print('rtt({}): '.format(sent.trg['bridge']) + form_trg(sent))
        print('trg    : ' + sent.trg['text'])


def show_history(sent):
    history = []
    for record in sent.history:
        if 'threshold' in record:
            if 'char_threshold' in record:
                desc = '{}({}, {})'.format(
                        record['name'],
                        record['threshold'],
                        record['char_threshold'])
            else:
                desc = '{}({})'.format(
                        record['name'],
                        record['threshold'])
        elif 'ratio' in record:
            desc = '{}<{}>'.format(
                    record['name'],
                    record['ratio'])
        else:
            desc = '{}'.format(
                    record['name'])
        history.append(desc)
    history_len = len(history)
    print(f'history ({history_len}): ' + ' '.join(history))


def en_show(
        hide_history = False,
        color = False,
        cor = None,
        tag = None,
        pos = None,
        dep = None,
        remove_identical = False):

    cond = Conds(color, cor, tag, pos, dep)

    for sent in sys.stdin:
        sent = decode(sent)
        if cond.check(sent):
            show_sents(sent)
            if not hide_history:
                show_history(sent)
            tab = Table(cond, sent)
            print(tab())

