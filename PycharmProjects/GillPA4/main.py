#Simar Gill
#Assignment 4
#CS7
#Tuesday, Febuary 27
import math
print("*** Section 1 ***")
for counter in range (1,11):
    print (counter, counter * counter, math.sqrt(counter))
print("*** Section 2 ***")
N1=int(input("enter the low bound"))
N2=int(input("enter the high bound"))
counter=N1
sum=0
for counter in range (N1,N2+1):
    sum= counter + sum
    counter = counter + 1
print(f'low bound: {N1}, high bound: {N2}, sum: {sum}')
print("*** Section 3 ***")
S1= input("enter any string")
count=0
for character in S1:
    count = count + 1
print(f'The count of characters in this string is {count}')
print("*** Section 4 ***")
print("I will only be counting lower case vowels")
S2= input("enter any string")
Vowel=0
for character in S2:
    if character in 'aeiou':
        Vowel= Vowel + 1
print(f'this string has {Vowel} vowels')
print("*** Section 5 ***")
Name = input("Enter your first and last name with a blank in between")
first_name, last_name= Name.split()
length_first_name=len(first_name)
length_last_name=len(last_name)
print(f'The number of characters in the first name is {length_first_name}')
print(f'The number of characters in the last name is {length_last_name}')



