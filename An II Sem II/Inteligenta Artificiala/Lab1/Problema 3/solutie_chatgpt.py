def produs_scalar(vector1, vector2):
    # Verificăm dacă vectorii au aceeași dimensiune
    if len(vector1) != len(vector2):
        return "Dimensiunile vectorilor nu corespund."

    # Inițializăm suma produselor elementelor nenule
    suma_produse = 0

    # Iterăm prin elementele vectorilor și înmulțim corespunzător elementele nenule
    for i in range(len(vector1)):
        suma_produse += vector1[i] * vector2[i]

    return suma_produse


# Exemplu de utilizare:
vector1 = [1, 0, 2, 0, 3]
vector2 = [1, 2, 0, 3, 1]

# Calculăm produsul scalar
rezultat = produs_scalar(vector1, vector2)

print("Produsul scalar al vectorilor:", rezultat)
