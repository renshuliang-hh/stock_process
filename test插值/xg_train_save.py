import pandas as pd
import numpy as np
import scipy.stats
from xgboost import XGBRegressor
from sklearn import ensemble
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
data_test=pd.read_csv('E:\\2015\\final_data_3\\city_data_spatiotemporal_withbaidu_light_lr.csv')
data_train=pd.read_csv('E:\\2015\\final_data_3\\data_spatiotemporal_withbaidu_light.csv',encoding='GBK')
data_test['pr_register']=np.nan
register_feature=set(data_test['register_model_chose'].values.tolist())
feature_map={
    1:'GDP',
10:'road_area',
100:'DMSP_sum',
1000:'Built_area',
10000:'baidu_index',
100000:'POP'
}
def minmaxscale(data_,mm_n):
    for i in mm_n:
        test = data_[i]
        max = test.max()
        min = test.min()
        data_[i]= (test - min) / (max - min)


    return data_



data_all=pd.concat([data_train,data_test])
data_all=minmaxscale(data_all.copy(),['GDP','road_area','DMSP_sum','Built_area','baidu_index','POP'])
data_train_=data_all[data_all['scale']==1]
data_train_.index=data_train.index
data_test_=data_all[data_all['scale']==2]
data_test_.index=data_test.index
def select_feature(feature_label):
    feature_name=[]
    for i in [1,10,100,1000,10000,100000]:
        a = (feature_label // i % 10)*i
        try:
            feature_name.append(feature_map[a])
        except KeyError:
            pass

    return feature_name

for feature_num in register_feature:
    feature_name = select_feature(feature_num)
    if len(feature_name) !=0:

        train_data_x=data_train_.dropna(how='any',subset=feature_name)[feature_name]
        train_data_y=data_train_.dropna(how='any',subset=feature_name)['register']
        # model=LinearRegression(fit_intercept=False)
        model = ensemble.RandomForestRegressor()
        # model=XGBRegressor(objective='reg:linear',booster='gblinear',n_estimators=50)

        model.fit(train_data_x,train_data_y)
        pr_data_x=data_test_[data_test_['register_model_chose']==feature_num][feature_name]
        pr_data_y=model.predict(pr_data_x)
        # pr_data_y=pd.DataFrame(model.predict(pr_data_x))
        # pr_data_y.index=pr_data_x.index
        data_test['pr_register'][data_test['register_model_chose']==feature_num]=pr_data_y
        print(feature_num, feature_name)
        # break
data_test.to_csv('pr_result\\pr_register_rf.csv')
city_screan=pd.read_csv('E:\\2015\\test_city_data.csv',encoding='GBK')
data_city=pd.merge(data_test,city_screan,how='left',left_on='city',right_on='市')
data_city=data_city[data_city['label']==1]
from sklearn.metrics import r2_score
data_city=data_city.dropna(how='any',subset=['register','pr_register'])
register_r=r2_score(data_city['register'],data_city['pr_register'])













