import pandas as pd
import numpy as np
import scipy.stats
data=pd.read_csv('E:\\2015\\final_data_3\\city_data_average_spatiotemporal_withbaidu_light.csv',encoding='GBK')
data=data[['stock','register','city','year','PGDP','wage_average','P_baidu_index','DMSP_mean','P_road_area','Built_area','scale']]
data_copy=data.copy()
feature=['PGDP','wage_average','P_baidu_index','DMSP_mean','P_road_area','Built_area']
num=1

for i in ['PGDP','wage_average','P_baidu_index','DMSP_mean','P_road_area','Built_area']:


    data_copy[i][data_copy[i] > -1] =num

    num*=10
#
#
data_copy.fillna({'PGDP': 0, 'wage_average': 0, 'P_baidu_index': 0, 'DMSP_mean': 0, 'P_road_area': 0,'Built_area':0},inplace=True)
data_copy['leixing']=data_copy['stock']
data_copy['leixing']=0
data_copy['road_area']=0
# data_copy['Built_area']=0
for i in ['PGDP','wage_average','P_baidu_index','DMSP_mean','P_road_area','Built_area']:
    data_copy['leixing'] = data_copy['leixing'] + data_copy[i]
data['stock_model_chose']=data_copy['leixing']
# data_copy['leixing']=data_copy['stock']
# data_copy['leixing']=0
# data_copy['Built_area']=0
# for i in ['GDP','road_area','DMSP_sum','Built_area','baidu_index','POP']:
#
#     data_copy['leixing'] = data_copy['leixing'] + data_copy[i]
# data['register_model_chose']=data_copy['leixing']
# aa=data_copy[data_copy['leixing']==1001]
# leixing=set(data_copy['leixing'].values.tolist())





data.to_csv('E:\\2015\\final_data_3\\city_data_average_spatiotemporal_withbaidu_light_RF_2_stock.csv',index=None)