'''
Program to find whether a given year is leap or not.

'''

year = int(input("Enter any year: "))
if ((year % 4 ==0 and year%100!=0) or (year%400 == 0 )):
    print("Leap Year")
else:
    print("Not a Leap Year")