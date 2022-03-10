'''
program to print the reverse of the number. program not working should redo it
page number 154 practical python reema theraja

'''

num = int(input("Enter the number: "))
print("The reversed number is: ")
while(num!=0):
    temp = num%10
    print(temp,end="")
    num = num/10

