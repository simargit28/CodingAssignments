#Assignment PA3
#CS7
#Sunday, Febuary 17 2023
#Simar Gill
import math
print("*** Section 3 ***")
N1=int(input("enter a number"))
N2=int(input("enter a second number"))
counter=N1
sum=0
while(counter <= N2):
    sum= counter + sum
    counter = counter + 1
print(f'low bound: {N1}, high bound: {N2}, sum: {sum}')