# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:13:42 2020

@author: felip
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r'D:\Dropbox\Estudos\FIAP\Aulas\MBA IA\BootCamp\2020\FIAP Dataset 1 - v2.csv')
df.head()


list(set(df.dtypes.tolist()))
df_num = df.select_dtypes(include = ['float64', 'int64'])
df_num.head()


df_num = df_num.drop(['Unnamed: 0'], axis = 1)

df_num.hist(figsize=(16, 20), bins=25, xlabelsize=8, ylabelsize=8)




corr = df_num.corr()

plt.figure(figsize=(8, 8))
chart = sns.heatmap(corr[(corr >= 0.5) | (corr <= -0.4)], 
            cmap='viridis', vmax=1.0, vmin=-1.0, linewidths=0.1,
            annot=True, annot_kws={"size": 8}, square=True);

chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right')
chart.set_yticklabels(chart.get_yticklabels(), rotation=45, horizontalalignment='right')