from .parser.main import parse_args

def main():
    args = parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        print('no handler')

