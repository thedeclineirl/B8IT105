'''
Thomas Higgins
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

class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells

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


class CarFleet(object):
    
    def __init__(self):
        self.__petrol_cars = []
        self.__electric_cars = []
        for i in range(1, 11):
            self.__petrol_cars.append(PetrolCar())
        for i in range(1, 6):
            self.__electric_cars.append(ElectricCar())

    def getPetrolCars(self):
        return self.__petrol_cars

    def getElectricCars(self):
        return self.__electric_cars

    def checkCarsInStock(self):
        print('Number of Petrol Cars : ' + str(len(self.getPetrolCars())))
        print('Number of Electric Cars : ' + str(len(self.getElectricCars())))

    def rent(self, type):
        if type == 'P':
            return self.__petrol_cars.pop()
        elif type == 'E':
            return self.__electric_cars.pop()

    def returnCar(self, type, car):
        if type == 'P':
            self.__petrol_cars.append(car)
        elif type == 'E':
            self.__electric_cars.append(car)

    def mainMenu(self):
        print('Welcome to DBScar')
        rentedCar = None
        answer = input('Would you like to rent a car R, return a car U, any key to quit?')
        while answer == 'R' or answer == 'U':
            if answer == 'R':
                type = input('What car would you like to rent - D for Diesel, E for electric, H for Hybrid, P for petrol')
                rentedCar = self.rent(type)
            elif answer == 'U':
                type = input('What car would you like to return - D for Diesel, E for electric, H for Hybrid, P for petrol')
                self.returnCar(type, rentedCar)
            self.checkCarsInStock()
            answer = input('Would you like to rent a car R, return a car U, any key to quit?')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
