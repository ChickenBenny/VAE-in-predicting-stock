# Monitor the industry by making index with web crawling
This project try to monitor the industry by making your own index.

### What you will get in this project
1. What is weighted Index.
2. What the difference between book value and market value.
3. How to use web-crawling to get the stock information.
4. How to build the index you own and try to monitor the industry.

### WorkFlow in this project
1. Analyze the industry, and focus on the industry which you are interested.
2. Selct the company which you are interested.
3. Use web-scrapying to collect the data, and compute the company market value.
![](https://i.imgur.com/9YStXAi.png)

### Requirement
* Python 3.6 or above
* requests
* pandas
* numpy
* pandas data-reader
* time

### Project structure
```
├── main.py
├── data_collector.py(use pandas datareader to collect data)
├── web_crawler.py(crawling the common stock share)
├── data_combine.py(combine the data and compute the index)
```

### Start
Investing can simply divide into two groups, one is index investing and the other is active investing. Most of people do the active investing and try to select the stock on its own. For me I am interesting in new technology, though most of the stock I invested are high-tech companies. However, high-tech companies usally are more risky. So how can I monitor the industry situation?

One simple way to solve the problem is that we can make a industry index like NASDQ, but the index only contain the company in the industry which we are invested.

### What is weighted Index
Weighted index is a index makes by many company, and will be divide in to price-weighted index and capitalization-weighted index.
* Price-weighted index : Sum all the stock as the denominator.(higher price will have higher weight)
* Capitalization-weighted index : Sum all the company value(market value) as denominator.

### Book value v.s Market value
* Book value : The book value is similar to a firm's net asset value, which jumps around much less than stock prices.
* Market value : The market value depends on what people are willing to pay for a company's stock.

### How to compute the market value?
1. Use pandas datareader to get the price of a company.
2. Use web crawling to get the common stock share.
3. Market value = common stock share * stock close price

