import random

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name())

from modu.template import ChangedTemperatureONMyBirthday
from modu.template.basic_hist import highest_about_seoul

def sorted_random_arr() -> []:
    arr = []
    [arr.append(random.randint(1,1000))for i in range(13)]
    return arr

def box_show(ls):
    plt.boxplot(ls)
    plt.show()

def box_show_hi(n):
    plt.boxplot(highest_about_seoul(n))
    plt.show()

def box_show_day(ls):
    plt.style.use('ggplot')
    plt.figure(figsize=(10,5), dpi=300)
    plt.boxplot(ls, showfliers=False)
    plt.show()

def show_box_month (n:str):
    ls = highest_about_seoul(n)
    return ls

def show_box_all_month():
    birth = ChangedTemperatureONMyBirthday()
    birth.read_data()
    ls=[]
    [ls.append([]) for i in range(12)]
    [ls[int(i[0].split('-')[1]) - 1].append(float(i[-1])) for i in birth.data if i[-1] !='']
    return ls

def show_box_all_month2 ():
    ls = []
    [ls.append(highest_about_seoul((str(i + 1) if len(str(i+1))==2 else str('0'+str(i + 1))))) for i in range(12)]
    plt.boxplot([i for i in ls])
    return ls

def show_box_per_date():
    birth = ChangedTemperatureONMyBirthday()
    birth.read_data()
    ls = []
    [ls.append([]) for i in range(31)]
    [ls[int(i[0].split('-')[2]) - 1].append(float(i[-1]))
        for i in birth.data
            if i[-1] != ''
                if i [0].split('-')[1]=='08']
    return ls

if __name__ == '__main__':
    #box_show_hi(input("몇월?"))
    # box_show(show_box_all_month())
    # box_show(show_box_all_month2())
    # box_show(show_box_per_date())
    box_show_day(show_box_per_date())

