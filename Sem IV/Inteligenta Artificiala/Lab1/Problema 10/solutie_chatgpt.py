def linia_cu_cele_mai_multe_unu(matrice):
    n, m = len(matrice), len(matrice[0])
    max_elemente_unu = 0
    index_linie = -1

    for i in range(n):
        # Căutare binară pentru a găsi prima apariție a valorii 1 în linie
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrice[i][mid] == 1:
                right = mid - 1
            else:
                left = mid + 1

        # Numărul de elemente de 1 în linie este dat de diferența dintre indexul primei apariții a valorii 1 și lungimea liniei
        elemente_unu = m - left

        if elemente_unu > max_elemente_unu:
            max_elemente_unu = elemente_unu
            index_linie = i

    return index_linie

# Exemplu de utilizare:
matrice = [
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1]
]
index_linie = linia_cu_cele_mai_multe_unu(matrice)
print("Indexul liniei cu cele mai multe elemente de 1:", index_linie)
