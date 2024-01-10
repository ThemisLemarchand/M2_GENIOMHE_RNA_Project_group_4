import os
import csv

# Paths to directories containing CSV files
directory1 = '../data/angles/TestSet'
directory2 = '../data/angles/TrainingSet'

# Definition of heuristic rules for classification according to 'delta'
def classifier_delta(delta_value):
    if delta_value == '':
        return 'error'
    try:
        delta_float = float(delta_value)
        if delta_float < -161:
            return "0"
        elif delta_float >= -161 and delta_float < -143:
            return "1"
        elif delta_float >= -143 and delta_float < -126:
            return "2"
        elif delta_float >= -126 and delta_float < -108:
            return "3"
        elif delta_float >= -108 and delta_float < -90:
            return "4"
        elif delta_float >= -90 and delta_float < -72:
            return "5"
        elif delta_float >= -72 and delta_float < -54:
            return "6"
        elif delta_float >= -54 and delta_float < 52:
            return "7"
        elif delta_float >= 52 and delta_float < 71:
            return "8"
        elif delta_float >= 71 and delta_float < 88:
            return "9"
        elif delta_float >= 88 and delta_float < 106:
            return "10"
        elif delta_float >= 106 and delta_float < 124:
            return "11"
        elif delta_float >= 124 and delta_float < 142:
            return "12"
        elif delta_float >= 142 and delta_float < 160:
            return "13"
        elif delta_float >= 160:
            return "14"
    except ValueError:
        return '15'

# Function to classify CSV files according to 'delta'
def classifier_fichiers(repertoire):
    fichiers_csv = [fichier for fichier in os.listdir(repertoire) if fichier.endswith('.csv')]
    resultats = {}

    for fichier in fichiers_csv:
        chemin_fichier = os.path.join(repertoire, fichier)
        lignes = []

        with open(chemin_fichier, newline='') as csvfile:
            lecteur_csv = csv.DictReader(csvfile)
            for ligne in lecteur_csv:
                ligne['Category'] = classifier_delta(ligne['delta'])
                lignes.append(ligne)

        resultats[fichier] = lignes

    return resultats

# Classification of files in specific directories
resultats_directory1 = classifier_fichiers(directory1)
resultats_directory2 = classifier_fichiers(directory2)

# Function to save classes in csv file
def save_classes(resultats, nom_fichier_resultat):
    with open(nom_fichier_resultat, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['classe'])

        for lignes in resultats.values():
            for ligne in lignes:
                classe = ligne['Category']
                if classe and classe not in ['error']:
                    writer.writerow([classe])


# Save classes in csv file
save_classes(resultats_directory1, '../data/angles/TestSet_classes.csv')
save_classes(resultats_directory2, '../data/angles/TrainingSet_classes.csv')
