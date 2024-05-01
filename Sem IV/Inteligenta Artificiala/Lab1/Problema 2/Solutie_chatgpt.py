import math

def distanta_euclidiana(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return pow((x2 - x1) ** 2 + (y2 - y1) ** 2, 0.5)

# Exemplu de utilizare:
punct1 = (1, 5)
punct2 = (4, 1)
distanta = distanta_euclidiana(punct1, punct2)
print("Distanța euclidiană între", punct1, "și", punct2, "este:", distanta)
