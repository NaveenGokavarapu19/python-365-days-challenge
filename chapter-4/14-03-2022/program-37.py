'''
program to sum the series 1 + 1/2 + .... 1/n

'''

from re import I


n = int(input("Enter the number: "))
s = 0.0
for i in range(1,n+1):
    a = 1.0/i 
    s = s+a

print("The sum of 1,1/2....1/"+ str(n) + " is " + str(s))