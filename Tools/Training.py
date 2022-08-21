import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import matplotlib.pyplot as plt

def training_AE(model, data, num_epochs, learning_rate):
    use_cuda = 1
    device = torch.device("cuda" if (torch.cuda.is_available() & use_cuda) else "cpu")
    model = model.to(device)
    loss_func = nn.MSELoss().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

    hist = np.zeros(num_epochs)
    for epoch in range(num_epochs):
        total_loss = 0
        loss_ = []
        for (x, y) in data:
            code, decode = model(x.to(device))
            loss = loss_func(decode, x)
            loss.backward()
            optimizer.step()
            loss_.append(loss.item())
        hist[epoch] = sum(loss_)
        if epoch % 10 == 0:
            print('[{}/{}] Loss:'.format(epoch+1, num_epochs), sum(loss_))

    plt.figure(figsize=(12, 6))
    plt.plot(hist)
    return model


def training_VAE(model, data, num_epochs, learning_rate):
    use_cuda = 1
    device = torch.device("cuda" if (torch.cuda.is_available() & use_cuda) else "cpu")
    model = model.to(device)   
    optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

    hist = np.zeros(num_epochs) 
    for epoch in range(num_epochs):
        total_loss = 0
        loss_ = []
        for (x, y) in data:
            output, z, mu, logVar = model(x.to(device))
            kl_divergence = 0.5* torch.sum(-1 - logVar + mu.pow(2) + logVar.exp())
            loss = F.binary_cross_entropy(output, x) + kl_divergence
            loss.backward()
            optimizer.step()
            loss_.append(loss.item())
        hist[epoch] = sum(loss_)
        if epoch % 10 == 0:
            print('[{}/{}] Loss:'.format(epoch+1, num_epochs), sum(loss_))

    plt.figure(figsize=(12, 6))
    plt.plot(hist)
    return model        

def sliding_window(x, y, window):
    x_ = []
    y_ = []
    for i in range(window, x.shape[0]):
        tmp_x = x[i - window: i, :]
        tmp_y = y[i]
        x_.append(tmp_x)
        y_.append(tmp_y)
    x_ = torch.from_numpy(np.array(x_)).float()
    y_ = torch.from_numpy(np.array(y_)).float()

    return x_, y_

def training_LSTM(model, data, num_epochs, learning_rate):
    use_cuda = 1
    device = torch.device("cuda" if (torch.cuda.is_available() & use_cuda) else "cpu")
    loss_fumc = torch.nn.MSELoss()
    optimiser = torch.optim.Adam(model.parameters(), lr = learning_rate)

    hist = np.zeros(num_epochs)
    for epoch in range(num_epochs):
        loss_ = []
        y_pred = []
        for i, (x, y) in enumerate(data):
            x = x.to(device)
            y = y.to(device)
            y_train_pred = model(x)
            loss = loss_fumc(y_train_pred, y)
            loss_.append(loss.item())
            y_pred.append(y_train_pred)
            optimiser.zero_grad()
            loss.backward()
            optimiser.step()
        hist[epoch] = sum(loss_)
        if epoch % 10 == 0:
            print('[{}/{}] Loss:'.format(epoch+1, num_epochs), sum(loss_))

    plt.figure(figsize = (12, 6))
    plt.plot(hist)
    return model