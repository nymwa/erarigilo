from argparse import ArgumentParser
import pickle
from tqdm import tqdm

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('vocab', help = 'path to vocabulary')
    parser.add_argument('model', help = 'path to model')
    parser.add_argument('--min-freq', type = int, default = 1000)
    return parser.parse_args()


def split_word(vocab, word):
    candidates = []
    for i in range(1, len(word)):
        left, right = word[:i], word[i:]
        if left in vocab and right in vocab:
            candidates.append(left + ' ' + right)
    return candidates


def make_vocab(args):
    vocab = []
    with open(args.vocab, 'r') as f:
        for x in f:
            word, freq = x.strip().split('\t')
            freq = int(freq)
            if freq >= args.min_freq:
                vocab.append(word)
    vocab = set(vocab)
    return vocab


def main():
    args = parse_args()
    vocab = make_vocab(args)

    orts = {}
    for word in tqdm(vocab, bar_format = '{l_bar}{r_bar}'):
        candidates = split_word(vocab, word)
        if len(candidates) > 0:
            orts[word] = candidates

    with open(args.model, 'wb') as f:
        pickle.dump(orts, f)

