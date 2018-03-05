# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:33:53 2018

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



#might want to have a tkinter graphic user interface that feeds stock inputs




#eventually might want to have global list that that has all the company tickers
# you care about 




#global variables
tickername="aapl".lower()
ticker2="snn".lower()
countrycodespecific=False

##if have master list of multiple countries will probably want to have a for loop here iterating through
#determines if the ticker is not a USA stock
if countrycodespecific==True:
    countrycode="uk".lower()
    countrycodeurl="?countrycode="+countrycode
    print("https://www.marketwatch.com/investing/stock/" + tickername +"/profile"+ countrycodeurl)
    resp=requests.get("https://www.marketwatch.com/investing/stock/" + tickername +"/profile"+ countrycodeurl)
    soup=bs.BeautifulSoup(resp.text, "lxml")
else:
    countrycode="usa"
    resp=requests.get("https://www.marketwatch.com/investing/stock/" + tickername + "/profile")
    soup=bs.BeautifulSoup(resp.text, "lxml")
    resp2=requests.get("https://www.marketwatch.com/investing/stock/" + ticker2 + "/profile")
    soup2=bs.BeautifulSoup(resp2.text, "lxml")
#these two lines ID the required information from marketwatch and populate variables
    ##might eventually want to change fundamentaldata to fundamentalratios
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
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
print(visible_text)
"""

# =============================================================================
# 
# 
# with open("testcsv.csv", "w") as f:
#     w=csv.DictWriter(f, new_dict.keys())
#     w.writeheader()
#     w.writerow(new_dict)
#     f.close()
# 
# pd.read_csv("testcsv.csv").T.to_csv("transformtest.csv", header=False)
#   
# =============================================================================


