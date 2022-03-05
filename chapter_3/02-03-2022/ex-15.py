'''
Program to calculate salary of an employee given basic pay,HRA and TA
'''

basic_salary = int(input("Enter the basic salary: "))
HRA = 0.1 * basic_salary
TA = 0.05 * basic_salary

total_salary = int(round(basic_salary+HRA+TA,2))

print("The total salary of the employee is: " + str(total_salary))