import pandas as pd
import numpy as np
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

class model():
    def __init__(self, epochs, batch_size):
        self.epochs = epochs
        self.batch_size = batch_size
        

    def make_model(self, train_x, train_y, test_x):
        model = Sequential()
        model.add(LSTM(units = 50, return_sequences = True, input_shape = (30, 1)))
        model.add(Dropout(0.2))
        model.add(LSTM(units = 50, return_sequences = True))
        model.add(Dropout(0.2))
        model.add(LSTM(units = 50))
        model.add(Dropout(0.2))
        model.add(Dense(units = 1))
        model.compile(optimizer = 'adam', loss = 'mean_squared_error')
        history = model.fit(train_x, train_y, epochs = self.epochs, batch_size = self.batch_size)
        predict_y = model.predict(test_x)
        return history, predict_y