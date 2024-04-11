# Program plottask.py
# This program generates and plot a histogram representing a normal distribution
# with 1000 values (mean=5, std dev=2)
# and a line of the function h(x)=x^3 over the range (0 to 10].
# Author: Filipe Carvalho

# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Set random seed to be reproduced with same value
np.random.seed(1) 
# Generate a random sample of 1000 values from a normal distribution
sample= np.random.normal(loc=5, scale = 2, size = 1000)



# Plot the histogram of the samples
plt.hist(sample, bins=30, color='y', alpha=0.7, label="Normal Distribution")
plt.title("Normal Distribution and Function Plot")
plt.xlabel("Value")
plt.ylabel("Occurrence")
plt.legend()

# Add a secondary y-axis to improve visitbility between historgram and line plot
ax2 = plt.gca().twinx()

# generate an array of x values within range (0 - 10]
x_points = np.array(range(0,11))
# calculate h(x) = x ^ 3 for each x value
h_points = x_points ** 3

# Plot of the function h(x) = x ^ 3 on same graphic
ax2.plot(x_points, h_points, color='b',label = "h(x) = x^3 (Right Y-Axis)")    # label for identification of secondary y-axis
ax2.set_ylabel('h(x) Value')                                                   # set ylabel
ax2.tick_params(axis='y', labelcolor='b')                                      # add label color for the secondary axis y
plt.legend(loc='upper left')

# Display the graph with histogram and line plot
plt.show()

# End of the Program