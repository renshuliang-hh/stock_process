import pandas as pd
import numpy as np
from scipy.stats import  pearsonr
from sklearn.metrics import r2_score
data_test=pd.read_csv('pr_result_corrected\\pr_stock_lr_corrected.csv')
data_test_all=data_test.dropna(how='any',subset=['stock','pr_stock'])
true_r2=r2_score(data_test_all['stock'],data_test_all['pr_stock'])
data_test_all=data_test.dropna(how='any',subset=['stock','pr_stock_corrected'])
true_correct_r2=r2_score(data_test_all['stock'],data_test_all['pr_stock_corrected'])


city_screan=pd.read_csv('E:\\2015\\test_city_data.csv',encoding='GBK')
data_city=pd.merge(data_test,city_screan,how='left',left_on='city',right_on='市')
data_city=data_city[data_city['label']==1]

data_city=data_city.dropna(how='any',subset=['stock','pr_stock'])
test_r2=r2_score(data_city['stock'],data_city['pr_stock'])
p=pearsonr(data_city['stock'],data_city['pr_stock'])
data_city=data_city.dropna(how='any',subset=['stock','pr_stock_corrected'])
test_correcte_r2=r2_score(data_city['stock'],data_city['pr_stock_corrected'])
p_c=pearsonr(data_city['stock'],data_city['pr_stock_corrected'])
