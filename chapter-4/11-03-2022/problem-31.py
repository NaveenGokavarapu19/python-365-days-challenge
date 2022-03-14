'''
program to print all numbers upto n and classifying then as even or odd.

'''

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

for i in range(m,n+1):
    if(i%2==0):
        print(i," is a even number ")
    else:
        print(i," is a odd number ")