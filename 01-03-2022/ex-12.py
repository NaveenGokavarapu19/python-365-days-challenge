'''
program to calculate simple and compound interest given principle,interest and tenure
'''

p = int(input("Enter the principal amount: "))
r = int(input("Enter the interest percentage per year: "))
t = int(input("Enter the duration or tenure of the loan: "))
n = 1 
simple_interest = (p * t * r) / 100

compound_interest = p * (1 + r / n )**n*t 

print(simple_interest,compound_interest)