'''
Github:         thedeclineirl
Student Name:   Thomas Higgins
Student Number: 10544739

Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA01

Created:        2020-03-23
Editted:        2020-05-16
'''
import unittest
from CA01 import *

class TestCA01(unittest.TestCase):

    def test_get(self):
       self.assertIsNotNone(get_soup())

    def test_wrangle(self):
        self.assertIsNotNone(wrangle_soup(get_soup()))

    def test_clean(self):
        self.assertIsNotNone(clean_soup(wrangle_soup(get_soup())))

    def test_write(self):
        self.assertIsNone(write_csv('testing.csv',clean_soup(wrangle_soup(get_soup()))))

if __name__ == '__main__':
    unittest.main()