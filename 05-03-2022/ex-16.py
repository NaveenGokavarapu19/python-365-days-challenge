'''
Program to prepare a grocery bill given name of item purchased,quantity and price per unit

'''

item_name = input("Enter the item name purchased: ")
item_quantity = int(input("Enter the quantity of the item purchased: "))
item_price = int(input("Enter the unit price: "))
total_price = item_quantity * item_price

print("************************BILL************************************")
print("Item Name" + "\t" + " Item Quantity " + "\t\t" +  " Item Price ")
print(item_name + "\t\t\t" + str(item_quantity) + "\t\t\t" + str(item_price))
print("****************************************************************")
print("Total Amount to be Paid: " + str(total_price))
print("****************************************************************")
