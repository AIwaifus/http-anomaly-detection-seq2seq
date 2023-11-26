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
        self.data = [x[0] for x in map_result]
        self.lengths = [x[1] for x in map_result]
        assert len(self.data) == len(self.lengths)

    def _process_request(self, req):
        """
        Splits a request into lines and convert a string into ints.
        """
        seq = self.vocab.string_to_int(req)
        l = len(seq)

        return seq, l


class Data(Reader):

    def __init__(self, data_path, vocab=Vocabulary(), predict=False):
        """
        Creates an object that gets data from a file.
        """
        super(Data, self).__init__(data_path, vocab)

        if not predict:
            self._train_test_split()

    def _train_test_split(self):
        """
        Train/val/test split for anom