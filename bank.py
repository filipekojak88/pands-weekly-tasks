# Program bank.py
# This program:
# - prompts the user and reads in two money amounts (in cents)
# - adds the two amounts 
# - prints out the answer in a human-readable format with a euro sign and decimal point between the euro and cent of the amount.
# Author: Filipe Carvalho

# Prompt the user to input the two amounts in cents
amount1 = int(input("Please enter the first amount (in cents): "))
amount2 = int(input("Please enter the second amount (in cents): "))

# Calculate the total sum of the two amounts
total = amount1 + amount2

# Separate the integer part and the decimal part of the total amount
integer_part = total // 100
decimal_part = total % 100

# Format and print the total amount in a euro currency format with two decimal places
# Note: Ensuring the correct display of euros and cents by using formatting
print(f'The sum of these amounts is: €{integer_part}.{decimal_part:02d}')

# End of the program