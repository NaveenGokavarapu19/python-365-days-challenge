'''
find the sum of the series 1^2/1 + 2^2/2 +...... n^2/n.

'''

n = int(input("Enter the n value till which sum will the calculated: "))
total_sum = 0
for number in range(1,n+1):
    numerator = number**2
    denominator = number
    total_sum = total_sum + (numerator/denominator)

print("The sum of numbers is ",total_sum)