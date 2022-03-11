import nltk
nltk.download('brown')
nltk.download('punkt')
from textblob import TextBlob
import spacy
nlp = spacy.load('en_core_web_sm')
def get_subject_phrase(doc):
    for token in doc:
        if ("subj" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            return doc[start:end]
def get_object_phrase(doc):
    for token in doc:
        if ("dobj" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            return doc[start:end]
sentences=["Arjun wanted a Jordan Shoe.","Somanshu saw it at the factory outlet.","He showed it to him and bought it."]
for sentence in sentences:
    doc = nlp(sentence)
    subject_phrase = get_subject_phrase(doc)
    object_phrase = get_object_phrase(doc)
    print("Subject : ",subject_phrase)
    print("Object : ",object_phrase)
txt1 = "Arjun wanted a Jordan shoe."
txt2 = "Somanshu saw it at the factory outlet."
txt3 = "He showed it to him and bought it."

blob1 = TextBlob(txt1)
print(blob1.noun_phrases)

blob2 = TextBlob(txt1)
print(blob2.noun_phrases)

blob3 = TextBlob(txt1)
print(blob3.noun_phrases)
