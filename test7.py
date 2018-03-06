# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 02:34:14 2018

@author: john3
"""


#gui
#pull all tickers from wiki for sp500
#pull stock data from api (either marketwatch or google)
#pull data from marketwatchfinancial sheet
#pull data from EDGAR with pySEC
#annotate code so can understand when running through
#see if possible to work in the categories thing
#make a higher better lower better column
#make liquidity , etc column 




import pandas as pd
import requests
import bs4 as bs
import pickle
from collections import OrderedDict

#Here we populate our list with desired tickers
totaltickers=["AAPL", "snn", "ptct"]
filename="hybridization"
totaltickers=[ticker.replace(ticker, ticker.lower()) for ticker in totaltickers]









tickerurldict={}
tickersoupdict={}
tickerlabelratiodict={}
numberasindexdict={}
for ticker in totaltickers:
    americaurl="https://www.marketwatch.com/investing/stock/" + ticker + "/profile"
    resp=requests.get(americaurl)
    soup3=bs.BeautifulSoup(resp.text, "lxml")
    fundamentalratiolabels=[e.get_text() for e in soup3.select(".sixwide .column")]
    fundamentalratios=[e.get_text() for e in soup3.select(".sixwide .data")]
    new_dict=OrderedDict({k:v for k, v in zip(fundamentalratiolabels, fundamentalratios)})
    tickerlabelratiodict[ticker.upper()]=OrderedDict(new_dict)
df=pd.DataFrame.from_dict(tickerlabelratiodict, orient="columns")
#putpicklehere
df.to_csv(filename+".csv")
print(df)  

