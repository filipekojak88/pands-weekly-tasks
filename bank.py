# Program bank.py
# This program:
# - prompt the user and read in two money amounts (in cent)
# - add the two amounts 
# - print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.
# Author: Filipe Carvalho

# Firstly, request the two amounts to be input

amount1 = int(input ("Please enter the first amount (in cents): "))
amount2 = int(input("Please enter the second amount (in cents): "))

# Then add the two amounts
total = amount1 + amount2

# Separate the interger part of total amount from the decimal part
intergerpart = total // 100
decimalpart = total % 100

# Add the format with the text followed by euro sign, the interger part, dot, and the decimal part.
# Note: As we are talking about money then we have to specify the number of decimals after dot to be 2 ...
# ... otherwise if we have a total of 500 then the value printed will be €5.0.
print (f'The sum of these is: €{intergerpart}.{decimalpart:02d}')

# End of the program