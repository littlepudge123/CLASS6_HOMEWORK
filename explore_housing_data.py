#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

os.makedirs('plots_class6/matplotlib_dataset_exploration', exist_ok=True)

for col1_idx, column1 in enumerate(df.columns):
    fig, axes = plt.subplots(1, 1, figsize=(5, 5))
    axes.hist(df[column1], bins=30, color='g', label=column1)
    axes.set_title(column1)
    axes.set_xlabel(column1)
    axes.set_ylabel('Distribution')
    axes.legend()
    plt.savefig(f'plots_class6/{column1}_hist.png', dpi=300)
    plt.close(fig)

    for col2_idx, column2 in enumerate(df.columns):
        if col1_idx < col2_idx:
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='green', marker='.')
            axes.set_title(f'{column1} to {column2}')
            axes.set_xlabel(column1)
            axes.set_ylabel(column2)
            axes.legend()
            plt.savefig(f'plots_class6/matplotlib_dataset_exploration/housing_{column1}_{column2}_scatter.png', dpi=300)
            plt.close(fig)

plt.close()