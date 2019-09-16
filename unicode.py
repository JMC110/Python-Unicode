# -*- coding: utf-8 -*-
import re
from collections import Counter
list_1 = []
list_2 = []
list_3 = []
list_4 = []

datafile1 = open('test.txt',encoding = "utf8")                     ##### Word Pair 1 #####
for line1 in datafile1:                                 
    s = line1
    set1 = {word for matched in re.findall(r'(\S+\S+)\s+रस्सी\s+(\S+\S)', s)   ##### Word search and extraction of contexts.
            for word in matched}
    list_1.extend(set1)
print ("list_Rassi =",list_1)
c = Counter(list_1)
c.keys()
NRassi = len(c.keys())                                                       ##### Count of contexts
print(NRassi)
