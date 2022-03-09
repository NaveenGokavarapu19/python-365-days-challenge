'''
Program to read a character until a * is encountered. Also count the number
of uppercase ,lowercase and number entered by the users. Program getting 
struck should look into it. page 152 python book reema theraja
'''

num_count = 0
up_count = 0
low_count = 0

ch = input("Enter any character: ")

while(ch!="*"):
    if(ch>="0" and ch <= "9" ):
      num_count = num_count+1
    elif(ch>="a" and ch<="9"):
       low_count = low_count+1
    elif (ch>="A" and ch<="Z"):
       up_count = up_count+1

print("Number of lowercase characters are: ",low_count)
print("Number pf uppercase characters are: ",up_count)
print("Number pf numerals are: ", num_count)

