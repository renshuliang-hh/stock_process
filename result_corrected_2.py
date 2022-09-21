
import pandas as pd
import numpy as np
from method.correct_stock import combin_data_2 as combin_stock
from method.accury_culate import calucate_r2_2 as r2_stock
from re_method.correct_stock import combin_data as combin_register
from re_method.accury_culate import calucate_r2 as r2_register

def match_index(name,year,add_data):
    data_1 = np.nan
    data_2 = np.nan
    # data_3 = np.nan
    # data_4 = np.nan
    for index, row in add_data.iterrows():
        if row['市'] in name or name in row['市']:
            try:
                data_1 = row[str(year)+'y2_corrected']
            except Exception:
                data_1 = np.nan
            try:
                data_2 = row[str(year)+'POP']
            except Exception:
                data_2 = np.nan

    return data_1,data_2
data=pd.read_csv('person_pre_result\\pr_stock_lr.csv')
data_correct=data[['stock','PGDP','scale','city','year','pr_stock']]
data_correct.columns=['stock','PGDP','scale','city','year','y2_pr']
data_corrected=combin_stock(data_correct)
r2_s=r2_stock(data_corrected)
add_data_list1=[]
add_data_list2=[]
for index, row in data.iterrows():
    print(index)
    data1,data2=match_index(row['city'],row['year'],data_corrected)
    add_data_list1.append(data1)
    add_data_list2.append(data2)
#
# #
add_data1_pd=pd.DataFrame({'pr_stock_corrected':add_data_list1})
add_data2_pd=pd.DataFrame({'pop':add_data_list2})
#
data['pr_stock_corrected']=add_data1_pd
data['pop']=add_data2_pd


data_corrected.to_csv('person_pre_result_corrected\\pr_stock_lr_corrected_everyear.csv',index=None)
data.to_csv('person_pre_result_corrected\\pr_stock_lr_corrected.csv',index=None)




# data_r=pd.read_csv('new_pr_result\\pr_register_lr_i.csv')
# data_correct_=data_r[['register','GDP','scale','city','year','pr_register']]
# data_correct_.columns=['register','GDP','scale','city','year','y1_pr']
# data_corrected_=combin_register(data_correct_)
# r2_r=r2_register(data_corrected_)
#
# add_data_list1=[]
# for index, row in data_r.iterrows():
#     print(index)
#     data1=match_index(row['city'],row['year'],data_corrected_)
#     add_data_list1.append(data1)
# #
# # #
# add_data1_pd=pd.DataFrame({'pr_register_corrected':add_data_list1})
#
# #
# data_r['pr_register_corrected']=add_data1_pd
#
# data_corrected_.to_csv('new_pr_result_corrected\\pr_register_lr_i_corrected_everyear.csv',index=None)
# data_r.to_csv('new_pr_result_corrected\\pr_register_lr_i_corrected.csv',index=None)