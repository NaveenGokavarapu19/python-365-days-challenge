'''
Program to find the average of first n numbers.

'''

sum = 0

number_entered = int(input("Enter a number upto which the average is to be calculated: "))

for number in range(0,number_entered+1):
    sum = number + sum

avg = sum/number_entered

print("The average of " + str(number_entered) + " numbers is " + str(avg) )

