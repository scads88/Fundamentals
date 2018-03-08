# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 23:27:30 2018

@author: john3
"""

import bs4 as bs
import requests
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web



style.use("ggplot")
start=dt.datetime(2000, 1, 1)
end=dt.datetime(2017, 12, 31)
 
df=web.DataReader("AAPL", "google", start, end)

print(df.tail())
 #attribute of all dataframe objects and got a name and file extension
#df.to_csv("tsla.csv")
"""
df=pd.read_csv("tsla.csv", parse_dates=True, index_col=0)
print(df.head())
# =============================================================================
df.plot()
plt.show()
df["Close"].plot()
plt.show()
print (df[["Open", "High"]].head())
"""











resp=requests.get("https://www.marketwatch.com/investing/stock/aapl/financials")
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




values2013=values[::5]
values2014=values[1::5]
values2015=values[2::5]
values2016=values[3::5]
values2017=values[4::5]

#print(values2017)
labelsvalues2013dict={}
for label, value in zip(labels, values2013):
    labelsvalues2013dict[label]=value
labelsvalues2014dict={}
for label, value in zip(labels, values2014):
    labelsvalues2014dict[label]=value
labelsvalues2015dict={}
for label, value in zip(labels, values2015):
    labelsvalues2015dict[label]=value
labelsvalues2016dict={}
for label, value in zip(labels, values2016):
    labelsvalues2016dict[label]=value
labelsvalues2017dict={}
for label, value in zip(labels, values2017):
    labelsvalues2017dict[label]=value
  
    
#print(labelsvalues2017dict.values()[5:7])
labdic=list(labelsvalues2017dict.values())
print(labelsvalues2016dict)
# =============================================================================
# labelvalue2013dict={}
# for label, value in zip(labels, values):
#     
#         labelvalue2013dict[label]=value
# #print(labelvalue2013dict)
# =============================================================================





# =============================================================================
# dict2013={}
# 
# for value in values:
#     if values.index(value)%5==0:
#         dict2013[2013]=value
#     print(dict2013)
# 
# =============================================================================

#print(cheese)
#",".join(rows)
#print(rows)
#print(rows[::7])
#####################we have the labels and values sorted, now just need years

"""


firsttabledict={}
labelsvalueslist=list()
for row in table.findAll("td"): 
   labelsvalueslist.append(row.get_text().strip())
#",".join(rows)
print(labelsvalueslist)
print(labelsvalueslist[::7])

cheese=[]
for row in table.findAll("tr"):
    cheese.append(row.get_text().strip())
print(cheese)
"""