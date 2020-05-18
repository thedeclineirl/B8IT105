'''
Github:         thedeclineirl
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA03

Created:        2020-05-14
Editted:        2020-05-17
'''

class Calc():
    # # Lambda Functions
    def add(x,y):
    	return lambda x,y: x+y

    def sub(x,y):
    	return lambda x,y: x-y
    
    def mult(x,y):
    	return lambda x,y: x*y

    def div(x,y):
    	return lambda x,y: x/y

    # # conversion functions
	def fahrenheit(t):
	    return ((float(9)/5)*t + 32)
	def celsius(t):
	    return (float(5)/9*(t - 32))
	temp = (36.5, 37, 37.5, 39)

	F = list(map(fahrenheit, temp))
	C = list(map(celsius, F))

    #advanced maths functions using map, reduce, filter & generator
    # # Map, Reduce functions




    # # Filter functions


    # # Generator Functions