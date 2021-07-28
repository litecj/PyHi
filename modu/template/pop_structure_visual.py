import csv

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name())


class Population():

    data : [] = list()

    def read_data(self):
        data = csv.reader(open('../data/202106_202106_연령별인구현황_월간.csv', encoding='utf-8'))
        next(data)
        self.data = data

    def pop_per_dong(self,dong) -> []:
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]]
        return  arr

    def show_plot(self, arr:[]):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()

    def population_structure_comparison(self):
        data = csv.reader(open('../data/202106_202106_연령별인구현황_월간.csv', encoding='utf-8'))
        next(data)
        data=list(data)

        name = input("어느동?")
        mn = 1
        result_name = ''
        result = 0

        for i in data :
            if name in i[0]:
                home = np.array(i[3:], dtype=int)/int(i[2].replace(',',''))

        for i in data :
            away = np.array(i[3:], dtype=int)/int(i[2].replace(',',''))
            s = np.sum((home-away)**2)
            if s < mn and name not in i[0] :
                mn = s
                result_name = i[0]
                result = away

        plt.style.use('ggplot')
        plt.figure(figsize=(10, 5), dpi=300)
        plt.title(name + '지역과 가방 비슷한 인구 구조를 가진 지역')
        plt.plot(home, label=name)
        plt.plot(result, label=result_name)
        plt.legend()
        plt.show()

    def show_population_structure_comparison(self, name, home, result, result_name):
        plt.style.use('ggplot')
        plt.figure(figsize=(10,5), dpi=300)
        plt.title(name + '지역과 가방 비슷한 인구 구조를 가진 지역')
        plt.plot(home, label=name)
        plt.plot(result, label = result_name)
        plt.legend()
        plt.show()

if __name__ == '__main__':
     pop = Population()
     #pop.read_data()
     # pop.show_plot(pop.pop_per_dong(input("어느 동?")))
     # pop.show_plot(pop.pop_per_dong('역삼1동'))
     pop.population_structure_comparison()