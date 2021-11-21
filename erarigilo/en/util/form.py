import json
from .token import EnToken
from .sent import EnSent

def decode(sent):
    sent = sent.strip()
    sent = json.loads(sent)
    sent = EnSent.decode(sent, token_class = EnToken)
    return sent


class Word:

    def __init__(self, index, word, left_space, right_space):
        self.index = index
        self.word = word
        self.left_space = left_space
        self.right_space = right_space

    def __lt__(self, other):
        return self.index < other.index


def make_word_list(token_list):
    word_list = []
    for token in token_list:
        if token.src is not None:
            word = token.src
        else:
            word = token.trg
        word = Word(
            token.index + token.shift,
            word,
            token.left_space,
            token.right_space)
        word_list.append(word)
    word_list.sort()
    return word_list


def remove_deleted_tokens(word_list):
    word_list = [
            word
            for word
            in word_list
            if word.word != '']
    return word_list


def word_list_to_text(word_list, capitalize = False):
    if len(word_list) > 0:
        text = word_list[0].word
        if capitalize and text.islower():
            text = text.capitalize()
    else:
        text = ''

    for i in range(1, len(word_list)):
        if word_list[i - 1].right_space and word_list[i].left_space:
            text += ' '
        text += word_list[i].word

    text = text.strip()
    return text


def form_src(sent, capitalize = False):
    token_list = []
    for token in sent:
        token_list.append(token)
        token_list += token.addition
    word_list = make_word_list(token_list)
    word_list = remove_deleted_tokens(word_list)
    text = word_list_to_text(word_list, capitalize = capitalize)
    return text


def form_trg(sent):
    lst = [token.trg for token in sent]
    return ' '.join(lst)

