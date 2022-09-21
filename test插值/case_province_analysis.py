import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import matplotlib as mpl
data=pd.read_csv('pr_result_corrected\\pr_stock_lr_corrected.csv')
city=['鄂尔多斯市','黄南藏族自治州','哈尔滨市','烟台市','威海市','长沙市','东莞市','厦门市','莆田市']
# data=data[]

mpl.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False


def smooth(aa):

    index_a=aa.index

    aa.index=list(range(len(aa)))
    cc = aa.copy()
    for i in aa.index.values.tolist()[1:-1]:
        cc[i] = (aa[i - 1] + aa[i] + aa[i + 1]) / 3.0

    cc.index=index_a

    return cc

for i in range(len(city)):

    x_name = city[i]
    city_name = city[i]
    try:
        data_pr = data[data['city']==city_name ].dropna(axis=0, how='any',subset=['year','pr_stock_corrected']).sort_values(by='year')
    except Exception:
        print(1,x_name)
    try:
        data_true = data[data['city']==city_name ].dropna(axis=0, how='any',subset=['year','stock']).sort_values(by='year')
    except Exception:
        print(2,x_name)



    ax1 = plt.subplot(3,3,i+1)
    # l += 1

    try:



        plt.sca(ax1)
        #
        plt.title(city_name)
        plt.plot(data_true['year'],data_true['stock'],label='真实')
        plt.plot(data_pr['year'], smooth(data_pr['pr_stock_corrected']),label='估测')


        plt.legend()
    except Exception as e:
        print(3,e)







plt.subplots_adjust(hspace=0.5)

plt.show()