'''
program to demonstrate nested if.

'''

inputted_number = int(input("Enter a number: "))

if inputted_number > 0:
    if inputted_number %2==0:
        print("An even number has been entered ")
    elif inputted_number %2 !=0:
        print("An odd number has been entered")