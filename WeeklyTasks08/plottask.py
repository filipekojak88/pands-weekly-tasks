# This program prints a histogram of a normal distribution
# of a 1000 values with a mean of 5 and standard deviation of 2
# and a plot of the function h(x)=x**3 in the range 0 to 10
# author: Filipe Carvalho

# Import Numpy and MatPlotLib.Pyplot.
import numpy as np
import matplotlib.pyplot as plt

# Set up the seed for random to 1 to avoid a new random number to be generated everytime this program is run
np.random.seed(1) 
# Generate the randome number using numpy
normalRand = np.random.normal(loc=5, scale = 2, size = 1000)
# print(normalRand)

# Reference: Programming and Scripting Lab Topic 08-plotting - Exercise 6
# Plot the histogram using the random data that was generated and formatting with colour yellow and label
# Add title, axis labels and legend
plt.hist(normalRand, color='y', label="Hist")
plt.title("Histogram of a Normal Distribution")
plt.xlabel("Number")
plt.ylabel("Occurrence")
plt.legend()

# Reference: Programming and Scripting Lab Tope 08-plotting - Exercise 9
# generate an array within a range from 1 to 10 
xpoints = np.array(range (1,10))
# add the numbers from the array to the power of 3
hpoints = xpoints ** 3 # y is equal x to the power of 3

# Plot on the same chart of the histogram a line
# with the numbers from the array in the x axis and 
# the second array with numbers calculated to the power of 3 in the y axis 
# format with colour blue with and label
# Add legend
plt.plot(xpoints, hpoints, color='b',label = "h(x) = x ^ 3")
plt.legend()
plt.show()