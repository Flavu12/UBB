def suma_submatricelor(matrice, perechi):
    sume = []

    for pereche in perechi:
        (p, q), (r, s) = pereche
        suma = 0
        for i in range(p, r + 1):
            for j in range(q, s + 1):
                suma += matrice[i][j]
        sume.append(suma)

    return sume

# Exemplu de utilizare:
matrice = [
    [0, 2, 5, 4, 1],
    [4, 8, 2, 3, 7],
    [6, 3, 4, 6, 2],
    [7, 3, 1, 8, 3],
    [1, 5, 7, 9, 4]
]
perechi = [((1, 1), (3, 3)), ((2, 2), (4, 4))]

sume_submatrici = suma_submatricelor(matrice, perechi)
for i, suma in enumerate(sume_submatrici, 1):
    print(f"Suma elementelor din submatricea {i}: {suma}")
