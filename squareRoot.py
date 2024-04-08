# Program squareroot.py
# This program reads in a number 
# and output the approximatelly square root of it.
# using Newton's method
# author: Filipe Carvalho

# function n_sqr is defined.
def sqrt ():
    
    # Input the number that will have its squareroot guessed
    # number has to be float type
    positive_number = float(input('Please enter a positive number:'))

    # Adding a if to ensure input is only acceptable if it is positive
    if positive_number <= 0:
        print('Please enter a positive number.')
        return None
    
    # Assuming that the sqrt of the guessed number as being itself
    approximation = positive_number

    # This is to count the number of iterations
    iteration_count = 0

    # While loop to guess the square root
    while True:
        # Approximated to a closer estimation
        new_approximation = 0.5 * (approximation + positive_number/approximation) 
        # Verifying if there is closeness       
        if (abs(new_approximation - approximation)<1e-10):             
            break
        # Update guess
        approximation = new_approximation   
        # Add 1 for each interation.                       
        iteration_count += 1
    # Then the output would be:
    print(f'The square root of {positive_number} is approx. {new_approximation}.') 
    return new_approximation
sqrt()   

# End of the program