# squareroot.py
# This program reads in a positive number and approximates its square root using Newton's method.
# Author: Filipe Carvalho

# Define the sqrt function to calculate the square root using Newton's method
def sqrt():
    # Prompt user to input a positive number and convert it to a float
    positive_number = float(input('Please enter a positive number: '))

    # Check if the input number is positive
    if positive_number <= 0:
        print('Please enter a positive number.')
        return None
    
    # Initial guess for the square root (starting point for approximation)
    approximation = positive_number

    # Initialize iteration counter
    iteration_count = 0

    # Iterate using Newton's method to approximate the square root
    while True:
        # Update the approximation to a closer estimate
        new_approximation = 0.5 * (approximation + positive_number / approximation)
        
        # Check if the difference between the new and previous approximation is small enough
        if abs(new_approximation - approximation) < 1e-10:
            break
        
        # Update the approximation for the next iteration
        approximation = new_approximation
        
        # Increment the iteration counter
        iteration_count += 1
    
    # Output the approximate square root
    print(f'The square root of {positive_number} is approximately {new_approximation}.')
    
    # Return the final approximation (although it's not explicitly used later)
    return approximation

# Call the sqrt function to execute the square root calculation
sqrt()

# End of the program