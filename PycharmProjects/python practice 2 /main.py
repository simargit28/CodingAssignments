# Ask the user for the lower and upper bounds
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

# Initialize sum
total_sum = 0

# Calculate the sum of integers in the range
current_number = lower_bound
while current_number <= upper_bound:
    total_sum += current_number
    current_number += 1

# Display the bounds and the sum
print(f"Lower bound: {lower_bound}")
print(f"Upper bound: {upper_bound}")
print(f"Sum of integers in the range: {total_sum}")
