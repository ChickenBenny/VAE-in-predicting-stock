import pandas as pd
import numpy as np
import pywt
from sklearn.preprocessing import MinMaxScaler

# all_data_1 = tsmc_data.iloc[:724, :] 2000 - 2003
# all_data_2 = tsmc_data.iloc[724:1470, :] 2003 - 2006
# add_data_3 = tsmc_data.iloc[1470:2209, :] 2006 - 2009
# add_data_4 = tsmc_data.iloc[2209:2953, :] 2009 - 2012
# add_data_5 = tsmc_data.iloc[2953:3690, :] 2012 - 2015
# all_data_6 = tsmc_data.iloc[3690:4419, :] 2015 - 2018
# all_data_7 = tsmc_data.iloc[4419:, :] 2018 - 2020

class make_train_test():
    def __init__(self, all_data, train_start, train_end, test_end, window):
        self.all_data = all_data
        self.train_start = train_start
        self.train_end = train_end
        self.test_end = test_end
        self.window = window

    def make_feature(self):
        self.all_data['log_ret'] = np.log(self.all_data['Close']/ self.all_data['Close'].shift(1))

    def make_train(self, target_feature):
        scaler = MinMaxScaler(feature_range = (0, 1))
        target_data = scaler.fit_transform(self.all_data.iloc[self.train_start: self.train_end, target_feature].values.reshape(-1, 1)).reshape(-1, )
        train_x = []
        train_y = []
        wavelet_transform_x = []
        for i in range(self.window, target_data.shape[0]):
            x = target_data[i - self.window: i]
            y = target_data[i]
            (ca, cd) = pywt.dwt(x, 'db4')
            caT = pywt.threshold(ca, np.std(ca), mode = 'soft')
            cdT = pywt.threshold(cd, np.std(cd), mode = 'soft')
            tx = pywt.idwt(caT, cdT, 'db4')
            train_x.append(x)
            wavelet_transform_x.append(tx)
            train_y.append(y)
        train_x = np.array(train_x)
        train_x = train_x.reshape(train_x.shape[0], train_x.shape[1], 1)
        wavelet_transform_x = np.array(wavelet_transform_x)
        wavelet_transform_x = wavelet_transform_x.reshape(wavelet_transform_x.shape[0], wavelet_transform_x.shape[1], 1)
        train_y = np.array(train_y)
        return train_x, train_y, wavelet_transform_x, scaler

    def make_test(self, target_feature, scaler):
        target_data = scaler.transform(self.all_data.iloc[self.train_end: self.test_end, target_feature].values.reshape(-1, 1)).reshape(-1, )
        test_x = []
        test_y = []
        wavelet_transform_test_x = []
        for i in range(self.window, target_data.shape[0]):
            x = target_data[i - self.window: i]
            y = target_data[i]
            wavelet_transform_test_x = []
            (ca, cd) = pywt.dwt(x, 'db4')
            caT = pywt.threshold(ca, np.std(ca), mode = 'soft')
            cdT = pywt.threshold(cd, np.std(cd), mode = 'soft')
            tx = pywt.idwt(caT, cdT, 'db4')
            test_x.append(x)
            wavelet_transform_test_x.append(tx)
            test_y.append(y)
        test_x = np.array(test_x)
        test_x = test_x.reshape(test_x.shape[0], test_x.shape[1], 1)
        wavelet_transform_test_x = np.array(wavelet_transform_test_x)
        wavelet_transform_test_x = wavelet_transform_test_x.reshape(wavelet_transform_test_x.shape[0], wavelet_transform_test_x.shape[1], 1)
        test_y = np.array(test_y)
        return test_x, test_y, wavelet_transform_test_x

