'''
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA01

Created:        2020-04-18
Editted:        2020-04-21
##############################

##############################
Brief
Assignment 3 - 10% - 10 Functional Calculator with Map Reduce Filter & Generator

For assignment 3 create a Calculator class and CalculatorTest class that will implement functionality from a calculator using lists.
Each function should use the lessons learned in the map, reduce, filter, and generator lecture.
'''


##############################

class Calc(self):
    #Basic maths functions with Lambda
    add = lambda x,y: x+y
    sub = lambda x,y: x-y
    multi = lambda x,y: x*y
    divide = lambda x,y: x/y

    #advanced maths functions using map, reduce, filter & generator




##############################
#Test class
import unittest

class TestCalc(unittest.TestCase):
    def testadd(self):
        self.assertEqual(25, add(20,5))
    def testsub(self):
        self.assertEqual(20, sub(25,5))
    def testmulti(self):
        self.assertEqual(15,multi(3,5))
    def testdivide(self):
        self.assertEqual(3,divide(15,5))

if __name__ == '__main__':
    unittest.main()


