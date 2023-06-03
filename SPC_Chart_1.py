import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('C:/Users/nl020568/Documents/GitHub/gitHubTest/sample_data.csv')

# Print the first few rows of the DataFrame
print(df.head())


# Define the sample data
# data = [1, 2, 2, 2, 3, 4, 5, 5, 2, 1]

# Import the sample data from a file
data = np.loadtxt('C:/Users/nl020568/Documents/GitHub/gitHubTest/sample_data.txt')

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
plt.axhspan(ymin=two_sigma_lower, ymax=two_sigma_upper, color='yellow', alpha=0.2)
plt.axhspan(ymin=one_sigma_lower, ymax=one_sigma_upper, color='orange', alpha=0.2)

# Plot the central line
plt.hlines(y=mean, xmin=0, xmax=len(data), color='black')

# Label the chart
plt.title("SPC Mean Chart")
plt.xlabel("Sample Number")
plt.ylabel("Value")

# Display the chart
plt.show()
