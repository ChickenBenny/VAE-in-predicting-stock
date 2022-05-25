import pandas as pd
import numpy as np

class read_data():
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        data = pd.read_excel(f'./{self.filename}.xlsx', index_col = 0)
        volume_mask = data['Volume'] != 0
        data = data[volume_mask].dropna()
        data.to_csv(f'./{self.filename}_split.csv')

if __name__ == '__main__':
    data = read_data('Tsmc')
    data.read_csv()
