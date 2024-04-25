# Repository: pands-weekly-tasks

This repository contains the weekly tasks that were completed as part of the Programming and Scripting classes in ATU with the lecturer Andrew Beatty.
These tasks display several Python scripts that were created to demonstrate the skills that were developed during the course.   
This README has been written with Github's documentation on READMEs in mind [[1]](#1).
MarkDown was used in this README file and was based on GitHub's Documentation [[2]](#2). 

## Overview

This README provides detailed descriptions of each weekly task completed during the Programming and Scripting course. Each task is outlined below with a brief explanation of its purpose and functionality. The README is organized to help readers navigate through the tasks effectively.

## Get Started

To better understand the tasks, have a look at the section About These Tasks below and start by reading through each one of the Weekly Tasks in numerical order. Once you have a glimpse of what the task is about, you can either go to a specific program to undestand the steps adopted to build up the script by reading through the comments provided or you can run the program in a Python interpreter and have fun by testing them out.     

Note: The numbers provided at end of the sentences are in-text citations linking to the appropriate material referenced during the completion of the task.

## About These Tasks

There were 8 tasks that were completed throughout the Programming and Scripting course and the details of each task is described under the headings below.

### Weekly Tasks 1: [helloworld.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/helloworld.py)

The program helloworld.py was the first program created during this course. It is a very simple program that uses the print() function to display the string "Hello World!" when run by the user [[3]](#3) [[4]](#4). 


### Weekly Tasks 2: [bank.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/bank.py)

The program bank.py displays a message for the user to enter two amounts in cents [[5]](#5). However, the value must be an integer. For instance, €10.33 should be input as 1033 [[6]](#6). After the two values are entered by the user, the program calculates and outputs the sum of the two values.  
The program first sum up the two values and then split the values into two parts. The first part is the integer part (using the integer division operator in Python // to divide the integer part of the number by 100) and the second part is the decimal part (using the operator % to return the remainder of a division by 100) [[7]](#7). Finally, the two parts (integer and decimal) are printed out using the function print () by concatenating both parts using an f-string formatting to interpolate the two values within a string [[8]](#8) [[9]](#9).


### Weekly Tasks 3: [accounts.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/accounts.py)

This accounts.py program is a Python script that mimics the security approach used by banks when displaying the account number to users.
In this program, users are prompted to input their account number, and the program displays the last four digits of the account number while replacing the other digits with X.
The program workflow follows these steps: 


- User is prompt to input their account number.
- The program converts the number into a string and counts the number of characters [[10]](#10) [[11]](#11).
- It calculates the number of characters that need to be convert to 'X' by subtracting 4 from the number of characters.
- It isolates the last 4 digits of the account number [[12]](#12).
- It converts all the characters except the last 4 to "X" [[13]](#13) [[14]](#14).
- Then it outputs the modified account number with all characters displaying X except for the last 4 digits, which are displayed as they appear in the account number [[15]](#15).

This program also accepts an account number of any number of characters.


### Weekly Tasks 4: [collatz.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/collatz.py)

The collatz.py program illustrates the calculation process for the [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture), a famours unresolved mathematical problem [[16]](#16) [[17]](#17). Despite being verified for all positive integers up to 2.95 x 10^20, it lacks a general proof [[18]](#18). The program requests that a user input any positive integer and check if the number is even or odd [[19]](#19) [[20]](#20). If the number is even, then the program divides the number by 2. But if the number is odd, then the number is multiplied by 3 and added by 1. The numbers are generated, stored in a sequence, and continuously reprocessed through the conditional check and calculation until the final result is 1 [[21]](#21) [[22]](#22) [[23]](#23) [[24]](#24).


###  Weekly Tasks 5: [weekday.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/weekday.py)

This program determines if the current date is a weekday or a weekend. The datetime module is imported and used in conjunction with the function now() to determine today's date [[25]](#25) [[26]](#26). Since this program only considers two groups, weekdays and weekends, the program defines weekends as a group consisting of just two elements "Saturday" and "Sunday" [[27]](#27). The program then uses strftime() method from datetime module to obtain the day's name from today's date and uses %A to ensure that the full name is returned. Finally the program verifies if the today's day is in the weekend group [[26]](#26). If it is in the weekend group, then it outputs a message confirming it is the weekend. Otherwise, it is a weekday, and it outputs a message confirming it is a weekday [[23]](#23).


### Weekly Tasks 6: [squareroot.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/squareRoot.py)

This program estimates the square root of a positive number using [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method) [[28]](#28) [[29]](#29) [[30]](#30). The squareroot.py program checks if the value is positive, and if it is not, it displays a message to the user that a positive number is required, and the program terminates  [[31]](#31) [[32]](#32) [[33]](#33) [[34]](#34). The main part of the program is the loop used to refine the approximation of the square root [[35]](#35) [[36]](#36). The program starts with a guess, which is the number itself, and iterates to improve the guess until the change between successive approximations is below a determined limit, indicating that the estimation is accurate [[37]](#37).


### Weekly Tasks 7: [es.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/es.py) 

The program es.py counts the number of times that the letter 'e' (lowercase and uppercase) appears in a text file. It was set up so that the user provides the file name on the command-line. The program is designed with two functions count_e(file_name) and main():

- The first one opens the file and reads it, counting and returning the total number of lowercase and uppercase 'e' found in the text file [[38]](#38) [[39]](#39) [[40]](#40). It checks to confirm that the provided file name exists, and if it does not, then an error message is provided, and the program terminates [[41]](#41) [[42]](#42) [[43]](#43).
- The second function works as an entry point. It verifies that a command-line argument was provided by the user and that the file has a '.txt' extension [[44]](#44) [[45]](#45). Any errors regarding these two verifications are fed back to the user through an error message, and program terminates [[46]](#46). If everything works well, then the count of 'e'(lowercase and uppercase) for the input file is output by the program [[47]](#47).

Note: To test this program, the text file [moby-dick.txt](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/moby-dick.txt) was added to pands-weekly-tasks, and a total of 59646 occurrences of the letter "e" were identified [[48]](#48) [[37]](#37).


### Weekly Tasks 8: [plottask.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/plottask.py)

This program creates a bar graph (histogram) showing how often certain numbers pop up in a set of 1000 numbers that behave like a typical set of data with an average of 5 and some variety around that average [[49]](#49) [[50]](#50) [[51]](#51) [[52]](#52) [[53]](#53). Alongside this, it draws a curved line (h (x) = x^3 function) showing what happens when you take each number from 0 to 10, multiply it by itself three times, and plot the result [[54]](#54). The chart is also improved with two y-axis to provide a better visualization of the histogram and line plot on the same graph [[55]](#55). The legends for both plots are grouped into the same legend for a cleaner and more organized presentation [[56]](#56) [[57]](#57) [[37]](#37).

## Use of these tasks

This repository pands-weekly-tasks, will be used to grade my learning from the Programming and Scripting course.     
This repository can be used by other users as a source of examples of codes that can be written by a new Python user.       
Also, these tasks reflect my understanding from the Python programming skills learned during the course, which is far from perfect but shows a perspective of a student who has started learning Python.


## Get Help

If questions are raised when reviewing these tasks, you can contact me via github, and I will be happy to provide more information.

## Contribute

This is a one-off repository completed with the goal of meeting the assignment requirements for the Programming and Scripting course at ATU, and the contribution will be based on feedback provided by Andrew Beatty during the lectures and during the grading of this Assignment.     
Any other activity has been entirely completed by the author.


## Author

[Filipe Carvalho](https://www.linkedin.com/in/filipe-carvalho-8146232a/)

I am a Quality Engineer with 10 years of experience in Automotive and Medical Device Industry.  
I am a Production Mechanical Engineer with a Master of Science degree in Management from Trinity College.  
To further develop myself and prepare to dive into AI in the future, I started the Data Analytics course at ATU in 2024.  


## References:

<a id="1">[1]</a> About readmes (2024) GitHub Docs. Available at: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes (Accessed: 22 April 2024). 

<a id="2">[2]</a> Basic writing and formatting syntax (2024) GitHub Docs. Available at: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax (Accessed: 22 April 2024). 

<a id="3">[3]</a> Hello, world! (no date) Learn Python - Free Interactive Python Tutorial. Available at: https://www.learnpython.org/en/Hello,_World! (Accessed: 22 April 2024). 

<a id="4">[4]</a> Nick  Parlante (2020) Print() and standard out, Computer Science. Available at: https://cs.stanford.edu/people/nick/py/python-print.html (Accessed: 22 April 2024). 

<a id="5">[5]</a> Built-in functions (2024) Python documentation. Available at: https://docs.python.org/3/library/functions.html#input (Accessed: 22 April 2024). 

<a id="6">[6]</a> Python int() (no date) Programiz. Available at: https://www.programiz.com/python-programming/methods/built-in/int (Accessed: 22 April 2024). 

<a id="7">[7]</a> Ramuglia, G. (2024) Python integer division: How to use the // floor operator, Linux Dedicated Server Blog. Available at: https://ioflood.com/blog/python-integer-division-how-to-use-the-floor-operator/#:~:text=Python%20provides%20two%20types%20of,in%203%20(integer%20division) (Accessed: 22 April 2024). 

<a id="8">[8]</a> Real Python (2023) Python’s F-string for string interpolation and formatting, Real Python. Available at: https://realpython.com/python-f-strings/ (Accessed: 22 April 2024).

<a id="9">[9]</a> Nair, A. (2023) What does {:02d} mean in python?, AskPython. Available at: https://www.askpython.com/python/string/02d-in-python (Accessed: 22 April 2024). 

<a id="10">[10]</a> VanderPlas, J. (2016) A whirlwind tour of python, A Whirlwind Tour of Python | A Whirlwind Tour of Python. Available at: https://jakevdp.github.io/WhirlwindTourOfPython/ (Accessed: 22 April 2024).

<a id="11">[11]</a> W3Schools (no date) Python string length. Available at: https://www.w3schools.com/python/gloss_python_string_length.asp (Accessed: 22 April 2024). 

<a id="12">[12]</a> W3Schools (no date) Python - slicing strings. Available at: https://www.w3schools.com/python/python_strings_slicing.asp (Accessed: 22 April 2024). 

<a id="13">[13]</a> Mallari, R. (2022) How can I dynamically mask all digits except the last 4 always?, Stack Overflow. Available at: https://stackoverflow.com/questions/70258603/how-can-i-dynamically-mask-all-digits-except-the-last-4-always (Accessed: 22 April 2024). 

<a id="14">[14]</a> W3Schools (no date) Python operators. Available at: https://www.w3schools.com/python/python_operators.asp (Accessed: 22 April 2024). 

<a id="15">[15]</a> W3Schools (no date) Python - string concatenation. Available at: https://www.w3schools.com/python/python_strings_concatenate.asp (Accessed: 22 April 2024). 

<a id="16">[16]</a> Delta Flyer (2015) Making a Collatz program automate the boring stuff, Stack Overflow. Available at: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff (Accessed: 22 April 2024).

<a id="17">[17]</a> Gupta, C. (2023) Exploring the Collatz conjecture with python, Medium. Available at: https://medium.com/@chakshugupta774/exploring-the-collatz-conjecture-with-python-7c5d9f31d233 (Accessed: 23 April 2024).

<a id="18">[18]</a> Collatz conjecture (2024) Wikipedia. Available at: https://en.wikipedia.org/wiki/Collatz_conjecture (Accessed: 22 April 2024).

<a id="19">[19]</a> Python program to check if a number is positive, negative, or 0: Example (2021) Toppr. Available at: https://www.toppr.com/guides/python-guide/examples/python-examples/decision-making-and-loops/positive-negative-zero/python-program-check-number-positive-negative-0/#:~:text=Python%20tests%20whether%20a%20number,Otherwise%2C%20it%20will%20be%20negative (Accessed: 23 April 2024). 

<a id="20">[20]</a> Python program to check if a number is odd or even: Python even or odd (2021) Toppr. Available at: https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-to-check-if-a-number-is-odd-or-even/#:~:text=If%20a%20number%20is%20completely,then%20the%20number%20is%20odd (Accessed: 23 April 2024). 

<a id="21">[21]</a> Real Python (2022) Python ‘while’ loops (indefinite iteration), Real Python. Available at: https://realpython.com/python-while-loop/ (Accessed: 22 April 2024). 

<a id="22">[22]</a> GeeksforGeeks (2023) Python: Printing string with double quotes. Available at: https://www.geeksforgeeks.org/python-printing-string-with-double-quotes/ (Accessed: 23 April 2024). 

<a id="23">[23]</a> Python if ... else (no date) Python Conditions. Available at: https://www.w3schools.com/python/python_conditions.asp (Accessed: 22 April 2024). 

<a id="24">[24]</a> LeBrun (2016) While loop with IF/else statement in Python, Stack Overflow. Available at: https://stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python (Accessed: 23 April 2024). 

<a id="25">[25]</a> Kumar, N. (2018) Python modules: What are and how to import modules in python?, DataCamp. Available at: https://www.datacamp.com/tutorial/modules-in-python (Accessed: 23 April 2024). 

<a id="26">[26]</a> Datetime - basic date and time types (no date) Python documentation. Available at: https://docs.python.org/3/library/datetime.html (Accessed: 23 April 2024).

<a id="27">[27]</a> Real Python (2023) Lists and tuples in Python, Real Python. Available at: https://realpython.com/python-lists-tuples/ (Accessed: 23 April 2024). 

<a id="28">[28]</a> Newton’s method (no date) Wikipedia. Available at: https://en.wikipedia.org/wiki/Newton%27s_method (Accessed: 23 April 2024). 

<a id="29">[29]</a> Find root of a number using Newton’s method (2023) GeeksforGeeks. Available at: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ (Accessed: 23 April 2024). 

<a id="30">[30]</a> 8.6. Newton’s method (no date) 8.6. Newton’s Method - How to Think like a Computer Scientist: Interactive Edition. Available at: https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html (Accessed: 23 April 2024). 

<a id="31">[31]</a> Defining your own python function (2023) Real Python. Available at: https://realpython.com/defining-your-own-python-function/ (Accessed: 23 April 2024). 

<a id="32">[32]</a> Singh, R. (2023) Python scientific notation, Scaler Topics. Available at: https://www.scaler.com/topics/python-scientific-notation/ (Accessed: 23 April 2024). 

<a id="33">[33]</a> Ravikiran A S (2023) Understanding float in python [with examples], Simplilearn.com. Available at: https://www.simplilearn.com/tutorials/python-tutorial/float-in-python#:~:text=Float%20is%20a%20function%20or,architecture%20subject%20to%20available%20memory (Accessed: 23 April 2024). 

<a id="34">[34]</a> Kumar, P. (2023) Python return statement, AskPython. Available at: https://www.askpython.com/python/python-return-statement (Accessed: 23 April 2024). 

<a id="35">[35]</a> Training, W. by: Pierian (2023) Counting in a python loop: A beginner’s guide, Pierian Training. Available at: https://pieriantraining.com/counting-in-a-python-loop-a-beginners-guide/#:~:text=To%20count%20down%20with%20a,and%20decrement%20it%20by%20one.&text=In%20this%20example%2C%20we%20start%20with%20a%20counter%20value%20of%205 (Accessed: 23 April 2024). 

<a id="36">[36]</a> Tagliaferri, L. (2021) How to use break, continue, and pass statements when working with loops in python 3, DigitalOcean. Available at: https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3 (Accessed: 23 April 2024). 

<a id="37">[37]</a> (No date) Chatgpt. Available at: https://chat.openai.com/ (Accessed: 22 April 2024). 

<a id="38">[38]</a> Beatty (2024) Pands-course-material/jupyternotebooks/topic07-files.ipynb at main · Andrewbeattycourseware/pands-course-material, GitHub. Available at: https://github.com/andrewbeattycourseware/pands-course-material/blob/main/jupyternotebooks/topic07-files.ipynb (Accessed: 23 April 2024). 

<a id="39">[39]</a> Python count() function: Why do we use Python string count() function?  (2021) Toppr. Available at: https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/count/python-string-count/#:~:text=How%20do%20you%20count%20characters,only%20a%20single%20substring%20parameter (Accessed: 23 April 2024). 

<a id="40">[40]</a> Real Python (2023) The python return statement: Usage and best practices, Real Python. Available at: https://realpython.com/python-return-statement/#returning-none-explicitly (Accessed: 23 April 2024). 

<a id="41">[41]</a> Built-in exceptions (no date) Python documentation. Available at: https://docs.python.org/3/library/exceptions.html (Accessed: 23 April 2024). 

<a id="42">[42]</a> GeeksforGeeks (2023) How to fix filenotfounderror in python, GeeksforGeeks. Available at: https://www.geeksforgeeks.org/why-am-i-getting-a-filenotfounderror-in-python/ (Accessed: 23 April 2024). 

<a id="43">[43]</a> Ali, M. (2023) The ultimate guide to command line arguments in python scripts, Medium. Available at: https://moez-62905.medium.com/the-ultimate-guide-to-command-line-arguments-in-python-scripts-61c49c90e0b3 (Accessed: 23 April 2024). 

<a id="44">[44]</a> Python - command-line arguments (no date) Tutorialspoint. Available at: https://www.tutorialspoint.com/python/python_command_line_arguments.htm (Accessed: 23 April 2024). 

<a id="45">[45]</a> Wkoomson (2011) How can I check the extension of a file?, Stack Overflow. Available at: https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file (Accessed: 23 April 2024).

<a id="46">[46]</a> Handling errors (no date) User input and error handling. Available at: http://hplgit.github.io/primer.html/doc/pub/input/._input-solarized007.html (Accessed: 23 April 2024). 

<a id="47">[47]</a> McAleer, K. (2023) What does the python ‘if name Equals Main’ construct do?: Theserverside, TheServerSide.com. Available at: https://www.theserverside.com/tip/What-does-the-Python-if-name-equals-main-construct-do#:~:text=to%20the%20console.-,The%20if%20__name__%20%3D%3D%20%22__main__%22%3A,it%20would%20not%20execute%20automatically. (Accessed: 23 April 2024). 

<a id="48">[48]</a> Clontz, S. (2013) Mobydick.txt, Git Hub. Available at: https://gist.github.com/StevenClontz/4445774 (Accessed: 23 April 2024). 

<a id="49">[49]</a> The absolute basics for beginners (no date) NumPy. Available at: https://numpy.org/doc/stable/user/absolute_beginners.html (Accessed: 23 April 2024). 

<a id="50">[50]</a> Pyplot tutorial (no date) Pyplot tutorial - Matplotlib 3.8.4 documentation. Available at: https://matplotlib.org/stable/tutorials/pyplot.html (Accessed: 23 April 2024). 

<a id="51">[51]</a> Numpy.random.seed# (no date) numpy.random.seed - NumPy v1.26 Manual. Available at: https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html (Accessed: 23 April 2024). 

<a id="52">[52]</a> NumPy (no date) numpy.random.normal - NumPy v2.1.dev0 Manual. Available at: https://numpy.org/devdocs/reference/random/generated/numpy.random.normal.html (Accessed: 23 April 2024). 

<a id="53">[53]</a> W3Schools (no date) Matplotlib histograms. Available at: https://www.w3schools.com/python/matplotlib_histograms.asp (Accessed: 23 April 2024). 

<a id="54">[54]</a> Quick start guide (no date) Matplotlib 3.8.4 documentation. Available at: https://matplotlib.org/stable/users/explain/quick_start.html# (Accessed: 23 April 2024). 

<a id="55">[55]</a> Joris (2011) Secondary axis with twinx(): How to add to legend, Stack Overflow. Available at: https://stackoverflow.com/questions/5484922/secondary-axis-with-twinx-how-to-add-to-legend (Accessed: 23 April 2024). 

<a id="56">[56]</a> Legend and legend_handler (no date) Matplotlib 2.0.2 documentation. Available at: https://matplotlib.org/2.0.2/api/legend_api.html (Accessed: 23 April 2024). 

<a id="57">[57]</a> Matplotlib.axes.axes.tick_params (no date) Matplotlib 3.8.4 documentation. Available at: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html (Accessed: 23 April 2024). 
