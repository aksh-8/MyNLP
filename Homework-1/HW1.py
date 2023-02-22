# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:22:02 2023

@author: Akash Biswal(axb200166)
"""
import sys
import string
import math

# Funciton to perform initial cleanup of the training corpus
def preprocessing(file):
    f = open(file,"r")
    text = f.read()
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    lines = text.splitlines()
    print("Number of lines in the training corpus: ", len(lines))
    return lines
    
# Function to create tokens of words in each line, add start and end line tags
def tokenize(lines):
    tokenized = []
    for i in range(len(lines)):
        temp = lines[i].split()
        temp.insert(0,"<start>")
        temp.append("<end>")
        tokenized.append(temp)
    return tokenized
    
# Function to create the vocabulary consisting of unique words based on 
def construct_vocab(tokenized):
    vocabulary = {}
    counts = 0
    for i in tokenized:
        counts += len(i) - 2 
        for j in i:
            if j not in vocabulary:
                vocabulary[j] = 1
            else:
                vocabulary[j] += 1
    #print("Number of Unique words in the training corpus: ", len(vocabulary)-2)
    #print("Total number of words in the training corpus(<start> & <end> tags are excluded): ", counts)
    #print()
    return vocabulary

# Function to construct dictionaries with the bigram counts and their probabilites
def construct_bigrams(tokenized, vocabulary):
    bigram_frequencies = {}
    for line in tokenized:
        for prev_word, word in zip(line, line[1:]):
            if (prev_word, word) not in bigram_frequencies:
                bigram_frequencies[(prev_word, word)] = 1
            else:
                bigram_frequencies[(prev_word, word)] += 1
    
    bigram_probablities = {}
    for pair in bigram_frequencies:
        if bigram_frequencies[pair] == 0 or vocabulary[pair[0]] == 0:
            bigram_probablities[pair] = 0
        else:
            #bigram_probablities[pair] = float(bigram_frequencies[pair])/float(vocabulary[pair[0]])
            bigram_probablities[pair] = bigram_frequencies[pair]/vocabulary[pair[0]]
            
    return bigram_frequencies, bigram_probablities

# Function to compute the bigram probabilities for the words in the test sentence
def sentence_bigram_probabilities(prev_word, curr_word, smoothing):
    if prev_word in vocabulary:
        prev_word_freq = vocabulary[prev_word]
    else:
        prev_word_freq = 0
    
    if (prev_word, curr_word) in bigram_frequencies:
        bigram_frequency = bigram_frequencies[(prev_word, curr_word)]
    else:
        bigram_frequency = 0
    
    if smoothing == 1:
        n, d = bigram_frequency+1, prev_word_freq + len(vocabulary)
        if n == 0 or d == 0:
            return 0.0
        else:
            #return float(n)/float(d)
            return n/d
    elif smoothing == 0:
        if (prev_word, curr_word) in bigram_probablities:
            return bigram_probablities[(prev_word, curr_word)]
        else:
            return 0

# Function to print and write the table showing the bigram counts and probabilities for test sentences
def print_and_write_tables(evaluation_sentences,smoothing):
    with open("output.txt","w") as f:
        # print bigram counts of test sentences
        for i in range(len(evaluation_sentences)):
            eval_tokens = tokenize(evaluation_sentences[i])
            eval_vocab = construct_vocab(eval_tokens)
            
            print("Printing the bigram counts for each word of sentence(without punctuations): \"" + evaluation_sentences[i][0] + "\"")
            print("Printing the bigram counts for each word of sentence(without punctuations): \"" + evaluation_sentences[i][0] + "\"", file = f)
    
            print("%12s"%(""),end="")
            print("%12s"%(""),end="", file=f)
            for header in eval_vocab:
                print("%12s"%(header),end="")
                print("%12s"%(header),end="", file =f)
            print()
            print(file=f)
            for w1 in eval_vocab:
                print("%12s"%(w1), end="")
                print("%12s"%(w1), end="", file=f)
                for w2 in eval_vocab:
                    if smoothing:
                        if (w1,w2) in bigram_frequencies:
                            print("%12d"%(bigram_frequencies[(w1,w2)]+1), end="")
                            print("%12d"%(bigram_frequencies[(w1,w2)]+1), end="",file=f)
                        else:
                            print("%12d"%(1), end="")
                            print("%12d"%(1), end="",file=f)
                    else:
                        if (w1,w2) in bigram_frequencies:
                            print("%12d"%(bigram_frequencies[(w1,w2)]), end="")
                            print("%12d"%(bigram_frequencies[(w1,w2)]), end="",file=f)
                        else:
                            print("%12d"%(0), end="")
                            print("%12d"%(0), end="",file=f)
                print()
                print(file=f)
            print()
            print(file=f)
            # print bigram probabilities
            print("#---------------------------Bigram Probabilities for the above sentence---------------------------#")
            print("#---------------------------Bigram Probabilities for the above sentence---------------------------#", file=f)
            print("%12s"%(""),end="")
            print("%12s"%(""),end="",file=f)
            for header in eval_vocab:
                print("%12s"%(header),end="")
                print("%12s"%(header),end="",file=f)
            print()
            print(file=f)
            for w1 in eval_vocab:
                print("%12s"%(w1), end="")
                print("%12s"%(w1), end="",file=f)
                for w2 in eval_vocab:
                    # print (w1,i, end="")
                    print("%12f"%(sentence_bigram_probabilities(w1,w2,smoothing)), end="")
                    print("%12f"%(sentence_bigram_probabilities(w1,w2,smoothing)), end="",file=f)
                print()
                print(file=f)
            print()
            print(file=f)
            print("###################################################################################################")
            print("###################################################################################################",file=f)
    
# Function to compute the final probability as well as log probability of the test sentences based on the training corpus
def sentence_probability(evaluation_sentences,smoothing):
    
    probability = 1
    log_probability = 0
    with open("output.txt","a") as f:
        for i in range(len(evaluation_sentences)):
            eval_tokens = tokenize(evaluation_sentences[i])
            eval_vocab = construct_vocab(eval_tokens)
            eval_frequencies, eval_bigrams = construct_bigrams(eval_tokens, eval_vocab)
            for pair in eval_frequencies:
                probability *= sentence_bigram_probabilities(pair[0],pair[1],smoothing)
                if probability == 0:
                    log_probability += 0
                else:
                    log_probability += abs(math.log(probability))
            print("THE SENTENCE PROBABILITY FOR \"" + evaluation_sentences[i][0] + "\" is: " + str(probability))
            print("THE LOG PROBABILITY OF THE ABOVE IS: " + str(log_probability))
            print("THE SENTENCE PROBABILITY FOR \"" + evaluation_sentences[i][0] + "\" is: " + str(probability),file=f)
            print("THE LOG PROBABILITY OF THE ABOVE IS: " + str(log_probability),file=f)

# Main Function
if __name__ == "__main__":
    
    # Command line check
    if len(sys.argv)<2:
        sys.exit("Enter all the arguments: Training file and Smoothing boolean")
    smoothing = int(sys.argv[2])
    file = sys.argv[1]
    evaluation_sentences = ["mark antony shall say i am not well , and for thy humor , i will stay at home .","talke not of standing . publius good cheere , there is no harme intended to your person , nor to no roman else : so tell them publius"]
    #smoothing = 1
    for i in range(len(evaluation_sentences)):
        evaluation_sentences[i] = [evaluation_sentences[i].translate(str.maketrans("", "", string.punctuation))]

    #file = "train.txt"
    lines = preprocessing(file)
    corpus_tokenized = tokenize(lines)
    vocabulary = construct_vocab(corpus_tokenized) 
    bigram_frequencies, bigram_probablities = construct_bigrams(corpus_tokenized, vocabulary)
    
    print_and_write_tables(evaluation_sentences, smoothing)
    sentence_probability(evaluation_sentences, smoothing)
    print()
    print("All Probabilities are computed and stored in the output.txt file")
    print("###################################################################################################")
    