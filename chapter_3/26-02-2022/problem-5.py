'''
program to perform addition,subraction,multiplication,divison,integer division,
and modulo division on two integer numbers.
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
add_res = num1 + num2
sub_res = num1 - num2
mul_res = num1 * num2
idiv_res = num1/num2
modiv_res = num1%num2
fdiv_res = float(num1)/num2
print(str(num1) + " + " + str(num2) + " = " + str(add_res))
print(str(num1) + " - " + str(num2) + " = " + str(sub_res))
print(str(num1) + " * " + str(num2) + " = " + str(mul_res))
print(str(num1) + " / " + str(num2) + " = " + str(idiv_res) + "  Integer Divsion")
print(str(num1) + " // " + str(num2) + " = " + str(fdiv_res) + "  Float Divsion")
print(str(num1) + " % " + str(num2) + " = " + str(modiv_res) + "  Modulo Divsion")