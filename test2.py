# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 00:35:16 2018

@author: john3
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:47:21 2018

@author: john3
"""




#GivenaURLpathforEDGAR10-Kfilein.txtformatfora company(CIK)inayear thiscodewillperformwordcount

import time
import csv
import sys
import urllib

#import urllib.request
#url = "http://www.google.com/"
#request = urllib.request.Request(url)
#response = urllib.request.urlopen(request)

CIK = "0001018724"
Year ="2013"
string_match1 = "edgar/data/1018724/0001193125-13-028520.txt"
url3 = "https://www.sec.gov/Archives/"+ string_match1
url4=urllib.request.Request(url3)
response3 = urllib.request.urlopen(url4)
words = ["anticipate", "believe", "depend", "fluctuate", "indefinite", "likelihood", "possible", "predict", "risk", "uncertain"]
count = {} 
for elem in words:
    count[elem] = 0
print(count)
for line in response3:
    elements = line.split()
    
for word in words:
    count[word] = count[word]+elements.count(word)
    
print (CIK)
print (Year)
print (url3)
print (count)