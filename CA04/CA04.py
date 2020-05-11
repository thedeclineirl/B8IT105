'''
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

'''
#Imports
##############################
import numpy as np
import pandas as pd

##############################

dataset = pd.read_csv("E-Shop.csv")
print(dataset.head())
print(dataset.shape)
print(dataset.info())
print(dataset.describe())