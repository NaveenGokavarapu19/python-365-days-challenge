'''
print the pattern shown in doc strings.

0 
1 2 
3 4 5 
6 7 8 9

'''

count = 0

for i in range(1,5):
    print()
    for j in range(1,i+1):
        print(count,end=" ")
        count = count + 1