from Domeniu.numar_complex import *
from Infrastructura.repository import *


def test_creeaza_numarul_complex():
    parte_reala = 12
    parte_imaginara = 13
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    assert(abs(parte_reala-get_parte_reala(numar_complex)) == 0.000001)
    assert (abs(parte_imaginara - get_parte_imaginara(numar_complex)) == 0.000001)

def test_setteri():
    parte_reala = 15
    parte_imaginara = 22
    numar_complex = creeaza_numar_complex(parte_reala, parte_imaginara)
    parte_reala_noua = 16
    parte_imaginara_noua = 30
    set_parte_reala(numar_complex, parte_reala_noua)
    set_parte_imaginara(numar_complex, parte_imaginara_noua)
    assert(abs(parte_reala_noua - get_parte_reala(numar_complex)) == 16)
    assert(abs(parte_imaginara_noua - get_parte_imaginara(numar_complex)) == 30)

def test_adauga_numar_complex():
    lista_test = {0: [1, 2]}
    adauga_numar_complex(lista_test, 5, 6)
    assert lista_test == {0: [1, 2], 1: [5, 6]}
    adauga_numar_complex(lista_test, -2, 1.2)
    assert lista_test =={0: [1, 2], 1: [5, 6], 2: [-2, 1.2]}

def test_stergere_numare_interval():
    lista_test = {0: [1, 2], 1: [10, 4], 2: [1, 1], 3: [12, 12], 4: [15, 1], 5: [9, 19]}
    stergere_numere_interval(lista_test, 2, 4)
    assert lista_test == {0: [1, 2], 1: [10, 4], 2: [], 3: [], 4: [], 5: [9, 19]}

def test_suma_numerelor_din_subsecventa():
    lista_test = {0: [1, 2], 1: [10, 4], 2: [1, 1], 3: [12, 12], 4: [15, 1], 5: [9, 19]}
    suma_numerelor_din_subsecventa(lista_test)



def test_all():
    test_creeaza_numarul_complex()
    test_setteri()
    test_adauga_numar_complex()
    test_suma_numerelor_din_subsecventa()
