'''
program to calculate the average of first n natural numbers.

'''

n = int(input("Enter the value of n: "))
avg = 0.0
for i in range(1,n+1):
    s = s+i
avg = s/i
print("The sum of first","natural numbers is",s)
print("The average of first",n,"natural numbers is",avg)
