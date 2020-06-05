class Employee(object):
    
    def __init__(self,name,salary=0):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def displayEmployee(self):
        print('Name: {0}, Salary: {1}'.format(self.__name,self.__salary))
 
    def salary_increase(self,increase):
        additional = (self.__salary/100)*increase
        self.__salary += additional
        print('{0} salary increased by {1}%'.format(self.__name,increase))

class ContractEmployee(object):
    def __init__(self,name,hourly):
        Employee.__init__(self,name)
        self.__hourly = hourly

    def get_hourly(self):
        return self.__hourly