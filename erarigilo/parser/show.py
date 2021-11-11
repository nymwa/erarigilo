from erarigilo.en.show import en_show

def en(second):

    def command(args):
        en_show(
            hide_history = args.hide_history,
            color = args.color,
            cor = args.cor,
            tag = args.tag,
            pos = args.pos,
            dep = args.dep)

    parser = sub_parsers.add_parser('en')
    parser.add_argument('--hide-history', action = 'store_true')
    parser.add_argument('--color', action = 'store_true')
    parser.add_argument('--cor', default = None)
    parser.add_argument('--tag', default = None)
    parser.add_argument('--pos', default = None)
    parser.add_argument('--dep', default = None)
    parser.set_defaults(handler = command)


def show(first):
    parser = first.add_parser('show')
    second = parser.add_subparsers()

    en(second)

