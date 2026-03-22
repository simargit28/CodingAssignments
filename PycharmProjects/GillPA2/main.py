#Assignment PA2
#CS7
#Sunday, Febuary 7 2023
#Simar Gill
#Part 1
#Ask the user to enter the cost of gas
import random

CG=float(input("Enter the cost of gas"))
formatted_number= "{:.2f}".format(CG)
#Ask the user to enter the number of miles driven on that tank of gas
MD=float(input("And how many miles did you drive on that tank of gas?"))
formatted_number2= "{:.2f}".format(MD)
#calculate the cost per mile
cost_per_mile=CG/MD
formatted_number3= "{:.2f}".format(cost_per_mile)
#display the input and results
print(f"Cost of gas:     $ {formatted_number}")
print(f"miles driven:      {formatted_number2}")
print(f"Cost per mile:   $   {formatted_number3}")

#Part 2
P=float(input("Please enter an amount in dollars and cents"))
formatted_number4= "{:.2f}".format(P)
I=float(input("Enter interest rate"))
formatted_number5= "{:.2f}".format(I)
print(f'For a loan of                 $    {formatted_number4}')
print(f'with a rate of                       {formatted_number5}%')
percent=(I*.01)
interest_compounded_annually=(P*percent)
formatted_number6= "{:.2f}" .format(interest_compounded_annually)
print(f'intesrest compounded annually $      {formatted_number6}')
YE_balance=(P + interest_compounded_annually)
formatted_number7="{:.2f}".format(YE_balance)
print(f'YE balance                    $    {formatted_number7}')
interest_compounded_daily=P*((1+(percent/365))**365)-P
formatted_number8= "{:.2f}".format(interest_compounded_daily)
print(f'Interest compounded daily     $      {formatted_number8}')
YE_balance2=(P + interest_compounded_daily)
formatted_number9="{:.2f}".format(YE_balance2)
print(f'YE balance                    $    {formatted_number9}')
# Part 3
H=int(input("Enter the height of the TV"))
W=int(input("Enter the width of the TV"))
Diagonal=(W**2)+(H**2)
print(f"The screen size is {Diagonal} inches")
#Part 4
import math
import random
die1= random.randint(1,6)
die2= random.randint(1,6)
die3= random.randint(1,6)
die4= random.randint(1,6)
total_result = die1 + die2
print(f'player rolls {die1} and {die2},', end= " ", )
if total_result == 7 or total_result ==11:
    print("winner.")
    exit()
else:
    if total_result == 12 or total_result == 3 or total_result ==2:
        print("loser")
        exit()
    else:
        print(f'the point is {total_result}. Player then roles {die3} and {die4},', end=" " )
total_result2= die3 + die4
if total_result2 == 7 or total_result2 ==11:
    print("winner")
else:
    if total_result2 == 12 or total_result2 == 3 or total_result2 ==2:
        print("loser")
    else:
        print("loser")

        