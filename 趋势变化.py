import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import matplotlib as mpl
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
data_pro_z=pd.read_csv('E:\\2015\\final_data_3\\data_spatiotemporal_withbaidu_light.csv',encoding='GBK')
# data_pro_z=pd.read_csv('province_data/data_province_all.csv')
# data_pro_aver_z=pd.read_csv('province_data/data_average_spatiotemporal_withbaidu_light.csv', encoding='GBK')

data_city=pd.read_csv('E:\\2015\\final_data_3\\city_data_spatiotemporal_withbaidu_light_lr.csv')

city_screan=pd.read_csv('E:\\2015\\test_city_data.csv',encoding='GBK')
data_city=pd.merge(data_city,city_screan,how='left',left_on='city',right_on='市')
data_city=data_city[data_city['label']==1]
# data_city_aver=pd.read_csv('city_data/city_data_average_spatiotemporal_withbaidu_light.csv', encoding='GBK')

feature_name=data_pro_z.columns.values.tolist()

feature_name.remove('register')
feature_name.remove('stock')
feature_name.remove('province')
feature_name.remove('year')
feature_name.remove('scale')


# for i in range(5):
#     for j in range(4):
#         ax = plt.subplot2grid((5,4), (i,j))
#         ax.scatter(range(20),range(20)+np.random.randint(-5,5,20))
for i in range(len(feature_name)):

    x_name = feature_name[i]
    chinese_name = feature_name[i]
    try:
        data_pro = data_pro_z[['register', x_name]].dropna(axis=0, how='any')
    except Exception:
        print(1,x_name)
    try:
        data_c = data_city[['register', x_name]].dropna(axis=0, how='any')
    except Exception:
        print(2,x_name)


    print(1)
    ax1 = plt.subplot(2,3,i+1)
    # l += 1

    try:
        plt.sca(ax1)
        sns.regplot(x=x_name, y='register', data=data_pro, label='Province')
        sns.regplot(x=x_name, y='register', data=data_c, label='City')
        plt.legend()
    except Exception:
        print(3,'pic')

mpl.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False





plt.subplots_adjust(hspace=0.5)

plt.show()
