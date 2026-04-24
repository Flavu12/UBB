import numpy as np
import pandas as pd
from PIL import Image
import os

# Salariul, bonusul, echipa
file_path = "data/employees.csv"
employees_data = pd.read_csv(file_path)

# Salariul si bonusul: normalizare min-max
salariu = np.array(employees_data['Salary'])
bonus = np.array(employees_data['Bonus %'])
salariu_normalizat = (salariu - salariu.min()) / (salariu.max() - salariu.min())
bonus_normalizat = (bonus - bonus.min()) / (bonus.max() - bonus.min())

employees_data['Salary'] = salariu_normalizat
employees_data['Bonus %'] = bonus_normalizat

# Normalizare echipa (one-hot encoding si apoi normalizare min-max)
# One-hot encoding
echipa_encoded = pd.get_dummies(employees_data['Team'])

echipa_encoded = echipa_encoded.astype(int)
# Normalizare min-max pe variabilele rezultate
for col in echipa_encoded.columns:
    echipa_encoded[col] = (echipa_encoded[col] - echipa_encoded[col].min()) / (echipa_encoded[col].max() - echipa_encoded[col].min())

employees_data = pd.concat([employees_data, echipa_encoded], axis=1)
employees_data.drop('Team', axis=1, inplace=True)

print(employees_data.head())


# Valorile pixelilor din imagini
image_folder = "data/images"
normalized_image_folder = "data/images"
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    image = Image.open(image_path)
    image_array = np.array(image)

    # Clipping
    clipped_image_array = np.clip(image_array, 0, 255)

    # Normalizare min-max
    normalized_image_array = (clipped_image_array - clipped_image_array.min()) / (
                clipped_image_array.max() - clipped_image_array.min())

    # Salvare imagine normalizata
    Image.fromarray((normalized_image_array * 255).astype(np.uint8)).save(
        os.path.join(normalized_image_folder, f'normalized_{image_file}'))

# Numarul de aparitii a cuvintelor la nivelul unei propozitii
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

file_path = "data/texts.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

propozitii = sent_tokenize(text)
cuvinte = [word_tokenize(sentence) for sentence in propozitii]

# Calculam nr maxim de aparttii a unui cuv in fiecare prop
nr_cuvinte = [Counter(sentence) for sentence in cuvinte]
max_nr_cuvinte = [max(cnt.values()) if cnt else 0 for cnt in nr_cuvinte]

# Normalizare
normalizare_nr = [list(map(lambda count: count / max_count if max_count != 0 else 0, counter.values())) for
                  counter, max_count in zip(nr_cuvinte, max_nr_cuvinte)]

# Vizualizare
for i, sentence in enumerate(propozitii):
    print(f"Propoziția {i + 1}:")
    for cuvant, count in zip(nr_cuvinte[i].keys(), normalizare_nr[i]):
        print(f"{cuvant}: {count}")
    print()
