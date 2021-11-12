from erarigilo.en.run import en_run

def en(second):

    def command(args):
        if args.languages is None:
            lang_list = None
        else:
            lang_list = args.languages.split(':')
        en_run(
            config_path = args.config,
            ratio = args.ratio,
            lang_list = lang_list)

    parser = second.add_parser('en')
    parser.add_argument('-c', '--config', default = 'config.yaml')
    parser.add_argument('-r', '--ratio', type=float, default=0.0)
    parser.add_argument('-l', '--languages', default=None)
    parser.set_defaults(handler = command)


def run(first):
    parser = first.add_parser('run')
    second = parser.add_subparsers()

    en(second)

