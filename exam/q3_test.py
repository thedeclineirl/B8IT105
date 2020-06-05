import unittest
from Employee import *

class TestQ3(unittest.TestCase):
    def test_employee(self):
        test = Employee('Test',25000)
        self.assertIsNone(test.displayEmployee())
        self.assertEqual('Test',test.get_name())
        self.assertEqual(25000,test.get_salary())
        test.salary_increase(10)
        self.assertEqual(27500,test.get_salary())

    def test_contract_employee(self):
        test = ContractEmployee('Test',15)
        self.assertEqual(15,test.get_hourly())


if __name__ == '__main__':
    unittest.main()