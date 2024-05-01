#Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1}
# astfel încât o singură valoare se repetă de două ori, să se identifice acea valoare care se repetă.
# De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.
def frecvente(numere):
    frecventa = [0] * (len(numere) + 1)
    for numar in numere:
        frecventa[numar] += 1

    for numar, count in enumerate(frecventa):
        if count == 2:
            return numar


numere = [1, 2, 3, 4, 2]

print(frecvente(numere))
