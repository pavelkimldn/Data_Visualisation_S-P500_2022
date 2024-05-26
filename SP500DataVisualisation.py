#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:47:45 2024

@author: pavelkim
"""

import pandas as pd
df = pd.read_csv('Desktop/financials.csv'
                )
df.dtypes

#histogram
import matplotlib.pyplot as plt

plt.hist(df['Price'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Price')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

#scatter plot

plt.scatter(df['Price'], df['Earnings/Share'], color='orange', alpha=0.5)
plt.title('Price vs. Earnings Per Share (Earnings/Share)')
plt.xlabel('Price')
plt.ylabel('Earnings/Share')
plt.show()

#boxplot

import seaborn as sns

plt.figure(figsize=(10, 6))
sns.boxplot(x='Sector', y='Dividend Yield', data=df)
plt.title('Dividend Yield by Sector')
plt.xlabel('Sector')
plt.ylabel('Dividend Yield')
plt.xticks(rotation=45)
plt.show()

#Heatmap

import seaborn as sns

# Exclude non-numeric columns from the correlation matrix
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Compute correlation matrix for numeric columns only
corr_matrix = numeric_df.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

#bubble chart

plt.figure(figsize=(10, 8))
sns.scatterplot(x='Price', y='Market Cap', size='EBITDA', data=df, sizes=(20, 200), alpha=0.6)
plt.title('Bubble Chart: Price vs Market Cap with EBITDA Size')
plt.xlabel('Price')
plt.ylabel('Market Cap')
plt.show()

#violin plot

plt.figure(figsize=(12, 8))
sns.violinplot(x='Sector', y='Price', data=df)
plt.title('Violin Plot of Price by Sector')
plt.xlabel('Sector')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.show()    

#pair plot
sns.pairplot(df[['Price', 'Price/Earnings', 'Dividend Yield', 'Earnings/Share', 'EBITDA']], diag_kind='kde')
plt.title('Pairplot of Numeric Variables')
plt.show()

#3D scatter plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Price'], df['Price/Earnings'], df['Market Cap'], c='skyblue', s=60, alpha=0.6)
ax.set_xlabel('Price')
ax.set_ylabel('Price/Earnings')
ax.set_zlabel('Market Cap')
plt.title('3D Scatter Plot of Price, EPS, and Market Cap')
plt.show()