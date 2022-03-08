'''
Program to convert lowercase to uppercase and vice versa

'''

ch = input('Enter any character: ')
if( ch >= 'A' and ch <= 'Z'):
    ch = ch.lower()
    print("The entered character was in uppercase. In lowercase it is : " + ch)
else:
    ch = ch.upper()
    print("The entered character was in lowercase. In uppercase it is : " + ch)
