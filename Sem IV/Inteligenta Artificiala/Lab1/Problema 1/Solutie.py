#1.Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea
# într-un text care conține mai multe cuvinte separate prin ” ” (spațiu).
# De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".

#O(n*logn)
def ultim(x):
    cuvinte = x.split()
    cuvinte.sort()
    ultimul = cuvinte[-1]
    return ultimul

# Exemplu de utilizare:
print(ultim("Ana are mere si banane"))
