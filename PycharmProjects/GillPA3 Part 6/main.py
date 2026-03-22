#Assignment PA3
#CS7
#Sunday, Febuary 17 2023
#Simar Gill
print("*** Section 6 ***")
name=input(f"Please enter the name,Frank or Betty")
while (name != "Frank" and name != "Betty"):
    print("please try again")
    name = input("Please enter the name, Frank or Betty")
else:
     print("Good job!")