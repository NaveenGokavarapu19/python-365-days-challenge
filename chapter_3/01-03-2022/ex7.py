'''
swapping a number using temporary variable
'''

from re import A


a = 2
b = 3
c = None

print("Values of a and b before swapping: " +  "a = "+ str(a) + " and  b = "  + str(b))

c = b
b = a 
a = c

print("Values of a and b after swapping are " + "a = " + str(a) + " and b = "+ str(b))