import numpy as np
import json
from tensorflow.keras.models import load_model

# load the model
model = load_model('../data/angles/model.h5')

def preprocess_fasta_sequence(fasta_sequence):
    sequence_lines = fasta_sequence.split('\n')[1:] if fasta_sequence.startswith('>') else fasta_sequence.split('\n')
    sequence = ''.join(sequence_lines)
    
    # Convert the sequence to one-hot encoding
    base_dict = {'A': 0, 'C': 1, 'G': 2, 'U': 3}
    sequence_length = len(sequence)
    one_hot_sequence = np.zeros((sequence_length, len(base_dict)), dtype=np.uint8)
    
    for i, base in enumerate(sequence):
        if base in base_dict:
            one_hot_sequence[i, base_dict[base]] = 1
    
    return one_hot_sequence

# Load the FASTA file
fasta_file_path = '../data/sample/example.fasta'
with open(fasta_file_path, 'r') as file:
    fasta_sequence = ''.join(file.read().split('\n')[1:])


preprocessed_sequence = preprocess_fasta_sequence(fasta_sequence)
predicted_angles = model.predict(preprocessed_sequence)
predicted_classes = np.argmax(predicted_angles, axis=1)

# Set the function to read the FASTA file
def read_fasta(file_path):
    sequences = []
    with open(file_path, "r") as file:
        sequence_name = None
        sequence = ""

        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence_name is not None:
                    sequences.append({
                        "nom_sequence": sequence_name,
                        "sequence": sequence
                    })
                    sequence = ""  

                sequence_name = line[1:]
            else:
                sequence += line

        if sequence_name is not None:
            sequences.append({
                "name_sequence": sequence_name,
                "sequence": sequence,
                "angles": predicted_classes
            })

    return sequences

sequences = read_fasta(fasta_file_path)

# Create a data structure for the JSON format
output_json = {}
for seq in sequences:
    sequence_name = seq['name_sequence']
    sequence = seq['sequence']
    prediction_angles = seq.get('angles', {}).tolist()
    
    output_json[sequence_name] = {
        "sequence": sequence,
        "angles": {"delta": prediction_angles}
    }

json_output = json.dumps(output_json, indent=4)

output_file_path = "../data/sample/example.json"

# Save the json file
with open(output_file_path, 'w') as output_file:
    json.dump(output_json, output_file, indent=4)

print(f"json save in {output_file_path}")
