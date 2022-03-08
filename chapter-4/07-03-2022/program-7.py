'''
Program to display bonus given gender and salary. For original problem look into
python programming book pg 141

'''

gender = input("Enter the gender of the employee ( m or f ): ")
sal = int(input("Enter the salary of the employee: "))

if (gender == 'm'):
    bonus = 0.05 * sal
else:
    bonus = 0.10 * sal

amt_to_be_paid = sal+bonus
print(" Salary = ",sal)
print(" Bonus = ",bonus)
print(" **********************************")
print("Amount to be paid : ", amt_to_be_paid)