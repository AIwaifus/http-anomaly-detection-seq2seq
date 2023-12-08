from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import numpy as np
import json


class Vocabulary():

    def __init__(self):
        self.vocab_file = os.path.dirname(os.path.abspath(__file__)) + '/vocab.json'
        with open(self.vocab_file, 'r') as f:
            self.vocab = json.load(f)

        self.reverse_vocab = {v: k for k, v in self.vocab.items()}

    def string_to_int(self, text):
        """
        Converts a string into its character integer representation.
        """
        try:
            text = text.decode('utf-8')
            characters = list(text)
        except Exception as e:
            characters = ['<UNK>']

     