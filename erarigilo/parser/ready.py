from erarigilo.en.ready import en_ready

def en(second):

    def command(args):
        quote = not args.no_quote_regularization
        en_ready(quote = quote, json_input = args.json_input)

    parser = second.add_parser('en')
    parser.add_argument('--no-quote-regularization', action = 'store_true')
    parser.add_argument('-j', '--json-input', action = 'store_true')
    parser.set_defaults(handler = command)


def ready(first):
    parser = first.add_parser('ready')
    second = parser.add_subparsers()

    en(second)

