# Program: plottask.py
# This program generates and plots a histogram representing a normal distribution
# with 1000 values (mean=5, standard deviation=2)
# and also plots the function h(x) = x^3 over the range (0 to 10].
# Author: Filipe Carvalho

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(1)

# Generate a random sample of 1000 values from a normal distribution
sample = np.random.normal(loc=5, scale=2, size=1000)

# Plot the histogram of the samples on the primary y-axis (left)
plt.hist(sample, bins=30, color='yellow', alpha=0.7, label="Normal Dist. (Y-left)")
plt.title("Normal Distribution and Function Plot")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Get the current axes for the primary plot
ax1 = plt.gca()

# Create a secondary y-axis (right) to plot the function h(x) = x^3
ax2 = ax1.twinx()

# Generate an array of x values within the range (0 - 10]
x_points = np.arange(0, 11)  # Using np.arange for better precision
# Calculate h(x) = x^3 for each x value
h_points = x_points ** 3

# Plot the function h(x) = x^3 on the secondary y-axis (right)
ax2.plot(x_points, h_points, color='blue', label="h(x) = x^3 (Y-right)")
ax2.set_ylabel('h(x) Value')
ax2.tick_params(axis='y', labelcolor='blue')

# Get handles and labels for both axes to combine into a single legend
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

# Combine handles and labels from both axes
handles = handles1 + handles2
labels = labels1 + labels2

# Plot a single legend for both plots
ax1.legend(handles, labels, loc='upper left')

# Display the plot containing the histogram and the function plot
plt.show()

# End of the Program