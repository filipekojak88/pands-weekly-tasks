# Program collatz.py
# This program prompts the user to input any positive integer
# and outputs the successive values of a calculation
# at each step calculates the next value by taking 
# the current value and, if it is even
# divides it by two, but if it is odd,
# multiply it by three and add one
# the program ends if the current value is one.
# author: Filipe Carvalho

                                                 
positiveInterger = int(input('Enter a positive integer: '))                 # Propmt user to input a positive value
while positiveInterger < 0:                                                 # This while loop is to ensure that a positive value is input by the user
    print ('This value is negative.')                                       # If the user enters a negative value then he is notified about that
    positiveInterger = int(input('Enter a \"Positive\"integer: '))          # The user is then requested to enter a positive integer value

while positiveInterger != 1:                                                    # This while loop generates new values until the value is 1
    print (positiveInterger)                                                    # Here the values that was initiated and generated in the loop are printed
    if (positiveInterger % 2) == 0:                                             # This verifies if it is an even number by comparing to 0 the remainder of a division by 2
        positiveInterger = positiveInterger // 2                                # and if it is an even number then divide by 2
    else:                                                                       # but if it is not an even number then this is the path forward if it is an odd number
        positiveInterger = (positiveInterger * 3) + 1                           # if it is an odd number then it can be multiplied by 3 and add 1
print(1)                                                                        # Print the last number: 1

# End of the program




                                           
    