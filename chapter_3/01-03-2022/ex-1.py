'''
Program to demonstrate all arithmetic operations  on two integers
'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add_res = num1 + num2
sub_res = num1 - num2
mul_res = num1 * num2
div_res = num1 / num2
floor_res = num1 // num2
mod_res = num1 % num2
exp_res = num1 ** num2

print("num1 + num2 = " + str(add_res))
print("num1 - num2 = " + str(sub_res))
print("num1 * num2 = " + str(mul_res))
print("num1 / num2 = " + str(div_res))
print("num1 // num2 = " + str(floor_res))
print("num1 % num2 = " + str(mod_res))
print("num1 ** num2 = " + str(exp_res))