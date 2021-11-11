import sys
import yaml
from erarigilo.module.factory import registory
from . import modules

def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config


def make_factory_list(config):
    factory_list = []
    for dct in config:
        for key, value in dct.items():
            factory_list.append((registory[key], value))
    return factory_list


def en_run(
        config_path,
        ratio = 0.0,
        lang_list = None):

    if lang_list is None:
        lang_list = []

    config = load_config(config_path)
    factory_list = make_factory_list(config)

    pipeline = EnPileline(
            factory_list,
            ratio,
            lang_list)

    batch = sys.stdin.readlines()
    batch = pipeline(batch)
    for sent in batch:
        print(sent)

