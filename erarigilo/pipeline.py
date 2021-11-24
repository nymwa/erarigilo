import sys
import json

from erarigilo.util.sampler import (
        UniformSampler,
        ChoiceSampler)
from erarigilo.util.log import init_logging
from logging import getLogger
init_logging()
logger = getLogger(__name__)

class Pipeline:

    def __init__(self,
            factory_list,
            ratio = 0.0,
            lang_list = None):

        self.factory_list = factory_list
        self.ratio = ratio
        self.lang_list = lang_list

        if lang_list is not None:
            self.uniform_sampler = UniformSampler()
            self.choice_sampler = ChoiceSampler(lang_list)

    def batch_decode(self, batch):
        for line in batch:
            line = line.strip()
            dct = json.loads(line)
            sent = self.sent_decode(dct)
            yield sent

    def batch_encode(self, batch):
        for sent in batch:
            sent = sent.encode()
            sent = json.dumps(sent, ensure_ascii = False)
            yield sent

    def __call__(self, batch):
        batch_size = len(batch)
        batch = self.batch_decode(batch)

        logger.info('Batch loaded, length = {}'.format(batch_size))

        for index, (factory, dct) in enumerate(self.factory_list, start = 1):
            module = factory(dct)
            logger.info('Module {}: {}'.format(
                index,
                module.rule.name))
            batch = [module(sent) for sent in batch]

        batch = self.batch_encode(batch)

        return batch

