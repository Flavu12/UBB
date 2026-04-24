#Considerându-se o matrice cu n x m elemente binare (0 sau 1)
# sortate crescător pe linii, să se identifice indexul liniei care conține cele mai multe elemente de 1.

#De ex. în matricea
#[[0,0,0,1,1],
#[0,1,1,1,1],
#[0,0,1,1,1]]
#a doua linie conține cele mai multe elemente 1.

def linii(matrice):
    n, m = len(matrice), len(matrice[0])
    max_elemente_unu = 0
    index_linie = -1

    for i in range(n):
        elemente_unu = 0
        for j in range(m):
            if matrice[i][j] == 1:
                elemente_unu += 1

        if elemente_unu > max_elemente_unu:
            max_elemente_unu = elemente_unu
            index_linie = i

    return index_linie+1

matrice = [
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1]
]
print(linii(matrice))
