import numpy as np


# Functia pentru a calcula punctul de intersectie a planului cu axele coordonatelor
def intersectie_axe(a, b, c, d):
    # Cu Ox: y = 0, z = 0 -> a * x + d = 0 => x = -d / a
    if a != 0:
        intersectie_x = -d / a
    else:
        intersectie_x = None

    # Cu Oy: x = 0, z = 0 -> b * y + d = 0 => y = -d / b
    if b != 0:
        intersectie_y = -d / b
    else:
        intersectie_y = None

    # Cu Oz: x = 0, y = 0 -> c * z + d = 0 => z = -d / c
    if c != 0:
        intersectie_z = -d / c
    else:
        intersectie_z = None

    return intersectie_x, intersectie_y, intersectie_z


# Translatia planului la origine
def matrice_translatie(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])


# Rotatia fata de o axa
def matrice_rotatie(axa, theta):
    if axa == 'x':
        return np.array([
            [1, 0, 0, 0],
            [0, np.cos(theta), -np.sin(theta), 0],
            [0, np.sin(theta), np.cos(theta), 0],
            [0, 0, 0, 1]
        ])
    elif axa == 'y':
        return np.array([
            [np.cos(theta), 0, np.sin(theta), 0],
            [0, 1, 0, 0],
            [-np.sin(theta), 0, np.cos(theta), 0],
            [0, 0, 0, 1]
        ])
    elif axa == 'z':
        return np.array([
            [np.cos(theta), -np.sin(theta), 0, 0],
            [np.sin(theta), np.cos(theta), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])


# Reflexia fata de plan
def matrice_reflexie_xOy():
    # Reflexia fata de planul xOy
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, 1]
    ])


def matrice_reflexie_xOz():
    # Reflexia fata de planul xOz
    return np.array([
        [1, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def matrice_reflexie_yOz():
    # Reflexia fata de planul yOz
    return np.array([
        [-1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


# Functie pentru aplicarea transformarii asupra coordonatelor poliedrului
def apply_transformation(varfuri, transformation_matrix):
    homogenous_varfuri = np.hstack([varfuri, np.ones((varfuri.shape[0], 1))])
    transformare_varfuri = homogenous_varfuri.dot(transformation_matrix.T)
    return transformare_varfuri[:, :3]


def main():
    # Citim datele de intrare
    plan_type = input("Introduceti tipul planului\n 1 pentru ecuatia generala\n 2 pentru punct si vector normal\n ")

    if plan_type == '1':
        print("Introduceti coordonatele pentru ecuatia ax+by+cz+d=0\n")
        a = float(input("Introduceti coeficientul a: "))
        b = float(input("Introduceti coeficientul b: "))
        c = float(input("Introduceti coeficientul c: "))
        d = float(input("Introduceti coeficientul d: "))
    elif plan_type == '2':
        print("Introduceti coordonatele punctului A(x, y) si avectorului v(x,yz)\n")
        px = float(input("Introduceti coordonata x a punctului: "))
        py = float(input("Introduceti coordonata y a punctului: "))
        pz = float(input("Introduceti coordonata z a punctului: "))
        nx = float(input("Introduceti coordonata x a vectorului normal: "))
        ny = float(input("Introduceti coordonata y a vectorului normal: "))
        nz = float(input("Introduceti coordonata z a vectorului normal: "))

        # Normam vectorul normal
        norm = np.sqrt(nx ** 2 + ny ** 2 + nz ** 2)
        nx, ny, nz = nx / norm, ny / norm, nz / norm
        d = -(nx * px + ny * py + nz * pz)
        a, b, c = nx, ny, nz

    x_int, y_int, z_int = intersectie_axe(a, b, c, d)
    print(f"Intersectia planului cu axele: Ox({x_int}, 0, 0), Oy(0, {y_int}, 0), Oz(0, 0,{z_int})")

    # Testam daca planul coincide sau este paralel cu unul dintre planele de coordonate
    if a == 0 and b == 0 and d == 0 and c != 0:
        print("Planul coincide cu planul xOy.")
        reflexie = matrice_reflexie_xOy()
        print("Matricea reflexiei fata de xOy:")
        print(reflexie)
        print("Nu sunt necesare rotatii si translatii")
    elif a == 0 and b != 0 and d == 0 and c == 0:
        print("Planul coincide cu planul xOz.")
        reflexie = matrice_reflexie_xOz()
        print("Matricea reflexiei fata de xOz:")
        print(reflexie)
        print("Nu sunt necesare rotatii si translatii")
    elif a != 0 and b == 0 and d == 0 and c == 0:
        print("Planul coincide cu planul yOz.")
        reflexie = matrice_reflexie_yOz()
        print("Matricea reflexiei fata de yOz:")
        print(reflexie)
        print("Nu sunt necesare rotatii si translatii")
    elif a == 0 and b == 0 and c != 0 and d != 0:
        print("Planul este paralel cu planul xOy.")
        # Translatia pentru a aduce planul in origine
        translatie = matrice_translatie(0, 0, -d / c)
        reflexie = matrice_reflexie_xOy()
        inversa_translatie = matrice_translatie(0, 0, d/c)
        transformation = translatie @ reflexie @ inversa_translatie
        print("Matricea translatiei:")
        print(translatie)
        print("Matricea reflexiei:")
        print(reflexie)
        print("Matricea traslatiei inverse:")
        print(inversa_translatie)
        print("Nu sunt necesare rotatii. Doar translatia si reflexia sunt aplicate.")
        print("Matricea transformarii:")
        print(transformation)
    elif a == 0 and b != 0 and c == 0 and d != 0:
        print("Planul este paralel cu planul xOz.")
        # Translatia pentru a aduce planul in origine
        translatie = matrice_translatie(0, -d / b, 0)
        reflexie = matrice_reflexie_xOz()
        inversa_translatie = matrice_translatie(0, d/b, 0)
        transformation = translatie @ reflexie @ inversa_translatie
        print("Matricea translatiei:")
        print(translatie)
        print("Matricea reflexiei:")
        print(reflexie)
        print("Matricea traslatiei inverse:")
        print(inversa_translatie)
        print("Nu sunt necesare rotatii. Doar translatia si reflexia sunt aplicate.")
        print("Matricea transformarii:")
        print(transformation)
    elif a != 0 and b == 0 and c == 0 and d != 0:
        print("Planul este paralel cu planul yOz.")
        # Translatia pentru a aduce planul in origine
        translatie = matrice_translatie(-d / a, 0, 0)
        reflexie = matrice_reflexie_yOz()
        inversa_translatie = matrice_translatie(d/a, 0, 0)
        transformation = translatie @ reflexie @ inversa_translatie
        print("Matricea translatiei:")
        print(translatie)
        print("Matricea reflexiei:")
        print(reflexie)
        print("Matricea traslatiei inverse:")
        print(inversa_translatie)
        print("Nu sunt necesare rotatii. Doar translatia si reflexia sunt aplicate.")
        print("Matricea transformarii:")
        print(transformation)

    else:
        # Verificam daca planul trece prin origine
        if d == 0:
            print("Planul trece prin origine. Nu este necesara translatia.")
            # Rotatie in jurul axei x
            theta_x = np.arctan2(b, c)
            rot_x = matrice_rotatie('x', theta_x)
            print("Matricea rotatiei fata de Ox:")
            print(rot_x)

            # Rotatie in jurul axei y
            theta_y = np.arctan2(a, c)
            rot_y = matrice_rotatie('y', theta_y)
            print("Matricea rotatiei fata de Oy:")
            print(rot_y)

            inverse_rot_x = matrice_rotatie('x', -theta_x)
            inverse_rot_y = matrice_rotatie('y', -theta_y)

            print("Matricea rotatiei inverse fata de Ox:")
            print(inverse_rot_x)
            print("Matricea rotatiei inverse fata de Oy:")
            print(inverse_rot_y)

            # Reflexia
            reflexie = matrice_reflexie_xOy()
            print("Matricea reflexiei la axa xy:")
            print(reflexie)
            transformare = rot_x @ rot_y @ reflexie @ inverse_rot_y @ inverse_rot_x
            print("Matricea transformarii:")
            print(transformare)
        else:
            # Translatia pentru a aduce planul in origine
            translatie = matrice_translatie(0, 0, -d / c if c != 0 else 0)
            print("Matricea translatiei:")
            print(translatie)
            # Rotatia pentru a face normala la plan paralela cu axa Oz
            theta_y = np.arctan2(a, c)
            rotation_y = matrice_rotatie('y', theta_y)

            theta_x = np.arctan2(b, c)
            rotation_x = matrice_rotatie('x', theta_x)

            print("Matricea rotatiei fata de Oy:")
            print(rotation_y)
            print("Matricea rotatiei fata de Ox:")
            print(rotation_x)

            # Matricea reflexiei fata de planul xy
            reflexie = matrice_reflexie_xOy()
            print("Matricea reflexiei fata de planul xy:")
            print(reflexie)

            # Inversele rotatiilor
            inverse_rotation_x = matrice_rotatie('x', -theta_x)
            inverse_rotation_y = matrice_rotatie('y', -theta_y)

            print("Matricea rotatiei inverse fata de Ox:")
            print(inverse_rotation_x)
            print("Matricea rotatiei inverse fata de Oy:")
            print(inverse_rotation_y)

            # Translatia inversa
            inverse_translatie = matrice_translatie(0, 0, d / c if c != 0 else 0)
            print("Matricea translatiei inverse:")
            print(inverse_translatie)

            # Matricea transformarii compuse
            transformation = inverse_translatie @ inverse_rotation_y @ inverse_rotation_x @ reflexie @ rotation_x @ rotation_y @ translatie
            print("Matricea transformarii compuse:")
            print(transformation)

    # Citirea varfurilor poliedrului
    n = int(input("Introduceti numarul de varfuri ale poliedrului: "))
    varfuri = []
    for i in range(n):
        vertex = list(map(float, input(f"Introduceti coordonatele varfului {i + 1} (x, y, z): ").split()))
        varfuri.append(vertex)

    varfuri = np.array(varfuri)

    # Aplicarea transformarii asupra varfurilor poliedrului
    transformare_varfuri = apply_transformation(varfuri, transformation)
    print("Coordonatele varfurilor poliedrului dupa transformare:")
    print(transformare_varfuri)


if __name__ == "__main__":
    main()
