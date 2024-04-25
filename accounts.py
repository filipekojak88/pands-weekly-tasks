# Program accounts.py
# This program reads in an account number of any length 
# and outputs the account number with the last 4 digits displayed
# and the initial digits replaced with Xs
# Author: Filipe Carvalho

# Prompt the user to enter their account number
account_no = input('Please enter your account number:')

# Convert the account number to a string
account_string = str(account_no)

# Determine the total number of characters in the account number
no_characters = len(account_string)

# Calculate the number of characters to replace with X (all except the last 4 digits)
no_characters_change = no_characters - 4

# Extract the last 4 digits of the account number
part_no = account_string[no_characters_change:no_characters]

# Create a string of X characters to replace the initial part of the account number
part_x = no_characters_change * 'X'

# Print the transformed account number with the initial part replaced by X and the last 4 digits unchanged
print(part_x + part_no)

# End of the program