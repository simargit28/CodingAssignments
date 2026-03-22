#Assignment PA3
#CS7
#Sunday, Febuary 17 2023
#Simar Gill
import math
print(" *** Section 1 ***")
counter = 1
while(counter <= 12):
    print (counter, counter * counter, math.sqrt(counter))
    counter = counter + 1
counter = 14
while(counter <= 15):
    print  (counter, counter * counter, math.sqrt(counter))
    counter = counter + 1
print("*** Section 2 ***")
counter = 30
sum=0
while(counter <= 40):
    print(counter)
    sum= sum + counter
    counter= counter + 1
print(f'{sum}')
print("*** Section 3 ***")
N1=int(input("enter a number that is the low bound "))
N2=int(input("enter a second number that is the high bound "))
counter=N1
sum=0
while(counter <= N2):
    sum= counter + sum
    counter = counter + 1
print(f'low bound: {N1}, high bound: {N2}, sum: {sum}')
print("*** Section 4 ***")
name=input(f"Please enter the name, Dangy, Hank, or Fransisco")
while (name != "Dagny" and name != "Hank" and name != "Fransisco"):
    print("please try again")
    name = input("Please enter the name, Dangy, Hank, or Fransisco")
else:
     print("success")
print("*** Section 5 ***")
number=int(input("Enter a number"))
while(number != 1 and number != 2 and number != 3 and number > 0):
            print("error")
            number = int(input("Enter a number"))
            if (number < 0):
                exit()
if number == 1:
    print("Abagail")
else:
    if number == 2:
        print("Bobby")
    else:
        if number == 3:
         print("Charmaine")
print("*** Section 6 ***")
name=input(f"Please enter the name,Frank or Betty")
while (name != "Frank" and name != "Betty"):
    print("please try again")
    name = input("Please enter the name, Frank or Betty")
else:
     print("Good job!")