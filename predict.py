import joblib
import pythainlp.util
from pythainlp.corpus.common import thai_stopwords
from pythainlp import word_tokenize
import numpy as np
import json
import scipy.sparse as sps
from textprocess import text_process

# Load model
sentiment_model = open('LRmodel15000.joblib', 'rb')
clf = joblib.load(sentiment_model)

# Dictionarie of words
with open('dictcvec15000.json', encoding='utf8') as j:
    word = j.read()
dictword = json.loads(word)

# Function predict text
def predict(text):
    # Create array for collect cvec
    arrword = np.array([0]*len(dictword))

    my_tokens = text_process(text) # process text
    listtokens = my_tokens.split(' ') # split word into list
    # Loop for find word in dict and save in array
    for w in listtokens:
        if w in dictword:
            arrword[dictword[w]] += 1

    # Change array to sparse matrix
    wordntx = sps.csr_matrix(arrword, dtype=np.int64)

    # Predict text
    my_prediction = clf.predict(wordntx)
    # print(listtokens)
    return my_prediction

# Text for prediction
# my_text = input('พิมพ์ข้อความ : ')
# print(predict(my_text))