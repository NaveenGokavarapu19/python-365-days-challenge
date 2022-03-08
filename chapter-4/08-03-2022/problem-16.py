'''
program to calculate the sum and average of first 10 numbers.

'''

from re import I


i = 0
s=0
while(i<=10):
    s= s+i 
    i = i + 1

avg = float(s)/10
print("The sum of first 10 numbers is :",s)
print("The average of first 10 numbers is: ",avg)