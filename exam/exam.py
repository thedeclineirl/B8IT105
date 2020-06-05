# ##################################################### #
# Student Name:   Thomas Higgins
# Student Number: 10544739
# Course title:   Programming for Big Data 
# Exam Date:      02/06/2020
# ##################################################### #

# Q2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# A
#load dataset
dataset = pd.read_csv("C:/Users/GBKXN/OneDrive - Bayer/Code/github/B8IT105/exam/mtcars.csv")
#examine dataset
dataset.shape
# 32 Variables & 12 observations

# B
dataset.plot(kind='scatter',x='hp',y='mpg')

#C
dataset.plot(kind='scatter',x='hp',y='mpg')
