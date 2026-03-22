#Assignment PA1
#CS7
#Sunday,Febuary 4 2023
#Simar Gill
#Part 1
# Ask the user how many days they worked last week
days=int(input("how many days did you work last week?"))
# Ask the user how many hours they worked last week
hours=int(input("how many hours did you work last week?"))
# Calculate the average number of hours per day
average=(days+hours)/2
# Display the result to the user
print(f"You averaged {average} hours per day")
#Part 2
#Ask the user to enter a temperature in Fahrenheit
temp=int(input("enter a temperature in Fahrenheit"))
#Convert from Fahrenheit to Centigrade
cent= (temp - 32) * 5 / 9
# Tell the user what his temperature is in Centigrade
print(f"That is {cent} in centigrade")
#Part 3
#Ask the user for their student id number
ID=int(input("Please enter your student id number"))
#Ask the user to enter the first item type
first_item=(input("enter the first item"))
#Ask the user to enter the first item cost
first_itemcost=float(input("enter the first item cost"))
#Ask the user to enter the second item type
second_item=(input("enter the second item"))
#Ask the user to enter the second item cost
second_itemcost=float(input("enter the second item cost"))
#Ask the user to enter the third item type
third_item=(input("enter the third item"))
#Ask the user to enter the third item cost
third_itemcost=float(input("enter the third item cost"))
#Print the reciept for the user
print(f"Receipt for {ID}")
print(f"{first_item} {first_itemcost}")
print(f"{second_item} {second_itemcost}")
print(f"{third_item} {third_itemcost}")
#print the subtotal
subtotal=(first_itemcost)+(second_itemcost)+(third_itemcost)
print(f"subtotal {subtotal}")
#print the tax
tax=(subtotal)*.1025
print(f"tax {tax}")
#print the grandtotal
total=(subtotal)+(tax)
print(f"total {total}")