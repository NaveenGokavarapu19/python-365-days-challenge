'''
Program to display decimal equivalent of binary number. 
Not able to work out the solution.

'''

from math import remainder


binary_num = int(input("Enter the binary number: "))
decimal_num = 0
i = 0
while(binary_num!=0):
    remainder = binary_num%10
    decimal_num = decimal_num+remainder*(2**i)
    binary_num = binary_num/10
    i = i+1
print("The decimal equivalent is",decimal_num)