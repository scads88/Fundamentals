# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 21:21:21 2018

@author: john3
"""
import os #be care with this will return true for directories and files
import pandas as pd
import requests
import bs4 as bs
from collections import OrderedDict
#{ticker:{year:{label:value}}}
filename="stillstruggling"
totaltickers=["snn", "aapl", "ptct"]
resp=requests.get("https://www.marketwatch.com/investing/stock/snn/financials")
cleanmoney=[]
tickerurldict={}
tickersoupdict={}
tickerlabelratiodict={}
numberasindexdict={}
for ticker in totaltickers:
    americaurl="https://www.marketwatch.com/investing/stock/"+ticker+"/financials"
    resp=requests.get(americaurl)
    soup3=bs.BeautifulSoup(resp.text, "lxml")
    moneyNyears=[e.get_text() for e in soup3.select(".topRow th")] #this generates usd, years, trend
    for i in moneyNyears:
        

    print(cleanmoney)
    fundamentalratios=[e.get_text() for e in soup3.select(".cellValue")]
    #print(fundamentalratios)
    additional=[e.get_text() for e in soup3.select("cellValue")]
    new_dict=OrderedDict({k:v for k, v in zip(moneyNyears, fundamentalratios)})
    tickerlabelratiodict[ticker.upper()]=OrderedDict(new_dict)
df=pd.DataFrame.from_dict(tickerlabelratiodict, orient="columns")
#putpicklehere
df.to_csv(filename+".csv")
#print(df)  

# =============================================================================
# for row in table.find("td"): 
#    rows.append(row.get_text().strip())
# #",".join(rows)
# print(rows)
# print(rows[::7])
# =============================================================================
