'''
program to calculate the value of an investment given initial value of investment 
and annual interest.

'''

initVal = float(input("Enter the initial value: "))
ROI = float(input("Enter the rate of interest: "))
yrs = int(input("Enter the number of years for which investment has to be done: "))
futureVal = initVal
print("\tYear \t\t Value")
print("-----------------")
for i in range(1,yrs+1):
    futureVal = futureVal * (1+ROI/100.0)
    print(i,"\t\t",futureVal)