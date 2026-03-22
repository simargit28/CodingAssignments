from random import randint

print("*** Part 1 ***")

def coinflip():
    result = randint(0, 1)
    if result == 0:
        return 'Heads'
    else:
        return 'Tails'

def main():
    user_input = int(input("How many times do you want to flip the four coins? "))
    counter = 0

    for _ in range(user_input):
        if all(coinflip() == 'Heads' for _ in range(4)):
            counter += 1

    percentage = (counter / user_input) * 100
    print(f"Percentage of all heads: {percentage:.2f}%")

if __name__ == "__main__":   
    main()

print("*** Part 2 ***")


def roll6():
    return randint(1, 6) + randint(1, 6)


def main():
    number_of_rolls = int(input("Enter the number of rolls to simulate: "))
    dict = {i: 0 for i in range(2, 13)}

    for _ in range(number_of_rolls):
        total = roll6()
        dict[total] += 1

    print("Roll occurrences report:")
    for roll, count in dict.items():
        percentage2 = (count / number_of_rolls) * 100
        print(f"Roll {roll} occurrences {count} {percentage2:.2f}%")


if __name__ == "__main__":
    main()
