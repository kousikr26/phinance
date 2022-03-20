# -*- coding: utf-8 -*-
"""utility_for_metrics_calculation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_FoQQHs028dFnKAv-E-nJYAmjl0BVf4M
"""

import pandas as pd

df1 = pd.read_csv('saare_metrics_v2.csv')

df1

df1['CAC payback period'] = 12*df1['CAC payback']/df1['ARPU']

df1

df2 = pd.read_csv('balance_sheet_se_metrics.csv')

df2

ASPs = []
for i in range(len(df1)-1):
    if df1.iloc[i][2]==df1.iloc[i+1][2]:
        val = df1.iloc[i][9] - df1.iloc[i+1][9]
        ASPs.append(val)
    else:
        ASPs.append('NaN')

ASPs.append('NaN')

df1['ASP'] = ASPs

df1

df1.columns

df1['LTV : CAC ratio'] = df1['LTV']/df1['CAC']

df1

a  =  list(df1['LTV : CAC ratio'])
print(a)

df1.columns

df1.to_csv('saare_metrics_v3.csv')
