import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class plot_result():
    def __init__(self, scaler, history, test_y, predict_y):
        self.scaler = scaler
        self.history = history
        self.test_y = test_y
        self.predict_y = predict_y

    def plot_predict_and_actual(self):
        plt.figure(figsize = (10, 6))
        plt.plot(self.test_y, color = 'blue', label = 'Actual Price')
        plt.plot(self.predict_y, color = 'orange', label = 'Predict Price')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend(loc = 'upper right')

    def plot_train_loss(self):
        epochs = range(len(self.history.history['loss']))
        plt.figure(figsize = (10, 6))
        plt.plot(epochs, self.history.history['loss'], label = 'Training loss')
        plt.xlabel('epochs')
        plt.ylabel('loss')
        plt.legend(loc = 'upper right')