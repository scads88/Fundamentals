# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:20:41 2018

@author: john3
"""
import datetime
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries

start=datetime.datetime.today()
def roundTime(dt=None, roundTo=60):
   """Round a datetime object to any time laps in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if dt == None : dt = datetime.datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)


print (roundTime(datetime.datetime(2012,12,31,23,44,59,1234),roundTo=15*60))

from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt

sp = SectorPerformances(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = sp.get_sector()
print(data.head())
data['Rank A: Real-Time Performance'].plot(kind="bar")
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()


