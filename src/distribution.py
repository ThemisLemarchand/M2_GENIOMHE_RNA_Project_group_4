import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Paths to the directories containing the CSV files
directory_1 = '../data/angles/TestSet'
directory_2 = '../data/angles/TrainingSet'

all_files = []

# Retrieve all CSV files in the first directory
for filename in os.listdir(directory_1):
    if filename.endswith('.csv'):
        all_files.append(os.path.join(directory_1, filename))

# Retrieve all CSV files in the second directory
for filename in os.listdir(directory_2):
    if filename.endswith('.csv'):
        all_files.append(os.path.join(directory_2, filename))

# Load all CSV files into a list of DataFrames
data_frames = [pd.read_csv(file) for file in all_files]
filtered_data_frames = [df.dropna(axis=1, how='all') for df in data_frames]
all_data = pd.concat(filtered_data_frames)

# Select the delta angles column and convert to numeric values
angles_delta = pd.to_numeric(all_data['delta'], errors='coerce')
angles_delta = angles_delta[~np.isnan(angles_delta)]

# Create a Histogram for the Distribution of Delta Angles
plt.figure(figsize=(8, 6))
plt.hist(angles_delta, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Delta Angle Values')
plt.ylabel('Frequency')
plt.title('Distribution of delta angles on all files')
plt.grid(True)
plt.show()
