# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 02:02:38 2018

@author: john3
"""

##########################USA ONLY########################




import pandas as pd
import requests
import bs4 as bs
import pickle
from collections import OrderedDict

#Here we populate our list with desired tickers
totaltickers=["AAPL", "snn", "ptct"]

#Do we care about country the ticker trades on
countrycodespecific=False
#here we put all tickers into lowercase to make formatting latter easier
totaltickers=[ticker.replace(ticker, ticker.lower()) for ticker in totaltickers]

print(totaltickers)





#countrycode="usa"
##if have master list of multiple countries will probably want to have a for loop here iterating through
#determines if the ticker is not a USA stock



#populates a dictionary with ticker and proper marketwatch url
tickerurldict={}
tickersoupdict={}
tickerlabelratiodict={}
#numberoftickers=len(totaltickers)
numberasindexdict={}
for ticker in totaltickers:
    americaurl="https://www.marketwatch.com/investing/stock/" + ticker + "/profile"
    resp=requests.get(americaurl)
    soup3=bs.BeautifulSoup(resp.text, "lxml")
    fundamentalratiolabels=[e.get_text() for e in soup3.select(".sixwide .column")]
    fundamentalratios=[e.get_text() for e in soup3.select(".sixwide .data")]
    new_dict={k:v for k, v in zip(fundamentalratiolabels, fundamentalratios)}
    tickerlabelratiodict[ticker.upper()]=new_dict

df=pd.DataFrame.from_dict(tickerlabelratiodict, orient="columns")
#df=pd.concat([df, df2], axis=1)
#df.to_csv(tickername+"_"+ticker2+"_"+countrycode+"_ratios.csv")
print(df)    
#print(tickerlabelratiodict.keys())    
    
"""    
    #tickerurldict[ticker]=americaurl


#check to make sure dict properly filled
#print(tickerurldict)


#create lists of tickers and tickerurls
tickerlist=list(tickerurldict.keys())
print(tickerlist)
tickerurllist=list(tickerurldict.values())
print(tickerurllist)


souplist=[]
for url in tickerurllist:
    print(url)
    resp=requests.get(url)
    soup3=bs.BeautifulSoup(resp.text, "lxml")
    souplist.append(soup3)
"""