# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:05:40 2018

@author: john3
"""

import urllib2
import time
import csv
import sys

CIK="0001018724"
Year="2013"
string_match1="edgar/data/1018724/0001193125-13-028520.txt"
url3="https://www.sec.gov/Archives/"+string_match1
response3=urllib2.urlopen(url3)

words=["anticipate", "believe", "depend", "fluctuate", "indefinite", "likelihood", "possible", "predict", "risk", "uncertain"]
count={}


for elem in words:
    count[elem]=0
    
for line in response3:
    elements=line.split()
    for word in words:
        count[word]=count[word]+elements.count(word)
print(CIK)
print(Year)
print(url3)
print(count)
