'''
program to let user guess the number (99) and give feedback.

'''

flag = True

while flag:
    guessed_number = int(input("Enter a number: "))
    if guessed_number > 99:
        print("You have entered a higher number. Try again")
    elif guessed_number < 99:
        print("You have entered a lower number. please try again")
    elif guessed_number == 99:
        print("You have entered the correct number ")
        flag = False 
        break