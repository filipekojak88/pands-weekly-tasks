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
    print ('This value is negative.')
    positiveInterger = int(input('Enter a \"Positive\"integer: '))

while positiveInterger != 1: 
    print (positiveInterger)
    if (positiveInterger % 2) == 0:                                             # This verifies if is an even number
        positiveInterger = positiveInterger // 2                                # if it is an even number then we can divide by 2
    else:                                                                       # This is the path forward if it is an odd number
        positiveInterger = (positiveInterger * 3) + 1                           # if it is an odd number then we can multiply by 3 and add 1
print(1)                                                                        # Print the last number: 1





                                           
    