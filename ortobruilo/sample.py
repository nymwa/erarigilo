from argparse import ArgumentParser
from .ortobruilo import OrtoBruilo 

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('path', help = 'path to dict')
    parser.add_argument('--penalty', type = float, default = 0.8)
    return parser.parse_args()


def main():
    args = parse_args()
    noiser = OrtoBruilo(args.path, args.penalty)
    while x := input():
        print(noiser(x)) 

