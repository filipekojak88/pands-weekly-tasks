# This program reads in a number 
# and output the approximatelly square root of it.
# using Newton's method
# author: Filipe Carvalho


def nSqr () :
    
    # Input the number that will have its sqrt guessed
    # number has to be float type
    anyNo = float(input('Please enter a positive number:'))

    # Adding a if to ensure input is only acceptable if it is positive
    if anyNo <= 0:
        print('Please enter a positive number.')
        return None
    
    # assuming that the sqrt of the guessed number as being itself
    itself = anyNo

    # count the number of iterations:
    zCount = 0

    while True:
        guess = 0.5 * (itself + anyNo/itself)        # Approximated to a more closed "q"
        if (abs(guess - itself)<1e-10):             # Verifying if there is closeness
            break
        itself = guess                          # Update guess
        zCount += 1
    # Then the output would be:
    print(f'The square root of {anyNo} is approx. {guess}.') 
    return guess
nSqr()   
# References:
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
# Chat GPT was used to identify errors.
