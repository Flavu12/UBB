#Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi
# formate din coordonatele a 2 căsuțe din matrice ((p,q) și (r,s)),
# să se calculeze suma elementelor din sub-matricile identificate de fieare pereche.

#De ex, pt matricea
#[[0, 2, 5, 4, 1],
#[4, 8, 2, 3, 7],
#[6, 3, 4, 6, 2],
#[7, 3, 1, 8, 3],
#[1, 5, 7, 9, 4]]
#și lista de perechi ((1, 1) și (3, 3)), ((2, 2) și (4, 4)),
# suma elementelor din prima sub-matrice este 38, iar suma elementelor din a 2-a sub-matrice este 44.

def sume(matrice, perechi):
    sume = []

    for pereche in perechi:
        (a, b), (c, d) = pereche
        suma = 0
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                suma += matrice[i][j]
        sume.append(suma)

    return sume

matrice = [
    [0, 2, 5, 4, 1],
    [4, 8, 2, 3, 7],
    [6, 3, 4, 6, 2],
    [7, 3, 1, 8, 3],
    [1, 5, 7, 9, 4]
]
perechi = [((1, 1), (3, 3)), ((2, 2), (4, 4))]

sume_submatrici = sume(matrice, perechi)
for i, suma in enumerate(sume_submatrici, 1):
    print(suma)
