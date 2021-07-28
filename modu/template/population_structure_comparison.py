import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager, rc
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name())


class Population_Structure_Comparison (object) :

    data: [] = list()
    name:str = ''
    name2 = ''
    home = list()
    away = None


    def read_data(self):
        # data = pd.read_csv('../data/202106_202106_연령별인구현황_월간.csv', encoding='utf-8', thousands = ',', index_col=0)
        # data.to_csv('../data/202106_202106_연령별인구현황_월간_without_comma.csv',sep=',',na_rep='NaN')
        data = csv.reader(open('../data/202106_202106_연령별인구현황_월간_without_comma.csv', encoding='utf-8'))
        next(data)
        self.data = list(data)

    def pop_per_dong(self):
        self.name = input("어느동 ")
        for i in self.data :
            if self.name in i[0]:
                self.home = np.array(i[3:], dtype=int)/int(i[2])
                self.name = i[0]

    def similar_pop_per_dong(self) -> []:
        mn = 1
        for i in self.data:
            away = np.array(i[3:], dtype=int)/int(i[2])
            s = np.sum((self.home-away)**2)  # ((self.home-self.away)**2) / (abs(self.home-self.away))
            if s < mn and self.name not in i[0]:
                mn = s
                self.name2 = i[0]
                self.away = away
        print(self.name2)


    def show_gf(self):
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 5), dpi=300)
        plt.title(self.name + '지역과 가방 비슷한 인구 구조를 가진 지역')
        plt.plot(self.home, label=self.name)
        plt.plot(self.away, label=self.name2)
        plt.legend()
        plt.show()

if __name__ == '__main__':
    pi= Population_Structure_Comparison()
    pi.read_data()
    pi.pop_per_dong()
    pi.similar_pop_per_dong()
    pi.show_gf()
