from __future__ import print_function
import random
import numpy as np

from sklearn.model_selection import train_test_split

from .vocab import Vocabulary
from .utils import get_requests_from_file, batch_generator, one_by_one_generator


class Reader(object):

    def __init__(self, data_path, vocab=Vocabulary()):
        self.vocab = vocab

        data = get_requests_from_file(data_path)
        print("Downloaded {} samples".format(len(data)))

        map_result = map(self._process_request, data)
        self.data = [x[0] for x in ma