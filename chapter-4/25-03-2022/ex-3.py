'''
program to determine entered value is alphabet,digit or whitespace.

'''

entered_value = input("Enter a value: ")

if entered_value.isalpha():
    print("An alphabet has been entered: ")
elif entered_value.isdigit():
    print("An digit has been entered ")

elif entered_value.isspace():
    print("Entered a white space ")