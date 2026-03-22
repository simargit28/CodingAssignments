# Assignment PA5
# Simar Gill
# 3/6/24
# CS7
import math

# Part 1
print("*** Part 1 ***")
temperature = []
while True:
    a = input("Enter a temperature or 'stop' ")
    if a == 'stop':
        break
    temperature.append(int(a))

for temp in temperature:
    print(f'You entered {temp}')
average_temperature = sum(temperature) / len(temperature)
print(f'The average temperature is {average_temperature: .2f}')
# Part 2
print("*** Part 2 ***")
Grades = []
Hours = []
Letters_to_Number ={'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
while True:
    Z = input("Enter a grade and number of hours, or CALC")
    if Z == 'CALC':
        break
    w1, w2 = Z.split()
    Grades.append(w1)
    Hours.append (int(w2))

Grades_Numbers = [Letters_to_Number[Letter] for Letter in Letters_to_Number]
print("The grades you entered were")
for f,g in zip(Grades,Hours):
    print(f,g)
result = [grade * hour for grade,hour in zip(Grades_Numbers,Hours)]
Sum1=(sum(result))
Sum2=(sum(Hours))
GPA=Sum1/Sum2
print(f'The GPA is {GPA: .2f}')







