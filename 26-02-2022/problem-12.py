'''
program to calculate the total amount of money in the piggybank, given the coins of Rs 10, Rs 5 , Rs 2 and Rs1.
'''

num_of_10_coins = int(input("Enter the number of the 10 Rs 10 coins in the piggybank: "))
num_of_5_coins = int(input("Enter the number of 5Rs coins in the piggybank: "))
num_of_2_coins = int(input("Enter the number of 2Rs coins in the piggybank: "))
number_of_1_coins = int(input("Enter the number of 1Re coins in the piggybank: "))

total_amt = num_of_10_coins * 10 + num_of_5_coins * 5 + num_of_2_coins * 2 + number_of_1_coins

print("Total amount in the piggybank = ",total_amt)