# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 19:16:09 2018

@author: john3
"""

#we will need to incorporate some signals for potential buy or sell that 
#will automatically trigger the generation of reports and ratios for the
#companies at hand

import bs4 as bs
import pandas as pd
import requests
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web
import sys
import numpy as np
######make into a module#####
from collections import OrderedDict

tickername="AAPL"
percentchangefilter=1
#number of days
## also want to have a subfilter to slice percent change by variations (maybe make it additive?)

style.use("ggplot")
start=dt.datetime.today()-dt.timedelta(days=10)
end=dt.datetime.today()
df=web.DataReader(tickername, "google", start, end)
df["HL_PCT"]=(df["High"]-df["Low"])/df["Low"]*100.0
df["PCT_change"]=(df["Close"]-df["Open"])/df["Open"]*100.0
print(df)


"""
df=df[["Adj. Close", "HL_PCT", "PCT_change", "Adj. Volume"]]

forecast_col="Adj. Close"
df.fillna(-99999, inplace=True)

"""
###could also have a nltk filter up here as well
#filter for generate reports
#could make a class and have different def modules to call
if all( abs(pctdeltareal)<percentchangefilter for pctdeltareal in df["PCT_change"])==True:
        sys.exit("no major moves because "+tickername+" experienced no absvalue percent change in the last 10 days was greater than "+ str(percentchangefilter)+ " percent")
else:
    #something if reformat compression above
    pass

#print("additionaL")    
"""


    if abs(i) > percentchangefilter: #if all
        print(i)
    if i > abs(percentchangefilter):
        print(type(i))
        print(i)
        print(percentchangefilter)
        break
"""
 #attribute of all dataframe objects and got a name and file extension
#df.to_csv("tsla.csv")
"""
df=pd.read_csv(tickername, parse_dates=True, index_col=0)
print(df.head())
# =============================================================================
df.plot()
plt.show()
df["Close"].plot()
plt.show()
print (df[["Open", "High"]].head())
"""




resp=requests.get("https://www.marketwatch.com/investing/stock/"+tickername+"/financials")
soup=bs.BeautifulSoup(resp.text, "lxml")
table = soup.find_all("td", class_="rowTitle")
rows=list()
for row in table:
    labels=[e.get_text().strip() for e in soup.select(".rowTitle")]
    values=[e.get_text().strip() for e in soup.select(".valueCell")]
####these are sensitive be care if fuck with them####
#values.insert(0,"Description")
labels.pop(0)
labels.pop(11)
#######################################################
##need to format values so that () goes to neg, M to million, B to billion
fucktable=list(sorted(set([e.get_text().strip() for e in soup.select("th")]))) #generates list with years, etc, redundancy; kills redundant; organizes; turns into list; forces to vbl, gets rid blank
fucktable.pop(0)
theyears=fucktable[:5]
#print(theyears)

#####should go through here and try to condense


#try to not hard code as much of this



values2013=values[::5]
values2014=values[1::5]
values2015=values[2::5]
values2016=values[3::5]
values2017=values[4::5]

labelsvalueslast5years=[]


#print(values2017)
#print(values2016)



labelsvalues2013dict={}
for label, value in zip(labels, values2013):
    labelsvalues2013dict[label]=value
    labelsvalueslast5years.append(labelsvalues2013dict)
labelsvalues2014dict={}
for label, value in zip(labels, values2014):
    labelsvalues2014dict[label]=value
    labelsvalueslast5years.append(labelsvalues2014dict)
labelsvalues2015dict={}
for label, value in zip(labels, values2015):
    labelsvalues2015dict[label]=value
    labelsvalueslast5years.append(labelsvalues2015dict)
labelsvalues2016dict={}
for label, value in zip(labels, values2016):
    labelsvalues2016dict[label]=value
    labelsvalueslast5years.append(labelsvalues2016dict)
labelsvalues2017dict={}
for label, value in zip(labels, values2017):
    labelsvalues2017dict[label]=value
    labelsvalueslast5years.append(labelsvalues2017dict)
  
# =============================================================================
# print(labelsvalues2016dict)
# print(labelsvalues2017dict)
# =============================================================================


##################could simply use the mini dicts above and make them all dataframes
###this is shit but gets resut i think 
years2labelsvaluesdict={}

    #years2labelsvaluesdict[year]=labelsvalues2013dict
    #years2labelsvaluesdict[year]=labelsvalues2014dict
    #years2labelsvaluesdict[year]=labelsvalues2015dict
    #years2labelsvaluesdict[year]=labelsvalues2016dict
    #years2labelsvaluesdict[year]=labelsvalues2017dict

years2labelsvaluesdict[theyears[0]]=labelsvalues2013dict
years2labelsvaluesdict[theyears[1]]=labelsvalues2014dict
years2labelsvaluesdict[theyears[2]]=labelsvalues2015dict
years2labelsvaluesdict[theyears[3]]=labelsvalues2016dict
years2labelsvaluesdict[theyears[4]]=labelsvalues2017dict

#print(labelsvalueslast5years)
#might want to be careful about this     #############around here is where your error is 
#butter=labelsvalueslast5years
#years2labelsvaluesdict={k:v for k, v in zip(theyears, labelsvalueslast5years)}
ticker2years2labelsvaluesdict={}
ticker2years2labelsvaluesdict[tickername]=years2labelsvaluesdict
#print(years2labelsvaluesdict.keys())
#print(ticker2years2labelsvaluesdict)   
#test=years2labelsvaluesdict.values()
#print(test)

#df=pd.concat([df, df2], axis=1)

years2labelsvaluesdict2=years2labelsvaluesdict.values()

dfx=pd.DataFrame.from_dict(years2labelsvaluesdict)# dictionary turned into a pandas dataframe
dfx.to_csv(tickername+".csv")
print("poop")


