import matplotlib.pyplot as plt

from common.menu import print_menu

"""
list 값은 Y축이고, X축은 0부터 1까지 자동으로 증가한다
"""
def plot_show():
    print('Foo-------------------------')
    plt.title('color')
    plt.plot([10, 20, 30, 40], color ='skyblue', linestyle = ':', label='asc')
    plt.plot([40, 30, 20, 10], 'pink', ls='--', label='desc')
    plt.plot([50, 20, 40, 60], 'y:', label='dashed')
    plt.legend()
    plt.show()
"""
첫번째 list 값은 X축, 두번째 list 값은 Y축이다
"""
def plot_two_list_show():
    plt.plot([1,2,3,4], [12,43,25,15])
    plt.show()

def scatter():
    plt.title('marker')
    plt.plot([10, 20, 30, 40], 'r.', label='circle')
    plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
    plt.plot([50, 20, 10, 60], 'y:', label='dashed')
    plt.legend()
    plt.show()

