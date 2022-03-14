'''
program to calculate pow(x,n)

'''

num = int(input("Enter the number: "))
n = int(input("Till which power to calculate? "))
result = 1
for i in range(n):
    result = result*num
print(num,"raised to the power",n,"is",result)

