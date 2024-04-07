# pands-weekly-tasks
This repository contains the weekly tasks that were completed as part of the Programming and Scripting classes in ATU with the lecturer Andrew Beatty.
These tasks display several Python scripts that were created to demonstrate the skills that were developed during the course.
This README has been written with [Github's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.
MarkDown was used in this README file and was based on [GitHub's Documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

## Get Started

To understand better the tasks have a look at the section About These Tasks below and start by reading through each one of the Weekly Tasks in numerical order. Once you have a glimse of what the task is about then you can either go to a specific program to undestand the steps adopted to build up the script by reading through the comments provided or you can run the program in a Python interpreter and have fun by testing them out.

## About These Tasks

There were 8 tasks that were completed throught the Programming and Scripting course and the details of each task is described under the headings below.


### Weekly Tasks 1: [helloworld.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/helloworld.py)

The program helloworld.py was the first program created by myself during this course. This is a very simple program that was created using the print() function to display a string "Hello World!" when this program is run by the user. 


#### References:

https://www.learnpython.org/en/Hello,_World!
https://cs.stanford.edu/people/nick/py/python-print.html
https://s3-us-west-2.amazonaws.com/python-notes/a-whirlwind-tour-of-python-2.pdf

### Weekly Tasks 2: [bank.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/bank.py)

The program bank.py is a program that when executed it displays a message for the user to enter two amounts in cents. However, the value must be an interger. For instance, €10.33 should be input as 1033. After the two values are entered by the user then the program calculates and output the sum of the two values.
The program was created to first sum up the two values and then split the values into two parts. The first part is the interger part (using the interger division operator in Python // to divide the interger part of the number by 100) and the second part is the decimal part (using the operator % to return the remainder of a division by 100). Finally the two parts (interger and decimal) are printed out via the function print () by concatenating both parts using an f string formatting to interpolate the two values within a string.


#### References:

https://docs.python.org/3/library/functions.html#input
https://www.w3schools.com/python/ref_func_input.asp
https://realpython.com/python-f-strings/
https://realpython.com/python-string-formatting/
https://www.programiz.com/python-programming/methods/built-in/int
https://www.w3schools.com/python/python_string_formatting.asp
https://www.askpython.com/python/string/02d-in-python
https://atlantictu-my.sharepoint.com/:v:/g/personal/andrew_beatty_atu_ie/ETmXpdhA8etHobd2Vm8ozZMBWYqHaNq0Cu94nHR4pOyz9A?e=6Tnuf3&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopiedShareExpTreatment%2Eview
https://ioflood.com/blog/python-integer-division-how-to-use-the-floor-operator/#:~:text=Python%20provides%20two%20types%20of,in%203%20(integer%20division)
https://www.w3schools.com/python/python_strings_concatenate.asp

### Weekly Tasks 3: [accounts.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/accounts.py)

This accounts.py program is a Python script that mimics the security approach that is used by banks when displaying the account number to users.
In this program the users are prompted to input their account number and the program displays the last four digits of the account number while replacing the other digits by X.
The program workflow follow the steps: 

1 - User is prompt to input their account number.
2 - The program converts the number into a string and counts the number of characters.
3 - It calculates the number of characters that need to be convert to 'X" by subtracting 4 from the amount of characters.
4 - It isolates the last 4 digits of the account number.
5 - It converts all the characters minus the last 4 to "X".
6 - The it outputs the modified account number with all characters displaying X except by the last 4 digits which are displayed in numbers as it appears in the account number.

This program also accepts an account number of any number of characters.


#### References:

https://realpython.com/python-string-formatting/
https://www.w3schools.com/python/python_strings_slicing.asp
https://www.w3schools.com/python/python_strings_concatenate.asp
https://www.w3schools.com/python/gloss_python_string_length.asp
https://stackoverflow.com/questions/70258603/how-can-i-dynamically-mask-all-digits-except-the-last-4-always

### Weekly Tasks 4: [collatz.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/collatz.py)

The collatz.py program illustrates the calculation process for the [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture), which is a mathematic problem that is considered quite famous for not being able to be resolved by the mathematicians as the conjecture has been proved to be held for all positive integers up to 2.95 x 10 ^ 20, but nobody was able to come up with a general proof. This program requests that a user inputs any positive integer and check if the number is even or odd. If the number is even then the program divides the number by 2. But if the number is odd then the number is multiplied by 3 and added one. As the numbers are generated from the conditional and subsequent calculation then these are stored in a sequence and returned into the loop to redo the conditional check and calculation until the final result ends in 1.


#### References:

https://www.w3schools.com/python/python_operators.asp
https://en.wikipedia.org/wiki/Collatz_conjecture
https://www.w3schools.com/python/python_conditions.asp
https://realpython.com/python-while-loop/
https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
https://medium.com/@chakshugupta774/exploring-the-collatz-conjecture-with-python-7c5d9f31d233
https://www.toppr.com/guides/python-guide/examples/python-examples/decision-making-and-loops/positive-negative-zero/python-program-check-number-positive-negative-0/#:~:text=Python%20tests%20whether%20a%20number,Otherwise%2C%20it%20will%20be%20negative.
https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-to-check-if-a-number-is-odd-or-even/#:~:text=If%20a%20number%20is%20completely,then%20the%20number%20is%20odd.
https://stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python
https://www.geeksforgeeks.org/python-printing-string-with-double-quotes/

###  Weekly Tasks 5: [weekday.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/weekday.py)


### Weekly Tasks 6: [squareroot.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/squareRoot.py)


### Weekly Tasks 7: [es.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/es.py) and [moby-dick.txt](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/moby-dick.txt)


### Weekly Tasks 8: [plottask.py](https://github.com/filipekojak88/pands-weekly-tasks/blob/main/plottask.py)


## Use of these tasks

This repository pands-weekly-tasks will be used to grade my learning from the Programming and Scripting course.
This repository can be used by other users as a source of examples of codes that can be written by a new Python user.
Also, these tasks reflect my understanding from the Python programming skills learned during the course, which is far from perfect but show a perspective of a student who has started learning Python.


## Get Help

If questions are raised when reviewing these tasks you can contact me via github and I will be happy to provide more information.

## Contribute

This is a one-off repository completed with the goal of attending the assignment requirements for the course of Programming and Scripting in ATU and the contribution will be based on feedback provided by Andrew Beatty during the lectures and during the grading of this Assignment. 
Any other activity has been entirely completed by the author.


## Author

[Filipe Carvalho](https://www.linkedin.com/in/filipe-carvalho-8146232a/)

I am a Quality Engineer with 10 years of experience in Automotive and Medical Device Industry.
I am a Production Mechanical Engineer with a Master Science degree in Management from Trinity College.
As a form of further develop myself and prepare to dive into AI in the future, I started in 2024 the course of Data Analytics in ATU.
