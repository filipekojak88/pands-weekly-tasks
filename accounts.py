# Program accounts.py
# This programs reads in a 10 characters account number 
# and outputs the account number with the last 4 digits displaying
# and the first 6 digits replaced with Xs
# author: Filipe Carvalho

# Fist Part:
# accountNo = input('Please enter a 10 digit account number:')
# accountString = str(accountNo)
# partNo = accountString[6:10]
# print ('XXXXXX'+partNo)

# Extra: Modify the program to deal with account number of any length
accountNo = input('Please enter your account number:')  # Removed the requirement for 10 to allow any number
accountString = str(accountNo)                          # Transform the number into string
noCharacters = len(accountString)                       # Measure how many characters are in the account
noCharactersToChange = noCharacters - 4                 # Find how many characters will have to be changed to X

partNo = accountString[noCharactersToChange:noCharacters]     # Isolate the 4 last digit
partX = noCharactersToChange*'X'                              # From the number of characters that will have to be changed to X and multiply by X
print (partX+partNo)                                          # Print the account with the part in X and the last four digits as number.

# End of the program