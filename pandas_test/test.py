import pandas as pd
import pandas_datareader.data as web

pdata = pd.Panel(dict((stk,web.get_data_yahoo(stk,'1/1/2009','6/1/2012')) for stk in ['AAPL','GOOG','MSFT','DELL']))


print pdata

