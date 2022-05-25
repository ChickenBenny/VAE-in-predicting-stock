import time
import pandas as pd
import numpy as np
import pandas_datareader as web
import datetime as dt

class data_collector():
    def __init__(self, company):
        self.company = company

    def collect_data(self):
        start = dt.datetime(2007, 1, 1)
        end = dt.datetime(2021, 12, 31)
        data = web.DataReader(self.company, "yahoo", start, end)
        data['year'] = (data.index.strftime("%Y")).astype(int)
        data['month'] = (data.index.strftime("%m")).astype(int)
        data = data.reset_index()
        data = data[['Date', 'year', 'month', 'High', 'Low', 'Open', 'Volume', 'Close', 'Adj Close']]
        return data
