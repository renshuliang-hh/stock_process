import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Load an example dataset with long-form data
# def smooth(data, sm=3):
#     if sm > 1:
#         smooth_data = []
#         for d in data:
#             y = np.ones(sm) * 3.0 / sm
#             d = np.convolve(y, d, "same")
#
#             smooth_data.append(d)
#
#     return smooth_data


aa = pd.DataFrame([0, 2.2, 3.3, 4.4, 5.5, 6.6, 7.8])[0]

# def smooth(data,sm=1):

def smooth(aa):
    cc = aa.copy()
    for i in aa.index.values.tolist()[1:-1]:
        cc[i] = (aa[i - 1] + aa[i] + aa[i + 1]) / 3.0
        print(cc[i])
    return cc

bb=smooth(aa)