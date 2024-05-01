#Se da un fisier care contine un text (format din mai multe propozitii) in limba romana - a se vedea fisierul ”data/texts.txt”. Se cere sa se determine si sa se vizualizeze:

#numarul de propozitii din text;
#numarul de cuvinte din text
#numarul de cuvinte diferite din text
#cel mai scurt si cel mai lung cuvant (cuvinte)
#textul fara diacritice
#sinonimele celui mai lung cuvant din text



import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from collections import Counter
from unidecode import unidecode
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from translate import Translator

#nltk.download('punkt')
#nltk.download('wordnet')

file_path = "texts.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Nr de propozitii
nr_prop = len(sent_tokenize(text))
print("Numarul de propozitii in text:", nr_prop)

# Nr de cuvinte
cuvinte = word_tokenize(text)
nr_cuv = len(cuvinte)
print("Numarul de cuvinte in text:", nr_cuv)


# Nr de cuvinte diferite
nr_cuv_dif = len(set(cuvinte))
print("Numarul de cuvinte diferite in text:", nr_cuv_dif)

# Cel mai scurt + cel mai lung cuvant
cuv_min = min(cuvinte, key=len)
cuv_max = max(cuvinte, key=len)
print("Cel mai scurt cuvant: ", cuv_min)
print("Cel mai lung cuvant: ", cuv_max)

# Textul fara diacritice
text_fara_diacritice = unidecode(text)
print("Textul fara diacritice: ", text_fara_diacritice)

# cuvintele sinonime cu cel mai lung cuvant
sinonime = []
for sinonim in wordnet.synsets(cuv_max, lang='ron'):
    for lemma in sinonim.lemmas(lang='ron'):
        sinonime.append(lemma.name())
print("Sinonimele celui mai lung cuvânt:")
print(set(sinonime))