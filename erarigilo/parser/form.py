from erarigilo.en.form import en_form

def en(second):

    def command(args):
        en_form(capitalize = args.capitalize)

    parser = second.add_parser('en')
    parser.add_argument('-c', '--capitalize', action = 'store_true')
    parser.set_defaults(handler = command)


def form(first):
    parser = first.add_parser('form')
    second = parser.add_subparsers()

    en(second)

