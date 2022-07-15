###### tags: `Finance`
# Technical indicator generator
### How to start
1. Clone this project
```
rmdir generator && cd generator
```
2. Import the package
```
from generator import Generator
```


This package is used to generator the feature to train the ML and DL model. Whenever I start a new model, I will write the same code, so I decide to write the generator package to avoid doing things repeatly.
### Simple Moving Average(SMA)
A simple moving average (SMA) calculates the average of a selected range of prices, usually closing prices, by the number of periods in that range.

### Exponential Moving Average(EMA)
An exponential moving average (EMA) is a type of moving average (MA) that places a greater weight and significance on the most recent data points. The exponential moving average is also referred to as the exponentially weighted moving average. An exponentially weighted moving average reacts more significantly to recent price changes than a simple moving average simple moving average (SMA), which applies an equal weight to all observations in the period.

### Moving Average Convergence Divergence
Moving average convergence divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. The MACD is calculated by subtracting the long-period exponential moving average (EMA) from the short-period EMA.

### Relative Strength Index
RSI measures the speed and magnitude of a security's recent price changes to evaluate overvalued or undervalued conditions in the price of that security.

### Average True Range
The true range indicator is taken as the greatest of the following: current high less the current low; the absolute value of the current high less the previous close; and the absolute value of the current low less the previous close. The ATR is then a moving average, generally using 14 days, of the true ranges.

### Bollinger Band
A Bollinger Band is a technical analysis tool defined by a set of trendlines plotted two standard deviations (positively and negatively) away from a simple moving average (SMA) of a security's price, but which can be adjusted to user preferences.