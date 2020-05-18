'''
Github:         thedeclineirl
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA04

Created:        2020-05-11
Editted:        2020-05-11
##############################

##############################
Brief
Pandas Data Interpretation
https://www.kaggle.com/hmavrodiev/london-bike-sharing-dataset/
'''

#Imports
##############################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##############################

dataset = pd.read_csv("London_merged.csv")
print(dataset.head())
print(dataset.shape)
print(dataset.info())
print(dataset.describe())
print(dataset.dtypes)

# Plot
# plt.figure(figsize=(8,8))
# sns.heatmap(dataset,annot=True)
# plt.title("London Bikes")
# plt.xlabel("??")
# plt.ylabel("??")
# plt.show()




