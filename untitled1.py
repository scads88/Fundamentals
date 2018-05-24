import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import datetime
import time
tickers=["MSFT", "NKE", "BA"]

import pandas as pd

#for ticker in tickers:
#    ts = TimeSeries(key="E82V6HPLXDMUN5TM")
#    data, meta_data = ts.get_intraday(ticker)
#    print(data)
    
    
print (datetime.date)
print(time.time())
print(datetime.datetime.now().strftime("%y-%m-%d"))
print(datetime.datetime.strftime)

print ("Current year: ", datetime.date.today().strftime("%Y-%M-%D"))

import datetime

mydate = datetime.date(1943,3, 13)  #year, month, day
print(mydate)


start=datetime.datetime.today()-datetime.timedelta(days=10)
end=datetime.datetime.today()

print(start)
print(end)


df['<column>'] = df['<column>'].apply(lambda dt: datetime.datetime(dt.year, dt.month, dt.day, dt.hour,15*(dt.minute // 15)))