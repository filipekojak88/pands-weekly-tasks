# This program prints a histogram of a normal distribution
# of a 1000 values with a mean of 5 and standard deviation of 2
# and a plot of the function h(x)=x**3 in the range 0 to 10
# author: Filipe Carvalho

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1) 
normalRand = np.random.normal(loc=5, scale = 2, size = 1000)
# print(normalRand)

# Reference: Programming and Scripting Lab Topic 08-plotting - Exercise 6
plt.hist(normalRand, color='y', label="Random Hist")
plt.title("Random Hist")
plt.xlabel("Number")
plt.ylabel("Occurrence")
plt.legend()
plt.show()

# Reference: Programming and Scripting Lab Tope 08-plotting - Exercise 9
xpoints = np.array(range (1,10))
ypoints = xpoints ** 3 # y is equal x to the power of 3

plt.plot(xpoints, ypoints, color='b',label = "Random Plot")
plt.title("Random Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()