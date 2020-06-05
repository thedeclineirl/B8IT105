# ##################################################### #
# Student Name:   Thomas Higgins
# Student Number: 10544739
# Course title:   Programming for Big Data 
# Exam Date:      02/06/2020
# ##################################################### #

# Q1
# a
attach(ToothGrowth)
ToothGrowth
?ToothGrowth
# 60 Treatment observations in the dataset

# b
str(ToothGrowth)
# data is structured as a dataframe conbtaing 60 observations of 3 variables
# Dose variable is measured in mg/day

# c
mean(ToothGrowth$len)
# Mean tooth length is 18.81333
sd(ToothGrowth$len)
# standard deviation of tooth length is 7.649315

# d



# e
ToothGrowth$treat=with(ToothGrowth,interaction(supp,dose))
model=lm(len~treat,data=ToothGrowth)
anova(model)

# f






#Q2