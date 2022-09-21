import pandas as pd
import numpy as np

data=pd.read_csv('E:\\2015\\final_data\\data_spatiotemporal_withbaidu_light.csv',encoding='GBK')


add_data1=pd.read_excel('E:\\2015\\final_data\\province_real_gdp_sum.xlsx')
add_data2=pd.read_excel('E:\\2015\\final_data\\【立方数据学社】全国各省份2000-2020年人口数据.xlsx')
# add_data3=pd.read_csv('VNL_mean_c.csv')
# add_data4=pd.read_csv('VNL_sum_c.csv')
def match_index(name,year):
    data_1 = np.nan
    data_2 = np.nan
    # data_3 = np.nan
    # data_4 = np.nan
    for index, row in add_data1.iterrows():
        if row['PR'] in name or name in row['PR']:
            try:
                data_1 = row[str(year)]
            except Exception:
                data_1 = np.nan
    for index, row in add_data2.iterrows():
        if row['PR'] in name or name in row['PR']:
            try:
                data_2 = row[str(year)]
            except Exception:
                data_2 = np.nan
    # for index, row in add_data3.iterrows():
    #     if row['地区'] in name:
    #         try:
    #             data_3 = row[str(year)]
    #         except Exception:
    #             data_3= np.nan
    # for index, row in add_data4.iterrows():
    #     if row['地区'] in name:
    #         try:
    #             data_4 = row[str(year)]
    #         except Exception:
    #             data_4= np.nan
    return data_1,data_2


#
#
#
add_data_list1=[]
add_data_list2=[]

for index, row in data.iterrows():
    print(index)
    data1,data2=match_index(row['province'],row['year'])
    add_data_list1.append(data1)
    add_data_list2.append(data2)
#
# #
add_data1_pd=pd.DataFrame({'real_GDP':add_data_list1})
add_data2_pd=pd.DataFrame({'image_POP':add_data_list2})
#
data['real_GDP']=add_data1_pd
data['image_POP']=add_data2_pd
#
# data.to_csv('E:\\2015\\final_data_2\\data_spatiotemporal_withbaidu_light.csv',index=None)
