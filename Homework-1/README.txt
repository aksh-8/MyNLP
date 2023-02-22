This python program (HW1.py) calculates the bigram frequencies, bigram probabilities and probability of both test sentences against the provided training corpus.

Assumptions:
1. All punctuations are removed from the training corpus
2. "<start>" and "<end>" tags are added to the corpus suring preprocessing to indicate start and end of the sentence
3. All text is converted to lower case
4. Only python libraries used are "string" and "math"
5. This file is written in Python3, therefore it must be tested in the same
6. On investigation using regex, no words with hyphen or apostrophes were found in the training corpus, therefore no special checks for such words are included in the preprocessing

- The training corpus is stored in "train.txt"
- The outputs are printed to the console and written to the "output.txt" file

Accepeted <smoothing> or "b" values are {0,1}

 
To run the program:
python3 HW1.py train.txt b

