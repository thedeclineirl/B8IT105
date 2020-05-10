'''
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA02

Created:        2020-03-25
Editted:        2020-05-10
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
from datetime import datetime

def importFleet():
    data = [line.strip() for line in open('log.csv', 'r')]
    count = data[-1].replace(',','').split()
    pcar = count[0]
    dcar = count[1] 
    hcar = count[2]
    ecar = count[3]
    return CarFleet(int(pcar),int(dcar),int(hcar),int(ecar))

def exportFleet(fleet):
    file = open('log.csv','a')
    file.write('\n' + datetime.now().strftime("%Y-%m-%d - %H:%M:%S") + '\n')
    file.write('pcar, dcar, hcar, ecar\n')
    file.write(str(fleet))

fleet = importFleet()
fleet.mainMenu()
exportFleet(fleet)