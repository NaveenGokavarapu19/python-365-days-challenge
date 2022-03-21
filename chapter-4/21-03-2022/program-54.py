'''
program to calculate square root of a number. Demonstrate use of break and continue.

'''

import math
total_prime = 0
total_composite = 0

while(1):
    num = int(input("Enter no: "))
    if (num==999):
        break
    elif num < 0:
        print("Square root of negative number cannot be calculated")
        continue
    else:
        print("Square root of ",num," = ",math.sqrt(num))