import math

from Domeniu import numar_complex
from Domeniu.numar_complex import creeaza_numar_complex, get_parte_imaginara, get_parte_reala


def adauga_numar_complex(dictionar_numere, parte_reala, parte_imaginara,var):
    '''
    Incearca sa adauge la dictionarul dictionar_numere numarul complex numar_complex
    :param dictionar_numere: dictionar de numere complexe
    :return: -
    '''
    numar_complex = creeaza_numar_complex(parte_reala,parte_imaginara)
    dictionar_numere[var] = numar_complex
    var = var + 1

def sterge_numar_pozitie(dictionar_numere):
    pozitie = int(input("Introduce pozitia:"))
    del dictionar_numere[pozitie]


def stergere_numere_interval(dictionar_numere, pozitie_initiala, pozitie_finala, var):
    for i in range (pozitie_initiala, pozitie_finala + 1):
        dictionar_numere[var].pop(i)

def suma_numerelor_din_subsecventa(dictionar_numere):
    '''
    Se calculeaza suma numerelor complexe pornind de la pozitia pozitie_initiala pana la pozitia pozitie_finala
    :return: -
    '''
    pozitia_initiala = int(input("Precizati pozitia inceputului intervalului: "))
    pozitia_finala = int(input("Precizati pozitia sfarsitului intervalului: "))
    suma_reala = 0
    suma_imaginara = 0
    for i in range(pozitia_initiala, pozitia_finala + 1):
        suma_reala = suma_reala + get_parte_reala(dictionar_numere[i]["parte_reala"])
        suma_imaginara = suma_imaginara + get_parte_imaginara(dictionar_numere[i]["parte_imaginara"])
    print(suma_reala, "+", suma_imaginara, "i")

def modul_numar_complex(a, b):
    return math.sqrt(a ** 2 + b ** 2)


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
    if semn == "<":
        while i < len(lista_numere):
            if(modul_numar_complex(get_parte_reala(i), get_parte_imaginara(i)) < numar):
                lista_numere.remove(i)
                i = i - 1
            i+=1

    if semn == "=":
        while i < len(lista_numere):
            if (modul_numar_complex(get_parte_reala(i), get_parte_imaginara(i)) == numar):
                lista_numere.remove(i)
                i = i - 1
            i+=1
    if semn == ">":
        while i < len(lista_numere):
            if (modul_numar_complex(get_parte_reala(i), get_parte_imaginara(i)) > numar):
                lista_numere.remove(i)
                i=i-1
            i+=1
    return lista_numere


def afisare_lista_numere(dictionar_numere):
    print(dictionar_numere)
    for i in range (0,len(dictionar_numere)):
        print(dictionar_numere[i]["parte_reala"], dictionar_numere[i]["parte_imaginara"])