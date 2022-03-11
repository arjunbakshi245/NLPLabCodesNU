import nltk
from nltk.parse.chart import BU_LC_STRATEGY

grammar = nltk.CFG.fromstring(
"""
S -> NP VP | VP NP | AUX PP | PP NP
PP -> P NP 
NP -> Det N | NP PP
VP -> V NP | VP PP
Det -> 'the'
N -> 'kids' | 'box' | 'floor' | 'map' | 'table' | 'scouts' | 'adults'
V -> 'opened' | 'closed' | 'jumped' | 'kicked'
P -> 'on'
""")
#sen = 'the kids opened the box on the floor'
sen = 'the scouts closed the map on the table'
s = sen.split(' ')

#parser=nltk.parse.EarleyChartParser(grammar,trace=1)
#print(parser.parse(s))

parser = nltk.ChartParser(grammar)
for tree in parser.parse(s):
    print(tree)



