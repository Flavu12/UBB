#Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n.
# De ex. dacă n = 4, numerele sunt: 1, 10, 11, 100.
def binar(x):
    numar = bin(x)[2:]
    return numar

n = int(input("Introduceți valoarea lui n: "))
for i in range(1, n+1):
    print(binar(i))
