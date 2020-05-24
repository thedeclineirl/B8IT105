'''
Github:         thedeclineirl
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA03

Created:        2020-04-18
Editted:        2020-05-17
##############################

##############################
Brief
Assignment 3 - 10% - 10 Functional Calculator with Map Reduce Filter & Generator

For assignment 3 create a Calculator class and CalculatorTest class that will implement functionality from a calculator using lists.
Each function should use the lessons learned in the map, reduce, filter, and generator lecture.
'''
##############################
from calc import *
from functools import reduce 

##############################
print(sub(25,5))

tempC = (36.5, 37, 37.5, 39)
F = list_to_fahrenheit(tempC)
# C = list_to_celcius(F)
print(F)
# print(C)

# a = [1,2,3,4]
b = [17,12,11,10]
# D = list_get(b)

# print(next(D))
# print(next(D))
# print(next(D))
# print(next(D))
# print('List Sum is {0}'.format(list_sum(b)))
# print('List Product is {0}'.format(list_product(b)))
# print('List Max Value is {0}'.format(list_max(b)))
# print('List Min value is {0}'.format(list_min(b)))

c = [-4,5,18,7,19,21,-99,107,88,-320]
# print(list_pos(c))
# print(list_neg(c))
evens = list_get_even(c)
odds = list_get_odd(c)
positives = list_get_pos(c)
negatives = list_get_neg(c)

print('Evens:')
print(next(evens))
print(next(evens))

print('Odds:')
print(next(odds))
print(next(odds))

print('Positives:')
print(next(positives))
print(next(positives))

print('Negatives')
print(next(negatives))
print(next(negatives))

# print(list_odd(a))
# print(list_even(a))
# print(list_odd(b))
# print(list_even(b))
# c = [-1, -4, 5, 9]
# print(list(map(lambda x,y:x+y, a,b)))
# print(list(map(lambda x,y,z:x+y+z, a,b,c)))
# print(list(map(lambda x,y,z:x+y-z, a,b,c)))

##      Filter Function     ##

# #Print odd numbers in fibonnaci sequence
# fib = [0,1,1,2,3,5,8,13,21,34,55]
# result = filter(lambda x: x % 2, fib)
# print(list(result))

# #Prints even numbers in fibonnaci sequence
# fib = [0,1,1,2,3,5,8,13,21,34,55]
# result = filter(lambda x: x % 2==0, fib)
# print(list(result))

##      Reduce Function     ##
#reduce() in Python
# The reduce(fun,seq) function is used to apply a particular function passed in its argument
# to all of the list elements mentioned in the sequence passed along.


# answer = reduce(lambda x, y: x+y, [47, 11, 42, 13])
# print(answer)

# f = lambda a,b: a if (a>b) else b
# ans01 = reduce(f, [47, 11, 42, 13]) 
# print('Ans 01 = '+str(ans01))
# ans02 =  reduce(lambda x, y: x+y, range(1, 101))
# print('Ans 02 = '+str(ans02))

lista = [ 1 , 3, 5, 6, 2, ] 

# list functions with 
# sumlist = reduce(lambda x,y: x+y,lista)
# maxlist = reduce(lambda x,y: x if x>y else y,lista)
# minlist = reduce(lambda x,y: x if x<y else y,lista)
# print(sumlist)
# print(maxlist)
# print(minlist)

# using reduce to compute maximum element from list 

maxlist = reduce(lambda x,y: x if x>y else y,lista)


## List comprehension with a filter     ##
# ans03 =  [(x,y,z) for x in range(1,30), for y in range(x,30), for z in range(y,30), if x**2 + y**2 == z**2]

def pythagorean_triplets(max_value):
    values = []
    for x in range(1, max_value):
        for y in range(x, max_value):
            for z in range(y,max_value):
                if x**2 + y**2 == z**2:
                    values.append((x,y,z))
    return values

# print('Pythagorean Triplets: \n'+str(pythagorean_triplets(45)))

# print(pythagorean_triplets(30))
# print(ans03) 


def city_generator():
    yield('London')
    yield('Hamburg')
    yield('Konstanz')

city = city_generator()

# print(next(city))
# print(next(city))
# print(next(city))


##############################
#Test class


# class TestCalc(unittest.TestCase):
#     def testadd(self):
#         self.assertEqual(25, add(20,5))
#     def testsub(self):
#         self.assertEqual(20, sub(25,5))
#     def testmulti(self):
#         self.assertEqual(15,multi(3,5))
#     def testdivide(self):
#         self.assertEqual(3,divide(15,5))

# if __name__ == '__main__':
#     unittest.main()


