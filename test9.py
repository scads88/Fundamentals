# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 17:19:22 2018

@author: john3
"""



import os #be care with this will return true for directories and files
import pandas as pd
import requests
import bs4 as bs
import pickle
from collections import OrderedDict




def save_sp500_tickers_TOOL():
    resp=requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup=bs.BeautifulSoup(resp.text, "lxml")
    table=soup.find('table', {"class":"wikitable sortable"})
    tickers=[]
    for row in table.findAll("tr")[1:]:
        ticker=row.findAll('td')[0].text
        tickers.append(ticker)
    return tickers


totaltickers=save_sp500_tickers_TOOL()[:5]


#if changing total tickers make sure to delete pickle file



#Here we populate our list with desired tickers
#totaltickers=["AAPL", "snn", "ptct"]
filename="hybridization3"
picklefilename=filename+".pickle"
totaltickers=[ticker.replace(ticker, ticker.lower()) for ticker in totaltickers]

dowehaveapickle=os.path.isfile(picklefilename)
print(os.path.abspath(picklefilename))

tickerurldict={}
tickersoupdict={}
tickerlabelratiodict={}
numberasindexdict={}
for ticker in totaltickers:
    if dowehaveapickle==True:
        with open(picklefilename, "rb") as f: #roughly copypasted from function above, but not write bites wb, you read bytes rb
            df=pickle.load(f)


    else:
        americaurl="https://www.marketwatch.com/investing/stock/" + ticker + "/profile" #creates the url template for usa stock ticker designation
        resp=requests.get(americaurl) # requests the info on americaurl and sends it to response variable
        soup3=bs.BeautifulSoup(resp.text, "lxml")# turns the resp variable into a soup
        fundamentalratiolabels=[e.get_text() for e in soup3.select(".sixwide .column")] #soup perused and labels and ratios extracted and fed into vbls based upon html characteristics
        fundamentalratios=[e.get_text() for e in soup3.select(".sixwide .data")]
        new_dict=OrderedDict({k:v for k, v in zip(fundamentalratiolabels, fundamentalratios)}) #the selected labels and selected ratios combined togteher into dictionary
        tickerlabelratiodict[ticker.upper()]=OrderedDict(new_dict) #label:ratio dictionary as values into another dictionary where stock ticker for each group is the key
        df=pd.DataFrame.from_dict(tickerlabelratiodict, orient="columns")# dictionary turned into a pandas dataframe

        with open(filename+".pickle", "wb") as f:
            pickle.dump(df, f)
            f.close()

#putpicklehere
df.to_csv(filename+".csv")
print(df)  
print("poop")