import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn import ensemble
from sklearn.metrics import r2_score

from xgboost import XGBRegressor
data=pd.read_csv('SPSS数据\\data_average_province_no_bd.csv')
# data=pd.read_csv('data_spatiotemporal_wispearmanrthbaidu_light_SPSS.csv')
y1=data[['register']].values
y2=data[['stock']].values
x=data.drop(['register','stock','province','year','scale'],axis=1)
x_name=x.columns

mm=MinMaxScaler()
x = mm.fit_transform(x)
model=ensemble.RandomForestRegressor()
# model=XGBRegressor(objective='reg:linear',booster='gblinear',n_estimators=50)
model.fit(x,y1)
p_y=model.predict(x)
r=r2_score(y1,p_y)
important=model.feature_importances_
important=pd.DataFrame(important)
important.index=x_name
important=important.sort_values(by=0,ascending=False)

# objective='reg:linear',booster='gblinear',