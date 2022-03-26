'''
Program to determine a year is leap year or not.

'''

year_entered = int(input("Enter a year: "))

if year_entered%4 == 0:
    if year_entered%100 == 0 and year_entered%4 !=0 :
        print("The entered year " + str(year_entered) +  " is not a  leap year ")
    elif year_entered%400==0:
        print("The entered year: "+ str(year_entered) + "  is a leap year")

else:
    print("The year entered: " + str(year_entered) + " is not a leap year")