# Student Name:   Thomas Higgins
# Student Number: 10544739
# Course title:   Programming for Big Data         
# Course ID:      B8IT105
# Assignment:     CA04

# Created:        2020-05-11
# Editted:        2020-05-30

# # Brief # #
#############
# Pandas Data Interpretation
# Using pandas and any other python libraries you choose, your task is to read in a dataset into a python dataframe. 
# Investigate the dataframe with python calls, and create a pythonic graphical visualisation similar to ones looked 
# at during the course. You may take inspiration from plots found in workbooks on Kaggle.

# # Sources # #
###############
# https://www.kaggle.com/hmavrodiev/london-bike-sharing-dataset/
#

#Imports
##############################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
from scipy import stats
from pylab import * 

##############################

#import dataset
dataset = pd.read_csv("London_merged.csv")

#examine dataset
dataset.head()
dataset.tail()
dataset.index
dataset.columns
dataset.shape
dataset.info()
dataset.describe()
dataset.dtypes
# dataset.mean()
# dataset.max()
# dataset.min()
# dataset.groupby('is_weekend').sum()
# dataset.groupby('is_holiday').sum()


#split datetime into seperate date & time columns
dataset[['date','time']] = dataset['timestamp'].str.split(expand=True)
dataset.dtypes

# split date into seperate year, month & day columns
dataset[['year','month','day']] = dataset['date'].str.split('-',expand=True)
dataset.dtypes

# split time into hour, min & sec columns
dataset[['hour','min','sec']] = dataset['time'].str.split(':',expand=True)
dataset.dtypes

# Delete columns no longer needed
del dataset['timestamp']
del dataset['date']
del dataset['time']
del dataset['min']
del dataset['sec']
dataset.dtypes

# convert new columns to int datatype
dataset['hour'] = dataset['hour'].astype(str).astype(int)
dataset['year'] = dataset['year'].astype(str).astype(int)
dataset['month'] = dataset['month'].astype(str).astype(int)
dataset['day'] = dataset['day'].astype(str).astype(int)
dataset.dtypes

# scatter plot of cnt by hour of day
dataset.plot(kind='scatter',x='hour',y='cnt')

# scatter plot of cnt by month
dataset.plot(kind='scatter',x='month',y='cnt')

# pie chart of cnt by year
dataset.plot(kind='pie',y='year',x='cnt',subplots=True)

# Plot
# plt.figure(figsize=(8,8))
# sns.heatmap(dataset,annot=True)
# plt.title("London Bikes")
# plt.xlabel("??")
# plt.ylabel("??")
# plt.show()

# liner regression
slope, intercept, r_value, p_value, std_err = stats.linregress(dataset['cnt'],dataset['weather_code'])





