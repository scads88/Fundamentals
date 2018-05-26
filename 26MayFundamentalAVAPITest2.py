# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:30:58 2018

@author: john3
"""


        
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
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries


gonogo="pass"
AVkey="E82V6HPLXDMUN5TM"


tickerbox=["OPK", "DGX", "NVTA", "LH"]
for i in tickerbox:
    tickername=i

    ts=TimeSeries(key=AVkey, output_format='pandas')

    tickerdic={}
    for ticker in tickername: 
        data, meta_data=ts.get_daily_adjusted(ticker)
        tickerdic[ticker]=data
        percentchangefilter=1
        df=data

    style.use("ggplot")
    start=dt.datetime.today()-dt.timedelta(days=10)
    end=dt.datetime.today()
    #df=web.DataReader(tickername, "google", start, end)
    df["HL_PCT"]=(df["2. high"]-df["3. low"])/df["3. low"]*100.0
    df["PCT_change"]=(df["5. adjusted close"]-df["1. open"])/df["1. open"]*100.0
    print(df.head())

###could also have a nltk filter up here as well
#filter for generate reports
#could make a class and have different def modules to call
    if gonogo=="pass":
        pass
    #elif all( abs(pctdeltareal)<percentchangefilter for pctdeltareal in df["PCT_change"])==True:
        #sys.exit("no major moves because "+tickername+" experienced no absvalue percent change in the last 10 days was greater than "+ str(percentchangefilter)+ " percent")

    resp=requests.get("https://www.marketwatch.com/investing/stock/"+tickername+"/financials")
    soup=bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find_all("td", class_="rowTitle")
    rows=list()
    for row in table:
        labels=[e.get_text().strip() for e in soup.select(".rowTitle")]
        values=[e.get_text().strip() for e in soup.select(".valueCell")]
####these are sensitive be care if fuck with them####
    labels.pop(0)
    labels.pop(11)
#######################################################
    fucktable=list(sorted(set([e.get_text().strip() for e in soup.select("th")]))) #generates list with years, etc, redundancy; kills redundant; organizes; turns into list; forces to vbl, gets rid blank
    fucktable.pop(0)
    theyears=fucktable[:5]

    values2013=values[::5]
    values2014=values[1::5]
    values2015=values[2::5]
    values2016=values[3::5]
    values2017=values[4::5]

    labelsvalueslast5years=[]

    print(values2016)
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

    years2labelsvaluesdict={}

    years2labelsvaluesdict[theyears[0]]=labelsvalues2013dict
    years2labelsvaluesdict[theyears[1]]=labelsvalues2014dict
    years2labelsvaluesdict[theyears[2]]=labelsvalues2015dict
    years2labelsvaluesdict[theyears[3]]=labelsvalues2016dict
    years2labelsvaluesdict[theyears[4]]=labelsvalues2017dict

#######################################
    ticker2years2labelsvaluesdict={}
    ticker2years2labelsvaluesdict[tickername]=years2labelsvaluesdict
    years2labelsvaluesdict2=years2labelsvaluesdict.values()
    dfx=pd.DataFrame.from_dict(years2labelsvaluesdict)# dictionary turned into a pandas dataframe
    dfx.to_csv("ass"+i+".csv")
    print("poop")
print("finalpoop")