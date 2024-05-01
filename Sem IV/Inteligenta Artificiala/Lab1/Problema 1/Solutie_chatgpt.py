def ultimul_cuvant(text):
    cuvinte = text.split()
    ultimul = sorted(cuvinte)[-1]
    return ultimul

# Exemplu de utilizare:
text = "Ana are mere rosii si galbene"
ultimul = ultimul_cuvant(text)
print("Ultimul cuvânt din textul dat, în ordine alfabetică, este:", ultimul)
