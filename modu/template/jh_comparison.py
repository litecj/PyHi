import csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy


class Population(object):
    data: [] = list()

    def read_data(self):
        df = pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', encoding='utf-8', index_col=0, thousands=',')
        # print(df)
        df.to_csv('./data/202106_202106_연령별인구현황_월간_without_comma.csv', sep=',', na_rep='NaN')
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간_without_comma.csv', encoding='utf-8'))
        next(data)
        self.data = data

    def pop_per_dong(self, dong: str) -> []:
        mn = 1
        ls = []
        self.read_data()
        for i in self.data:
            if dong in i[0]:
                arr1 = numpy.array(i[3:], dtype=int) / int(i[2])
        self.read_data()
        for i in self.data:
            arr2 = numpy.array(i[3:], dtype=int) / int(i[2])
            s = np.sum(arr1-arr2)
            if s < mn:
                mn = s
                dong2 = i[0]
                result = arr2
        plt.rc('font', family='Malgun Gothic')
        plt.plot(arr1, label=dong)
        plt.plot(arr2, label=dong2)
        plt.legend()
        plt.show()

    def show_plot(self, arr: [], name):
        plt.rc('font', family='Malgun Gothic')
        plt.title('인구 차이?')
        plt.style.use('ggplot')
        plt.plot(arr, label=f'{name}')
        plt.show()


if __name__ == '__main__':
    pop = Population()
    # pop.show_plot(pop.pop_per_dong('방이1동'))
    pop.pop_per_dong('필동')