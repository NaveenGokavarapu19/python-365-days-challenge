'''
program to check whether a number or character. Determine entered letter
is upper or lowercase.
'''
ch = input("Enter the character: ")
if (ch >="A" and ch<="Z"):
    print("Uppercase character was entered")
elif(ch>="a" and ch<="z"):
    print("Lowercase character was entered")
elif(ch>="0" and ch<="9"):
    print("A number was entered")
    