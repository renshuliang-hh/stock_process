import os
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

from pykrige.rk import RegressionKriging
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
data=pd.read_csv('2015_city_data.csv',encoding='GBK')
data_province=pd.read_csv('2015_province_data.csv')
data_p_Y=data_province[['stock']]
data_p_X=data_province[['GDP','DMSP_sum','baidu_index']]
data_p_l=data_province[['location_x','location_y']]
data_Y=data[['stock']]
data_X=data[['GDP','DMSP_sum','baidu_index']]
data_l=data[['location_x','location_y']]
train_l,test_l,train_X,test_X,train_y,test_y = train_test_split(data_l,data_X,data_Y,train_size=124,shuffle=False)


model_lr=LinearRegression().fit(train_X,train_y)
model_lr_r=model_lr.score(test_X,test_y)

model_lr_=LinearRegression()
model_lr_k=RegressionKriging(regression_model=model_lr_, n_closest_points=5)
model_lr_k.fit(train_X.values,train_l.values, train_y.values.reshape(-1))
model_lr_r_k=model_lr_k.score(test_X.values,test_l.values,test_y.values.reshape(-1))

model_rf=RandomForestRegressor().fit(train_X,train_y)
model_rf_r=model_rf.score(test_X,test_y)

model_rf_=RandomForestRegressor()
model_rf_k=RegressionKriging(regression_model=model_rf_, n_closest_points=5)
model_rf_k.fit(train_X.values,train_l.values, train_y.values.reshape(-1))
model_rf_r_k=model_rf_k.score(test_X.values,test_l.values,test_y.values.reshape(-1))



model_lr_P=LinearRegression(fit_intercept=False).fit(data_p_X,data_p_Y)
model_lr_r_P=model_lr_P.score(test_X,test_y)

model_lr_P_=LinearRegression(fit_intercept=False)
model_lr_P_k=RegressionKriging(regression_model=model_lr_P_, n_closest_points=5)
model_lr_P_k.fit(data_p_X.values,data_p_l.values, data_p_Y.values.reshape(-1))
model_lr_r_P_k=model_lr_P_k.score(test_X.values,test_l.values,test_y.values.reshape(-1))



#
model_rf_P=RandomForestRegressor().fit(data_p_X,data_p_Y)
model_rf_r_P=model_rf_P.score(test_X,test_y)

model_rf_P_=RandomForestRegressor()
model_rf_P_k=RegressionKriging(regression_model=model_rf_P_, n_closest_points=5)
model_rf_P_k.fit(data_p_X.values,data_p_l.values, data_p_Y.values.reshape(-1))
model_rf_r_P_k=model_rf_P_k.score(test_X.values,test_l.values,test_y.values.reshape(-1))

