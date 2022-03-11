from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tabulate import tabulate
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


X = open("Doc1.txt", "r")
Y = open("Doc2.txt", "r")
X_ = X.read()
Y_ = Y.read()

# tokenization
X_list = word_tokenize(X_)
Y_list = word_tokenize(Y_)

# sw contains the list of stopwords
sw = stopwords.words('english')

# form a set containing keywords of both strings
for i in range(0, len(Y_list), 6):
    l1 = []
    l2 = []
    new_x = X_list[i:i+6]
    new_Y = Y_list[i:i+6]
    rvector = new_x + new_Y
    lis_vector = list(rvector)
    print(new_x, new_Y)
    for w in rvector:
        if w in new_x:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in new_Y:
            l2.append(1)
        else:
            l2.append(0)
    c = 0
    x = zip(l1, l2)
    both = [i for i in x]
    q = [(lis_vector[i], both[i]) for i in range(len(l1))]

    # cosine formula
    for i in range(len(rvector)):
        c += l1[i]*l2[i]
    try:
        cosine = c / float((sum(l1)*sum(l2))**0.5)
    except ZeroDivisionError:
        cosine = 0
    print("Similarity: ", cosine)

# W/O stopwords
print("\nW/O stopwords\n")
for i in range(0, len(Y_list), 6):
    l1 = []
    l2 = []
    new_x = X_list[i:i+6]
    new_Y = Y_list[i:i+6]
    X_set = {w for w in new_x if not w in sw}
    Y_set = {w for w in new_Y if not w in sw}
    rvector = X_set.union(Y_set)
    lis_vector = list(rvector)
    print(X_set, Y_set)
    for w in rvector:
        if w in X_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0
    x = zip(l1, l2)
    both = [i for i in x]
    q = [(lis_vector[i], both[i]) for i in range(len(l1))]

    # cosine formula
    for i in range(len(rvector)):
        c += l1[i]*l2[i]
    try:
        cosine = c / float((sum(l1)*sum(l2))**0.5)
    except ZeroDivisionError:
        cosine = 0
    print("Similarity: ", cosine)
