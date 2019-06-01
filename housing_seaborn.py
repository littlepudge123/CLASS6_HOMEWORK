#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

os.makedirs('plots_class6/seaborn_categorical', exist_ok=True)

sns.set(style='white')# ticks, darkgrid, whitegrid

boston_df = pd.read_csv('data/boston/housing.data',
                        sep='\s+',
                        header=None)

boston_df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                     'MEDV']

boston_df['int_LSTAT'] = boston_df['LSTAT'].astype(int)

sns.violinplot('int_LSTAT', 'AGE', data=boston_df, hue='TAX', dodge=True, palette='seismic')
plt.savefig('plots_class6/seaborn_categorical/boston_int_LSTAT_AGE_TAX_violinplot.png')
plt.clf()

sns.swarmplot('int_LSTAT', 'AGE', data=boston_df, hue='TAX', dodge=True)
plt.savefig('plots_class6/seaborn_categorical/boston_int_LSTAT_AGE_TAX_swarmplot.png')

plt.close()
