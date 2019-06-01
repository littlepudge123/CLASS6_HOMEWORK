#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

df.drop('AGE', axis=1, inplace=True)
os.makedirs('plots_class6/matplotlib_with_boston', exist_ok=True)

# malign = df[df['CRIM'] == 'M']
# benign = df[df['CRIM'] == 'B']
# fig = plt.figure()
# axes = fig.add_subplot(1, 1, 1, projection='3d')
# line1 = axes.scatter(malign['mean CRIM'], malign['mean MEDV'], malign['mean PTRATTO'])
# line2 = axes.scatter(benign['mean CRIM'], benign['mean MEDV'], benign['mean PTRATTO'])
# axes.legend((line1, line2), ('Malign', 'Benign'))
# axes.set_xlabel('mean CRIM')
# axes.set_ylabel('mean MEDV')
# axes.set_zlabel('mean PTRATTO')
# plt.savefig('plots_class6/matplotlib_with_boston/housing_3d.png')
# FAILED

plt.close()