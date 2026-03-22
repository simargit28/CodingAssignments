import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from random import randint

print("*** Part 1 ***")

def coinflip():
    result = randint(0, 1)
    return 'Heads' if result == 0 else 'Tails'

def main_coinflip():
    user_input = int(input("How many times do you want to flip the four coins? "))
    counter = 0

    for _ in range(user_input):
        if all(coinflip() == 'Heads' for _ in range(4)):
            counter += 1

    percentage = (counter / user_input) * 100
    print(f"Percentage of all heads: {percentage:.2f}%")

if __name__ == "__main__":
    main_coinflip()

print("*** Part 2 ***")

def roll6():
    return randint(1, 6) + randint(1, 6)

def main_dice_roll():
    number_of_rolls = int(input("Enter the number of rolls to simulate: "))
    roll_counts = {i: 0 for i in range(2, 13)}

    for _ in range(number_of_rolls):
        total = roll6()
        roll_counts[total] += 1
        print(roll_counts)

    print("Roll occurrences report:")
    for roll, count in roll_counts.items():
        percentage2 = (count / number_of_rolls) * 100
        print(f"Roll {roll} occurrences: {count} ({percentage2:.2f}%)")

    plt.bar(roll_counts.keys(), roll_counts.values(), color ='blue')
    plt.title("simar's graph")
    plt.xlabel("roll #")
    plt.ylabel("roll occurrences")
    plt.show()


if __name__ == "__main__":
    main_dice_roll()


