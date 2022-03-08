'''
program to read the numbers until -1 is encountered and finds average 
of positives numbers and negative numbers.

'''

neg_count = pos_count = neg_s = pos_s = 0
print("Enter -1 to exit ....")
num = int(input("Enter the number: "))
while(num!=-1):
    if(num<0):
        neg_count = neg_count+1
        neg_s=neg_s+num
    else:
        pos_count = pos_count+1
        pos_s = pos_s + num

neg_avg = float(neg_s)/neg_count
pos_avg = float(pos_s)/pos_count
print("The average pf negative number is: ",neg_avg)
print("The average of positive numbers is: ",pos_avg)