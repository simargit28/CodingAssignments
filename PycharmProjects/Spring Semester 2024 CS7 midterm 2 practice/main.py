import statistics

#Write a Python program that defines a list of your favorite fruits. Then, using a for loop, print each fruit in the list.
#Create a list of numbers and iterate through it using a while loop, printing each number.
#Use the enumerate() function to print both the index and value of each element in a list of animals.

fav_fruits = ['apple', 'banana', 'carrot', 'blueberry']
for fav in fav_fruits:
    print(fav)

numbers = [1,2,3,4,5,6,]
a = 0
while a < len(numbers):
    print(numbers[a])
    a += 1

animals = ['tiger', 'gorilla', 'bear', 'racoon']
for index, element in enumerate(animals):
    print(index, element)

# Write a program that takes a list of numbers and calculates their average.

a1 = []
while True:
    a1_input = input("Enter a list of numbers or stop")
    if a1_input == 'stop':
        break
    else:
        a1.append(int(a1_input))

print(a1)

b = (sum(a1)/len(a1))
print(b)

c = statistics.mean(a1)
print(c)


#Write a Python program that takes a list of names as input and prints each name along with its position in the list.
names = []
while True:
    C = input("Enter a list of names or stop")
    if C == 'stop':
        break
    else: names.append(C)
print(names)

for index, element in enumerate(names):
    print(index, element)

# You are given a list of numbers. Write a Python program to find and print the maximum and minimum numbers in the list.
# Given list of numbers
numbers = [3, 8, 2, 5, 10]

# Write your code to find and print the maximum and minimum numbers in the list

max = max(numbers)
min = min(numbers)

print(max)
print(min)

# Sample list of numbers
numbers1 = [10, 20, 30, 40, 50]

average = statistics.mean(numbers1)
print(average)

z = sum(numbers1)/len(numbers1)
print(z)




