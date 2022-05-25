from web_crawler import web_crawler
from data_collector import data_collector
from data_combine import data_combine
import numpy as np
import pandas as pd

class data_generate():
    def __init__(self, company, stock_name):
        self.company = company
        self.stock_name = stock_name

    def generator(self):
        web_crawl = web_crawler(self.company, 97, 110)
        data_after_102 = web_crawl.crawl_after_102()
        data_before_102 = web_crawl.crawl_befor_102()
        data_with_equity = np.concatenate((data_before_102, data_after_102), axis = 0)
        data_with_equity = pd.DataFrame(data_with_equity, columns = ['Date', 'Equity'])

        collector = data_collector(self.stock_name)
        data_with_price = collector.collect_data()

        combinator = data_combine(data_with_equity, data_with_price)
        all_data = combinator.combine()
        all_data.to_csv(f"./{self.company}.csv")

if __name__ == "__main__":
    company = str(input("Company name :"))
    stock_symbol = str(input("stock symbol :"))
    generator = data_generate(company, stock_symbol)
    generator.generator()