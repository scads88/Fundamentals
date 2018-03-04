# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:33:53 2018

@author: john3
"""


import pandas as pd

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
    print(new_dict)
else:
    print("Something is wrong with the matchu of data to label")
    
    
df=pd.DataFrame.from_dict(new_dict, orient="index")
#df.loc[0:0, "", "0"]="Labels", "Data"
print(df.head())
df.to_csv("data1.csv")
print(df.index.values)
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


