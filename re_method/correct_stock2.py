import pandas as pd
import numpy as np
import math
def missing_value_process_1_1(data, year, province_name):
    province_data = pd.read_excel('re_method\新注册民用汽车拥有量.xls', sheet_name='分省年度数据', index_col='地区')
    data[str(year) + 'y1_correct'] = data[str(year) + 'y1_pr']
    data[str(year) + 'y1_correct'][data[str(year) + 'y1_correct'] < 0] = np.nan
    sum_len = len(data)
    sum_sub_non_len = len(data.dropna(how='any', subset=[str(year) + 'y1_correct']))
    # if data[str(year) + 'y1_correct'][data[str(year) + 'y1_correct'] < 0]
    if sum_sub_non_len / sum_len > 0.5:
        data_noneed_fill = data.dropna(how='any', subset=[str(year) + 'y1_correct'])[
            str(year) + 'y1_correct'].values.tolist()

        data_noneed_fill.sort()
        data_noneed_fill = data_noneed_fill[:math.ceil(sum_sub_non_len / 3)]
        data.fillna({str(year) + 'y1_correct': (sum(data_noneed_fill) / len(data_noneed_fill))}, inplace=True)
        stock_p = province_data[year][province_name]
        data_need_correct = data[str(year) + 'y1_correct']
        correct_ratio = stock_p / sum(data_need_correct)
        data[str(year) + 'y1_correct'] = data[str(year) + 'y1_correct'] * correct_ratio
    return data

def missing_value_process_1_2(data, year, province_name):
    province_data = pd.read_excel('re_method\新注册民用汽车拥有量.xls', sheet_name='分省年度数据', index_col='地区')
    data[str(year) + 'y1_correct'] = data[str(year) + 'y1_pr']
    # data[str(year) + 'y1_correct'][data[str(year) + 'y1_correct'] < 0]=np.nan
    if len(data[str(year) + 'y1_correct'][data[str(year) + 'y1_correct'] < 0])>0:
        sum_len = len(data)
        sum_sub_non_len = len(data.dropna(how='any', subset=[str(year) + 'y1_correct']))
        if sum_sub_non_len / sum_len > 0.5:
            data_noneed_fill = data.dropna(how='any', subset=[str(year) + 'y1_correct'])[
                str(year) + 'y1_correct'].values.tolist()

            data_noneed_fill.sort()
            data_noneed_fill = data_noneed_fill[:math.ceil(sum_sub_non_len / 3)]
            data.fillna({str(year) + 'y1_correct': (sum(data_noneed_fill) / len(data_noneed_fill))}, inplace=True)
            stock_p = province_data[year][province_name]
            data_need_correct = data[str(year) + 'y1_correct']
            correct_add = (stock_p-sum(data_need_correct))/len(data_need_correct)
            data[str(year) + 'y1_correct'] = data[str(year) + 'y1_correct'] + correct_add
    else:
        sum_len = len(data)
        sum_sub_non_len = len(data.dropna(how='any', subset=[str(year) + 'y1_correct']))
        if sum_sub_non_len / sum_len > 0.5:
            data_noneed_fill = data.dropna(how='any', subset=[str(year) + 'y1_correct'])[
                str(year) + 'y1_correct'].values.tolist()
            data_noneed_fill.sort()
            data_noneed_fill = data_noneed_fill[:math.ceil(sum_sub_non_len / 3)]
            data.fillna({str(year) + 'y1_correct': (sum(data_noneed_fill) / len(data_noneed_fill))}, inplace=True)
            stock_p = province_data[year][province_name]
            data_need_correct = data[str(year) + 'y1_correct']
            correct_ratio = stock_p / sum(data_need_correct)
            data[str(year) + 'y1_correct'] = data[str(year) + 'y1_correct'] * correct_ratio
    return data
def missing_value_process_2(data, year, province_name):
    province_data = pd.read_excel('re_method\新注册民用汽车拥有量.xls', sheet_name='分省年度数据', index_col='地区')
    data[str(year) + 'y2_correct'] = data[str(year) + 'y2_pr']*data[str(year) + 'POP']
    data[str(year) + 'y2_correct'][data[str(year) + 'y2_correct']<0]=np.nan
    sum_len = len(data)
    sum_sub_non_len = len(data.dropna(how='any', subset=[str(year) + 'y2_correct']))

    if sum_sub_non_len / sum_len > 0.5:
        data_noneed_fill = data.dropna(how='any', subset=[str(year) + 'y2_correct'])[
            str(year) + 'y2_correct'].values.tolist()

        data_noneed_fill.sort()
        data_noneed_fill = data_noneed_fill[:math.ceil(sum_sub_non_len / 3)]
        data.fillna({str(year) + 'y2_correct': (sum(data_noneed_fill) / len(data_noneed_fill))}, inplace=True)
        stock_p = province_data[year][province_name]
        data_need_correct = data[str(year) + 'y2_correct']
        correct_ratio = stock_p / sum(data_need_correct)
        # data[str(year) + 'y2_correct'] = data[str(year) + 'y2_correct'] * correct_ratio
        data[str(year) + 'y2_correct'] = data[str(year) + 'y2_correct'] * correct_ratio/data[str(year) + 'POP']
    else:
        data[str(year) + 'y2_correct'] = data[str(year) + 'y2_pr']
    return data
def missing_value_process_2_2(data, year, province_name):
    province_data = pd.read_excel('re_method\新注册民用汽车拥有量.xls', sheet_name='分省年度数据', index_col='地区')
    data[str(year) + 'y2_correct'] = data[str(year) + 'y2_pr']*data[str(year) + 'POP']
    # data[str(year) + 'y2_correct'][data[str(year) + 'y2_correct']<0]=np.nan
    if len(data[str(year) + 'y2_correct'][data[str(year) + 'y2_correct']<0])>0:
        sum_len = len(data)
        sum_sub_non_len = len(data.dropna(how='any', subset=[str(year) + 'y2_correct']))
        if sum_sub_non_len / sum_len > 0.5:
            data_noneed_fill = data.dropna(how='any', subset=[str(year) + 'y2_correct'])[
                str(year) + 'y2_correct'].values.tolist()
            data_noneed_fill.sort()
            data_noneed_fill = data_noneed_fill[:math.ceil(sum_sub_non_len / 3)]
            data.fillna({str(year) + 'y2_correct': (sum(data_noneed_fill) / len(data_noneed_fill))}, inplace=True)
            stock_p = province_data[year][province_name]
            data_need_correct = data[str(year) + 'y2_correct']
            correct_add = (stock_p - sum(data_need_correct))/len(data_need_correct)
            # data[str(year) + 'y2_correct'] = data[str(year) + 'y2_correct'] * correct_ratio
            data[str(year) + 'y2_correct'] = (data[str(year) + 'y2_correct'] +correct_add)/ data[str(year) + 'POP']
        else:
            data[str(year) + 'y2_correct'] = data[str(year) + 'y2_pr']
    else:
        sum_len = len(data)
        sum_sub_non_len = len(data.dropna(how='any', subset=[str(year) + 'y2_correct']))
        if sum_sub_non_len / sum_len > 0.5:
            data_noneed_fill = data.dropna(how='any', subset=[str(year) + 'y2_correct'])[
                str(year) + 'y2_correct'].values.tolist()
            data_noneed_fill.sort()
            data_noneed_fill = data_noneed_fill[:math.ceil(sum_sub_non_len / 3)]
            data.fillna({str(year) + 'y2_correct': (sum(data_noneed_fill) / len(data_noneed_fill))}, inplace=True)
            stock_p = province_data[year][province_name]
            data_need_correct = data[str(year) + 'y2_correct']
            correct_ratio = stock_p / sum(data_need_correct)
            # data[str(year) + 'y2_correct'] = data[str(year) + 'y2_correct'] * correct_ratio
            data[str(year) + 'y2_correct'] = data[str(year) + 'y2_correct'] * correct_ratio / data[str(year) + 'POP']
        else:
            data[str(year) + 'y2_correct'] = data[str(year) + 'y2_pr']

    return data
def corrected_result(city_data):
    print("正在校正第一部分数据")

    # city_data = pd.read_csv('relation_with_stock_pr.csv')

    # city_data=city_data.drop('新疆维吾尔自治区',0)
    # city_data=city_data.drop('2021stock',1)
    # city_data = city_data[(city_data['市类型'] == '地级市') | (city_data['市类型'] == '自治州')]
    province_list = sorted(list(set(city_data['省'].values.tolist())))
    for year in range(2002, 2021):
        print(year)
        df1 = pd.DataFrame(columns=('市', str(year) + 'y1_pr', str(year) + 'register', str(year) + 'y1_correct'))
        for province_name in province_list:
            data = city_data[(city_data['省'] == province_name)][['市', str(year) + 'y1_pr', str(year) + 'register']]
            data = missing_value_process_1_2(data, year, province_name)
            df1 = pd.concat([df1, data], axis=0)
        city_data[str(year) + 'y1_corrected'] = df1[str(year) + 'y1_correct']

    return city_data

def corrected_result_2(city_data):
    print("正在校正第二部分数据")
    # city_data = pd.read_csv('relation_with_stock_pr_2.csv')
    city_data = city_data[(city_data['市类型'] == '地级市') | (city_data['市类型'] == '自治州')]
    province_list = sorted(list(set(city_data['省'].values.tolist())))
    for year in range(2002, 2021):
        print(year)
        df1 = pd.DataFrame(columns=('市', str(year) + 'y2_pr', str(year) + 'register', str(year) + 'y2_correct'))
        for province_name in province_list:
            data = city_data[(city_data['省'] == province_name)][
                ['市', str(year) + 'y2_pr', str(year) + 'register', str(year) + 'POP']]
            data = missing_value_process_2_2(data, year, province_name)
            df1 = pd.concat([df1, data], axis=0)
        city_data[str(year) + 'y2_corrected'] = df1[str(year) + 'y2_correct']
        city_data[str(year) + 'POP'] = city_data[str(year) + 'POP']

    return city_data


    #
# city_data.to_csv('city_data_with_corrected_pr.csv', index=None)
