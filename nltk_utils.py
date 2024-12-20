import numpy as np
import nltk
# Uncomment if not already downloaded
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    """
    Tokenize the sentence into words
    """
    return nltk.word_tokenize(sentence)

def stem(word):
    """
    Stem the word using PorterStemmer
    """
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    """
    Return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    """
    sentence_words = [stem(word) for word in tokenized_sentence]  # Stem each word
    bag = np.zeros(len(all_words), dtype=np.float32)  # Initialize bag with 0's
    for idx, word in enumerate(all_words):
        if word in sentence_words:  # If the word is in the sentence, mark it as 1
            bag[idx] = 1
    return bag


    
