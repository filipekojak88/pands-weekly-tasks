# Program es.py
# This program reads a file and counts the 
# number of lowercase and uppercase 'e'
# Author: Filipe Carvalho
            
import sys

# Define a function to count lowercase and uppercase 'e' in a given file
def count_e(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the entire file content into a string
            data = file.read()
            # Count occurrences of lowercase 'e' and uppercase 'E'
            return data.count('e') + data.count('E')
    except FileNotFoundError:
        # Handle file not found error
        print(f'Error: The file {file_name} does not exist')
        sys.exit(1)

# Define the main function to process command-line arguments
def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print('Error: You need to provide a text file as an argument')
        sys.exit(1)
    
    # Extract the file name from the command-line argument
    file_name = sys.argv[1]

    # Check if the provided file has a .txt extension
    if not file_name.endswith('.txt'):
        print("Error: Input file must have a .txt file extension.")
        sys.exit(1)
    
    # Count occurrences of 'e' in the specified file
    e_count = count_e(file_name)
    
    # Print the total count of 'e' (case-insensitive) in the file
    print(e_count)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()