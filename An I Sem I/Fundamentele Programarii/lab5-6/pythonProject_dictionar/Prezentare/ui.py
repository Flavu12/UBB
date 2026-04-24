from Domeniu.numar_complex import set_parte_reala, set_parte_imaginara
from Infrastructura.repository import *


def citire_numere(dictionar_numere, var):
    parte_reala = int(input("Introdu partea reala: "))
    parte_imaginara = int(input("Introdu partea imaginara: "))
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    adauga_numar_complex(dictionar_numere, parte_reala,parte_imaginara, var)



def modifica_numarul_complex(lista_numere):
    parte_reala = int(input("Alegeti partea reala a numarului de modificat:"))
    parte_imaginara = int(input("alegeti partea imaginara a numarului de modificat:"))
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    parte_reala_noua = int(input("Alegeti partea reala afisata dupa modificare:"))
    parte_imaginara_noua = int(input("Alegeti partea imaginara afisata dupa modificare:"))
    set_parte_reala(numar_complex, parte_reala_noua)
    set_parte_imaginara(numar_complex, parte_imaginara_noua)
    print(lista_numere)
def Tipareste_partea_imaginara_pentru_numerele_din_lista_din_interval_dat(lista_numere):
    '''
    Tipareste partea imaginara a numerelor complexe dintr-un interval dat
    :param lista_numere: lista de dictionare de tipul numar complex
    :return: -
    '''
    pozitia_initiala = int(input("Precizati pozitia inceputului intervalului: "))
    pozitia_finala = int(input("Precizati pozitia sfarsitului intervalului: "))
    lista_numere1 = []
    for i in range(pozitia_initiala, pozitia_finala):
        b = get_parte_imaginara(lista_numere[i])
        lista_numere1.append(b)
    afisare_lista_numere(lista_numere1)

def tiparire_numere_cu_modulul_mai_mic_decat_10(lista_numere):
    '''
    Tipareste numerele complexe care au modulul mai mic decat 10
    :param lista_numere: lista de dictionare de tipul numar complex
    :return: -
    '''
    i = 0
    ok = 0
    lista_numere1 = []
    while i < len(lista_numere):
        a = get_parte_reala(lista_numere[i])
        b = get_parte_imaginara(lista_numere[i])
        if modul_numar_complex(a, b) < 10:
            lista_numere1.append(lista_numere[i])
            ok += 1
        i += 1
    if ok == 0:
        print("Lista nu mai are elemente")
    else:
        afisare_lista_numere(lista_numere1)


def tiparire_numere_cu_modulul_egal_cu_10(lista_numere):
    '''
    Tipareste numerele complexe care au modulul egal cu 10
    :param lista_numere: lista de dictionare de tipul numar complex
    :return: -
    '''
    i = 0
    ok = 0
    lista_numere1 = []
    while i < len(lista_numere):
        a = get_parte_reala(lista_numere[i])
        b = get_parte_imaginara(lista_numere[i])
        if modul_numar_complex(a, b) == 10:
            lista_numere1.append(lista_numere[i])
            ok += 1
        i += 1
    if ok == 0:
        print("Lista nu mai are elemente")
    else:
        afisare_lista_numere(lista_numere1)

def produsul_numerelor_din_subsecventa(lista_numere):
    '''
    Se calculeaza podusul numerelor complexe pornind de la pozitia pozitie_initiala pana la pozitia pozitie_finala
    :param lista_numere: lista de dictionare de tipul numar complex
    :return: -
    '''
    pass


def afisare_filtrare_numar_prim(lista_numere):
    print(filtrare_parte_reala_prima(lista_numere))

def afisare_filtrare_modul(lista_numere):
    numar = int(input("introduceti numarul de comparat:"))
    semn = input("introduceti semnul:")
    filtrare_modul(lista_numere,numar,semn)
    print(lista_numere)

def afisare_ordonare_descrescatoare(lista_numere):
    print(ordonare_descrescatoare(lista_numere))

def afisare():
    print('''
    1.Introduceti numarul complex
    2. Afisare numarul complex
    3. Stergere numarul complex de pe o pozitie data
    4. Stergere numere complexe dintr-un interval
    5. Modifica toate aparitiile unui numar complex cu alt numar complex
    6. Tipărește partea imaginara pentru numerele din listă
    7. Tipărește toate numerele complexe care au modulul mai mic decât 10
    8. Tipărește toate numerele complexe care au modulul egal cu 10
    9. Suma numerelor complexe dintr-o subsecventa
    10. Produsul numerelor complexe dintr_o subsecventa
    11. Ordonare descrescatoare dupa partea imaginara
    12. Filtrare parte reala prima
    13. Filtrare dupa modul
    x. Exit
    ''')


def menu():
    lista_numere = {}
    var = 0
    val = True
    while val:
        afisare()
        optiune = input("Optiunea ta este:")
        if optiune == "1":
            citire_numere(lista_numere, var)
            var = var + 1
        elif optiune == "2":
            afisare_lista_numere(lista_numere)
        elif optiune == "3":
            sterge_numar_pozitie(lista_numere)
        #elif optiune == "4":
            #stergere_numere_interval(lista_numere)
        elif optiune == "5":
            modifica_numarul_complex(lista_numere)
        elif optiune == "6":
            Tipareste_partea_imaginara_pentru_numerele_din_lista_din_interval_dat(lista_numere)
        elif optiune == "7":
            tiparire_numere_cu_modulul_mai_mic_decat_10(lista_numere)
        elif optiune == "8":
            tiparire_numere_cu_modulul_egal_cu_10(lista_numere)
        elif optiune == "9":
            suma_numerelor_din_subsecventa(lista_numere)
        elif optiune == "10":
            produsul_numerelor_din_subsecventa(lista_numere)
        elif optiune == "11":
            afisare_ordonare_descrescatoare(lista_numere)
        elif optiune =="12":
            afisare_filtrare_numar_prim(lista_numere)
        elif optiune == "13":
            afisare_filtrare_modul(lista_numere)
        elif optiune == "x":
            return
        else:
            print("Comanda este gresita")