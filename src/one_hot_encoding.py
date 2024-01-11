import os
import pandas as pd
import numpy as np

# Source and Target Directory Paths
sourceTestSet = '../data/angles/TestSet'
targetTestSet = '../data/angles/TestSetMatrix'

sourceTrainingSet = '../data/angles/TrainingSet'
targetTrainingSet = '../data/angles/TrainingSetMatrix'

# Function to filter missing or non-divergent values in sequences
def filter_sequences(data):
    filtered_data = data.dropna(subset=['delta'])
    return filtered_data

def create_one_hot_matrix(source_directory, target_directory):
    # Checking and creating the target directory if it doesn't exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    files = os.listdir(source_directory)
    base_to_index = {'A': 0, 'C': 1, 'G': 2, 'U': 3}
    
    # Function to perform one-hot encoding for a sequence
    def one_hot_encode_sequence(sequence, base_to_index):
        one_hot_matrix = np.zeros((len(sequence), 4))
    
        for i, base in enumerate(sequence):
            if base in base_to_index:
                index = base_to_index[base]
                one_hot_matrix[i][index] = 1
    
        return one_hot_matrix
    
    # Function to count occurrences of A, C, G, U in a sequence
    def count_nucleotides(sequence):
        count_A = sequence.count('A')
        count_C = sequence.count('C')
        count_G = sequence.count('G')
        count_U = sequence.count('U')
        return count_A, count_C, count_G, count_U
    
    # Browse files in the source directory
    for file in files:
        if file.endswith('.csv'):
            source_file_path = os.path.join(source_directory, file)
            
            data = pd.read_csv(source_file_path)
            filtered_data = filter_sequences(data)
            sequences = filtered_data['sequence']
            one_hot_matrices = []

            # Cycle footage and perform one-hot encoding for delta angles
            for idx, sequence in enumerate(sequences):
                delta_matrix = one_hot_encode_sequence(sequence, base_to_index)
                one_hot_matrices.append(delta_matrix)
            
            delta_one_hot_matrix = np.concatenate(one_hot_matrices)
            target_name_file = os.path.splitext(file)[0] + '_one_hot_encoded.csv'
            target_file_path = os.path.join(target_directory, target_name_file)
            delta_one_hot_df = pd.DataFrame(delta_one_hot_matrix)
            delta_one_hot_df.to_csv(target_file_path, index=False, header=False)
            print(f"Matrix one-hot encoding {file} saves in {target_file_path}") 

create_one_hot_matrix(sourceTestSet, targetTestSet)
create_one_hot_matrix(sourceTrainingSet, targetTrainingSet)


