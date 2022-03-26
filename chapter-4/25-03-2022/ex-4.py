'''
program to determine whether a digit,uppercase or a lowercase is entered.
similar to previous exercise.

'''

entered_value = input("Enter the value: ")

if entered_value.isdigit():
    print("Numerical  value has been entered ")
elif entered_value.isupper():
    print("An uppercase letter has  been entered")
elif entered_value.islower():
    print("An lowercase letter has been has been entered")