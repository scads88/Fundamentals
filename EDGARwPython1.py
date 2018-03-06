# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:47:21 2018

@author: john3
"""




#GivenaURLpathforEDGAR10-Kfilein.txtformatfora company(CIK)inayear thiscodewillperformwordcount

import time
import csv
import sys
from urllib.request import urlopen 
import bs4 as bs
import requests




CIK = "1018724"
Year ="2013"
string_match1 = "edgar/data/1018724/0001193125-13-028520.txt"
url3 = "https://www.sec.gov/Archives/"+ string_match1
print(url3)
response3 = urlopen(url3)
response4=response3.read()
print(type(response3.read()))
response4=str(response4)

print(response4.count("uncertain"))
response4=response4.strip()
print(response4.count("uncertain"))
#print(response4)
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)
remove_tags(response4)

print(response4)
#print(response4)


words = ["anticipate", "believe", "depend", "fluctuate", "indefinite", "likelihood", "possible", "predict", "risk", "uncertain"]
counterdic={}
counter=0



for i in words:
    counterdic[i]=0

print(counterdic)
print(response4.count("uncertain"))


"""


#load the page in for the given url in response3
#urllib2 is a Python module that can be used for fetching URLs\
response3 = urlopen(url3)

rp=response3.read()
#print(rp)
#words: list of uncertainty words from Loughran and McDonald (2011)
words = ["anticipate", "believe", "depend", "fluctuate", "indefinite", "likelihood", "possible", "predict", "risk", "uncertain"]
count = {} # is a dictionary data structure in Python











#for elem in words:
    #count[elem] = 0
#The method split() returns a list of all the words in the string
#The split function splits a single string into a string array using #the separator defined.
#If no separator is defined, whitespace is used.
for line in rp:
    elements = line.split()
    
for word in words:
    count[word] = count[word]+elements.count(word)
    
print (CIK)
print (Year)
print (url3)
print (count) 

"""