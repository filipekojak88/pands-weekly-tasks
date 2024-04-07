# Program collatz.py
# This program prompts the user to input any positive integer
# and outputs the successive values of a calculation
# at each step calculates the next value by taking 
# the current value and, if it is even
# divides it by two, but if it is odd,
# multiply it by three and add one
# the program ends if the current value is one.
# author: Filipe Carvalho

# Prompt user to input a positive value                                                
positive_integer = int(input('Enter a positive integer: '))    
# This while loop is to ensure that a positive value is input by the user
while positive_integer <= 0:                                                 
    print ('This value is not positive.')                                       # If the user enters a negative value or 0 then he is notified about that
    positive_integer = int(input('Please enter a \"Positive\"integer: '))       # The user is then requested to enter a positive integer value

# This while loop generates new values until the value is 1
while positive_integer != 1:                                                    
    print (positive_integer, end=' ')                                           # Here the values that was initiated and generated in the loop are printed
    if (positive_integer % 2) == 0:                                             # This verifies if it is an even number by comparing to 0 the remainder of a division by 2
        positive_integer = positive_integer // 2                                # it divides the value by 2
    else:                                                                       # but if it is not an even number then this is the path forward for an odd number
        positive_integer = (positive_integer * 3) + 1                           # it multiplies the value by 3 and add 1
print(positive_integer)                                                         # Print the last number in the sequence, 1

# End of the program




                                           
    