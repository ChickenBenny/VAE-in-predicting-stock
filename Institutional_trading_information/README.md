###### tags: `Finance` `Web Crawler`
# Institutional Trading Information
This project is trying to crawl the trading information of Institutional, because of my research in predicting in stock price.
* ***About this project***
     1. Institutional investment
     2. Web crawler design
     3. Rate limiting
### Instiutional investment
In stock market, investors are divided into two part by law. One is ***Natural person*** and the other is ***Juridical person***.
There are three major Juridical person in Taiwan stock market.
1. Foreign Institutional Investors.
2. Investment trust registration
3. Dealer.

And because Taiwan stock market is a thin market, which is easily be affect by many factor. Therefore, I want to crawl the information of Juridical person trading information to improve my prediction.

### Web crawler design
First go to https://www.twse.com.tw/zh/.
Try to use DevTool to find the url the data stored.
![](https://i.imgur.com/m3oCfeT.png)
We can use this url => `https://www.twse.com.tw/fund/BFI82U?response=json&dayDate={datetime}` to crawl the data.
##### Crawler design step
1. The URL need the date, so we need to develop the time parser to parse the time into the specific format.
```
    def date_list_generate(start, end): #2022-06-26 need to seperate by '-'
        date_list = pd.date_range(start, end, freq = "D").strftime("%Y%m%d").tolist()
        return date_list
```
2. Design the main function to crawl the data through the target date.
3. Try to find out the limiting rate of the server and let the program sleep during the crawling.

### Rate Limiting
Use the program to test the rate of the web limitation.
```
sdata(0) : "延遲秒:3.0  次數:200  花費時間:0d 0h 10m 7s 105sss" 
sdata(1) : "延遲秒:2.9  次數:200  花費時間:0d 0h 9m 47s 539sss" 
sdata(2) : "延遲秒:2.8  次數:200  花費時間:0d 0h 9m 47s 515sss" 
sdata(3) : "延遲秒:2.7  次數:200  花費時間:0d 0h 9m 56s 222sss" 
sdata(4) : "延遲秒:2.6  次數:200  花費時間:0d 0h 9m 34s 375sss" 
sdata(5) : "延遲秒:2.5  次數:200  花費時間:0d 0h 9m 15s 367sss" 
sdata(6) : "延遲秒:2.4  次數:200  花費時間:0d 0h 8m 54s 289sss" 
sdata(7) : "延遲秒:2.3  次數:200  花費時間:0d 0h 8m 34s 894sss" 
sdata(8) : "延遲秒:2.2  次數:200  花費時間:0d 0h 8m 14s 226sss" 
sdata(9) : "延遲秒:2.1  次數:198  花費時間:0d 0h 7m 52s 546sss" 
```
We find that each iteration sleep 2.5sec will solve the web limitation. 