# Program es.py
# This program reads a file and counts the 
# number of lowercase and uppercase 'e'
# Author: Filipe Carvalho
            
import sys

# define the count_e function
def count_e (file_name):

    try:
        # read the file
        with open(file_name, 'r') as file:
            data = file.read()
            # count lowercase and uppercase 'e'
            return data.count('e') + data.count('E')  
    # Exception for error file not found
    except FileNotFoundError:
       print (f'Error: The File {file_name} does not exist')
       sys.exit(1)

# define the main function for the command line arguments 
def main():
    
    # confirm the command line argument.
    if len(sys.argv) != 2:
        print('Error: You need to input an argument text file')
        sys.exit(1)

    
    file_name = sys.argv[1]

    # confirm the argument is a ".txt" file
    if not file_name.endswith('.txt'):
        print("Error: Input file must be a .txt file extension.")
        sys.exit(1)
    
    # count e(s) in the file
    e_count = count_e(file_name)
    print(e_count)

if __name__ == "__main__":
    main()

# End of the Program
