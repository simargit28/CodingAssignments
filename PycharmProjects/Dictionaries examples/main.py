# Creating a dictionary
student = {
    'name': 'John',
    'age': 20,
    'major': 'Computer Science'
}

# Accessing values using keys
print("Name:", student['name'])
print("Age:", student['age'])
print("Major:", student['major'])

# Adding a new key-value pair
student['gpa'] = 3.5

# Modifying a value
student['age'] = 21

# Removing a key-value pair
del student['major']

print(student)
