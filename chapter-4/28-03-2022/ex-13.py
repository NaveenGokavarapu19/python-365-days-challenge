'''
program which takes user input displays length of it until QUIT word is entered as input.

'''

flag = True

while flag:
    print("Enter 'QUIT' to exit the program")
    string_inputted = input("Enter the word for which length is to be calculated: ")
    if string_inputted == "QUIT":
        flag = False
        break
    else:
        print("The length of the word " + string_inputted + " is " + str(len(string_inputted)) )