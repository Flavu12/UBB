from Business.validator import numar_complex_valid, validare_index_service
from Domeniu.numar_complex import *
from Infrastructura.repository import *

#Numar_complex
def test_creeaza_numarul_complex():
    parte_reala = 12
    parte_imaginara = 13
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    assert(abs(parte_reala-get_parte_reala(numar_complex)) == 0.000001)
    assert (abs(parte_imaginara - get_parte_imaginara(numar_complex)) == 0.000001)

def test_setteri():
    parte_reala= 15
    parte_imaginara = 22
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    parte_reala_noua = 16
    parte_imaginara_noua = 30
    set_parte_reala(numar_complex, parte_reala_noua)
    set_parte_imaginara(numar_complex, parte_imaginara_noua)
    assert(abs(parte_reala_noua - get_parte_reala(numar_complex)) < 0.00001)
    assert(abs(parte_imaginara_noua - get_parte_imaginara(numar_complex)) < 0.00001)

#Repository
def test_adauga_numar_complex():
    lista_numere = []
    parte_reala = 2
    parte_imaginara = 4
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    assert (len(lista_numere) == 0)
    adauga_numar_complex(lista_numere, numar_complex)
    assert (len(lista_numere) == 1)


def test_sterge_numar_dupa_pozitie():
    lista_numere = []
    parte_reala = 1
    parte_imaginara = 2
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    adauga_numar_complex(lista_numere, numar_complex)
    parte_reala = 3
    parte_imaginara = 50
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    adauga_numar_complex(lista_numere, numar_complex)
    parte_reala = 4
    parte_imaginara = 25
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    adauga_numar_complex(lista_numere, numar_complex)
    sterge_numarul_dupa_pozitie(lista_numere, 1)
    assert (len(lista_numere) == 2)

def test_sterge_numar_dupa_interval():
    lista_numere = []
    numar_complex = creeaza_numar_complex(1, 100)
    adauga_numar_complex(lista_numere, numar_complex)
    numar_complex = creeaza_numar_complex(3, 50)
    adauga_numar_complex(lista_numere, numar_complex)
    numar_complex = creeaza_numar_complex(4, 25)
    adauga_numar_complex(lista_numere, numar_complex)
    sterge_numarul_dupa_interval(lista_numere, 0, 2)
    assert (len(lista_numere) == 1)

def test_modul():
    a = 3
    b = 4
    assert modul_numar_complex(a, b) == 5
    a = 6
    b = 8
    assert modul_numar_complex(a, b) == 10

def test_suma_numerelor_din_subsecventa():
    numar_complex = creeaza_numar_complex(1, 100)
    assert get_parte_reala(numar_complex) == 1
    assert get_parte_imaginara(numar_complex) == 100
    numar_complex = creeaza_numar_complex(3, 50)
    assert get_parte_reala(numar_complex) == 3
    assert get_parte_imaginara(numar_complex) == 50
    numar_complex = creeaza_numar_complex(4, 25)
    assert get_parte_reala(numar_complex) == 4
    assert get_parte_imaginara(numar_complex) == 25

def test_numar_prim():
    assert prim(1) == 0
    assert prim(0) == 0
    assert prim(3) == 1
    assert prim(2) == 1
    assert prim(25) == 0
    assert prim(-7) == 0


#Validator
def test_validare_numar():
    parte_reala = 12
    parte_imaginara = 13
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    numar_complex_valid(numar_complex)

    parte_reala_gresita = "ab"
    parte_imaginara_gresita = "jfdvd"
    numar_complex_gresit = creeaza_numar_complex(parte_reala_gresita, parte_imaginara_gresita)
    try:
        numar_complex_valid(numar_complex_gresit)
        assert False
    except ValueError as ve:
        assert(str(ve)=="parte reala invalida!\nparte imaginara invalida!\n")

def test_validare_index_service():
    lista_numere=[1, 2, 3, 4, 5]
    index_start = 1
    index_end = 4
    validare_index_service(lista_numere, index_start, index_end)

    index_start_gresit = "sks"
    index_end_gresit = "kdf"
    try:
        validare_index_service(lista_numere, index_start_gresit, index_end_gresit)
        assert False
    except ValueError as ve:
        assert(str(ve)=="indecsii nu sunt numere intregi!\n")

    index_start_prea_mare = 4
    index_end_corect = 2
    try:
        validare_index_service(lista_numere, index_start_prea_mare, index_end_corect)
        assert False
    except ValueError as ve:
        assert(str(ve)=="indexul de inceput nu poate fi mai mare decat cel de final!\n")

def teste_undo():
    numar_complex1 = creeaza_numar_complex(1, 100)
    numar_complex2 = creeaza_numar_complex(12, 13)
    numar_complex3 = creeaza_numar_complex(2, -4)
    lista_numere = []
    copie = []
    adauga_numar_complex(lista_numere, numar_complex1)
    adauga_numar_complex(lista_numere, numar_complex2)
    adauga_numar_complex(lista_numere, numar_complex3)
    copie.append(lista_numere[:])
    assert(len(lista_numere)) == 3
    copie.pop()
    assert (len(lista_numere)) == 2
    sterge_numarul_dupa_pozitie(lista_numere, 1)
    assert(len(lista_numere)) == 1
    copie.pop()
    assert (len(lista_numere)) == 2

def test_all():
    test_creeaza_numarul_complex()
    test_setteri()
    test_adauga_numar_complex()
    test_sterge_numar_dupa_pozitie()
    test_sterge_numar_dupa_interval()
    test_modul()
    test_suma_numerelor_din_subsecventa()
    test_numar_prim()
    test_validare_numar()
    test_validare_index_service()
    teste_undo()
