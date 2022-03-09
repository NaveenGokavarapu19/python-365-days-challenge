'''
program to calculate the sum of the digits.

'''

sum_of_digits = 0
num = int(input("Enter the number: "))
while(num!=0):
    temp=num%10
    sum_of_digits = sum_of_digits+temp
    num=num/10
print("The sum of digits is: ")