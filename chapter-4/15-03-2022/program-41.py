'''

calculate sum of cubes of numbers from 1 to n.

'''

from re import A


n =int(input("Enter the value of n: "))
s = 0
for i in range(1,n+1):
    a = i**3
    s = s + a 

print("The sum of cubes is ",s )
