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
# Produce a scatterplot of the horse power (on the x-axis) against the miles per gallon variable (y-axis).
dataset.plot(kind='scatter',x='hp',y='mpg')

#C
# Use the type='n' argument (or otherwise) to help you to create a
# scatterplot of the horse-power variable against the miles per gallon
# variable where there are three distinct groups in the plot, depending
# on the cyl (number of cylinders) type of the cars.
# You should:
# ● Select a different plotting character than the default pch
# ● Colour the three groups differently
# ● Include a legend to explain these groups
# ● Include sensible x-axis and y-axis labels and a main title
# ● Rotate the numbers on the y-axis so they appear horizontal
# Comment on the resulting graph.

dataset.plot(kind='scatter',x='hp',y='mpg')

# We were not shown how to do this
