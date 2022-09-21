import pandas as pd
import numpy as np
import scipy.stats
from sklearn import ensemble
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data_test = pd.read_csv('E:\\2015\\final_data_3\\city_data_average_spatiotemporal_withbaidu_light_lr_stock.csv')
data_train = pd.read_csv('E:\\2015\\final_data_3\\data_average_spatiotemporal_withbaidu_light.csv', encoding='GBK')
data_test['pr_stock'] = np.nan
stock_feature = set(data_test['stock_model_chose'].values.tolist())
feature_map = {
    1: 'GDP',
    10: 'road_area',
    100: 'DMSP_sum',
    1000: 'Built_area',
    10000: 'baidu_index',
    100000: 'POP'
}


def minmaxscale(data_, mm_n):
    for i in mm_n:
        test = data_[i]
        max = test.max()
        min = test.min()
        data_[i] = (test - min) / (max - min)
    return data_
feature_name=['PGDP']

data_all = pd.concat([data_train, data_test])
data_all = minmaxscale(data_all.copy(), feature_name)
data_train_ = data_all[data_all['scale'] == 1]
data_train_.index = data_train.index
data_test_ = data_all[data_all['scale'] == 2]
data_test_.index = data_test.index


def select_feature(feature_label):
    feature_name = []
    for i in [1, 10, 100, 1000, 10000, 100000]:
        a = (feature_label // i % 10) * i
        try:
            feature_name.append(feature_map[a])
        except KeyError:
            pass

    return feature_name



train_data_x = data_train_.dropna(how='any', subset=feature_name)[feature_name]
train_data_y = data_train_.dropna(how='any', subset=feature_name)['stock']
model = LinearRegression(fit_intercept=False)
# model = ensemble.RandomForestRegressor()
train_data_x_=PolynomialFeatures(degree=3).fit_transform(train_data_x)
model.fit(train_data_x_, train_data_y)
# model.intercept_ = 0
feature_name_test=feature_name.copy()
feature_name_test.insert(0,'stock')
pr_data_x = data_test_.dropna(how='any', subset=feature_name_test)
true_test_y=data_test_.dropna(how='any', subset=feature_name_test)[['stock']]
pr_data_x_=PolynomialFeatures(degree=3).fit_transform(pr_data_x[feature_name])
pr_data_y = model.predict(pr_data_x_)
from sklearn.metrics import r2_score
pr_data_y=pd.DataFrame(pr_data_y)
pr_data_y.index=true_test_y.index
stock_r = r2_score(true_test_y, pr_data_y)
pr_data_x['pr_stock']=pr_data_y
#
# # break
# pr_data_x.to_csv('new_pr_result\\pr_stock_lr_NOi_ONLY_GDP_build.csv')
city_screan = pd.read_csv('E:\\2015\\test_city_data.csv', encoding='GBK')
data_city = pd.merge(pr_data_x, city_screan, how='left', left_on='city', right_on='市')
data_city = data_city[data_city['label'] == 1]
from sklearn.metrics import r2_score
#
data_city = data_city.dropna(how='any', subset=['stock', 'pr_stock'])
stock_r_2 = r2_score(data_city['stock'], data_city['pr_stock'])
