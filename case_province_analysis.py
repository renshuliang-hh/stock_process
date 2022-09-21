import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import matplotlib as mpl
# data=pd.read_csv('pr_result_corrected\\pr_stock_lr_corrected.csv')####
# data=pd.read_csv('pr_result_corrected\\pr_stock_rf_corrected.csv')####
# data=pd.read_csv('pr_result_corrected\\pr_stock_lr_noi_corrected.csv')####
# data=pd.read_csv('pr_result_corrected\\pr_stock_lr_i_corrected.csv')####
data=pd.read_csv('pr_result_corrected\\pr_stock_lr_i_corrected_2.csv')####
# data=pd.read_csv('new_pr_result_corrected\\ONLY_GDP_add_pr_stock_lr_i_corrected_5.csv')####
# data=pd.read_csv('new_pr_result_corrected\\ONLY_GDP_time_pr_stock_lr_i_corrected_2.csv')####
# data=pd.read_csv('new_pr_result_corrected\\ONLY_GDP_add_pr_stock_lr_NOi_corrected_2.csv')
# data=pd.read_csv('new_pr_result_corrected\\ONLY_GDP_time_pr_stock_lr_NOi_corrected_2.csv')
# data=pd.read_csv('new_pr_result_corrected\\ONLY_GDP_PMSD_add_pr_stock_lr_i_corrected_2.csv')####
# data=pd.read_csv('new_pr_result_corrected\\ONLY_GDP_PMSD_time_pr_stock_lr_i_corrected_2.csv')####
# data=pd.read_csv('new_pr_result_corrected\\ONLY_GDP_PMSD_add_pr_stock_lr_NOi_corrected_2.csv')####
# data=pd.read_csv('new_pr_result_corrected\\ONLY_GDP_PMSD_time_pr_stock_lr_NOi_corrected_2.csv')####
# city=['广州市','深圳市']
# city=['武汉市','青岛市','南京市','长沙市']
# city=['哈尔滨市','济南市','太原市','中山市']
# city=['淄博市','信阳市','绵阳市','桂林市']
# city=['德州市','拉萨市','荆门市','黔南布依族苗族自治州']
city=['那曲市','白银市','酒泉市','赤峰市']
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



    ax1 = plt.subplot(3,2,i+1)
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