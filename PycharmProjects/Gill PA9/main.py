my_file = "/Users/simar/Downloads/titanic.csv"

passenger_ids = []
survived = []
pclass = []
sex = []
age = []
sibsp = []
parch = []
ticket = []
fare = []
cabin = []
embarked = []

with open(my_file, 'r') as file:
    header = file.readline()
    for line in file:
        fields = line.strip().split(",")
        passenger_ids.append(int(fields[0]))
        survived.append(int(fields[1]))
        pclass.append(int(fields[2]))
        sex.append(0 if fields[4] == "male" else 1)

        age_value = float(fields[5]) if fields[5].replace('.', '').isdigit() else None
        age.append(age_value)

        sibsp_value = int(float(fields[6])) if fields[6].replace('.', '').isdigit() else None
        sibsp.append(sibsp_value)

        parch.append(int(fields[7]))
        ticket.append(fields[8])

        fare_value = float(fields[9]) if fields[9].replace('.', '').isdigit() else None
        fare.append(fare_value)

        cabin_value = fields[10] if fields[10] else "missing"
        cabin.append(cabin_value)
        embarked_value = fields[11] if fields[11] else "X"
        embarked.append(embarked_value)


age_values = [a for a in age if a is not None]
average_age = sum(age_values) / len(age_values) if age_values else None
age = [average_age if a is None else a for a in age]

fare_values = [f for f in fare if f is not None]
average_fare = sum(fare_values) / len(fare_values) if fare_values else None
fare = [average_fare if f is None else f for f in fare]

with open("/Users/simar/Downloads/titanic_cleansed.csv", "w") as output_file:
    output_file.write("passengerID,survived,pclass,sex,age,sibsp,parch,fare,cabin,embarked\n")
    for i in range(len(passenger_ids)):
        output_file.write(f"{passenger_ids[i]},{survived[i]},{pclass[i]},{sex[i]},{age[i]},{sibsp[i]},"
                          f"{parch[i]},{fare[i]},{cabin[i]},{embarked[i]}\n")

print("Cleansing complete. Data written to titanic_cleansed.csv.")

with open("/Users/simar/Downloads/titanic_cleansed.csv", 'r') as file:
    cleansed_data = file.read()
    print(cleansed_data)
