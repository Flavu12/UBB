#Să se determine produsul scalar a doi vectori rari care conțin numere reale.
# Un vector este rar atunci când conține multe elemente nule.
# Vectorii pot avea oricâte dimensiuni.
# De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.
def produs_scalar(vector1, vector2):
    if len(vector1) != len(vector2):
        return 0

    produs = 0
    for i in range(len(vector1)):
        produs += vector1[i] * vector2[i]
    return produs

vector1 = [1, 0, 2, 0, 3]
vector2 = [1, 2, 0, 3, 1]

print(produs_scalar(vector1, vector2))
