# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:30:42 2018

@author: john3
"""
from urllib.request import urlopen

import time
import csv
import sys

CIK="1018724" #the CIK of amazon
Year="2013"
FILE="10-K"

url="https://www.sec.gov/Archives/edgar/full-index/%s/QTR1/master.idx" %(Year)
response=urlopen(url)
string_match1="edgar/data"
element2=None
element3=None
element4=None

for line in response:
    if CIK in line and FILE in line:
        for element in line.split(""):
            if string_match1 in element:
                element2=element.split("|")
                for element3 in element2:
                    if string_match1 in element3:
                        element4=element3

url3="https://www.sec.gov/Archives/"+element4
response3=urlopen(url3)
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