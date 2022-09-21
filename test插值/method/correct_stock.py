import pandas as pd
import numpy as np

from .correct_stock2 import corrected_result,corrected_result_2
def match_index(name, year, data):
    y1_pr, stock = np.nan, np.nan
    data_year = data[data['year'] == year]
    for index, row in data_year.iterrows():
        if row['city'] in name or name in row['city']:
            try:
                y1_pr, stock = row['y1_pr'], row['stock']
            except Exception:
                y1_pr, stock = np.nan, np.nan

    return y1_pr, stock

def match_index_2(name, year, data,POP):
    y2_pr, stock = np.nan, np.nan
    pop=np.nan
    data_year = data[data['year'] == year]
    for index, row in data_year.iterrows():
        if row['city'] in name or name in row['city']:
            try:
                y2_pr, stock = row['y2_pr'], row['stock']
            except Exception:
                y2_pr, stock = np.nan, np.nan
    data_pop = POP[POP['year'] == year]
    for index, row in data_pop.iterrows():
        if row['city'] in name or name in row['city']:
            try:
                pop = row['POP_']
            except Exception:
                pop = np.nan

    return y2_pr, stock,pop

def combin_data(data):
    print("拼接第一部分数据")
    relation = pd.read_csv('method\省市对应表.csv', engine='python')
    # data = pd.read_csv('data_to_correct.csv')
    for year in range(2002, 2021):
        print(year)
        add_data_list1 = []
        add_data_list2 = []
        for index, row in relation.iterrows():
            data1, data2 = match_index(row['市'], year, data)
            # print(index)
            add_data_list1.append(data1)
            add_data_list2.append(data2)
        add_data1_pd = pd.DataFrame({str(year) + 'y1_pr': add_data_list1})
        add_data2_pd = pd.DataFrame({str(year) + 'stock': add_data_list2})
        relation[str(year) + 'y1_pr'] = add_data1_pd
        relation[str(year) + 'stock'] = add_data2_pd

    # relation.to_csv('relation_with_stock_pr.csv', index=None)
    out_data = corrected_result(relation)
    return out_data

def combin_data_2(data):
    print("拼接第二部分数据")
    relation = pd.read_csv('method\省市对应表.csv', engine='python')
    # data = pd.read_csv('data_to_correct_2.csv')
    data_city_pop = pd.read_csv('method\city_data_spatiotemporal_withbaidu_light.csv')
    data_city_pop['POP_'] = data_city_pop['GDP'] / data_city_pop['PGDP'] * 10000
    POP = data_city_pop[['year', 'city', 'POP_']]
    for year in range(2002, 2021):
        print(year)
        add_data_list1 = []
        add_data_list2 = []
        add_data_list3 = []
        for index, row in relation.iterrows():
            data1, data2, data3 = match_index_2(row['市'], year, data, POP)
            # print(index)
            add_data_list1.append(data1)
            add_data_list2.append(data2)
            add_data_list3.append(data3)
        add_data1_pd = pd.DataFrame({str(year) + 'y2_pr': add_data_list1})
        add_data2_pd = pd.DataFrame({str(year) + 'stock': add_data_list2})
        add_data3_pd = pd.DataFrame({str(year) + 'POP': add_data_list3})
        relation[str(year) + 'y2_pr'] = add_data1_pd
        relation[str(year) + 'stock'] = add_data2_pd
        relation[str(year) + 'POP'] = add_data3_pd

    # relation.to_csv('relation_with_stock_pr_2.csv', index=None)
    out_data = corrected_result_2(relation)
    return out_data





