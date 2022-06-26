import requests
import pandas as pd
import numpy as np
import random
import time

class web_crawler():
    def __init__(self, target_company, start, end):
        self.target_company = target_company
        self.start = start
        self.end = end

    def crawl_after_102(self):
        # IFRS Change the version after 102.
        # Therefore, this function will crawl the data after 102.
        url = "https://mops.twse.com.tw/mops/web/ajax_t164sb03"
        # The url will help you crawl the data from Financail statement.
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
        delay_choices = [1, 3, 5, 7, 9, 11, 13, 15]
        all_data = []
        for i in range(102, self.end + 1):
            for j in range(1, 5):
                # Cause the company will release the financial statemnt 4 times a year, so we need to fetch the data 4 times a year.
                post_information = {
                    "encodeURIComponent": "1",
                    "step": "1",
                    "firstin": "1", 
                    "off": "1",
                    "queryName": "co_id",
                    "inpuType": "co_id",
                    "TYPEK": "all",
                    "isnew": "false",
                    "co_id": f"{str(self.target_company)}",
                    "year": str(i),
                    "season": "0" + str(j)
                }
                date = str(i) + "-" + str(j)
                res = requests.post(url, data = post_information, headers = {"user-Agent": user_agent})
                try:
                    if len(pd.read_html(res.text)) == 2:
                        print(f"{date} : True")
                        data = pd.read_html(res.text)[1]
                        filter = data.iloc[:, 0] == "普通股股本"
                        target = data[filter].values[0, 1]
                        date_combine = [date, target]
                        all_data.append(date_combine)
                except:
                    print(f"{date} : False")
            time.sleep(random.choice(delay_choices))    
        return all_data

    def crawl_befor_102(self):
        # This function will crawl the data before 102.
        url = "https://mops.twse.com.tw/mops/web/ajax_t05st33"
        # The url will help you crawl the data from Financail statement.
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
        delay_choices = [1, 3, 5, 7, 9, 11, 13, 15]
        all_data = []
        for i in range(self.start, 102):
            for j in range(1, 5):
                # Cause the company will release the financial statemnt 4 times a year, so we need to fetch the data 4 times a year.
                post_information = {
                    "encodeURIComponent": "1",
                    "step": "1",
                    "firstin": "1", 
                    "off": "1",
                    "queryName": "co_id",
                    "inpuType": "co_id",
                    "TYPEK": "all",
                    "isnew": "false",
                    "co_id": f"{str(self.target_company)}",
                    "year": str(i),
                    "season": "0" + str(j)
                }
                date = str(i) + "-" + str(j)
                res = requests.post(url, data = post_information, headers = {"user-Agent": user_agent})
                try:
                    if len(pd.read_html(res.text)) == 3:
                        print(f"{date} : True")
                        data = pd.read_html(res.text)[2]
                        filter = data.iloc[:, 0] == "普通股股本"
                        target = data[filter].values[0, 1]
                        date_combine = [date, target]
                        all_data.append(date_combine)
                except:
                    print(f"{date} : False")
            time.sleep(random.choice(delay_choices))    
        return all_data

    def concate_data(self, data_before_102, data_after_102):
        all_data = np.concatenate((data_before_102, data_after_102), axis = 0)
        all_data = pd.DataFrame(all_data, columns = ['Date', 'Equity'])
        return all_data