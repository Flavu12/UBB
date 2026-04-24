def parte_reala_test(numar_complex):
    '''
    functia returneaza true daca partea reala a numarului complex este un float si false in caz contrar
    :param numar_complex:numar_complex
    :return: -True daca partea reala este float
             -False altfel
    '''
    try:
        float(numar_complex[0])
        return True
    except ValueError:
        return False


def parte_imaginara_test(numar_complex):
    '''
    Functia returneaza true daca partea reala a numarului complex este un float si false in caz contrar
    :param numar_complex: numar_complex
    :return: -True daca partea imaginara este float
             -False altfel
    '''
    try:
        float(numar_complex[1])
        return True
    except ValueError:
        return False

def numar_complex_valid(numar_complex):
    '''
    Raises a ValueError cu textul specific daca partea reala sau cea imaginara nu este valida
    :param numar_complex: numar_complex
    :return: -
    raises ValueError cu un text care descrie ce parte nu este valida
    '''
    err = ""
    if not parte_imaginara_test(numar_complex):
        err+="Parte imaginara invalida!\n"
    if not parte_reala_test(numar_complex):
        err+="Parte reala invalida!\n"
    if len(err) > 0:
        raise ValueError(err)

def validare_index_service(lista_numere, index_start, index_end):
    '''
    functie responsabila pentru a valida daca index_start si index_end pot forma o subsecventa
    :param lista_numere: lista elementelor complexe
    :param index_start: int
    :param index_end: int
    :return: -
    reises ValueError cu un mesaj de eroare corespunzator
    '''
    err=""
    try:
        index_start = int(index_start)
        index_end = int(index_end)
    except ValueError:
        raise ValueError("indecsii nu sunt numere intregi!\n")

    if index_start > index_end:
        err+="indexul de inceput nu poate fi mai mare decat cel de final!\n"
    else:
        if index_start < 0:
            err+="Index de inceput prea mic!\n"

        if index_start >= len(lista_numere):
            err +="indexul de inceput este prea mare!\n"

    if len(err)>0 :
        raise ValueError(err)


