import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file into a pandas DataFrame
df = pd.read_csv('C:/Users/nl020568/Documents/GitHub/gitHubTest/sample_data.csv')
data = df['temp'].values

# Calculate the mean and standard deviation of the data
mean = np.mean(data)
std = np.std(data)

# Calculate the upper and lower limits and the one and two sigma limits
upper_limit = mean + 3 * std
lower_limit = mean - 3 * std
one_sigma = mean + std
two_sigma = mean + 2 * std

# Plot the data as a line chart
plt.plot(data)

# Add the upper and lower limits and the one and two sigma limits to the chart
plt.axhline(y=upper_limit, color='red', linestyle='--')
plt.axhline(y=lower_limit, color='red', linestyle='--')
plt.axhline(y=one_sigma, color='green', linestyle='--')
plt.axhline(y=two_sigma, color='green', linestyle='--')

# Add the mean to the chart as a central line
plt.axhline(y=mean, color='black', linewidth=2)

# Add the colored bands to the chart
plt.fill_betweenx([lower_limit, one_sigma], 0, len(data), color='yellow')
plt.fill_betweenx([one_sigma, two_sigma], 0, len(data), color='orange')
plt.fill_betweenx([two_sigma, upper_limit], 0, len(data), color='red')

# Add a title and axis labels to the chart
plt.title('SPC Mean Chart')
plt.xlabel('Samples')
plt.ylabel('Value')

# Show the chart
plt.show()
