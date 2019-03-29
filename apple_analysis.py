import pandas as pd

def quarter_volume():
   data=pd.read_csv('apple.csv',header=0)
   #print(data)

   list_d=list(data['Date'])
   list_v=list(data['Volume'])
   d_timeindex=pd.to_datetime(list_d)
   #print(d_timeindex)
   s1=pd.Series(list_v,index=d_timeindex)
   return sorted(list(s1.resample('Q').sum()))[-2]
quarter_volume()
