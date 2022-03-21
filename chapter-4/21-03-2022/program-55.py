'''
program to take input until -1 is entered and finally print the count

of prime numbers and composite number.

'''

prime_count = 0 
comp_count = 0
n = int(input("Enter the number: "))
while(n!=-1):
    flag = 0
    for i in range(2,n):
        flag = 1
        break
    if (flag==0):
        prime_count=prime_count+1
    else:
        comp_count = comp_count+1
    n = int(input("Enter the number: "))

print("Number of prime numbers is:", prime_count)
print("Number of composite numbers is: ",comp_count)