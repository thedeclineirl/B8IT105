'''
Github:         thedeclineirl
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA03

Created:        2020-05-14
Editted:        2020-05-24
'''
import unittest
from calc import *

class TestCalc(unittest.TestCase):
    def testBasicMaths(self):
        self.assertEqual(25,add(20,5))
        self.assertEqual(20,sub(25,5))
        self.assertEqual(15,mult(3,5))
        self.assertEqual(3,div(15,5))
    
    def testMapFunctions(self):
        tempC = [36.5, -40, 37.5, 39]
        tempF = [97.7, -40, 99.5, 102.2]
        self.assertEqual(tempF,list_to_fahrenheit(tempC))
        self.assertEqual(tempC,list_to_celcius(tempF))

    def testReduceFunctions(self):
        data = [2,3,4,5] 
        self.assertEqual(14,list_sum(data))
        self.assertEqual(120,list_product(data))
        self.assertEqual(5,list_max(data))
        self.assertEqual(2,list_min(data))

    def testFilterFunctions(self):
        data = [-4,5,18,7,19,21,-99,107,88,-320]
        self.assertEqual([-4,18,88,-320],list_even(data))
        self.assertEqual([5,7,19,21,-99,107],list_odd(data))
        self.assertEqual([5,18,7,19,21,107,88],list_pos(data))
        self.assertEqual([-4,-99,-320],list_neg(data))

    def testGeneratorFunctions(self):
        data = [-4,5,18,7,19,21,-99,107,88,-320]
        evens = list_get_even(data)
        odds = list_get_odd(data)
        positives = list_get_pos(data)
        negatives = list_get_neg(data)
        
        self.assertEqual(-4,next(evens))
        self.assertEqual(18,next(evens))
        self.assertEqual(88,next(evens))
        self.assertEqual(-320,next(evens))
        self.assertRaises(StopIteration,lambda:next(evens))

        self.assertEqual(5, next(odds))
        self.assertEqual(7, next(odds))
        self.assertEqual(19, next(odds))
        self.assertEqual(21, next(odds))
        self.assertEqual(-99, next(odds))
        self.assertEqual(107, next(odds))
        self.assertRaises(StopIteration,lambda:next(odds))

        self.assertEqual(5,next(positives))
        self.assertEqual(18,next(positives))
        self.assertEqual(7,next(positives))
        self.assertEqual(19,next(positives))
        self.assertEqual(21,next(positives))
        self.assertEqual(107,next(positives))
        self.assertEqual(88,next(positives))
        self.assertRaises(StopIteration,lambda:next(positives))
        
        self.assertEqual(-4,next(negatives))
        self.assertEqual(-99,next(negatives))
        self.assertEqual(-320,next(negatives))
        self.assertRaises(StopIteration,lambda:next(negatives))

if __name__ == '__main__':
    unittest.main()
