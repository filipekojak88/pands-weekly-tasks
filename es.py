# Part 1: This program reads in a text file
# Part 2: and outputs the number of e's
# that the text file contains.
# Part 3: The program takes the filename from 
# an argument # on the comand line
# Parts 4, 6 - 9: dealing with errors.
# e.g. no argument, file does not exist,
# is not a text file

# The script references part followed by a number.
# This is to facilitate the documentation of the steps 
# performed to create this program. 
# For more details see section History
# located at the end of the program.

# Author: Filipe Carvalho

# Part 5:


# import "os" from os for 4.2:
# import os  # Part 9: Obsoleted this part. 

# import "sys" from part 3, 4.1 and 4.3:             
import sys

# Here we add the function to count the E's
# Part 2:
def countEs (fileName):
    # Part 6: File Not Found added here:
    try:
        with open(fileName, 'r') as md:
            data = md.read()
            qtyEs = data.count('e') + data.count('E')  # Count both lowercase and uppercase 'e'
        return qtyEs
    # Part 7: Added FileNotFoundError to except to be more specific
    except FileNotFoundError:
       # Part 48
       return None
# Here we add another function for the argument. 
def argument():
    
    # Part 4.3 - Erro for no argument on the command line.
    if len(sys.argv) != 2:
        print('Error: You need to enter an argument "fileName"')
        sys.exit(1)

    # Part 3: File from an argument on the command line
    # This part has to come after the part 4.3 to avoid Index Error
    fileName = sys.argv[1]

    # Part 4.1 - Error: no argument
    if not fileName.endswith('.txt'):
        print("Error: Input file must be a text file.")
        sys.exit(1)

    # Part 4.2 - Error: files does not exist_# Part 9 - Obsoleted Part 4.2:
    # if not os.path.isfile(fileName):
    #    print ("Error: File does not exist")

        
    # This is the return of the function argument:
    return fileName
# Returning the fileName variable from the argument() function
# allows me to pass the fileName argument to countEs function:
fileName = argument()
  
# 4.5: check if file is None:
if fileName is not None:
    qty_Es = countEs(fileName)
    if qty_Es is not None:
        # Here I print the quantity of e's from the file of interest.
        print(f"The file {fileName} contains {countEs(fileName)} e(s).")
    else: 
        print("Error: File not found")


# History:

# Part 1 _ open the file:
# Reference:
# https://github.com/andrewbeattycourseware/pands-course-material/blob/main/jupyternotebooks/topic07-files.ipynb

# with open("mobydick.txt", 'r') as md:
#     data = md.read()
# test:
#    print(data)

# Part 2 _ Count characters in Python
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

# Part 3 _ Take the filename from an argument
# on the comand line
# Reference: 
# https://moez-62905.medium.com/the-ultimate-guide-to-command-line-arguments-in-python-scripts-61c49c90e0b3
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm 


# Command-line arguments are accessed through sys.argv list.
# import sys
# fileName = sys.argv[1]
# Test:
# print (f'filename is {fileName}')
    
# Part 4 _ Errors:

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


# Part 5 _ Join the parts:
# we start the program by importing 
# so these can be used within the functions

# After running this program and testing for errors,
# other issues were identified:

# Part 6 _ Error File Nout Found appeared for countEs and open functions.
# Reference: https://www.geeksforgeeks.org/why-am-i-getting-a-filenotfounderror-in-python/
# try:
#    file1 = open ('mobydick.txt')
# except:
#    print("file not found")

# Part 7 _ When testing for file not file does not exist.
# the program was printing three messages:
# Error: File does not exist, file not found, 
# The file mobydicc.txt. contains None e(s).
# Consulting Chat GPT on this issue it was found
# that countEs needs FileNotFoundError to be more specific.
# add a check if fileName is none.
# Reference: 
# For FileNotFoundError: https://docs.python.org/3/library/exceptions.html
# For returning None: https://realpython.com/python-return-statement/#returning-none-explicitly

# Part 8 _ after applying the corrections from Part 7,
# there were still three messages appearing:
# Error: File does not exist, file not found,
# Error: File not found.
# To ensure that the message appears just once
# the print statement from inside the countES function
# will be removed.
# support from Chat GPT
        
# Part 9 _ still appearing two messages after Part 8 implemented:
# Error: File does not exist,
# Error: File not found.
# To sort his issue I just had to remove the Part 4.2
# as it is already covered in section Part 7.


# Source of raw data for mobydick.txt:
# https://gist.github.com/StevenClontz/4445774
