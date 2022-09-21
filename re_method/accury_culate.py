import pandas as pd
import numpy as np
from sklearn.metrics import r2_score


def calucate_r2(data):
    print("正在计算第一部分精度")
    # data = pd.read_csv('city_data_with_corrected_pr.csv')
    data_out = pd.DataFrame(columns=('register', 'y1_pr', 'y1_corrected'))
    for i in range(2002, 2021):
        y1_pr = data[[str(i) + 'y1_pr', str(i) + 'y1_corrected', str(i) + 'register']]
        y1_pr.rename(
            columns={str(i) + 'y1_pr': 'y1_pr', str(i) + 'y1_corrected': 'y1_corrected', str(i) + 'register': 'register'},
            inplace=True)

        data_out = pd.concat([data_out, y1_pr], axis=0)
    data_out = data_out.dropna(how='any', subset=['register'])

    r1 = r2_score(data_out['register'], data_out['y1_corrected'])
    r2 = r2_score(data_out['register'], data_out['y1_pr'])
    return r1, r2


def calucate_r2_2(data):
    print("正在计算第二部分精度")
    # data = pd.read_csv('city_data_with_corrected_pr_2.csv')
    data_out = pd.DataFrame(columns=('register', 'y2_pr', 'y2_corrected', 'POP'))
    for i in range(2002, 2021):
        y1_pr = data[[str(i) + 'y2_pr', str(i) + 'y2_corrected', str(i) + 'register', str(i) + 'POP']]
        y1_pr.rename(
            columns={str(i) + 'y2_pr': 'y2_pr', str(i) + 'y2_corrected': 'y2_corrected', str(i) + 'register': 'register',
                     str(i) + 'POP': 'pop'},
            inplace=True)

        data_out = pd.concat([data_out, y1_pr], axis=0)
    data_out = data_out.dropna(how='any', subset=['register'])
    r1 = r2_score(data_out['register'], data_out['y2_corrected'])
    r2 = r2_score(data_out['register'], data_out['y2_pr'])
    r3 = r2_score(data_out['register'] * data_out['pop'], data_out['y2_corrected'] * data_out['pop'])
    r4 = r2_score(data_out['register'] * data_out['pop'], data_out['y2_pr'] * data_out['pop'])
    return r1, r2,r3,r4



