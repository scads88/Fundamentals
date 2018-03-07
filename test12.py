# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 20:26:53 2018

@author: john3
"""

#scraping of income statement 

import os #be care with this will return true for directories and files
import pandas as pd
import requests
import bs4 as bs
import pickle
from collections import OrderedDict


# =============================================================================
# respIncomeStatement=requests.get("https://www.marketwatch.com/investing/stock/snn/financials")
# soup=bs.BeautifulSoup(respIncomeStatement.text, "lxml")
# t2=[e.get_text() for e in soup.select(".rowTitle")] #soup perused and labels and ratios extracted and fed into vbls based upon html characteristics
# t3=fundamentalratiolabels=[e.get_text() for e in soup.select(".valueCell")] #soup perused and labels and ratios extracted and fed into vbls based upon html characteristics
# 
# print(t2)
# 
# 
# t3[0]="Currency"
# print(t3)
# =============================================================================








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
totaltickers=["AAPL", "snn", "ptct"]
filename="Income1"
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
        IncomeUrl="https://www.marketwatch.com/investing/stock/"+ticker+"/financials"
        respIncomeStatement=requests.get(IncomeUrl)
        soup=bs.BeautifulSoup(respIncomeStatement.text, "lxml")
        IncomeLabels=[e.get_text() for e in soup.select(".rowTitle")] #soup perused and labels and ratios extracted and fed into vbls based upon html characteristics
        IncomeValues=[e.get_text() for e in soup.select(".valueCell")] #soup perused and labels and ratios extracted and fed into vbls based upon html characteristics
        IncomeValues[0]="Currency"
        new_dict=OrderedDict({k:v for k, v in zip(IncomeLabels, IncomeValues)}) #the selected labels and selected ratios combined togteher into dictionary
        tickerlabelratiodict[ticker.upper()]=OrderedDict(new_dict) #label:ratio dictionary as values into another dictionary where stock ticker for each group is the key
        df=pd.DataFrame.from_dict(tickerlabelratiodict, orient="columns")# dictionary turned into a pandas dataframe

        with open(filename+".pickle", "wb") as f:
            pickle.dump(df, f)
            f.close()

print(new_dict)


df.to_csv(filename+".csv")
#print(df)  
#print("poop")




# =============================================================================
# 
# 
# resp=requests.get("https://www.marketwatch.com/investing/stock/snn/financials")
# soup=bs.BeautifulSoup(resp.text, "lxml")
# 
# #soup.find("table")[2]would give you the second table
# table = soup.find( "table", {"class":"crDataTable"} )
# 
# rows=list()
# for row in table.findAll("td"): 
#    rows.append(row.get_text().strip())
# #",".join(rows)
# #print(rows)
# #print(rows[::7])
# ##fundamentalratiolabels=[e.get_text() for e in soup3.select(".sixwide .column")] #soup perused and labels and ratios extracted and fed into vbls based upon html characteristics
# 
# =============================================================================
