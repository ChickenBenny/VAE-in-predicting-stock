import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class data_preprocessing():
    def init(self, file_name):
        self.file_name = file_name

    def make_data(self):
        tsmc_data = pd.read_csv(f'./{self.file_name}.csv', index_col = 'Date')
        mask = tsmc_data['Volume'] != 0
        tsmc_data = tsmc_data[mask]
        tsmc_data['High_Low'] = tsmc_data['High'] - tsmc_data['Low']
        tsmc_data['liq'] = tsmc_data['Close'] * tsmc_data['Volume']
        tsmc_data['vol_return'] = np.log(tsmc_data['Volume']/ tsmc_data['Volume'].shift(1))
        tsmc_data['day_return'] = np.log(tsmc_data['Close']/ tsmc_data['Close'].shift(1))
        for i in range(2, 31, 2):
            tsmc_data[f'{i}day_ret'] = tsmc_data['day_return'] - tsmc_data['day_return'].shift(1)
            tsmc_data[f'{i}ma'] = tsmc_data['Close'].rolling(i).mean()
            tsmc_data[f'{i}ema'] = tsmc_data['Close'].ewm(span = i).mean()
            tsmc_data[f'{i}day_ret_ma'] = tsmc_data['day_return'].rolling(i).mean()
            tsmc_data[f'{i}day_ret_ema'] = tsmc_data['day_return'].ewm(span = i).mean()
            tsmc_data[f'{i}liq_ret'] = tsmc_data['liq']/ tsmc_data['liq'].shift(1)
        tsmc_data['y_close'] = tsmc_data['Close'].shift(-1)
        tsmc_data['y_ret'] = tsmc_data['day_return'].shift(-1)
        tsmc_data.dropna(inplace = True)
        tsmc_data.drop(columns = ['High', 'Low', 'Open', 'Adj Close'], inplace = True)
        tsmc_data = tsmc_data.iloc[-1000:, :]

        train_scaler = MinMaxScaler(feature_range = (-1, 1))
        train_x = tsmc_data.iloc[:int(tsmc_data.shape[0]* 0.8), :-2]
        train_x = train_scaler.fit_transform(train_x.values).reshape(train_x.shape[0], 1, train_x.shape[1])
        test_x = tsmc_data.iloc[int(tsmc_data.shape[0]* 0.8):, :-2]
        test_x = train_scaler.transform(test_x.values).reshape(test_x.shape[0], 1, test_x.shape[1])

        #close
        close_scaler = MinMaxScaler(feature_range = (-1, 1))
        train_y_close = tsmc_data.iloc[:int(tsmc_data.shape[0]* 0.8), -2].values.reshape(-1, 1)
        train_y_close = close_scaler.fit_transform(train_y_close)
        test_y_close = tsmc_data.iloc[int(tsmc_data.shape[0]* 0.8):, -2].values.reshape(-1, 1)
        test_y_close = close_scaler.transform(test_y_close)

        #ret
        # ret_scaler = MinMaxScaler(feature_range = (0, 1))
        train_y_ret = tsmc_data.iloc[:int(tsmc_data.shape[0]* 0.8), -1].values.reshape(-1, 1)
        # train_y_ret = ret_scaler.fit_transform(train_y_close)
        test_y_ret = tsmc_data.iloc[int(tsmc_data.shape[0]* 0.8):, -1].values.reshape(-1, 1)
        # test_y_ret = ret_scaler.transform(test_y_ret)

        print('x:', train_x.shape, '\n', test_x.shape)
        print('close:', train_y_close.shape, '\n', test_y_close.shape)
        print('ret:', train_y_ret.shape, '\n', test_y_ret.shape)

        return train_scaler, close_scaler, train_x, train_y_close, train_y_ret, test_x, test_y_close, test_y_ret