#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.scatter(df['MEDV'], df['CRIM'], s = 1 , label = 'Crime', color = 'red', marker = '*' )
axes.set_title('Crime vs Value')
axes.set_xlabel('Value')
axes.set_ylabel('Crime')
axes.legend()

os.makedirs('plots_class6/matplotlib_with_boston', exist_ok=True)

plt.savefig('plots_class6/matplotlib_with_boston/boston_crime_value_scatter.png',dpi = 300)

plt.close()