import nltk
from nltk.parse.chart import BU_LC_STRATEGY
grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | NP PP
VP -> V NP | VP PP
Det -> 'the'
N -> 'kids' | 'box' | 'floor' | 'map' | 'table' | 'scouts' 
V -> 'opened' | 'closed' |
P -> 'on'
""")

#sen = 'the kids opened the box on the floor'
sen = 'the scouts closed the map on the table'
#sen = "The large can can hold the water"
s = sen.split()

tokens = s
parser = nltk.ChartParser(grammar)
print(grammar)

for tree in parser.parse(s):
    tree.draw()

'''
import nltk


gram_rules = nltk.CFG.fromstring("""
S -> V NP PP CONJ V NP PP
PP -> PRP NP 
NP -> Det N | PRP N |DET ADJ CONJ ADJ N P 
Det -> 'a' | 'every' | 'all'
N -> 'work'  | 'Word Document' | 'results' | 'step'
ADJ -> 'intermediate' | 'final'
V -> 'Describe' | 'present' 
P -> 'of' | 'in'
CONJ -> 'and'
PRP -> 'your'
""")

sent = ['Describe', 'every', 'step' ,'of', 'your', 'work', 'and' ,\
        'present', 'all', 'intermediate' ,'and' ,'final', 'results', 'in' ,'a', 'Word Document']
parser = nltk.ChartParser(gram_rules)
print(gram_rules)
for tree in parser.parse(sent):
    print(tree)
'''