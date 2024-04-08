# Program squareroot.py
# This program reads in a number 
# and output the approximatelly square root of it
# using Newton's method.
# Author: Filipe Carvalho

# function n_sqr is defined.
def sqrt ():
    
    # Input the number that will have its squareroot guessed
    # number is transformed to a float type
    positive_number = float(input('Please enter a positive number:'))

    # this is to ensure the input is positive
    if positive_number <= 0:
        print('Please enter a positive number.')
        return None
    
    # Assuming that the sqrt of the guessed number as being itself
    approximation = positive_number

    # This is to start the counter for the number of iterations
    iteration_count = 0

    # While loop to guess the square root based on Newton's method 
    while True:
        # Approximate to a closer estimation
        new_approximation = 0.5 * (approximation + positive_number/approximation) 
        # Verifying if there is closeness to the previous value      
        if (abs(new_approximation - approximation)<1e-10):             
            break
        # Update the approximation and iteration counter.
        approximation = new_approximation                     
        iteration_count += 1
    # Output the result
    print(f'The square root of {positive_number} is approx. {new_approximation}.') 
    
    return approximation

# Call the sqrt function to execute the square root calculation.
sqrt()   

# End of the program