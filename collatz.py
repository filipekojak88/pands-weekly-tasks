# Program collatz.py
# This program calculates the Collatz sequence for a given positive integer:
# - The Collatz sequence starts with a positive integer.
# - At each step, the program calculates the next value:
#   - If the current value is even, it divides it by two.
#   - If the current value is odd, it multiplies it by three and adds one.
# - The sequence continues until the current value reaches 1, at which point the program ends.
# Author: Filipe Carvalho

# Prompt the user to input a positive integer
positive_integer = int(input('Enter a positive integer: '))

# Validate user input to ensure it is a positive value
while positive_integer <= 0:
    print('This value is not positive.')
    positive_integer = int(input('Please enter a positive integer: '))

# Generate and print the Collatz sequence until the current value reaches 1
while positive_integer != 1:
    print(positive_integer, end=' ')  # Print the current value in the sequence
    if positive_integer % 2 == 0:     # Check if the current value is even
        positive_integer //= 2        # If even, divide the value by 2
    else:
        positive_integer = (positive_integer * 3) + 1  # If odd, apply the 3n + 1 rule
print(positive_integer)  # Print the final value of the sequence (always 1)

# End of the program




                                           
    