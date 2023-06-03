import matplotlib.pyplot as plt
import numpy as np

# Define the sample data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate the mean and standard deviation of the data
mean = np.mean(data)
std = np.std(data)

# Calculate the one and two sigma limits
one_sigma_lower = mean - std
one_sigma_upper = mean + std
two_sigma_lower = mean - 2 * std
two_sigma_upper = mean + 2 * std

# Plot the sample data and the control limits
plt.plot(data, 'bo-')
plt.hlines(y=one_sigma_lower, xmin=0, xmax=len(data), color='red')
plt.hlines(y=one_sigma_upper, xmin=0, xmax=len(data), color='red')
plt.hlines(y=two_sigma_lower, xmin=0, xmax=len(data), color='green')
plt.hlines(y=two_sigma_upper, xmin=0, xmax=len(data), color='green')

# Label the chart
plt.title("SPC Mean Chart")
plt.xlabel("Sample Number")
plt.ylabel("Value")

# Display the chart
plt.show()
