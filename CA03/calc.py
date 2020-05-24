'''
Github:         thedeclineirl
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA03

Created:        2020-04-18
Editted:        2020-05-24
'''
from functools import reduce

# # Basic mathematical functions using lambda function
add = lambda x,y: x+y
sub = lambda x,y: x-y
mult = lambda x,y: x*y
div = lambda x,y: x/y

# # conversion functions using map
def fahrenheit(t):
    return ((float(9)/5)*t + 32)

def celsius(t):
    return (float(5)/9*(t - 32))
temp = (36.5, 37, 37.5, 39)

#advanced maths functions using map, reduce, filter & generator
# # Map Functions
def list_to_fahrenheit(data):
    # convert a given list of celcius temperatures, data, to fahrenheit
    return list(map(fahrenheit, data))

def list_to_celcius(data):
    # convert a given list of fahrenheit temperatures, data, to celcius
    return list(map(celsius, data))

# # Reduce functions
def list_sum(data):
    # returns the sum of the given list, data
    return reduce((lambda x, y: x + y),data)
    
def list_product(data):
    # returns the product of the given list, data
    return reduce((lambda x, y: x * y),data)

def list_max(data):
    # returns max value in given list, data
    return reduce(lambda x,y: x if x>y else y,data)

def list_min(data):
    # retunes min value in given list, data
    return reduce(lambda x,y: x if x<y else y,data)

# # Filter functions
def list_odd(data):
    #return odd numbers in given list, data
    return list(filter(lambda x: x % 2, data))

def list_even(data):
    # return even numbers in given list, data
    return list(filter(lambda x: x % 2==0, data))

def list_pos(data):
    # return the positive results in given list, data
    return list(filter(lambda x: x > 0, data))

def list_neg(data):
    # return the negative results in given list, data
    return list(filter(lambda x: x < 0, data))

# # Generator Function
def list_get_next(data):
    # return next item in given list, data
    for i in data:
        yield(i)

def list_get_even(data):
    # return next even item in given list, data
    evens = list_even(data)
    for i in evens:
        yield(i)

def list_get_odd(data):
    # return next odd item in given list, data
    odds = list_odd(data)
    for i in odds:
        yield(i)

def list_get_pos(data):
    # return next positive item in given list, data
    pos = list_pos(data)
    for i in pos:
        yield(i)

def list_get_neg(data):
    # return next negative item in given list, data
    neg = list_neg(data)
    for i in neg:
        yield(i)
