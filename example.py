import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
data = np.random.randn(1000)

# Create histogram
plt.hist(data, bins=30, density=True, alpha=0.5, color='blue')

# Overlay a plot
x = np.linspace(-4, 4, 100)
y = 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * x**2)
plt.plot(x, y, color='red')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency / Probability Density')
plt.title('Histogram and Plot Overlay')

# Show plot
plt.show()