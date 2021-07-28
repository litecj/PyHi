import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager, rc
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name())

def similar_pandas():
    df = pd.read_csv('../data/uint_15_age.csv', encoding='UTF-8', index_col=0)
    df = df.div(df['총인구수'], axis=0)
    del df['총인구수'], df['연령구간인구수']

    name = input('원하는 지역의 이름을 입력해주세요 : \n')
    a = df.index.str.contains(name)
    df2 = df[a]


    # x = df.sub(df2.iloc[0], axis=1)


    df.loc[np.power(df.sub(df2.iloc[0], axis=1), 2).sum(axis=1).sort_values().index[:5]].T.plot()

    plt.show()


if __name__ == '__main__':
    similar_pandas()