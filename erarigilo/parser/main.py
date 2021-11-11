from argparse import ArgumentParser
from .ready import ready
from .run import run
from .form import form
from .show import show

def parse_args():
    parser = ArgumentParser()
    first = parser.add_subparsers()

    ready(first)
    run(first)
    form(first)
    show(first)

    return parser.parse_args()

