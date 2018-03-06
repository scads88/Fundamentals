# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 22:53:29 2018

@author: john3
"""


#modules imported
import pandas as pd
from collections import OrderedDict
import bs4 as bs
import pickle
import requests
import csv
import numpy as np
import re
import pprint



"""


urls = ['www.website1.com', 'www.website2.com', 'www.website3.com', .....]
#scrape elements
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    #print titles only
    h1 = soup.find("h1", class_= "class-headline")
    print(h1.get_text())

"""
#might want to have a tkinter graphic user interface that feeds stock inputs




#eventually might want to have global list that that has all the company tickers
# you care about 


#Here we populate our list with desired tickers
totaltickers=["AAPL", "snn", "ptct"]

#Do we care about country the ticker trades on
countrycodespecific=False
#here we put all tickers into lowercase to make formatting latter easier
totaltickers=[ticker.replace(ticker, ticker.lower()) for ticker in totaltickers]

print(totaltickers)




countrycodespecific=False
countrycode="usa"
##if have master list of multiple countries will probably want to have a for loop here iterating through
#determines if the ticker is not a USA stock



#populates a dictionary with ticker and proper marketwatch url
tickerurldict={}
for ticker in totaltickers:
    if countrycodespecific==True:
        countrycode=countrycode.lower()#drives country code to lowercase
        countrycodeurl="?countrycode="+countrycode #preprocess country code
        totalurl="https://www.marketwatch.com/investing/stock/" + ticker +"/profile"+ countrycodeurl
        tickerurldict[ticker]=totalurl

    else:
        countrycode="usa"
        americaurl="https://www.marketwatch.com/investing/stock/" + ticker + "/profile"
        tickerurldict[ticker]=americaurl


#check to make sure dict properly filled
print(tickerurldict)


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

#might come back later to make this a dictionary
#create a list of soups to scrape
# =============================================================================
# tickersoupdict={}
# for url in tickerurllist:
#     resp=requests.get(url)
#     soup3=bs.BeautifulSoup(resp.text, "lxml")
# for i in tickerlist:
#     tickersoupdict[i]=soup3
# 
# =============================================================================

#we have created a ticker:soupdictionary       
#print(tickersoupdict.keys())


#souplist=list(tickersoupdict.values())
print(souplist)
for soup in souplist:
    fundamentalratiolabels=[e.get_text() for e in soup.select(".sixwide .column")]
    fundamentalratios=[e.get_text() for e in soup.select(".sixwide .data")]

    print(fundamentalratios)








"""

listofdick=[]
df={}
for soup in souplist:
 
    fundamentalratiolabels=[e.get_text() for e in soup.select(".sixwide .column")]
    fundamentalratios=[e.get_text() for e in soup.select(".sixwide .data")]
    new_dict={k:v for k, v in zip(fundamentalratiolabels, fundamentalratios)}
    print(new_dict)
"""











#print(fundamentalratios)   
"""    
    new_dict={k:v for k, v in zip(fundamentalratiolabels, fundamentalratios)}
    listofdick.append(new_dict)

print(listofdick[1])
"""




# =============================================================================
# 
# 
# souplist=[]
# for url in tickerurllist:
#     print (url)
#     resp=requests.get(url)
#     soup3=bs.BeautifulSoup(resp.text, "lxml")
#     souplist.append(soup3)
# 
# 
# 
# new_dict={}
# for soup in souplist:
# 
#     fundamentalratiolabels=[e.get_text() for e in soup.select(".sixwide .column")]
#     fundamentalratios=[e.get_text() for e in soup.select(".sixwide .data")]
#     new_dict={k:v for k, v in zip(fundamentalratiolabels, fundamentalratios)}
# 
# 
# 
# 
#     print (new_dict)
# =============================================================================







# =============================================================================
# new_dict={}
# for soup in souplist:
#     fundamentalratiolabels=[e.get_text() for e in soup.select(".sixwide .column")]
#     fundamentalratios=[e.get_text() for e in soup.select(".sixwide .data")]
#     new_dict={k:v for k, v in zip(fundamentalratiolabels, fundamentalratios)}
#     print(new_dict)
# =============================================================================

    
# =============================================================================
#     for soup in souplist:
#         for e in soup.select(".sixwide .column"):
#             pussy=e.get_text()
#             #print(pussy)
# =============================================================================
    
#print(souplist)

#f=open("testsoup.txt", "w")
#f.write(str(soup3))
#f.close()
#these two lines ID the required information from marketwatch and populate variables
    ##might eventually want to change fundamentaldata to fundamentalratios
    
# =============================================================================
# 
# fundamentallabels=[e.get_text() for e in soup.select(".sixwide .column")]
# fundamentaldata=[e.get_text() for e in soup.select(".sixwide .data")]
# fundamentallabels2=[e.get_text() for e in soup2.select(".sixwide .column")]
# fundamentaldata2=[e.get_text() for e in soup2.select(".sixwide .data")]
# 
# #this is the categories that i would like to use as a key for the fundamentallabels and fundamentaldata above
# category=[e.get_text().strip() for e in soup.select("h2")]
# category5=category[1:6]
# print(category5)
# 
# =============================================================================










#these two lines ID the required information from marketwatch and populate variables
    ##might eventually want to change fundamentaldata to fundamentalratios
    
  
"""
fundamentallabels=[e.get_text() for e in soup.select(".sixwide .column")]
fundamentaldata=[e.get_text() for e in soup.select(".sixwide .data")]
fundamentallabels2=[e.get_text() for e in soup2.select(".sixwide .column")]
fundamentaldata2=[e.get_text() for e in soup2.select(".sixwide .data")]

#this is the categories that i would like to use as a key for the fundamentallabels and fundamentaldata above
category=[e.get_text().strip() for e in soup.select("h2")]
category5=category[1:6]
print(category5)



#this is a check to ensure that the ratios and their labels match up so no NAN entries
if len(fundamentaldata)==len(fundamentallabels):
    new_dict={k:v for k, v in zip(fundamentallabels, fundamentaldata)}
else:
    print("Something is wrong with the matchu of data to label")


if len(fundamentaldata2)==len(fundamentallabels2):
    new_dict2={k:v for k, v in zip(fundamentallabels2, fundamentaldata2)}
else:
    print("Something is wrong with the matchu of data to label")
# =============================================================================
# ballcheese=[]
# for i in range(len(fundamentaldata)):
#     ballcheese.append(i+1)
# print(ballcheese)
# =============================================================================
namecolfordf=tickername.upper()+"_"+countrycode.upper()
biggerdic={namecolfordf:new_dict}
df=pd.DataFrame.from_dict(biggerdic, orient="columns")



namecolfordf2=ticker2.upper()+"_"+countrycode.upper()
biggerdic2={namecolfordf2:new_dict2}
df2=pd.DataFrame.from_dict(biggerdic2, orient="columns")

# =============================================================================
# t=pd.DataFrame(index=ballcheese, data=biggerdic)
# butt=t.append(df)
# =============================================================================

#print(butt)
titty=[e.get_text().strip() for e in soup.select(".sixwide .block h2")]





#Things that are still needed in the reports
#Year Data generated
#The etc data
#having a sector index against which it can be compared

###THIS ADDS AN EXTRA ROW TO DATAFRAME####
#df=df.reindex(df.index.values.tolist()+['Yourindex'])


###THIS ADDS EXTRA COLUMNS TO DATAFRAME
#mentaldata)+1)))
#df=pd.concat([df, df1] , axis=1)
df=pd.concat([df, df2], axis=1)
df.to_csv(tickername+"_"+ticker2+"_"+countrycode+"_ratios.csv")
print(df)
"""

