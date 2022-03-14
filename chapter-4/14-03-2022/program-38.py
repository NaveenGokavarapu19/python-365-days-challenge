'''
program to sum the series 1 + 1/2^2 + .... 1/n^2

'''

from re import A


n = int(input("Enter the number: "))
s = 0.0
for i in range(1,n+1):
    a = 1.0/(i**2)
    s = s+a 

print("The sum of series is", s)