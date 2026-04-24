#Pentru un șir cu n numere întregi care conține și duplicate,
# să se determine elementul majoritar (care apare de mai mult de n / 2 ori).
# De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].

def majoritar(numere):
    frecventa = [0] * (len(numere) + 1)

    for i in numere:
        frecventa[i] += 1

    for i, count in enumerate(frecventa):
        if count > len(numere) // 2:
            return i

numere = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
print(majoritar(numere))
