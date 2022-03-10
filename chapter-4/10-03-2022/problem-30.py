'''
program to print multiplication table of given number n.

'''

n = int(input("Enter any number: "))
print("Multiplication table of",n)
print("******************************")
for i in range(1,11):
    print(n,"X",i,"=",n*i)