'''
program to print the pattern shown in the doc strings.  Question not clear 

don't pay attention. Copy of question 48.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

'''

N = 5 

for i in range(1,N+1):
    for k in range(N,i-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("\n")