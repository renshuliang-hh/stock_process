import os
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

from pykrige.rk import RegressionKriging
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
data_pop=pd.read_csv('AA/2015_city_data.csv')
data_pop['POP_']=data_pop['GDP']/data_pop['PGDP']*10000
data_pop=data_pop[['city','POP_']]

data=pd.read_csv('2015_city_average_data.csv')
data=pd.merge(data,data_pop,how='left',left_on='city',right_on='city')
data=data[['stock','PGDP','taxi','DMSP_sum','wage_average','autobus','P_baidu_index','location_x','location_y','POP_']].dropna(how='any')


data_province=pd.read_csv('2015_province_average_data.csv',encoding='GBK')
data_province=data_province[['stock','PGDP','taxi','DMSP_sum','wage_average','autobus','P_baidu_index','location_x','location_y']].dropna(how='any')

data_p_Y=data_province[['stock']]
data_p_X=data_province[['PGDP','taxi','DMSP_sum','wage_average','autobus','P_baidu_index']]
data_p_l=data_province[['location_x','location_y']]
data_Y=data[['stock']]
data_X=data[['PGDP','taxi','DMSP_sum','wage_average','autobus','P_baidu_index']]
data_l=data[['location_x','location_y']]
data_pop=data[['POP_']]
train_l,test_l,train_X,test_X,train_y,test_y,_,test_pop = train_test_split(data_l,data_X,data_Y,data_pop,test_size=0.5)

model_lr=LinearRegression().fit(train_X,train_y)
model_lr_r=r2_score(test_y.values*test_pop,model_lr.predict(test_X)*test_pop)

model_lr_=LinearRegression()
model_lr_k=RegressionKriging(regression_model=model_lr_, n_closest_points=10)
model_lr_k.fit(train_X.values,train_l.values, train_y.values.reshape(-1))
# model_lr_r_k=model_lr_k.predict(test_X.values,test_l.values)
model_lr_r_K=r2_score(test_y.values*test_pop,model_lr_k.predict(test_X.values,test_l.values).reshape(-1,1)*test_pop)


model_rf=RandomForestRegressor().fit(train_X,train_y)
# model_rf_r=model_rf.score(test_X,test_y)
model_rf_r=r2_score(test_y.values*test_pop,model_rf.predict(test_X).reshape(-1,1)*test_pop)


model_rf_=RandomForestRegressor()
model_rf_k=RegressionKriging(regression_model=model_rf_, n_closest_points=10)
model_rf_k.fit(train_X.values,train_l.values, train_y.values.reshape(-1))
# model_rf_r_k=model_rf_k.score(test_X.values,test_l.values,test_y.values.reshape(-1))
model_rf_r_K=r2_score(test_y.values*test_pop,model_rf_k.predict(test_X.values,test_l.values).reshape(-1,1)*test_pop)


model_lr_P=LinearRegression().fit(data_p_X,data_p_Y)
# model_lr_r_P=model_lr_P.score(test_X,test_y)
model_lr_r_P=r2_score(test_y.values*test_pop,model_lr_P.predict(test_X)*test_pop)

model_lr_P_=LinearRegression()
model_lr_P_k=RegressionKriging(regression_model=model_lr_P_, n_closest_points=10)
model_lr_P_k.fit(data_p_X.values,data_p_l.values, data_p_Y.values.reshape(-1))
model_lr_r_P_k=model_lr_P_k.score(test_X.values,test_l.values,test_y.values.reshape(-1))



#
model_rf_P=RandomForestRegressor().fit(data_p_X,data_p_Y)
model_rf_r_P=model_rf_P.score(test_X,test_y)
#
model_rf_P_=RandomForestRegressor()
model_rf_P_k=RegressionKriging(regression_model=model_rf_P_, n_closest_points=10)
model_rf_P_k.fit(data_p_X.values,data_p_l.values, data_p_Y.values.reshape(-1))
model_rf_r_P_k=model_rf_P_k.score(test_X.values,test_l.values,test_y.values.reshape(-1))