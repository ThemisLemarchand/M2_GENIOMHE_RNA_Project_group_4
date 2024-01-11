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
def create_all_one_hot_matrix(source_directory, target_directory):
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
    
    all_training_matrices = []
    all_test_matrices = []
    
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
            
            if source_directory == sourceTrainingSet:
                all_training_matrices.append(delta_one_hot_matrix)
            elif source_directory == sourceTestSet:
                all_test_matrices.append(delta_one_hot_matrix)
    
    if all_training_matrices:
        all_training_concatenated = np.concatenate(all_training_matrices)
        all_training_df = pd.DataFrame(all_training_concatenated)
        all_training_df.columns = ['A', 'C', 'G', 'U']
        target_name_file_train = 'all_training_matrix_one_hot_encoded.csv'
        target_file_path_train = os.path.join(target_directory, target_name_file_train)
        all_training_df.to_csv(target_file_path_train, index=False)
        print(f"all one-hot encoding training saves in {target_file_path_train}") 
    
    if all_test_matrices:
        all_test_concatenated = np.concatenate(all_test_matrices)
        all_test_df = pd.DataFrame(all_test_concatenated)
        all_test_df.columns = ['A', 'C', 'G', 'U']
        source_name_file_test = 'all_test_matrix_one_hot_encoded.csv'
        source_file_path_test = os.path.join(target_directory, source_name_file_test)
        all_test_df.to_csv(source_file_path_test, index=False)
        print(f"all one-hot encoding test saves in{source_file_path_test}") 

create_all_one_hot_matrix(sourceTrainingSet, targetTrainingSet)
create_all_one_hot_matrix(sourceTestSet, targetTestSet)

