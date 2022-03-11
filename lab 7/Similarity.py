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

X_list = word_tokenize(X_)
Y_list = word_tokenize(Y_)
l1 = []
l2 = []


X_set = {w for w in X_list}
Y_set = {w for w in Y_list}

# form a set containing keywords of both strings
rvector = X_set.union(Y_set)
lis_vector = list(rvector)
for w in rvector:
    if w in X_list:
        l1.append(1)  # create a vector
    else:
        l1.append(0)
    if w in Y_list:
        l2.append(1)
    else:
        l2.append(0)
c = 0
# cosine formula
for i in range(len(rvector)):
    c += l1[i]*l2[i]
cosine = c / float((sum(l1)*sum(l2))**0.5)

t = X_
u = Y_
data = [t, u]
count_vectorizer = CountVectorizer(stop_words='english')
sparse_matrix = count_vectorizer.fit_transform(data)
doc_term_matrix = sparse_matrix.todense()
df = pd.DataFrame(doc_term_matrix, columns=count_vectorizer.get_feature_names(
), index=["doc_a", "doc_b"])
print(df)
# print(cosine_similarity(df, df))
print("Similarity: ", cosine)
