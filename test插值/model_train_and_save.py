import pandas as pd
import numpy as np
import scipy.stats
data=pd.read_csv('E:\\2015\\final_data_2\\city_data_spatiotemporal_withbaidu_light.csv')
data=data[['stock','register','city','year','GDP','road_area','DMSP_sum','Built_area','baidu_index','POP','scale']]
data_copy=data.copy()
feature=['GDP','road_area','DMSP_sum','Built_area','baidu_index']
num=1

for i in ['GDP','road_area','DMSP_sum','Built_area','baidu_index','POP']:


    data_copy[i][data_copy[i] > -1] =num

    num*=10
#
#
data_copy.fillna({'GDP': 0, 'road_area': 0, 'DMSP_sum': 0, 'Built_area': 0, 'baidu_index': 0,'POP':0},inplace=True)
data_copy['leixing']=data_copy['stock']
data_copy['leixing']=0
for i in ['GDP','road_area','DMSP_sum','Built_area','baidu_index','POP']:
    data_copy['leixing'] = data_copy['leixing'] + data_copy[i]
data['stock_model_chose']=data_copy['leixing']
data_copy['leixing']=data_copy['stock']
data_copy['leixing']=0
# data_copy['Built_area']=0
for i in ['GDP','road_area','DMSP_sum','Built_area','baidu_index','POP']:

    data_copy['leixing'] = data_copy['leixing'] + data_copy[i]
data['register_model_chose']=data_copy['leixing']
# aa=data_copy[data_copy['leixing']==1001]
# leixing=set(data_copy['leixing'].values.tolist())





data.to_csv('E:\\2015\\final_data_3\\city_data_spatiotemporal_withbaidu_light_xg.csv',index=None)