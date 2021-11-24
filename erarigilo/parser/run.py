from erarigilo.en.run import en_run

def en(second):

    def command(args):
        if args.languages is None:
            lang_list = None
        else:
            lang_list = args.languages.split(':')
        en_run(
            config_path = args.config,
            is_run_by_batch = args.run_by_batch,
            batch_size = args.batch_size,
            no_error = args.no_error,
            ratio = args.ratio,
            lang_list = lang_list)

    parser = second.add_parser('en')
    parser.add_argument('-c', '--config', default = 'config.yaml')
    parser.add_argument('-b', '--run-by-batch', action = 'store_true')
    parser.add_argument('-s', '--batch-size', type = int, default = 1000)
    parser.add_argument('-n', '--no-error', action = 'store_true')
    parser.add_argument('-r', '--ratio', type = float, default = 0.0)
    parser.add_argument('-l', '--languages', default = None)
    parser.set_defaults(handler = command)


def run(first):
    parser = first.add_parser('run')
    second = parser.add_subparsers()

    en(second)

