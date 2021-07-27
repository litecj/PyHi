import csv
import random

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name())

from modu.template import ChangedTemperatureONMyBirthday

def hist_show(ls , n):
    plt.hist(ls, bins=100, color='skyblue', label=f'{n}mouth')
    plt.legend()
    plt.show()

def box_show(ls):
    plt.boxplot(ls)
    plt.show()


def dice1(self):
    print(random.randint(1,6))

def dice2(n:int) ->[]:
    dice=[]
    [dice.append(random.randint(1,6)) for i in range(int(n))]
    print(dice)
    return dice

def highest_about_seoul (n:str) -> []:
    birth = ChangedTemperatureONMyBirthday ()
    birth.read_data()
    ls = []
    [ls.append(float(i[-1])) for i in birth.data if i[-1] !='' if i[0].split('-')[1] == n]
    return ls
    #aug, jan = []
    #[dataes.append(float(i[-1])) for i in data if i[-1]!='']
    #return dataes



if __name__ == '__main__':
    #hist_show(dice2 (int(input("몇번??"))))
    #hist_show(show_hist_about_seoul())
    #hist_show(highest_about_seoul(input("몇월?")), input("몇월?"))
    box_show(highest_about_seoul(input("몇월?")))