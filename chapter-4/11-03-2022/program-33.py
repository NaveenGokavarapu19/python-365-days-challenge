'''
program to classify a given number as prime or composite

'''

number = int(input("Enter a number: "))
isComposite = 0
for i in range(2,number):
    if(number%i == 0 ):
        isComposite = 1
        break
if(isComposite == 1 ):
    print("Number is composite")
else:
    print("Number is prime")
    