from sklearn.preprocessing import MinMaxScaler

def train_test_split(data, split_rate):
    x = data.iloc[:, :60].values
    y = data.iloc[:, 60].values

    split = int(data.shape[0]* 0.8)
    train_x, test_x = x[: split, :], x[split - 20:, :]
    train_y, test_y = y[: split, ], y[split - 20: , ]

    print(f'trainX: {train_x.shape} trainY: {train_y.shape}')
    print(f'testX: {test_x.shape} testY: {test_y.shape}')

    x_scaler = MinMaxScaler(feature_range = (0, 1))
    y_scaler = MinMaxScaler(feature_range = (0, 1))

    train_x = x_scaler.fit_transform(train_x)
    test_x = x_scaler.transform(test_x)

    train_y = y_scaler.fit_transform(train_y.reshape(-1, 1))
    test_y = y_scaler.transform(test_y.reshape(-1, 1))

    return x_scaler, y_scaler, train_x, train_y, test_x, test_y
