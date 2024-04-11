# This program prints a histogram of a normal distribution
# of a 1000 values with a mean of 5 and standard deviation of 2
# and a plot of the function h(x)=x**3 in the range 0 to 10
# Author: Filipe Carvalho

# Import Numpy and MatPlotLib.Pyplot.
import numpy as np
import matplotlib.pyplot as plt

# Set up the seed for random to 1 to avoid a new random number to be generated everytime this program is run
np.random.seed(1) 
# Generate the randome number using numpy
normalRand = np.random.normal(loc=5, scale = 2, size = 1000)
# print(normalRand)


# Plot the histogram using the random data that was generated and formatting with colour yellow and label
# Add title, axis labels and legend
# Add bin to provide clearer visual representation of the normal distribution
# Add alpha to give a slight transparency to the histrogram
# and help distinguish the line plot
plt.hist(normalRand, bins=30, color='y', alpha=0.7, label="Normal Distribution")
plt.title("Normal Distribution and Function Plot")
plt.xlabel("Value")
plt.ylabel("Occurrence")
plt.legend()


# generate an array within a range from 1 to 10
# rande (11) was added to attend to this requirement
# as in range (1,10) the number 10 is not inclusive.
x_points = np.array(range(11))
# add the numbers from the array to the power of 3
h_points = x_points ** 3 # y is equal x to the power of 3

# Plot on the same chart a line
# with the numbers from the array in the x axis and 
# the second array with numbers calculated to the power of 3 in the y axis 
# format with colour blue and label
# Add legend
plt.plot(x_points, h_points, color='b',label = "h(x) = x ^ 3")
plt.legend()
plt.show()

# End of the Program