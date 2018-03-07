# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 21:17:16 2018

@author: john3
"""
import os #be care with this will return true for directories and files
import pandas as pd
import requests
import bs4 as bs
from collections import OrderedDict

#{ticker:{year:{label:value}}}


tickers=["snn"]
yearlabelvaluedict={}
tickeryearlabelvaluedict={}

for ticker in tickers:
    IncomeUrl="https://www.marketwatch.com/investing/stock/"+ticker+"/financials"
    respIncomeStatement=requests.get(IncomeUrl)
    soup=bs.BeautifulSoup(respIncomeStatement.text, "lxml")
    IncomeLabels=[e.get_text() for e in soup.select(".rowTitle")] #soup perused and labels and ratios extracted and fed into vbls based upon html characteristics
    IncomeValues=[e.get_text() for e in soup.select(".valueCell")] #soup perused and labels and ratios extracted and fed into vbls based upon html characteristics
    IncomeValues[0]="Currency"
    new_dict=OrderedDict({k:v for k, v in zip(IncomeLabels, IncomeValues)})
print(new_dict)
    #the selected labels and selected ratios combined togteher into dictionary
    #tickerlabelratiodict[ticker.upper()]=OrderedDict(new_dict) #label:ratio dictionary as values into another dictionary where stock ticker for each group is the key
    #df=pd.DataFrame.from_dict(tickerlabelratiodict, orient="columns")# dictionary turned into a pandas dataframe