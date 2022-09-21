import pandas as pd
import numpy as np
import scipy.stats
data=pd.read_csv('E:\\2015\\final_data_2\\data_average_spatiotemporal_withbaidu_light.csv',encoding='GBK')
feature_name=data.columns.values.tolist()
feature_name.remove('register')
feature_name.remove('stock')
feature_name.remove('province')
feature_name.remove('year')
feature_name.remove('scale')
corr={}
# for i in feature_name:
#     data_cor=data.dropna(how='any',subset=['stock',i])
#     corr[i]=scipy.stats.pearsonr(data_cor['stock'], data_cor[i])[0]

data=pd.read_csv('E:\\2015\\final_data_2\\data_average_spatiotemporal_withbaidu_light.csv',encoding='GBK')
data_all=data.dropna(how='any')
data_all.to_csv('SPSS数据/data_average_province_all.csv',index=None)

data_without_bd=data.drop('baidu_index',axis=1).dropna(how='any')
data_all.to_csv('SPSS数据/data_average_province_no_bd.csv',index=None)

data_without_bd_pr=data.drop(['baidu_index','P_road_area'],axis=1).dropna(how='any')
data_all.to_csv('SPSS数据/data_average_province_no_bd_pr.csv',index=None)

