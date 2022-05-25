import pandas as pd
import numpy as np

class data_combine():
    def __init__(self, data_equity, data_price):
        self.data_equity = data_equity
        self.data_price = data_price

    def combine(self):
        self.data_equity['year'] = (self.data_equity['Date'].apply(lambda x: x.split('-')[0])).astype(int)
        self.data_equity['year'] = self.data_equity['year'] + 1911
        self.data_equity['month'] = (self.data_equity['Date'].apply(lambda x: x.split('-')[1])).astype(int)
        self.data_equity['Equity'] = (self.data_equity['Equity'].apply(lambda x: x.split('.')[0])).astype(float)* 1000/10
        self.data_equity.drop(['Date'], axis = 1, inplace = True)
        self.data_price['year'] = self.data_price['year'].astype(int)
        self.data_price['month'] = self.data_price['month'].astype(int)
        data_merge = self.data_price.merge(self.data_equity, left_on = ['year', 'month'], right_on = ['year', 'month'])
        data_merge['market_price'] = data_merge['Adj Close'] * data_merge['Equity']
        data_merge = data_merge.set_index('Date')
        return data_merge