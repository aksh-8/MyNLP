import os
import sys
import numpy as np

def load_corpus(path):
    """ Load corpus from a folder / directory

    Arg:
        path: a text sequence denotes the path of corpus

    Return:
        sentences: a list of sentences that are preprocessed in the corpus
    """
    pass

class HMMTagger:

    def __init__(self):
        """ Define variables that are used in the whole class

        You shuold initial all variables that are necessary and will be used
        globally in this class, such as the initial probability.
        """
        pass

    def initialize_probabilities(self, sentences):
        """ Initialize / learn probabilities from the corpus

        In this function, you should learn inital probability, transition
        probability, and emission probability. Also, you should apply the
        add-one smoothing properly here.

        Arg:
            sentences: a list of sentences that are preprocessed in the corpus
        """
        pass

    def viterbi_decode(self, sentence):
        """ Viterbi decoding algorithm implementation

        Arg:
            sentence: a text sequence needed to be decoded
        """
        pass

if __name__ == "__main__":
    # Initialize the tagger class
    tagger = HMMTagger()

    # Read a corpus and learn from it
    folder_name = input("Input path: ")
    sentences = load_corpus(folder_name)
    tagger.initialize_probabilities(sentences)

    # Test
    sentence = "the planet jupiter and its moons are in effect a mini solar system ."
    result = tagger.viterbi_decode(sentence)
    print(sentence)
    print(result)

    sentence = "computers process programs accurately ."
    result = tagger.viterbi_decode(sentence)
    print(sentence)
    print(result)
