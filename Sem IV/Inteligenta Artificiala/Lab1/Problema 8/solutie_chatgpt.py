def numere_binar(n):
    for i in range(1, n + 1):
        print(bin(i)[2:])

# Exemplu de utilizare:
n = 4
print(f"Numerele în reprezentare binară cuprinse între 1 și {n} sunt:")
numere_binar(n)