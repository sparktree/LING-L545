# Histogram generator, courtesy of Manojkumar Patil on medium.com

import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.7, 9.09, 9.52, 10.0, 11.11, 11.76, 12.5, 13.33, 13.33, 13.33, 14.29, 14.29, 15.38, 15.38, 16.0, 16.22, 16.67, 17.39, 17.39, 18.18, 19.05, 19.05, 20.0, 20.0, 20.0, 20.83, 21.05, 21.05, 21.74, 22.22, 22.22, 22.86, 23.53, 23.53, 24.0, 24.0, 25.0, 25.0, 25.0, 25.93, 26.09, 26.67, 26.67, 27.27, 27.27, 27.78, 28.0, 29.17, 29.63, 29.63, 29.63, 30.0, 31.43, 31.58, 32.0, 32.0, 32.35, 32.43, 33.33, 33.33, 33.33, 33.33, 33.33, 33.33, 33.33, 33.33, 33.33, 34.48, 35.0, 35.29, 35.71, 35.71, 36.36, 37.5, 37.5, 37.5, 37.5, 38.1, 38.3, 38.71, 38.89, 39.02, 39.02, 39.13, 40.0, 40.0, 40.0, 40.74, 41.18, 42.31, 42.86, 42.86, 42.86, 42.86, 42.86, 44.0, 44.0, 44.44, 45.0, 45.45, 45.83, 46.15, 46.43, 47.06, 47.37, 47.37, 47.62, 50.0, 50.0, 50.0, 50.0, 52.0, 52.17, 52.5, 53.33, 53.85, 54.76, 54.84, 55.56, 55.56, 56.25, 56.25, 56.67, 57.14, 57.14, 57.14, 57.89, 58.33, 58.33, 58.82, 59.09, 60.0, 60.0, 60.0, 60.71, 60.71, 60.87, 60.87, 61.54, 61.54, 61.54, 62.5, 62.5, 62.86, 64.1, 65.22, 65.62, 66.67, 68.18, 68.42, 68.42, 70.59, 72.0, 72.22, 75.0, 76.67, 77.27, 77.78, 77.78, 78.57, 80.0, 80.0, 80.0, 80.0, 80.0, 80.77, 81.25, 82.35, 83.33, 85.71, 85.71, 87.5, 90.0, 91.3, 92.0, 100.0, 100.0, 103.57, 105.0, 109.52, 111.11, 116.67, 117.65, 123.08, 129.63, 136.67, 138.89, 166.67, 190.91, 211.11, 252.63]

# Plot a histogram
plt.hist(data, bins=25)

# Add x-axis and y-axis titles
plt.xlabel('WER')
plt.ylabel('Frequency')

# Save image
plt.savefig('werHist.png')

# Display the plot
plt.show()