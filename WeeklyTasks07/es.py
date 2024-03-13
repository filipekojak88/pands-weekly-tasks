# Part 1: This program reads in a text file
# Part 2: and outputs the number of e's
# that the text file contains.
# Part 3: The program takes the filename from 
# an argument # on the comand line
# Part 4: dealing with errors.
# e.g. no argument, file does not exist,
# is not a text file

# Author: Filipe Carvalho

# Part 1: open the file:
# Reference:
# https://github.com/andrewbeattycourseware/pands-course-material/blob/main/jupyternotebooks/topic07-files.ipynb

# with open("mobydick.txt", 'r') as md:
#     data = md.read()
# test:
#    print(data)

# Part 2: Count characters in Python
# Reference:
# https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/count/python-string-count/#:~:text=How%20do%20you%20count%20characters,only%20a%20single%20substring%20parameter.
# In this part I have to add to the part 1
# define the variable countEs function

# Here I define the function "countEs" 
# def countEs():
    # Here I associate the argument fileName to "mobydick.txt"
#    fileName = "mobydick.txt"
    # Same open function as used in Pat 1 with 
    # the argument fileName instead of "mobydick.txt"

#    with open(fileName, 'r') as md:
#        data = md.read()
        # Add count
#        qntEs = data.count('e')+ data.count('E')  # Count both lowercase and uppercase.
#        return qntEs
# Test
# num = countEs()
# print (num)

# Part 3:
# Take the filename from an argument
# on the comand line
# Reference: 
# https://moez-62905.medium.com/the-ultimate-guide-to-command-line-arguments-in-python-scripts-61c49c90e0b3
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm 


# Command-line arguments are accessed through sys.argv list.
# import sys
# fileName = sys.argv[1]
# Test:
# print (f'filename is {fileName}')
    
# Part 4:
# Errors:

# 4.1 - Error: no argument
# Reference: http://hplgit.github.io/primer.html/doc/pub/input/._input-solarized007.html
# import sys
# if len(sys.argv) != 2:
# Test:
#     print (f'Error: You need to enter an argument "fileName"')
#     sys.exit(1)


# 4.2 - Error: Files does not exist:
# Reference: https://atu-main-mdl-euwest1.s3.eu-west-1.amazonaws.com/c4/b6/c4b699e20a2c8376efcb7ca04eb1cf7097617a4c?response-content-disposition=inline%3B%20filename%3D%22Lab%2007%20files.pdf%22&response-content-type=application%2Fpdf&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAWRN6GJFLWCMOG6H7%2F20240313%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240313T201553Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21547&X-Amz-Signature=7ff80859a42e4e5bc6a41449fa02f40dad7ab3232b20bd386ee69b48204167d4

# import os.path
# fileName = "mobydick.txt"
# if not os.path.isfile(fileName):
#    print ("File does not exist")
# Test:
# else:
#    print (f'{fileName} exists')
    #initialise file here

# 4.3 - Error: is not a text file
# Reference: https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file
# import sys
# fileName = 'mobydick.txt'
# if not fileName.endswith('.txt'):
#    print("Error: Input file must be a text file.")
#    sys.exit(1) 
# Test:
# else:
#    print(f'{fileName} is of type text')




# Part 5: Join the parts:

# import "sys" from part 3, 4.1 and 4.3; 
# import and "os" from os from 4.2
# we start the program by importing 
# so these can be used within the functions

import os                 
import sys

# Here we add the function to count the E's

# Here we add another function for the argument. 
def argument():
    # Part 3: File from an argument on the command line
    fileName = sys.argv[1]

    # Part 4.1 - Error: no argument
    if not fileName.endswith('.txt'):
        print("Error: Input file must be a text file.")
        sys.exit(1)

    # Part 4.2 - Error: files does not exist
    if not os.path.isfile(fileName):
        print ("Error: File does not exist")

    # Part 4.3 - Erro for no argument on the command line.
    if len(sys.argv) != 2:
        print('Error: You need to enter an argument "fileName"')
        sys.exit(1)
    
    # This is the return of the function argument:
    return fileName
# Returning the fileName variable from the argument() function
# allows me to pass the fileName argument to countEs function:
fileName = argument()

# Part 2 (Part 1 was already added into Part 2):
def countEs (fileName):
    with open(fileName, 'r') as md:
        data = md.read()
        qtyEs = data.count('e') + data.count('E')  # Count both lowercase and uppercase 'e'
    return qtyEs
    


# Here I print the quantity of e's from the file of interest.
print(f"The file {fileName} contains {countEs(fileName)} e(s)")


# Source of raw data for mobydick.txt:
# https://gist.github.com/StevenClontz/4445774
