import math

from Domeniu import numar_complex
from Domeniu.numar_complex import creeaza_numar_complex, get_parte_imaginara, get_parte_reala


def adauga_numar_complex(lista_numere, numar_complex):
    '''
    Incearca sa adauge la lista lista_numere numarul complex numar_complex
    :param lista_numere: lista de numere complexe
    :param numar_complex: numar_complex
    :return: -
    '''
    lista_numere.append(numar_complex)


def sterge_numarul_dupa_pozitie(lista_numere, pozitie):
    '''
    Sterge numarul complex de pe o anumita pozitie
    :param lista_numere: lista de dictionare de tipul cheltuieli
    :param pozitie: int
    :return:
    '''
    lista_numere.pop(pozitie - 1)


def sterge_numarul_dupa_interval(lista_numere, pozitie_initiala, pozitie_finala):
    '''
    sterge numerele complexe dintr-un anumit interval
    :param lista_numere: lista de dictionare de tipul numar complex
    :param pozitie_initiala: int
    :param pozitie_finala: int
    :return:-
    '''
    for i in range(pozitie_initiala, pozitie_finala + 1):
        lista_numere.remove(lista_numere[i])


def modul_numar_complex(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def suma_numerelor_din_subsecventa(lista_numere):
    '''
    Se calculeaza suma numerelor complexe pornind de la pozitia pozitie_initiala pana la pozitia pozitie_finala
    :param lista_numere: lista de dictionare de tipul numar complex
    :return: -
    '''
    pozitia_initiala = int(input("Precizati pozitia inceputului intervalului: "))
    pozitia_finala = int(input("Precizati pozitia sfarsitului intervalului: "))
    suma_reala = 0
    suma_imaginara = 0
    for i in range(pozitia_initiala, pozitia_finala + 1):
        suma_reala = suma_reala + get_parte_reala(lista_numere[i])
        suma_imaginara = suma_imaginara + get_parte_imaginara(lista_numere[i])
    print(suma_reala, "+", suma_imaginara, "i")

def produs_numere_complexe(numar_complex_1, numar_complex_2):
    '''
    Returneaza un numar complex egal cu produsul celor doua numere complexe
    :param numar_complex_1:
    :param numar_complex_2:
    :return:
    '''
    produs1 = get_parte_reala(numar_complex_1)*get_parte_reala(numar_complex_2)
    produs2 = get_parte_imaginara(numar_complex_1)* get_parte_imaginara(numar_complex_2)
    produs_real = produs1 - produs2
    produs3 = get_parte_reala(numar_complex_1) * get_parte_imaginara(numar_complex_2)
    produs4 = get_parte_imaginara(numar_complex_1) * get_parte_reala(numar_complex_2)
    produs_imaginar = produs3 + produs4
    rezultat_complex = creeaza_numar_complex(produs_real, produs_imaginar)
    return rezultat_complex



def ordonare_descrescatoare(lista_numere):

    return (sorted(lista_numere, key=lambda x:x[1], reverse=True))

def sortbyvalue(t):
    return get_parte_imaginara(numar_complex)


def prim(x):
    if x < 2:
        return 0
    else:
        s = int(x/2)
        for d in range(2, s+1):
            if x % d == 0:
                return 0
        return 1

def filtrare_parte_reala_prima(lista_numere):
    '''
     Elimina din lista numerele complexe care au partea reala un numar prim
    :param lista_numere: lista de dictionare de tipul numar prim
    :return:
    '''
    for numar_complex in lista_numere:
        parte_reala = int(get_parte_reala(numar_complex))
        if prim(parte_reala) == 1:
            lista_numere.remove(numar_complex)
    return lista_numere


def filtrare_modul(lista_numere,numar,semn):
    '''
    Elimina din lista numarul complex la care modulul este <, =, > decat un numar dat
    :param lista_numere: lista de dictionare de tipul numar complex
    :return:
    '''
    i=0
    if semn == -1:
        while i < len(lista_numere):
            if(modul_numar_complex(get_parte_reala(i), get_parte_imaginara(i)) < numar):
                lista_numere.pop(i)
                i = i - 1
            i+=1

    if semn == 0:
        while i < len(lista_numere):
            if (modul_numar_complex(get_parte_reala(i), get_parte_imaginara(i)) == numar):
                lista_numere.pop(i)
                i = i - 1
            i+=1
    if semn == 1:
        while i < len(lista_numere):
            if (modul_numar_complex(get_parte_reala(i), get_parte_imaginara(i)) > numar):
                lista_numere.pop(i)
                i=i-1
            i+=1
    return lista_numere

def afisare_lista_numere(lista_numere):
    for x in lista_numere:
        print(x)

