'''
program to sum the seriess 1 + 2^3/2 + 3^3 + .. + n^2/n.

'''

n = int(input("Enter the value of n: "))
s = 0.0
for i in range(1,n+1):
    a = float(i**i)/i
    s = s+a 

print("The sum of the series is ", s)