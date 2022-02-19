'''
write a program to enter a number and display its hex and octal equivalent
and its equivalent square root.
'''

num = int(input("Enter a number: "))
print("Hexadecimal of " + str(num)+ " : " + str(hex(num)))
print("Octal of " + str(num) + ":" + str(num**0.5))