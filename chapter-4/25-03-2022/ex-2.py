'''
program to print corresponding grades for letters (O,A,B,C,F) with if-elif 
constructs.

'''

letter_entered = input("Enter the letter: ")

if letter_entered == "O":
    print("Outstanding")

elif letter_entered == "A":
    print("Very good")

elif letter_entered == "B":
    print("Good")
elif letter_entered == "C":
    print("Average")
elif letter_entered == "F":
    print("Failed")
