# RNA bioinformatics - M2-GENIOMHE project - group 4

## Repository

The folder is composed of: 
- `data`: a folder with the training (`data/TrainingSet`), testing (`data/TestSet`), sample (`data/sample`) folders and `SPOT-RNA-1D` folder.
        The `sample` folder contains a `.fasta` file that should be used to do inference for the delivery. 
        The `SPOT-RNA-1D` folder contains the predictions from `SPOT-RNA-1D` for the Training set (`data/SPOT-RNA-1D/training.json`) and Test set (`data/SPOT-RNA-1D/test.json`).
- `lib`: a folder containing a code that computes the dihedral angles from the following repository :(https://github.com/EvryRNA/rna_angles_prediction_dssr/tree/main)
- `requirements.txt` contains the necessary python library versions.
- `src`: a folder with all our implementations.
            - `select_chainA` : Selection of the chain A only when the RNA is multi-stranded, the results are the pdb files in data/TrainingSet/chainA and in                      data/TestSet/chainA and are used for the computation of the angles with the dssr tool.  
          - `distribution.py`: Visualization of the distribution of delta angles from CSV files in the `angles/TestSet` and `angles/TrainingSet`.  
          - `classication.py` : Classification according to predefined intervals based on the values in the 'delta' column from CSV files in the                                `angles/TestSet` and `angles/TrainingSet`.
          - `one_hot_encoding.py` : Creation of one-hot encoding matrices from genetic sequences extracted from CSV files in the `angles/TestSet` and                           `angles/TrainingSet` directories. The resulting matrices are then saved in the directories `angles/TestSetMatrix` and                                         `angles/TrainingSetMatrix`, respectively. (optional)
          - `all_one_hot_encoding.py`: Creation of a 2 unique one-hot encoding matrices from genetic sequences extracted from CSV files in the                                 `angles/TestSet` and 'angles/TrainingSet' directories, respectively. The resulting matrices are then saved in the directories                                 `angles/TestSetMatrix` and `angles/TrainingSetMatrix`, respectively.
          - `MLP.py` : Build, train, and evaluate a deep neural network (Deep MLP) model for the classification of genetic data.One-hot encoding data is                         loaded from CSV files, the model is configured with regularization layers, and its training is optimized with early termination. The model                    is evaluated on a test set, and its performance is recorded, with the trained model saved for later use.
          - `fasta_to_json.py` : Prediction of delta angles from genetic sequences in FASTA format from the previously trained deep neural network (Deep MLP)                         model. The results are then saved in a JSON file that contains information about the sequences, their nucleic acid sequences, and the                         associated delta angle predictions. Finally, the JSON file is saved in the `.. directory. /data/sample/` as `example.json`.
