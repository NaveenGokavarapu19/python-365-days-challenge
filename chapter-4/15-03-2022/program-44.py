'''
program to generate calendar of a month given the start_day and 
the number of days in that month.

'''

StartDay = int(input("Enter the start day of month (1-7): "))
num_of_days = int(input("Enter number of days: "))
print("Sun Mon Tues Wed Thrus Fri Sat ")
print("---------------------------------------------")
for i in range(StartDay-1):
    print(end="  ")

i = StartDay-1
for j in range(1,num_of_days+1):
    if(i>6):
        print()
        i=1
    else:
        i = i + 1
    print(str(j) + "  ",end=" ")