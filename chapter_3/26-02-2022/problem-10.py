'''
Program to calculate average of two numbers. print their deviation

'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter the second number: "))

avg = (num1 + num2 ) / 2
dev1 = num1 - avg
dev2 = num2 - avg
print("AVERAGE = ",avg)
print("Deviation of first num = ", dev1)
print("Deviation of second num = ",dev2)