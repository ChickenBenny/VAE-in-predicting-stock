import pandas as pd
import numpy as np
import datetime as dt
import requests
import time

class web_crawler():
    def __init__(self, start, end):
        self.start = start #2022-06-26 need to seperate by '-'
        self.end = end #Do not need to consider the vacation

    def date_list_generate(self):
        date_list = pd.date_range(self.start, self.end, freq = "D").strftime("%Y%m%d").tolist()
        return date_list

    def generate_dataframe(self):
        columns = ['日期', '自營商(買賣)買進', '自營商(買賣)賣出', '自營商(買賣)買賣差額', '自營商(避險)買進', '自營商(避險)賣出', '自營商(避險)買賣差額', '投信買進', '投信賣出', '投信買賣差額', '外資買進', '外資賣出', '外資買賣差額']
        data= pd.DataFrame(columns = columns)
        return data

    def crawler(self, data, date_list):
        columns = ['自營商(買賣)買進', '自營商(買賣)賣出', '自營商(買賣)買賣差額', '自營商(避險)買進', '自營商(避險)賣出', '自營商(避險)買賣差額', '投信買進', '投信賣出', '投信買賣差額', '外資買進', '外資賣出', '外資買賣差額']
        delay_choices = [0, 0, 0, 2, 3, 1, 0, 4, 5, 0]
        for i in date_list:
            url = f"https://www.twse.com.tw/fund/BFI82U?response=json&dayDate={i}"
            res = requests.get(url)
            res = res.json()
            if res['stat'] == "OK": #Check whether that day has transaction
                df_res = pd.DataFrame.from_dict(res['data']) #the information stor in data
                df_res = df_res.drop(0, axis = 1)
                df_res = df_res.iloc[:-1, ]
                df_res = df_res.values.reshape(1, -1)
                df_res = pd.DataFrame(df_res, columns = columns)
                df_res.insert(0, '日期', dt.datetime.strptime(i, "%Y%m%d"))
                if len(df_res.columns) == len(data.columns):
                    data = data.append(df_res)
                    print(f"{i} True")
                else:
                    print(f"{i} False")
            else:
                    print(f"{i} False")
            time.sleep(2.5) 
        data.to_csv("./Institutional_information.csv")

if __name__ == "__main__":
    crawler = web_crawler("2020-01-01", "2021-12-31")
    dateList = crawler.date_list_generate()
    allData = crawler.generate_dataframe()
    crawler.crawler(allData, dateList)
