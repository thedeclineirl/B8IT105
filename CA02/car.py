'''
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA02

Created:        2020-03-25
Editted:        2020-05-10
'''

class Car(object):
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__model = ''
        self.__mileage = 0

    def setColour(self, colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setMileage(self, mileage):
        self.__mileage = mileage

    def getMileage(self):
        return self.__mileage

    def move(self, distance):
        print('Moved ' + str(distance) + 'kms')
        self.__mileage = self.__mileage + distance

    def paint(self, colour):
        print('Getting a paint job - new colour is: ' + colour)
        self.__colour = colour

class PetrolCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''
        
    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize

class DieselCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''
        
    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize

class HybridCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''
        self.__numberFuelCells = ''

    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize

    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells

class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = ''
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells

class CarFleet(object):
    
    def __init__(self, pcar, dcar, hcar, ecar):
        self.__petrol_cars = []
        self.__diesel_cars = []
        self.__hybrid_cars = []
        self.__electric_cars = []
        for i in range(1, pcar+1):
            self.__petrol_cars.append(PetrolCar())
        for i in range(1, dcar+1):
            self.__diesel_cars.append(DieselCar())
        for i in range(1, hcar+1):
            self.__hybrid_cars.append(HybridCar())    
        for i in range(1, ecar+1):
            self.__electric_cars.append(ElectricCar())

    def getPetrolCars(self):
        return self.__petrol_cars
    
    def getDieselCars(self):
        return self.__diesel_cars

    def getHybridCars(self):
        return self.__hybrid_cars
    
    def getElectricCars(self):
        return self.__electric_cars

    def __str__(self):
        return '{0}, {1}, {2}, {3}\n'.format(
            len(self.getPetrolCars()), len(self.getDieselCars()),len(self.getHybridCars()), len(self.getElectricCars()))

    def checkCarsInStock(self):
        print('Number of Petrol Cars : ' + str(len(self.getPetrolCars())))
        print('Number of Diesel Cars : ' + str(len(self.getDieselCars())))
        print('Number of Hybrid Cars : ' + str(len(self.getHybridCars())))
        print('Number of Electric Cars : ' + str(len(self.getElectricCars())))

    def rent(self, type):
        if type == 'P':
            return self.__petrol_cars.pop()
        elif type == 'D':
            return self.__diesel_cars.pop()
        elif type == 'H':
            return self.__hybrid_cars.pop()        
        elif type == 'E':
            return self.__electric_cars.pop()

    def returnCar(self, type, car):
        if type == 'P':
            self.__petrol_cars.append(car)
        elif type == 'D':
            self.__diesel_cars.append(car)
        elif type == 'H':
            self.__hybrid_cars.append(car)                    
        elif type == 'E':
            self.__electric_cars.append(car)

    def mainMenu(self):
        print('Welcome to DBScar')
        rentedCar = None
        answer = input('Would you like to rent a car R, return a car U, any key to quit?')
        answer = answer.upper()
        while answer == 'R' or answer == 'U':
            if answer == 'R':
                type = input('What car would you like to rent - P for petrol, D for Diesel, H for Hybrid, E for electric')
                type = type.upper()
                rentedCar = self.rent(type)
            elif answer == 'U':
                type = input('What car would you like to return - P for petrol, D for Diesel, H for Hybrid, E for electric')
                type = type.upper()
                self.returnCar(type, rentedCar)
            self.checkCarsInStock()
            answer = input('Would you like to rent a car R, return a car U, any key to quit?')
            answer = answer.upper()
