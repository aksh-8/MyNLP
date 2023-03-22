# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:15:18 2023

@author: Akash Biswal (axb200166)
"""  

import os
import sys
import numpy as np
import pandas as pd

# PATH = E:\MS-CE-UTD\Sem-4\MyNLP\Homework-2\modified_brown

def load_corpus(path):
    '''
    Function : Loads corpus from directory
    Argument : Path to directory as a string
    Return : POS tagged list of lists
    '''
    sentences = []
    for filename in os.listdir(path):
        with open(os.path.join(path,filename), "r") as f:
            lines = f.readlines()
            for line in lines:
                temp = line.split()
                sentence = []
                for inp in temp:
                    pair = inp.split('/')
                    token, POS = pair[0], pair[1]
                    sentence.append((token,POS))
                if sentence:
                    sentences.append(sentence)
    return sentences

class HMMTagger:

    def __init__(self):
        '''
        Function : Initializes all variables to be used in the HMMTagger class
        '''
        self.word_tag_pairs = {} # all unique word and tag pairs in the corpus 
        self.tags = set()  # all tags in corpus
        self.words = set() # to contain unique words in the corpus
        self.tag_counts = {} # tag frequencies
        self.tag_transistion_counts = {} # transistion frequencies

    def initialize_probabilities(self, sentences):
        '''
        Function : Loads corpus from directory, populate the necessary dictionaries used for viterbi decoding
        Argument : Path to directory as a string
        Return : POS tagged list of lists
        '''
        for sentence in sentences:
            for pair in sentence:
                if pair not in self.word_tag_pairs:
                    self.word_tag_pairs[pair] = 1
                self.word_tag_pairs[pair] += 1
                self.words.add(pair[0])
                self.tags.add(pair[1])
                if pair[1] not in self.tag_counts:
                    self.tag_counts[pair[1]] = 1
                self.tag_counts[pair[1]] += 1
                
            # updating tag transition frequencies  
            for i in range(len(sentence)-1):
                if (sentence[i][1],sentence[i+1][1]) in self.tag_transistion_counts:
                    self.tag_transistion_counts[(sentence[i][1],sentence[i+1][1])] += 1
                else:
                    self.tag_transistion_counts[(sentence[i][1],sentence[i+1][1])] = 1
        
        # Transistion probabilities calculated with add-one smoothing
        tags_values = np.zeros((len(self.tags),len(self.tags)))
        for i, tag1 in enumerate(list(self.tags)):
            for j, tag2 in enumerate(list(self.tags)):
                tags_values[i,j] = (self.tag_transistion_counts[(tag1,tag2)]+1)/(self.tag_counts[tag1]+len(self.tags))
        # Tags matrix in a dataframe
        self.tags_matrix = pd.DataFrame(tags_values,index=list(self.tags),columns=list(self.tags))
        
    def viterbi_decode(self, sentence):
        '''
        Function : Implementation of the Viterbi Decoding Algorithm
        Argument : Test sentence that needs to be decoded and POS tagged
        Return : List of Tuples with sentence words and it's corresponding tag
        '''
        max_prob_tags = []
        # Using default tag as PUNCT for the start of the sentence, this is done w.r.t the dataset
        prev_tag = 'PUNCT'
        sentence = sentence.split(' ')
        for word in sentence:
            word_prob = {}
            for tag in self.tags:
                #Add one smoothing in emission probabilities calculation
                word_prob[tag] = (self.word_tag_pairs.get((word, tag), 0) + 1) / (self.tag_counts[tag] + len(self.words)) 
                # Calculate and store transition probablities 
                transistion_prob = self.tags_matrix.loc[prev_tag,tag]
                word_prob[tag] = word_prob[tag]*transistion_prob
            # Get tag with highest probability
            max_prob_tag = max(word_prob, key=word_prob.get)
            max_prob_tags.append(max_prob_tag)
            prev_tag = max_prob_tag
        # list of word and tag pair for the test sentence
        return list(zip(sentence, max_prob_tags))


if __name__ == "__main__":
    # Initialize the tagger class
    tagger = HMMTagger()

    # Read a corpus and learn from it
    folder_name = input("Input path: ")
    sentences = load_corpus(folder_name)
    res = tagger.initialize_probabilities(sentences)

    #Test
    sentence = "the planet jupiter and its moons are in effect a mini solar system ."
    result = tagger.viterbi_decode(sentence)
    print(sentence)
    print(result)

    sentence = "computers process programs accurately ."
    result = tagger.viterbi_decode(sentence)
    print(sentence)
    print(result)