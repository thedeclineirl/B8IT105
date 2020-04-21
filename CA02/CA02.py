'''
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA02

Created:        2020-03-25
Editted:        2020-04-11
'''

'''
Based on the Object Oriented lecture and sample code provided, extend the code to create the system for 
# DBS Car Rental which has 40 cars in its inventory, made up of 
# # 20 petrol
# # 10 diesel 
# # 6 electric
# # 4 hybrid

Your application should ask users if they'd like to rent a car, the type of car and how many they'd like to rent. 
The rental status of the cars should be stored in some suitable storage mechanism - say a csv file.

Unit tests should be written to ensure that your application is adequately tested.
'''


from car import *
x = Car()
x.setColour('Red')
print(x.getColour())

