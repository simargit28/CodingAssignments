my_file = open("/Users/simar/Downloads/A7dataSP24.data")

line = my_file.readline()
dictionary = {}

while len(line) != 0:
    line = line.rstrip()
    abbreviation = line[20:25].strip()
    department_name = line[0:20].strip()
    dictionary[abbreviation] = department_name
    line = my_file.readline()

def display():
    print("Department Abbreviation  Department Name")
    print("---------------------------------------")
    for abbreviation, department_name in dictionary.items():
        print(format(abbreviation, '10'), department_name)

def search_department(key):
    if key in dictionary:
        print(dictionary[key])
    else:
        print(key, "does not exist")

def delete_department(key):
    if key in dictionary:
        del dictionary[key]
        print(key, "has been deleted")
    else:
        print(key, "does not exist")

def add_department(key, value):
    if key not in dictionary.values() and key not in dictionary:
        dictionary[key] = value
        print("Department added successfully")
    else:
        print("Department/Abbreviation already exists")

def update_department(key, value):
    if key in dictionary:
        dictionary[key] = value
        print("Department name updated successfully")
    else:
        print(key, "does not exist")

def process_user_input(user_input):
    if len(user_input) == 1:
        if user_input[0] == 'x':
            return False
        elif user_input[0] == 'l':
            display()
    elif len(user_input) == 2:
        action, key = user_input
        if action == "s":
            search_department(key)
        elif action == "d":
            delete_department(key)
    elif len(user_input) == 3:
        action, key, value = user_input
        if action == "a":
            add_department(key, value)
        elif action == "c":
            update_department(key, value)
    return True

display()

running = True
while running:
    user_input = input().split()
    running = process_user_input(user_input)

my_file.close()
