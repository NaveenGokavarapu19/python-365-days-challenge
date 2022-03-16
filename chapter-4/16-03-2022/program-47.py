'''
program to print the following pattern mentioned in docstrings. 

*
**
***
****
*****

'''

for i in range(1,6):
    print()
    for j in range(i):
        print("*",end="")

print("\n")