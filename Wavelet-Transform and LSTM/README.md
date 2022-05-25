# Wavelet Transform and LSTM model to predict stock price

This project is using wavelet transform to filter the fianace signal and combing LSTM model to predict the stock price.

* ### WorkFlow
The workflow for this project is essentially in these steps:

1. Acquire stock price data.(In this project we use tsmc as target company)
2. Denoise the data using ***wavelet transform***
3. Train the model with ***LSTM*** model

* ### Data Acquisition
In this project we acquire the data by pandas_datareader an API for Yahoo Finance.
Use pandas-datareader to aquire the data.

```
pip install pandas-datareader
```
* ### Wavelet Transform
Stock data generally has noise and is non-stationary, which is a huge challenge for predict future.However wavelet transform can serve good as a very good filter to decrease the noise in stock index and smooth the data
![](https://i.imgur.com/X35VBAh.png)
The data is transformed using , then the remove coefficients that more than a full standard deviation away (out of all the coefficients), and inverse transform the new coefficients to get the denoised data.

Here is the code for how to denoise data:
```
x = np.array(self.stock_data.iloc[i: i + 11, j])                
(ca, cd) = pywt.dwt(x, "haar")                
cat = pywt.threshold(ca, np.std(ca), mode="soft")                
cdt = pywt.threshold(cd, np.std(cd), mode="soft")                
tx = pywt.idwt(cat, cdt, "db4")
```
* ### Feature
In this project we use the close price as the feature, because i am curious about whether using denoised data can help the model predict the future price more precisely.

* ### Model
Using neural networks for the prediction of time series has become widespread and the power of neural networks is well known. I have used a LSTM model for its memory property.And I compare the data with after denoised and the original data.

* ### Result
![](https://i.imgur.com/ZK8w8d6.png)
![](https://i.imgur.com/ie8fOey.png)

![](https://i.imgur.com/OrQq6qC.png)
![](https://i.imgur.com/Gl8RajA.png)

## Analysis
It seems using wavelet transform to denoise the data might not help the predict, the reason I think are as follow: 
1. When using wavelet transform to denoise the data, we need to set the threshold.However, we need to normalize the data, to get the better loss.But if we do the normalize the data will be compress in 0 to 1, which might reduce effect of denoising.
2. The data after wavelet transform is indeed more smooth than the original data, but I use the past 30 day to predict 1 day after.Smooth data might have a good effect in predicting long-term trend, but it might not help the short-term forecasting.
