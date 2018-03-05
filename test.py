# -*- coding: utf-8 -*-
import re
import pandas as pd
import numpy as np
import bs4 as bs
import pickle
import requests
import csv



tickername="snn".lower()

resp=requests.get("https://www.marketwatch.com/investing/stock/" + tickername + "/profile?countrycode=uk")
soup=bs.BeautifulSoup(resp.text, "lxml")

#these two lines ID the required information from marketwatch and populate variables
fundamentallabels=[e.get_text() for e in soup.select(".sixwide .column")]
fundamentaldata=[e.get_text() for e in soup.select(".sixwide .data")]



if len(fundamentaldata)==len(fundamentallabels):
    new_dict={k:v for k, v in zip(fundamentallabels, fundamentaldata)}
    #new_dict=dict(zip(fundamentallabels, fundamentaldata))
    #print(new_dict)
else:
    print("Something is wrong with the matchu of data to label")
    
   
df=pd.DataFrame.from_dict(new_dict, orient="index")
#df["Company"]="SNN"
df.to_csv("data1.csv")
print(df.head())

gay=[e.get_text() for e in soup.select("h2")]
print(gay)
#print(gay[1:6])
# =============================================================================
# 
# biggergay=[e for e in soup.select(".block h2")]
# print(biggergay[1:6])
# =============================================================================
biggergay=[e.get_text().strip() for e in soup.select(".block div")]
print(biggergay[1:15])

