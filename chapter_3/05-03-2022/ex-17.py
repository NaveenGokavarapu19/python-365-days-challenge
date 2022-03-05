'''
Write a program to calculate momentum given mass and velocity of the object.

'''

m = int(input("Enter the mass of the object in kg: "))
c = int(input("Enter the velocity of object in m/s: "))
e = m * (c ** 2)
print("The momentum of the object is: " + str(e))