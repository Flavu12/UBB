#Să se determine distanța Euclideană între două locații identificate prin perechi de numere.
# De ex. distanța între (1,5) și (4,1) este 5.0
import math

#O(1)
def distanta(x1, x2, y1, y2):
    distanta = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distanta


x1 = int(input("introduceti x1: "))
x2 = int(input("introduceti x2: "))
y1 = int(input("introduceti y1: "))
y2 = int(input("introduceti y2: "))
print(distanta(x1, x2, y1, y2))
