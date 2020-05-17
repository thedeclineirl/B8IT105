'''
Github:         thedeclineirl
Student Name:   Thomas Higgins
Student Number: 10544739


Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA02

Created:        2020-03-25
Editted:        2020-05-17
'''

import unittest
from CA02 import *


class TestCA02(unittest.TestCase):

    def test_import(self):
       self.assertIsNotNone(import_fleet())

    def test_export(self):
        self.assertIsNone(export_fleet(import_fleet()))

class TestCar(unittest.TestCase):
    
    def test_car_colour(self):
        test = Car()
        test.setColour('Red')
        self.assertEqual('Red',test.getColour())
        test.paint('Yellow')
        self.assertEqual('Yellow',test.getColour())

    def test_car_mileage(self):
        test = Car()
        test.setMileage(15)
        self.assertEqual(15,test.getMileage())
        test.move(10)
        self.assertEqual(25,test.getMileage())

    def test_car_make(self):
        test = Car()
        test.setMake('Ford')
        self.assertEqual('Ford',test.getMake())

    def test_car_model(self):
        test = Car()
        test.setModel('Fiesta')
        self.assertEqual('Fiesta',test.getModel())

    def test_petrol(self):
        test = PetrolCar()
        test.setEngineSize(1.1)
        self.assertEqual(1.1,test.getEngineSize())

    def test_diesel(self):
        test = DieselCar()
        test.setEngineSize(3.0)
        self.assertEqual(3.0,test.getEngineSize())

    def test_hybrid(self):
        test = HybridCar()
        test.setEngineSize(1.2)
        self.assertEqual(1.2,test.getEngineSize())
        test.setNumberFuelCells(8)
        self.assertEqual(8,test.getNumberFuelCells())

    def test_electric(self):
        test = ElectricCar()
        test.setNumberFuelCells(16)
        self.assertEqual(16,test.getNumberFuelCells())

    def test_Fleet(self):
        test = CarFleet(5,4,3,2)
        self.assertEqual(5,len(test.getPetrolCars()))
        self.assertEqual(4,len(test.getDieselCars()))
        self.assertEqual(3,len(test.getHybridCars()))
        self.assertEqual(2,len(test.getElectricCars()))
        self.assertIsNotNone(test.rent('P'))
        self.assertIsNone(test.returnCar('P',PetrolCar()))

if __name__ == '__main__':
    unittest.main()
