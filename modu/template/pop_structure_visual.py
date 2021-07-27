import csv

import matplotlib.pyplot as plt
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

if __name__ == '__main__':
     pop = Population()
     pop.read_data()
     pop.show_plot(pop.pop_per_dong(input("어느 동?")))
    # pop.show_plot(pop.pop_per_dong('역삼1동'))
