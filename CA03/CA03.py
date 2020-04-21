'''
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA01

Created:        2020-04-18
Editted:        2020-04-21
'''

#Basic maths functions with Lambda
add = lambda x,y: x+y
sub = lambda x,y: x-y
multi = lambda x,y: x*y
divide = lambda x,y: x/y





#Testing
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


