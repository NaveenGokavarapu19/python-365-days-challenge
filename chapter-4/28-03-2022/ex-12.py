'''
program to print the square and cube upto given range. 

'''

n = int(input("Enter the n till which the squares and cubes will be displayed: "))

for number in range(1,n+1):
    square = number **2
    cube = number **3 
    print("square of " + str(number) + " is " + str(square))
    print("cube of " + str(number) + " is " + str(cube))