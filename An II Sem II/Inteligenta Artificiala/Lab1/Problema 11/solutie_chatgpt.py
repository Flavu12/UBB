def inlocuire_0_cu_1(matrice):
    n, m = len(matrice), len(matrice[0])
    matrice_noua = [[elem for elem in rand] for rand in matrice]

    def vecini_tot_1(i, j):
        return all(matrice[i + dx][j + dy] == 1 for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)])

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrice[i][j] == 0 and vecini_tot_1(i, j):
                matrice_noua[i][j] = 1

    return matrice_noua

# Exemplu de utilizare:
matrice = [
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

matrice_noua = inlocuire_0_cu_1(matrice)
for rand in matrice_noua:
    print(rand)
